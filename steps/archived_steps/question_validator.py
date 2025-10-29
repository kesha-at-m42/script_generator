"""
Question Validator - Validates generated questions for quality and feasibility
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.pipeline import Step
from typing import Dict, List, Any


class QuestionValidator(Step):
    """Validates questions for quality, variety, and technical feasibility"""
    
    def __init__(self):
        super().__init__(name="Question Validator", prompt_id="question_validator")
        
        # Define valid interaction types
        self.VALID_INTERACTION_TYPES = {
            "Multiple Choice", "Multiple Select", "Click", "Shade", 
            "Drag and Drop", "Input", "True/False"
        }
        
        # Target difficulty distribution (from difficulty_levels.md)
        self.TARGET_DISTRIBUTION = {
            0: 0.10,  # 10% - Support
            1: 0.15,  # 15% - Confidence
            2: 0.30,  # 30% - Baseline (MASTERY)
            3: 0.25,  # 25% - Stretch (MASTERY)
            4: 0.20   # 20% - Challenge (MASTERY)
        }
        
        # Define which interaction types work for which cognitive verbs
        self.INTERACTION_TYPE_COMPATIBILITY = {
            "partition": ["Click", "Drag and Drop", "Input"],
            "identify": ["Multiple Choice", "Multiple Select", "Click"],
            "recognize": ["Multiple Choice", "Multiple Select", "Click"],
            "shade": ["Shade", "Click"],
            "count": ["Input", "Multiple Choice"],
            "compare": ["Multiple Choice", "Click", "Drag and Drop"],
            "apply": ["Input", "Drag and Drop", "Multiple Choice"],
            "divide": ["Click", "Drag and Drop", "Input"],
        }
        
        # Questions requiring answer_choices
        self.NEEDS_ANSWER_CHOICES = {"Multiple Choice", "Multiple Select"}
    
    def execute(self, input_data, **kwargs):
        """Execute validation on generated questions"""
        
        validation_report = {
            "status": "pass",
            "total_questions": 0,
            "total_goals": 0,
            "warnings": [],
            "errors": [],
            "suggestions": []
        }
        
        if "goals" in input_data:
            goals_data = input_data["goals"]
            validation_report["total_goals"] = len(goals_data)
            
            for goal_group in goals_data:
                goal_id = goal_group["goal_id"]
                questions = goal_group["questions"]
                validation_report["total_questions"] += len(questions)
                
                # Validate this goal's questions
                self._validate_goal_questions(goal_id, questions, validation_report)
        
        # Determine overall status
        if validation_report["errors"]:
            validation_report["status"] = "fail"
        elif validation_report["warnings"]:
            validation_report["status"] = "warning"
        
        # Print summary
        self._print_summary(validation_report)
        
        # Return original data plus validation report
        return {
            **input_data,
            "validation": validation_report
        }
    
    def _validate_goal_questions(self, goal_id: int, questions: List[Dict], report: Dict):
        """Validate questions for a specific goal"""
        
        # Check for variety
        interaction_types_used = [q.get("interaction_type") for q in questions]
        visual_contexts = [q.get("visual_context", "").lower() for q in questions]
        difficulty_levels = [q.get("difficulty_level") for q in questions]
        
        # 1. Check for repeated interaction types
        if len(interaction_types_used) != len(set(interaction_types_used)):
            duplicates = [t for t in interaction_types_used if interaction_types_used.count(t) > 1]
            report["warnings"].append({
                "goal_id": goal_id,
                "type": "repeated_interaction_type",
                "message": f"Goal {goal_id}: Repeated interaction types: {set(duplicates)}",
                "severity": "medium"
            })
        
        # 2. Check for similar visual contexts (same shape/number appearing multiple times)
        visual_words = [set(vc.split()) for vc in visual_contexts]
        for i, words1 in enumerate(visual_words):
            for j, words2 in enumerate(visual_words[i+1:], i+1):
                overlap = len(words1 & words2) / max(len(words1), len(words2))
                if overlap > 0.6:  # More than 60% similar
                    report["warnings"].append({
                        "goal_id": goal_id,
                        "type": "similar_visual_context",
                        "message": f"Goal {goal_id}: Questions {i+1} and {j+1} have very similar visual contexts",
                        "severity": "low"
                    })
        
        # 3. Check difficulty progression
        if difficulty_levels == sorted(difficulty_levels):
            report["suggestions"].append({
                "goal_id": goal_id,
                "type": "good_difficulty_progression",
                "message": f"Goal {goal_id}: ✓ Good difficulty progression from easy to hard"
            })
        else:
            report["warnings"].append({
                "goal_id": goal_id,
                "type": "difficulty_progression",
                "message": f"Goal {goal_id}: Difficulty levels don't progress smoothly: {difficulty_levels}",
                "severity": "low"
            })
        
        # 4. Validate each question
        for i, question in enumerate(questions, 1):
            self._validate_single_question(goal_id, i, question, report)
    
    def _validate_single_question(self, goal_id: int, q_num: int, question: Dict, report: Dict):
        """Validate a single question"""
        
        # Check required fields
        required_fields = [
            "question_text", "interaction_type", "difficulty_level", 
            "question_type", "cognitive_verb", "visual_context", 
            "correct_answer", "explanation", "vocabulary_reinforced"
        ]
        
        missing_fields = [f for f in required_fields if f not in question]
        if missing_fields:
            report["errors"].append({
                "goal_id": goal_id,
                "question_num": q_num,
                "type": "missing_fields",
                "message": f"Goal {goal_id}, Q{q_num}: Missing fields: {missing_fields}",
                "severity": "high"
            })
        
        # Validate interaction type
        interaction_type = question.get("interaction_type")
        if interaction_type and interaction_type not in self.VALID_INTERACTION_TYPES:
            report["errors"].append({
                "goal_id": goal_id,
                "question_num": q_num,
                "type": "invalid_interaction_type",
                "message": f"Goal {goal_id}, Q{q_num}: Invalid interaction type '{interaction_type}'",
                "severity": "high"
            })
        
        # Check interaction type compatibility with cognitive verb
        cognitive_verb = question.get("cognitive_verb", "").lower()
        if cognitive_verb in self.INTERACTION_TYPE_COMPATIBILITY:
            compatible_types = self.INTERACTION_TYPE_COMPATIBILITY[cognitive_verb]
            if interaction_type not in compatible_types:
                report["warnings"].append({
                    "goal_id": goal_id,
                    "question_num": q_num,
                    "type": "incompatible_interaction",
                    "message": f"Goal {goal_id}, Q{q_num}: '{interaction_type}' may not work well for '{cognitive_verb}'. Consider: {compatible_types}",
                    "severity": "medium"
                })
        
        # Check if explanation actually explains the learning goal
        explanation = question.get("explanation", "").lower()
        if explanation and len(explanation) < 50:
            report["warnings"].append({
                "goal_id": goal_id,
                "question_num": q_num,
                "type": "short_explanation",
                "message": f"Goal {goal_id}, Q{q_num}: Explanation is too short (< 50 chars)",
                "severity": "low"
            })
        
        # Check if question text is actually a question or instruction
        question_text = question.get("question_text", "")
        if question_text and not any(indicator in question_text.lower() for indicator in 
                                      ["?", "click", "select", "choose", "shade", "draw", "show", "drag"]):
            report["warnings"].append({
                "goal_id": goal_id,
                "question_num": q_num,
                "type": "unclear_question",
                "message": f"Goal {goal_id}, Q{q_num}: Question text may not clearly indicate what to do",
                "severity": "medium"
            })
    
    def _print_summary(self, report: Dict):
        """Print validation summary"""
        status_emoji = {
            "pass": "✅",
            "warning": "⚠️",
            "fail": "❌"
        }
        
        print(f"\n  {status_emoji[report['status']]} VALIDATION {report['status'].upper()}")
        print(f"  📊 Validated {report['total_questions']} questions across {report['total_goals']} goals")
        
        if report["errors"]:
            print(f"\n  ❌ {len(report['errors'])} ERRORS:")
            for error in report["errors"][:5]:  # Show first 5
                print(f"     • {error['message']}")
            if len(report["errors"]) > 5:
                print(f"     ... and {len(report['errors']) - 5} more errors")
        
        if report["warnings"]:
            print(f"\n  ⚠️  {len(report['warnings'])} WARNINGS:")
            for warning in report["warnings"][:5]:  # Show first 5
                print(f"     • {warning['message']}")
            if len(report["warnings"]) > 5:
                print(f"     ... and {len(report['warnings']) - 5} more warnings")
        
        if report["suggestions"]:
            print(f"\n  💡 {len(report['suggestions'])} SUGGESTIONS:")
            for suggestion in report["suggestions"][:3]:
                print(f"     • {suggestion['message']}")


# Test it
if __name__ == "__main__":
    print("Testing QuestionValidator...\n")
    
    validator = QuestionValidator()
    
    # Sample test data
    test_data = {
        "metadata": {"total_questions": 3},
        "goals": [
            {
                "goal_id": 1,
                "goal_text": "Test goal",
                "questions": [
                    {
                        "id": 1,
                        "question_text": "Click to divide the bar into 2 parts.",
                        "interaction_type": "Click",
                        "difficulty_level": 0,
                        "question_type": "procedural",
                        "cognitive_verb": "divide",
                        "visual_context": "A rectangle bar",
                        "correct_answer": "Click once",
                        "explanation": "This teaches partitioning by having students physically divide a shape.",
                        "vocabulary_reinforced": ["partition"]
                    },
                    {
                        "id": 2,
                        "question_text": "Click to divide the bar into 4 parts.",
                        "interaction_type": "Click",  # Repeated!
                        "difficulty_level": 1,
                        "question_type": "procedural",
                        "cognitive_verb": "divide",
                        "visual_context": "A rectangle bar",  # Similar!
                        "correct_answer": "Click three times",
                        "explanation": "This teaches partitioning.",  # Short!
                        "vocabulary_reinforced": ["partition"]
                    }
                ]
            }
        ]
    }
    
    result = validator.execute(test_data)
    
    print("\n" + "=" * 70)
    print("Validation report:")
    print(f"Status: {result['validation']['status']}")
    print(f"Errors: {len(result['validation']['errors'])}")
    print(f"Warnings: {len(result['validation']['warnings'])}")
