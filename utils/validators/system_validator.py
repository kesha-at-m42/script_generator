"""
System Validator - Deterministic structural and business rule checks
"""

import json
from typing import Dict, List, Tuple


class SystemValidator:
    """Performs fast, deterministic validation checks"""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def validate_question(self, question: dict, module_data: dict = None) -> Tuple[bool, float, List[str]]:
        """
        Validate a question from question_generator step

        Returns:
            (is_valid, score_0_to_100, issues_list)
        """
        issues = []
        score = 100.0

        # Required fields check
        required_fields = ['question_id', 'goal_id', 'question_text', 'difficulty_level', 'cognitive_type']
        for field in required_fields:
            if field not in question or not question[field]:
                issues.append(f"Missing or empty required field: {field}")
                score -= 20

        if not issues:  # Only do deeper checks if basic structure is valid
            # Difficulty level validation
            difficulty = question.get('difficulty_level', 0)
            if not isinstance(difficulty, int) or difficulty < 1 or difficulty > 3:
                issues.append(f"Invalid difficulty_level: {difficulty} (must be 1-3)")
                score -= 15

            # Cognitive type validation
            valid_cognitive_types = ['RECALL', 'APPLY', 'UNDERSTAND', 'CREATE', 'ANALYZE', 'EVALUATE']
            cognitive_type = question.get('cognitive_type', '').upper()
            if cognitive_type not in valid_cognitive_types:
                issues.append(f"Invalid cognitive_type: {cognitive_type}")
                score -= 10

            # Question text validation
            question_text = question.get('question_text', '')
            if len(question_text) < 10:
                issues.append("Question text too short (< 10 chars)")
                score -= 15
            elif len(question_text) > 500:
                issues.append("Question text too long (> 500 chars)")
                score -= 5

            # Variables validation (should have some fractions or numbers)
            variables = question.get('variables', {})
            if not variables or len(variables) == 0:
                issues.append("No variables defined for question")
                score -= 10

            # Fractions validation
            fractions = question.get('fractions', [])
            if not isinstance(fractions, list):
                issues.append("Fractions field should be a list")
                score -= 10
            elif len(fractions) == 0:
                issues.append("No fractions specified")
                score -= 5

        # Determine if valid (pass if score >= 50)
        is_valid = score >= 50 and len(issues) == 0

        return is_valid, max(0, score), issues

    def validate_interaction(self, sequence: dict, module_data: dict = None) -> Tuple[bool, float, List[str]]:
        """
        Validate an interaction sequence from interaction_designer step

        Returns:
            (is_valid, score_0_to_100, issues_list)
        """
        issues = []
        score = 100.0

        # Required fields
        required_fields = ['sequence_id', 'question_id', 'goal_id', 'interactions']
        for field in required_fields:
            if field not in sequence or sequence[field] is None:
                issues.append(f"Missing required field: {field}")
                score -= 20

        if 'interactions' in sequence and isinstance(sequence['interactions'], list):
            interactions = sequence['interactions']

            if len(interactions) == 0:
                issues.append("No interactions in sequence")
                score -= 30

            for idx, interaction in enumerate(interactions):
                # Check interaction type
                interaction_type = interaction.get('type', '')
                valid_types = ['select', 'multi_select', 'click', 'text_input', 'dialogue', 'instruction']

                if interaction_type not in valid_types:
                    issues.append(f"Interaction {idx}: Invalid type '{interaction_type}'")
                    score -= 10
                    continue

                # Validate choice-based interactions
                if interaction_type in ['select', 'multi_select', 'click']:
                    choices = interaction.get('choices', [])
                    tangible = interaction.get('tangible', {})

                    if not choices or len(choices) < 2:
                        issues.append(f"Interaction {idx}: {interaction_type} must have at least 2 choices")
                        score -= 15

                    if not tangible or not isinstance(tangible, dict):
                        issues.append(f"Interaction {idx}: {interaction_type} missing tangible")
                        score -= 10
                    else:
                        # Check tangible structure
                        if 'type' not in tangible:
                            issues.append(f"Interaction {idx}: Tangible missing 'type' field")
                            score -= 5

                    # Check that choices have required fields
                    for choice_idx, choice in enumerate(choices):
                        if not isinstance(choice, dict):
                            issues.append(f"Interaction {idx}, choice {choice_idx}: Invalid choice format")
                            score -= 5
                            continue

                        if 'text' not in choice or not choice['text']:
                            issues.append(f"Interaction {idx}, choice {choice_idx}: Missing choice text")
                            score -= 5

                        if 'correct' not in choice:
                            issues.append(f"Interaction {idx}, choice {choice_idx}: Missing 'correct' field")
                            score -= 5

                    # Check that at least one choice is correct
                    has_correct = any(c.get('correct', False) for c in choices)
                    if not has_correct:
                        issues.append(f"Interaction {idx}: No correct choice marked")
                        score -= 15

                # Validate dialogue interactions
                elif interaction_type == 'dialogue':
                    if 'text' not in interaction or not interaction['text']:
                        issues.append(f"Interaction {idx}: Dialogue missing text")
                        score -= 10

        # Determine validity
        is_valid = score >= 50 and len([i for i in issues if 'Missing required field' in i]) == 0

        return is_valid, max(0, score), issues

    def validate_remediation(self, sequence: dict, module_data: dict = None) -> Tuple[bool, float, List[str]]:
        """
        Validate a remediation sequence

        Returns:
            (is_valid, score_0_to_100, issues_list)
        """
        issues = []
        score = 100.0

        # Check that remediation events exist
        if 'interactions' not in sequence:
            issues.append("Missing interactions field")
            return False, 0, issues

        interactions = sequence['interactions']
        has_remediation = False

        for interaction in interactions:
            # Check for remediation in choice-based interactions
            if interaction.get('type') in ['select', 'multi_select', 'click']:
                choices = interaction.get('choices', [])
                for choice in choices:
                    if 'remediation_event' in choice and choice['remediation_event']:
                        has_remediation = True

                        # Validate remediation event structure
                        remediation = choice['remediation_event']
                        if not isinstance(remediation, dict):
                            issues.append("Invalid remediation_event structure")
                            score -= 10
                        elif 'event_name' not in remediation:
                            issues.append("Remediation event missing event_name")
                            score -= 10

        if not has_remediation:
            issues.append("No remediation events found in sequence")
            score -= 50

        is_valid = score >= 50
        return is_valid, max(0, score), issues

    def validate_batch(self, items: List[dict], validation_type: str, module_data: dict = None) -> Dict:
        """
        Validate a batch of items

        Args:
            items: List of items to validate
            validation_type: 'question', 'interaction', or 'remediation'
            module_data: Optional module context

        Returns:
            {
                'total': int,
                'valid': int,
                'invalid': int,
                'results': [{'item': dict, 'is_valid': bool, 'score': float, 'issues': list}]
            }
        """
        validator_map = {
            'question': self.validate_question,
            'interaction': self.validate_interaction,
            'remediation': self.validate_remediation
        }

        validator = validator_map.get(validation_type)
        if not validator:
            raise ValueError(f"Unknown validation type: {validation_type}")

        results = []
        for item in items:
            is_valid, score, issues = validator(item, module_data)
            results.append({
                'item': item,
                'is_valid': is_valid,
                'score': score,
                'issues': issues
            })

        valid_count = sum(1 for r in results if r['is_valid'])

        if self.verbose:
            print(f"\n  System Validation ({validation_type}):")
            print(f"    Total: {len(items)}")
            print(f"    Valid: {valid_count}")
            print(f"    Invalid: {len(items) - valid_count}")
            print(f"    Avg Score: {sum(r['score'] for r in results) / len(results):.1f}/100")

        return {
            'total': len(items),
            'valid': valid_count,
            'invalid': len(items) - valid_count,
            'results': results
        }
