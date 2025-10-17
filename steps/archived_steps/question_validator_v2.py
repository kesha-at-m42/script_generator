"""
Question Validator V2 - Validates and filters questions for quality
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.pipeline import Step
from typing import Dict, List, Any
from rich.console import Console

console = Console()


class QuestionValidatorV2(Step):
    """Validates questions for quality, variety, and technical feasibility.
    Can filter low-quality questions and keep only the best."""
    
    def __init__(self):
        super().__init__(name="Question Validator V2", prompt_id="question_validator_v2")
        
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
    
    def execute(self, input_data, filter_low_quality=True, keep_per_goal=4, **kwargs):
        """Execute validation and optional filtering on generated questions
        
        Args:
            input_data: Question data with "goals" array
            filter_low_quality: If True, filter out low quality questions
            keep_per_goal: Number of best questions to keep per goal (only if filtering)
        """
        console.print("\n[bold cyan]Validating and scoring questions...[/bold cyan]")
        
        validation_report = {
            "status": "pass",
            "total_questions_generated": 0,
            "total_questions_kept": 0,
            "total_goals": 0,
            "warnings": [],
            "errors": [],
            "suggestions": [],
            "quality_stats": {}
        }
        
        if "goals" not in input_data:
            validation_report["errors"].append({
                "type": "missing_data",
                "message": "Missing 'goals' in data structure",
                "severity": "high"
            })
            validation_report["status"] = "fail"
            return {**input_data, "validation": validation_report}
        
        goals_data = input_data["goals"]
        validation_report["total_goals"] = len(goals_data)
        
        filtered_goals = []
        all_scores = []
        
        for goal_group in goals_data:
            goal_id = goal_group["goal_id"]
            goal_text = goal_group.get("goal_text", "")
            questions = goal_group["questions"]
            
            validation_report["total_questions_generated"] += len(questions)
            
            # Score each question
            scored_questions = []
            for question in questions:
                score = self._score_question(question, goal_text, validation_report)
                scored_questions.append({
                    "question": question,
                    "score": score
                })
                all_scores.append(score)
            
            # Sort by score (highest first)
            scored_questions.sort(key=lambda x: x["score"], reverse=True)
            
            # Keep best questions if filtering
            if filter_low_quality:
                num_to_keep = min(keep_per_goal, len(scored_questions))
                kept_questions = scored_questions[:num_to_keep]
                
                # Add quality metadata
                filtered_goal = {
                    **goal_group,
                    "questions": [sq["question"] for sq in kept_questions],
                    "quality_metadata": {
                        "questions_generated": len(scored_questions),
                        "questions_kept": num_to_keep,
                        "questions_filtered": len(scored_questions) - num_to_keep,
                        "avg_score": sum(sq["score"] for sq in kept_questions) / num_to_keep,
                        "score_range": f"{kept_questions[-1]['score']:.0f}-{kept_questions[0]['score']:.0f}"
                    }
                }
                
                validation_report["total_questions_kept"] += num_to_keep
                
                if len(scored_questions) > num_to_keep:
                    validation_report["suggestions"].append({
                        "goal_id": goal_id,
                        "type": "filtered_questions",
                        "message": f"Goal {goal_id}: Kept top {num_to_keep}/{len(scored_questions)} questions "
                                 f"(avg score: {filtered_goal['quality_metadata']['avg_score']:.1f}/100)"
                    })
            else:
                # Just add scores without filtering
                filtered_goal = {
                    **goal_group,
                    "question_scores": [sq["score"] for sq in scored_questions]
                }
                validation_report["total_questions_kept"] += len(questions)
            
            filtered_goals.append(filtered_goal)
            
            # Validate this goal's kept questions
            kept_questions = filtered_goal["questions"]
            self._validate_goal_variety(goal_id, kept_questions, validation_report)
            self._check_difficulty_distribution(goal_id, kept_questions, validation_report)
        
        # Calculate overall quality stats
        if all_scores:
            validation_report["quality_stats"] = {
                "avg_score": sum(all_scores) / len(all_scores),
                "min_score": min(all_scores),
                "max_score": max(all_scores),
                "total_scored": len(all_scores)
            }
        
        # Determine overall status
        if validation_report["errors"]:
            validation_report["status"] = "fail"
        elif validation_report["warnings"]:
            validation_report["status"] = "warning"
        
        # Print summary
        self._print_summary(validation_report, filter_low_quality)
        
        # Return filtered data with validation report
        return {
            "metadata": {
                "total_goals": validation_report["total_goals"],
                "total_questions": validation_report["total_questions_kept"],
                "questions_per_goal": keep_per_goal if filter_low_quality else "varied",
                "filtered": filter_low_quality,
                "avg_quality_score": validation_report["quality_stats"].get("avg_score", 0)
            },
            "goals": filtered_goals,
            "validation": validation_report
        }
    
    def _score_question(self, question: Dict[str, Any], goal_text: str, 
                       report: Dict[str, Any]) -> float:
        """Score a question's quality (0-100)
        
        Scoring criteria:
        - Completeness: Has all required fields (30 points)
        - Clarity: Question text is clear and specific (20 points)
        - Alignment: Matches goal and difficulty level (25 points)
        - Feasibility: Visual/interaction type is implementable (15 points)
        - Vocabulary: Uses appropriate vocabulary (10 points)
        """
        score = 0.0
        question_text = question.get("question_text", "")
        q_id = question.get("id", "unknown")
        
        # Completeness (30 points)
        required_fields = [
            "question_text", "difficulty_level", "interaction_type",
            "visual_context", "correct_answer", "explanation"
        ]
        has_fields = sum(1 for field in required_fields if question.get(field))
        completeness_score = (has_fields / len(required_fields)) * 30
        score += completeness_score
        
        # Check answer_choices for MC/MS
        interaction_type = question.get("interaction_type", "")
        if interaction_type in self.NEEDS_ANSWER_CHOICES:
            if not question.get("answer_choices"):
                report["errors"].append({
                    "question_id": q_id,
                    "type": "missing_answer_choices",
                    "message": f"Question {q_id}: {interaction_type} missing answer_choices",
                    "severity": "high"
                })
                score -= 10  # Penalty
            elif len(question.get("answer_choices", [])) < 3:
                report["warnings"].append({
                    "question_id": q_id,
                    "type": "insufficient_answer_choices",
                    "message": f"Question {q_id}: Only {len(question.get('answer_choices', []))} answer choices (need 3-4)",
                    "severity": "medium"
                })
                score -= 5
            else:
                score += 5  # Bonus for having answer_choices
        
        # Clarity (20 points)
        clarity_score = 0
        if len(question_text) > 20:
            clarity_score += 5
        if "?" in question_text or any(word in question_text.lower() 
                                       for word in ["click", "select", "shade", "drag"]):
            clarity_score += 5
        if any(word in question_text.lower() for word in ["which", "what", "how", "show"]):
            clarity_score += 5
        if question.get("explanation") and len(question.get("explanation", "")) > 30:
            clarity_score += 5
        score += clarity_score
        
        # Alignment (25 points)
        alignment_score = 0
        difficulty_level = question.get("difficulty_level", 0)
        
        # Check if difficulty matches question complexity
        if difficulty_level == 0 and any(word in question_text.lower() 
                                         for word in ["show", "identify", "click"]):
            alignment_score += 8
        elif difficulty_level in [1, 2] and any(word in question_text.lower() 
                                                 for word in ["which", "what", "partition", "divide"]):
            alignment_score += 8
        elif difficulty_level in [3, 4] and any(word in question_text.lower() 
                                                 for word in ["explain", "why", "compare", "apply"]):
            alignment_score += 8
        
        # Check vocabulary alignment
        vocab_reinforced = question.get("vocabulary_reinforced", [])
        if vocab_reinforced and len(vocab_reinforced) > 0:
            alignment_score += 8
        
        # Check goal alignment (word overlap)
        if goal_text:
            goal_words = set(goal_text.lower().split())
            question_words = set(question_text.lower().split())
            overlap = len(goal_words & question_words)
            if overlap > 0:
                alignment_score += min(overlap * 2, 9)
        
        score += alignment_score
        
        # Feasibility (15 points)
        feasibility_score = 0
        if interaction_type in self.VALID_INTERACTION_TYPES:
            feasibility_score += 8
        
        visual_context = question.get("visual_context", "")
        if visual_context and len(visual_context) > 20:
            feasibility_score += 4
        if "rectangle" in visual_context.lower() or "bar" in visual_context.lower():
            feasibility_score += 3
        
        score += feasibility_score
        
        # Vocabulary (10 points)
        if vocab_reinforced:
            vocab_score = min(len(vocab_reinforced) * 3, 10)
            score += vocab_score
        
        return min(score, 100.0)  # Cap at 100
    
    def _validate_goal_variety(self, goal_id: int, questions: List[Dict], report: Dict):
        """Check variety within a goal's questions"""
        
        interaction_types = [q.get("interaction_type") for q in questions]
        visual_contexts = [q.get("visual_context", "").lower() for q in questions]
        
        # Check for repeated interaction types
        unique_types = len(set(interaction_types))
        if unique_types < len(interaction_types) * 0.75:  # Less than 75% unique
            duplicates = [t for t in interaction_types if interaction_types.count(t) > 1]
            report["warnings"].append({
                "goal_id": goal_id,
                "type": "low_interaction_variety",
                "message": f"Goal {goal_id}: Low interaction type variety - repeated: {set(duplicates)}",
                "severity": "medium"
            })
        
        # Check for very similar visual contexts
        for i, vc1 in enumerate(visual_contexts):
            for j, vc2 in enumerate(visual_contexts[i+1:], i+1):
                words1 = set(vc1.split())
                words2 = set(vc2.split())
                if words1 and words2:
                    overlap = len(words1 & words2) / max(len(words1), len(words2))
                    if overlap > 0.7:  # More than 70% similar
                        report["warnings"].append({
                            "goal_id": goal_id,
                            "type": "similar_visuals",
                            "message": f"Goal {goal_id}: Questions {i+1} and {j+1} have very similar visuals",
                            "severity": "low"
                        })
    
    def _check_difficulty_distribution(self, goal_id: int, questions: List[Dict], report: Dict):
        """Check if difficulty distribution is balanced"""
        
        difficulty_counts = {}
        for q in questions:
            level = q.get("difficulty_level", 0)
            difficulty_counts[level] = difficulty_counts.get(level, 0) + 1
        
        total = len(questions)
        
        # Check if we have good coverage of Levels 2-3 (mastery levels)
        mastery_questions = difficulty_counts.get(2, 0) + difficulty_counts.get(3, 0)
        mastery_percentage = mastery_questions / total if total > 0 else 0
        
        if mastery_percentage < 0.4:  # Less than 40% at mastery levels
            report["warnings"].append({
                "goal_id": goal_id,
                "type": "insufficient_mastery_questions",
                "message": f"Goal {goal_id}: Only {mastery_percentage:.0%} questions at Levels 2-3 (target: 55%)",
                "severity": "medium"
            })
        elif mastery_percentage >= 0.5:
            report["suggestions"].append({
                "goal_id": goal_id,
                "type": "good_mastery_coverage",
                "message": f"Goal {goal_id}: ✓ Good mastery coverage ({mastery_percentage:.0%} at Levels 2-3)"
            })
    
    def _print_summary(self, report: Dict, filtered: bool):
        """Print validation summary"""
        status_emoji = {
            "pass": "✅",
            "warning": "⚠️",
            "fail": "❌"
        }
        
        console.print(f"\n[bold]{status_emoji[report['status']]} VALIDATION {report['status'].upper()}[/bold]")
        console.print(f"  📊 Generated: {report['total_questions_generated']} questions")
        
        if filtered:
            console.print(f"  ✅ Kept: {report['total_questions_kept']} high-quality questions")
            console.print(f"  🗑️  Filtered: {report['total_questions_generated'] - report['total_questions_kept']} lower-quality questions")
        
        if report.get("quality_stats"):
            stats = report["quality_stats"]
            console.print(f"  📈 Quality scores: avg={stats['avg_score']:.1f}, range={stats['min_score']:.0f}-{stats['max_score']:.0f}")
        
        if report["errors"]:
            console.print(f"\n  [bold red]❌ {len(report['errors'])} ERRORS:[/bold red]")
            for error in report["errors"][:5]:
                console.print(f"     • {error['message']}")
            if len(report["errors"]) > 5:
                console.print(f"     ... and {len(report['errors']) - 5} more errors")
        
        if report["warnings"]:
            console.print(f"\n  [yellow]⚠️  {len(report['warnings'])} WARNINGS:[/yellow]")
            for warning in report["warnings"][:5]:
                console.print(f"     • {warning['message']}")
            if len(report["warnings"]) > 5:
                console.print(f"     ... and {len(report['warnings']) - 5} more warnings")
        
        if report["suggestions"] and len(report["suggestions"]) <= 10:
            console.print(f"\n  [green]💡 QUALITY REPORT:[/green]")
            for suggestion in report["suggestions"]:
                console.print(f"     • {suggestion['message']}")


# Test it
if __name__ == "__main__":
    import json
    
    console.print("[bold]Testing QuestionValidatorV2...[/bold]\n")
    
    validator = QuestionValidatorV2()
    
    # Sample test data with varying quality
    test_data = {
        "metadata": {"total_questions": 6},
        "goals": [
            {
                "goal_id": 1,
                "goal_text": "Students will partition rectangles into equal parts",
                "questions": [
                    # High quality question
                    {
                        "id": 1,
                        "question_text": "Click to divide this rectangle into 2 equal parts.",
                        "interaction_type": "Click",
                        "difficulty_level": 0,
                        "question_type": "procedural",
                        "cognitive_verb": "partition",
                        "visual_context": "A horizontal rectangle bar showing 1 whole",
                        "correct_answer": "Click once in the center to create 2 equal parts",
                        "explanation": "This introduces partitioning by having students physically divide a shape into halves, reinforcing the concept of equal parts.",
                        "vocabulary_reinforced": ["partition", "equal parts"]
                    },
                    # Medium quality - missing explanation detail
                    {
                        "id": 2,
                        "question_text": "Which shows 4 equal parts?",
                        "interaction_type": "Multiple Choice",
                        "difficulty_level": 2,
                        "question_type": "conceptual",
                        "cognitive_verb": "recognize",
                        "visual_context": "Three rectangles with different divisions",
                        "correct_answer": "Option B",
                        "explanation": "Shows 4 equal parts.",  # Too short!
                        "vocabulary_reinforced": ["equal parts"],
                        "answer_choices": ["Option A", "Option B", "Option C"]
                    },
                    # Low quality - repeated interaction, similar visual
                    {
                        "id": 3,
                        "question_text": "Click to make 3 parts.",
                        "interaction_type": "Click",  # Repeated!
                        "difficulty_level": 1,
                        "question_type": "procedural",
                        "cognitive_verb": "partition",
                        "visual_context": "A horizontal rectangle bar",  # Similar!
                        "correct_answer": "Click twice",
                        "explanation": "Divide the bar into thirds.",  # Short!
                        "vocabulary_reinforced": []  # Missing vocab!
                    },
                    # High quality mastery question
                    {
                        "id": 4,
                        "question_text": "Select all rectangles that show equal partitioning.",
                        "interaction_type": "Multiple Select",
                        "difficulty_level": 3,
                        "question_type": "conceptual",
                        "cognitive_verb": "identify",
                        "visual_context": "Four rectangles: A (2 equal parts), B (3 unequal parts), C (4 equal parts), D (4 unequal parts)",
                        "correct_answer": "A and C",
                        "explanation": "Equal partitioning means all parts are the same size. Rectangles A and C show equal divisions, while B and D have unequal parts.",
                        "vocabulary_reinforced": ["equal parts", "partition"],
                        "answer_choices": ["Rectangle A", "Rectangle B", "Rectangle C", "Rectangle D"]
                    },
                    # Medium quality - missing answer_choices
                    {
                        "id": 5,
                        "question_text": "Which rectangle is divided into thirds?",
                        "interaction_type": "Multiple Choice",
                        "difficulty_level": 2,
                        "question_type": "conceptual",
                        "cognitive_verb": "identify",
                        "visual_context": "Three rectangles with 2, 3, and 4 parts",
                        "correct_answer": "The middle one",
                        "explanation": "Thirds means divided into 3 equal parts, which is shown in the middle rectangle.",
                        "vocabulary_reinforced": ["thirds"]
                        # Missing answer_choices!
                    },
                    # High quality challenge question
                    {
                        "id": 6,
                        "question_text": "Drag the dividing lines to create 6 equal parts.",
                        "interaction_type": "Drag and Drop",
                        "difficulty_level": 4,
                        "question_type": "application",
                        "cognitive_verb": "apply",
                        "visual_context": "A blank rectangle with 5 movable vertical lines",
                        "correct_answer": "Place 5 lines evenly spaced to create 6 equal sections",
                        "explanation": "Creating 6 equal parts requires 5 dividing lines placed at regular intervals. This challenges students to apply their understanding of equal partitioning to a more complex scenario.",
                        "vocabulary_reinforced": ["equal parts", "partition", "sixths"]
                    }
                ]
            }
        ]
    }
    
    # Test WITH filtering (keep top 4)
    console.print("[bold cyan]Test 1: WITH filtering (keep top 4)[/bold cyan]")
    result1 = validator.execute(test_data, filter_low_quality=True, keep_per_goal=4)
    
    console.print("\n[bold]Kept questions:[/bold]")
    for q in result1["goals"][0]["questions"]:
        console.print(f"  • Q{q['id']}: {q['interaction_type']} (Level {q['difficulty_level']})")
    
    console.print("\n" + "=" * 70)
    
    # Test WITHOUT filtering (just scoring)
    console.print("\n[bold cyan]Test 2: WITHOUT filtering (just scoring)[/bold cyan]")
    result2 = validator.execute(test_data, filter_low_quality=False)
    
    console.print("\n[bold]Question scores:[/bold]")
    for i, score in enumerate(result2["goals"][0]["question_scores"], 1):
        console.print(f"  • Q{i}: {score:.1f}/100")
