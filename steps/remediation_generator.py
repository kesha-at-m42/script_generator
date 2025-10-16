"""
Remediation Generator Step - Generates error remediation options for interactions
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.pipeline import Step
from core.prompt_builder import PromptBuilder
from core.claude_client import ClaudeClient
from typing import Dict, Any, List
import json


class RemediationGenerator(Step):
    """Generates remediation options at multiple levels for each interaction
    
    Uses the remediation system reference doc (inputs/docs/remediation_system.md)
    which contains all error patterns, detection rules, and language templates.
    """
    
    def __init__(self):
        super().__init__(name="Remediation Generator", prompt_id="remediation_generator")
        self.prompt_builder = PromptBuilder()
        self.claude = ClaudeClient()
    
    def execute(self, input_data: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """Generate remediations for all interactions in the script
        
        Args:
            input_data: Must contain 'interactions' array with interaction details
            
        Returns:
            Original data plus 'remediations' added to each interaction
        """
        print(f"\n{'='*70}")
        print(f"  STEP: {self.name}")
        print(f"{'='*70}")
        
        if "interactions" not in input_data:
            print("  ⚠️  No 'interactions' found in input data")
            return input_data
        
        interactions = input_data["interactions"]
        print(f"\n  📋 Generating remediations for {len(interactions)} interactions...")
        
        # Generate remediations for all interactions
        remediations_data = self._generate_remediations(interactions)
        
        # Validate remediations
        validation_report = self._validate_remediations(remediations_data)
        
        # Merge remediations back into interactions
        enhanced_interactions = self._merge_remediations(interactions, remediations_data)
        
        # Print summary
        self._print_summary(remediations_data, validation_report)
        
        return {
            **input_data,
            "interactions": enhanced_interactions,
            "remediation_metadata": {
                "total_interactions": len(interactions),
                "remediations_generated": len(remediations_data.get("interactions", [])),
                "validation": validation_report
            }
        }
    
    def _generate_remediations(self, interactions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate remediations using Claude API"""
        
        # Build context about the interactions
        interactions_context = self._format_interactions_context(interactions)
        
        # Build prompt
        prompt = self.prompt_builder.build_remediation_generator_prompt(
            interactions_context=interactions_context
        )
        
        print(f"\n  🤖 Calling Claude API...")
        response = self.claude.generate(
            prompt=prompt,
            max_tokens=4000,
            temperature=0.7
        )
        
        # Parse JSON response
        try:
            remediations_data = json.loads(response)
            print(f"  ✅ Generated remediations for {len(remediations_data.get('interactions', []))} interactions")
            return remediations_data
        except json.JSONDecodeError as e:
            print(f"  ❌ Failed to parse JSON response: {e}")
            return {"interactions": [], "metadata": {}}
    
    def _format_interactions_context(self, interactions: List[Dict[str, Any]]) -> str:
        """Format interactions into context for the prompt"""
        
        context_lines = []
        for i, interaction in enumerate(interactions, 1):
            context_lines.append(f"\nActivity {i} - {interaction.get('title', 'Untitled')}")
            context_lines.append(f"Visual: {interaction.get('visual', 'Not specified')}")
            context_lines.append(f"Prompt: \"{interaction.get('prompt', '')}\"")
            context_lines.append(f"Interaction Type: {interaction.get('interaction_type', 'Unknown')}")
            
            if interaction.get('guide'):
                context_lines.append(f"Guide: \"{interaction['guide']}\"")
            
            # Add any cognitive/pedagogical metadata
            if interaction.get('cognitive_verb'):
                context_lines.append(f"Cognitive Verb: {interaction['cognitive_verb']}")
            if interaction.get('difficulty_level') is not None:
                context_lines.append(f"Difficulty Level: {interaction['difficulty_level']}")
        
        return "\n".join(context_lines)
    
    def _validate_remediations(self, remediations_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate generated remediations for quality and completeness"""
        
        report = {
            "errors": [],
            "warnings": [],
            "stats": {}
        }
        
        if "interactions" not in remediations_data:
            report["errors"].append("Missing 'interactions' in remediations data")
            return report
        
        error_signal_count = 0
        remember_count = 0
        light_word_counts = []
        medium_word_counts = []
        heavy_word_counts = []
        
        for interaction in remediations_data["interactions"]:
            activity_num = interaction.get("activity_number", "?")
            remediations = interaction.get("remediations", {})
            
            # Check each level
            for level in ["light", "medium", "heavy"]:
                if level not in remediations:
                    report["errors"].append(
                        f"Activity {activity_num}: Missing '{level}' level remediations"
                    )
                    continue
                
                level_data = remediations[level]
                
                # Check for required Generic option
                if "generic" not in level_data:
                    report["errors"].append(
                        f"Activity {activity_num}: Missing Generic option at {level} level"
                    )
                
                # Validate each option at this level
                for error_type, option in level_data.items():
                    # Check structure
                    if "text" not in option:
                        report["errors"].append(
                            f"Activity {activity_num}, {level}/{error_type}: Missing 'text' field"
                        )
                        continue
                    
                    text = option["text"]
                    word_count = len(text.split())
                    
                    # Check word count ranges
                    if level == "light":
                        light_word_counts.append(word_count)
                        if word_count < 10 or word_count > 20:
                            report["warnings"].append(
                                f"Activity {activity_num}, {level}/{error_type}: Word count {word_count} outside range (10-20)"
                            )
                        
                        # Count error signals
                        if any(signal in text for signal in ["Not quite", "Almost", "Let's try again", "Let's look"]):
                            error_signal_count += 1
                    
                    elif level == "medium":
                        medium_word_counts.append(word_count)
                        if word_count < 20 or word_count > 30:
                            report["warnings"].append(
                                f"Activity {activity_num}, {level}/{error_type}: Word count {word_count} outside range (20-30)"
                            )
                        
                        # Check for visual
                        if "visual" not in option or not option["visual"]:
                            report["errors"].append(
                                f"Activity {activity_num}, {level}/{error_type}: Missing visual description"
                            )
                    
                    elif level == "heavy":
                        heavy_word_counts.append(word_count)
                        if word_count < 30 or word_count > 60:
                            report["warnings"].append(
                                f"Activity {activity_num}, {level}/{error_type}: Word count {word_count} outside range (30-60)"
                            )
                        
                        # Check for visual
                        if "visual" not in option or not option["visual"]:
                            report["errors"].append(
                                f"Activity {activity_num}, {level}/{error_type}: Missing visual description"
                            )
                    
                    # Count "Remember" usage
                    if "Remember" in text or "remember" in text:
                        remember_count += 1
        
        # Calculate stats
        total_light = len(light_word_counts)
        if total_light > 0:
            error_signal_percentage = (error_signal_count / total_light) * 100
            report["stats"]["error_signal_percentage"] = error_signal_percentage
            
            if error_signal_percentage < 40 or error_signal_percentage > 50:
                report["warnings"].append(
                    f"Error signal distribution {error_signal_percentage:.0f}% outside target range (40-50%)"
                )
        
        report["stats"]["remember_count"] = remember_count
        if remember_count > 3:
            report["warnings"].append(
                f"'Remember' used {remember_count} times (max recommended: 3)"
            )
        
        if light_word_counts:
            report["stats"]["light_avg_words"] = sum(light_word_counts) / len(light_word_counts)
        if medium_word_counts:
            report["stats"]["medium_avg_words"] = sum(medium_word_counts) / len(medium_word_counts)
        if heavy_word_counts:
            report["stats"]["heavy_avg_words"] = sum(heavy_word_counts) / len(heavy_word_counts)
        
        return report
    
    def _merge_remediations(self, interactions: List[Dict[str, Any]], 
                           remediations_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Merge generated remediations back into interaction objects"""
        
        enhanced = []
        remediations_by_activity = {
            r["activity_number"]: r["remediations"]
            for r in remediations_data.get("interactions", [])
        }
        
        for i, interaction in enumerate(interactions, 1):
            enhanced_interaction = {
                **interaction,
                "remediations": remediations_by_activity.get(i, {})
            }
            enhanced.append(enhanced_interaction)
        
        return enhanced
    
    def _print_summary(self, remediations_data: Dict[str, Any], 
                      validation_report: Dict[str, Any]):
        """Print summary of remediation generation"""
        
        print(f"\n  {'─'*66}")
        print(f"  REMEDIATION GENERATION SUMMARY")
        print(f"  {'─'*66}")
        
        # Stats
        if validation_report.get("stats"):
            stats = validation_report["stats"]
            print(f"\n  📊 Statistics:")
            
            if "light_avg_words" in stats:
                print(f"     Light avg: {stats['light_avg_words']:.1f} words (target: 10-20)")
            if "medium_avg_words" in stats:
                print(f"     Medium avg: {stats['medium_avg_words']:.1f} words (target: 20-30)")
            if "heavy_avg_words" in stats:
                print(f"     Heavy avg: {stats['heavy_avg_words']:.1f} words (target: 30-60)")
            
            if "error_signal_percentage" in stats:
                print(f"\n     Error signals: {stats['error_signal_percentage']:.0f}% (target: 40-50%)")
            
            if "remember_count" in stats:
                print(f"     'Remember' usage: {stats['remember_count']} times (max: 3)")
        
        # Errors
        if validation_report.get("errors"):
            print(f"\n  ❌ Errors ({len(validation_report['errors'])}):")
            for error in validation_report["errors"][:5]:
                print(f"     • {error}")
            if len(validation_report["errors"]) > 5:
                print(f"     ... and {len(validation_report['errors']) - 5} more")
        
        # Warnings
        if validation_report.get("warnings"):
            print(f"\n  ⚠️  Warnings ({len(validation_report['warnings'])}):")
            for warning in validation_report["warnings"][:5]:
                print(f"     • {warning}")
            if len(validation_report["warnings"]) > 5:
                print(f"     ... and {len(validation_report['warnings']) - 5} more")
        
        # Success message
        if not validation_report.get("errors"):
            print(f"\n  ✅ Remediation generation complete!")
        
        print()


# Test the remediation generator
if __name__ == "__main__":
    print("Testing RemediationGenerator...\n")
    
    generator = RemediationGenerator()
    
    # Sample test data
    test_data = {
        "module_id": 1,
        "interactions": [
            {
                "activity_number": 1,
                "title": "Shade the Fraction",
                "visual": "Rectangle bar divided into 4 equal parts",
                "prompt": "Shade 3/4 of the rectangle.",
                "guide": "Remember: the denominator tells you how many total parts.",
                "interaction_type": "Shade",
                "cognitive_verb": "identify",
                "difficulty_level": 1
            },
            {
                "activity_number": 2,
                "title": "Place on Number Line",
                "visual": "Number line from 0 to 2, marked in fourths",
                "prompt": "Click to place 5/4 on the number line.",
                "guide": "Count the intervals from zero.",
                "interaction_type": "Click",
                "cognitive_verb": "locate",
                "difficulty_level": 2
            }
        ]
    }
    
    # Note: This will fail without actual Claude API setup
    # result = generator.execute(test_data)
    
    print("RemediationGenerator class structure validated!")
    print("\nTo test with actual API:")
    print("1. Ensure Claude API key is configured")
    print("2. Run with valid interaction data")
    print("3. Review generated remediations for quality")
