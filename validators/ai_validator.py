"""
AI Validator - Uses Claude to perform semantic quality evaluation
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# Add core to path for ClaudeClient
sys.path.insert(0, str(Path(__file__).parent.parent / "core"))
from claude_client import ClaudeClient


class AIValidator:
    """Uses Claude to evaluate semantic quality of generated content"""

    def __init__(self, verbose: bool = False):
        self.client = ClaudeClient()
        self.verbose = verbose
        self.prompts_dir = Path(__file__).parent / "prompts"

    def _load_prompt_template(self, validation_type: str) -> str:
        """Load validation prompt template"""
        prompt_file = self.prompts_dir / f"{validation_type}_validator.txt"
        with open(prompt_file, 'r', encoding='utf-8') as f:
            return f.read()

    def _fill_template(self, template: str, variables: dict) -> str:
        """Fill template with variables"""
        result = template
        for key, value in variables.items():
            placeholder = "{{" + key + "}}"
            result = result.replace(placeholder, str(value))
        return result

    def validate_question(self, question: dict, module_data: dict) -> Tuple[bool, float, dict]:
        """
        Use AI to validate question quality

        Returns:
            (is_valid, score_0_to_100, detailed_results)
        """
        try:
            # Load and fill template
            template = self._load_prompt_template("question")

            # Prepare misconceptions text
            misconceptions_text = "\n".join([
                f"- {m['misconception']}: {m['description']}"
                for m in module_data.get('misconceptions', [])
            ])

            variables = {
                'module_name': module_data.get('module_name', 'Unknown'),
                'grade_level': module_data.get('grade_level', 'Unknown'),
                'goal': question.get('goal', 'Unknown'),
                'difficulty_level': question.get('difficulty_level', 'Unknown'),
                'cognitive_type': question.get('cognitive_type', 'Unknown'),
                'misconceptions': misconceptions_text,
                'question_json': json.dumps(question, indent=2)
            }

            prompt = self._fill_template(template, variables)

            # Call Claude
            response = self.client.generate(
                prompt,
                max_tokens=2000,
                temperature=0.3
            )

            # Parse response
            if "```json" in response:
                json_start = response.find("```json") + 7
                json_end = response.find("```", json_start)
                response_json = response[json_start:json_end].strip()
            else:
                response_json = response.strip()

            result = json.loads(response_json)

            # Extract score (0-100 scale)
            overall_score = result.get('overall_score', 0) * 10  # Convert 0-10 to 0-100

            # Determine validity
            is_valid = result.get('recommendation', 'REJECT').upper() == 'ACCEPT'

            return is_valid, overall_score, result

        except Exception as e:
            if self.verbose:
                print(f"    ⚠️  AI validation error: {e}")
            # Return neutral score on error
            return True, 50.0, {'error': str(e)}

    def validate_interaction(self, sequence: dict, module_data: dict) -> Tuple[bool, float, dict]:
        """
        Use AI to validate interaction quality

        Returns:
            (is_valid, score_0_to_100, detailed_results)
        """
        try:
            template = self._load_prompt_template("interaction")

            misconceptions_text = "\n".join([
                f"- {m['misconception']}: {m['description']}"
                for m in module_data.get('misconceptions', [])
            ])

            tangibles = module_data.get('available_visuals', {}).get('tangibles', [])
            tangibles_text = ", ".join(tangibles) if tangibles else "Not specified"

            variables = {
                'module_name': module_data.get('module_name', 'Unknown'),
                'grade_level': module_data.get('grade_level', 'Unknown'),
                'goal': sequence.get('goal', 'Unknown'),
                'misconceptions': misconceptions_text,
                'tangibles': tangibles_text,
                'sequence_json': json.dumps(sequence, indent=2)
            }

            prompt = self._fill_template(template, variables)

            response = self.client.generate(
                prompt,
                max_tokens=2500,
                temperature=0.3
            )

            # Parse response
            if "```json" in response:
                json_start = response.find("```json") + 7
                json_end = response.find("```", json_start)
                response_json = response[json_start:json_end].strip()
            else:
                response_json = response.strip()

            result = json.loads(response_json)

            overall_score = result.get('overall_score', 0) * 10
            is_valid = result.get('recommendation', 'REJECT').upper() == 'ACCEPT'

            return is_valid, overall_score, result

        except Exception as e:
            if self.verbose:
                print(f"    ⚠️  AI validation error: {e}")
            return True, 50.0, {'error': str(e)}

    def validate_batch(self, items: List[dict], validation_type: str, module_data: dict) -> Dict:
        """
        Validate a batch of items using AI

        Args:
            items: List of items to validate
            validation_type: 'question' or 'interaction'
            module_data: Module context

        Returns:
            {
                'total': int,
                'valid': int,
                'results': [{'item': dict, 'is_valid': bool, 'score': float, 'details': dict}]
            }
        """
        validator_map = {
            'question': self.validate_question,
            'interaction': self.validate_interaction
        }

        validator = validator_map.get(validation_type)
        if not validator:
            raise ValueError(f"Unknown validation type: {validation_type}")

        results = []
        for idx, item in enumerate(items):
            if self.verbose:
                print(f"    Validating item {idx + 1}/{len(items)}...", end=' ')

            is_valid, score, details = validator(item, module_data)

            if self.verbose:
                status = "✓" if is_valid else "✗"
                print(f"{status} (score: {score:.1f}/100)")

            results.append({
                'item': item,
                'is_valid': is_valid,
                'score': score,
                'details': details
            })

        valid_count = sum(1 for r in results if r['is_valid'])
        avg_score = sum(r['score'] for r in results) / len(results) if results else 0

        if self.verbose:
            print(f"\n  AI Validation ({validation_type}):")
            print(f"    Total: {len(items)}")
            print(f"    Valid: {valid_count}")
            print(f"    Invalid: {len(items) - valid_count}")
            print(f"    Avg Score: {avg_score:.1f}/100")

        return {
            'total': len(items),
            'valid': valid_count,
            'invalid': len(items) - valid_count,
            'results': results
        }
