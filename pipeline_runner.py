"""
Interactive Pipeline Runner
Chains prompts together with intuitive configuration
"""

import sys
import os
import json
import time
from pathlib import Path
from datetime import datetime

# Add paths
sys.path.insert(0, str(Path(__file__).parent / "core"))

from prompt_builder import PromptBuilder
from claude_client import ClaudeClient


class PipelineRunner:
    """Runs a sequence of prompts, chaining outputs as inputs"""

    def __init__(self, module_number: int, path_letter: str, output_dir: str = None, verbose: bool = False):
        self.module_number = module_number
        self.path_letter = path_letter
        self.verbose = verbose

        # Create output directory
        if output_dir is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_dir = f"outputs/pipeline_module{module_number}_path{path_letter}_{timestamp}"

        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize builders and client
        self.builder = PromptBuilder(module_number=module_number, path_letter=path_letter, verbose=verbose)
        self.client = ClaudeClient()

        if self.verbose:
            print(f"\n{'='*70}")
            print(f"Pipeline Runner - Module {module_number} Path {path_letter}")
            print(f"Output Directory: {self.output_dir}")
            print(f"{'='*70}\n")

    def run_step_item_by_item(self, step_config: dict) -> dict:
        """Process items one at a time (question-by-question, sequence-by-sequence)"""
        name = step_config["name"]
        prompt_id = step_config["prompt_id"]
        input_file = step_config["input_file"]
        output_file = step_config["output_file"]
        item_key = step_config["item_key"]
        item_variable = step_config.get("item_variable")  # Optional if extract_fields is used
        collect_key = step_config["collect_key"]
        extract_fields = step_config.get("extract_fields")  # NEW: Dict mapping var names to field paths
        variables = step_config.get("variables", {})
        max_tokens = step_config.get("max_tokens", 8000)
        temperature = step_config.get("temperature", 0.3)
        limit = step_config.get("limit")

        if self.verbose:
            print(f"{'='*70}")
            print(f"STEP: {name} (ITEM-BY-ITEM MODE)")
            print(f"{'='*70}")
            print(f"  Prompt ID: {prompt_id}")
            print(f"  Input: {input_file}")

        # Create subfolder for this step's prompts and raw outputs
        step_dir = self.output_dir / prompt_id
        step_dir.mkdir(exist_ok=True)

        # Load input
        try:
            # Resolve placeholders in input_file path
            resolved_input_file = input_file
            if "{module_number}" in input_file:
                resolved_input_file = input_file.replace("{module_number}", str(self.module_number))
            if "{path_letter}" in resolved_input_file:
                resolved_input_file = resolved_input_file.replace("{path_letter}", self.path_letter)

            input_path = Path(resolved_input_file)

            # Smart path resolution:
            # 1. If absolute, use as-is
            # 2. If file exists at the given path, use as-is
            # 3. Otherwise, treat as relative to output_dir
            if not input_path.is_absolute():
                if input_path.exists():
                    # File exists at this relative path
                    pass
                else:
                    # Try relative to output_dir
                    input_path = self.output_dir / resolved_input_file

            with open(input_path, 'r', encoding='utf-8') as f:
                input_data = json.load(f)
            items = input_data.get(item_key, [])
            num_items = len(items)
            if self.verbose:
                print(f"  ✓ Loaded {num_items} items")
        except Exception as e:
            print(f"  ✗ Error loading input: {e}")
            return {"success": False, "error": str(e)}

        num_to_process = min(limit, num_items) if limit else num_items
        if self.verbose:
            print(f"    DEBUG: limit={limit}, num_items={num_items}, num_to_process={num_to_process}")
            print(f"    Processing {num_to_process} item(s)...")
            print(f"    ")

        all_collected = []
        for idx in range(num_to_process):
            item = items[idx]
            item_id = item.get('id', item.get('question_id', item.get('sequence_id', idx + 1)))
            if self.verbose:
                print(f"  [{idx+1}/{num_to_process}] Item {item_id}...")

            try:
                prompt_variables = variables.copy()

                # Field extraction mode: extract multiple fields from item
                if extract_fields:
                    for var_name, field_path in extract_fields.items():
                        # Special case: None field_path means pass entire item
                        if field_path is None:
                            field_value = item
                        else:
                            field_value = item.get(field_path)

                        # Everything becomes a string - prompts only handle strings anyway
                        if field_value is None or field_value == "":
                            prompt_variables[var_name] = ""
                        elif isinstance(field_value, str):
                            prompt_variables[var_name] = field_value
                        else:
                            # Complex types (dict, list, etc) → JSON string
                            prompt_variables[var_name] = json.dumps(field_value)
                else:
                    # Legacy mode: pass entire item as one variable
                    item_json = json.dumps(item, indent=2)
                    prompt_variables[item_variable] = item_json

                # Generate dynamic prefill if needed (for remediation_generator, etc.)
                from utils.prefill_generator import generate_prefill
                prefill_text = generate_prefill(prompt_id, item)
                if prefill_text:
                    prompt_variables["prefill_sequence"] = prefill_text
                    if self.verbose:
                        print(f"      ✓ Generated dynamic prefill ({len(prefill_text)} chars)")

                # Debug: Print variables being passed
                if self.verbose:
                    print(f"      Variables being passed:")
                    for k, v in prompt_variables.items():
                        v_preview = str(v)[:50] if v else "(empty)"
                        print(f"        {k}: {v_preview}")

                result = self.builder.build_prompt(prompt_id=prompt_id, variables=prompt_variables)
                prompt, prefill = (result if isinstance(result, tuple) else (result, None))
  
                # Save prompt to subfolder
                prompt_file = step_dir / f"item_{idx + 1}_prompt.txt"
                with open(prompt_file, 'w', encoding='utf-8') as f:
                    f.write(prompt)
                    if prefill:
                        f.write(f"\n\n{'='*70}\nPREFILL:\n{'='*70}\n{prefill}")
            except Exception as e:
                print(f"      ✗ Error building prompt: {e}")
                continue

            try:
                response = self.client.generate(prompt, prefill=prefill, max_tokens=max_tokens, temperature=temperature)

                # Save raw response to subfolder
                raw_file = step_dir / f"item_{idx + 1}_raw.txt"
                with open(raw_file, 'w', encoding='utf-8') as f:
                    f.write(response)
            except Exception as e:
                print(f"      ✗ Error generating: {e}")
                continue

            try:
                if "```json" in response:
                    json_start = response.find("```json") + 7
                    json_end = response.find("```", json_start)
                    response_json = response[json_start:json_end].strip()
                else:
                    response_json = response.strip()
                parsed = json.loads(response_json)

                # Apply deterministic post-processing for godot_formatter
                if prompt_id == "godot_formatter":
                    from utils.metadata_mapper import map_to_mastery_metadata
                    from utils.bbcode_formatter import process_godot_sequences
                    from utils.module_utils import get_module_field

                    # Get vocabulary if module_number is set
                    vocabulary_list = None
                    if self.module_number:
                        vocabulary = get_module_field(self.module_number, 'vocabulary', required=False)
                        if vocabulary:
                            vocabulary_list = vocabulary
                            if self.verbose:
                                print(f"      ✓ Loaded vocabulary: {', '.join(vocabulary_list)}")

                    # Apply metadata mapping to each sequence
                    for seq in parsed.get('sequences', []):
                        # Extract fields from original input item for mapping
                        input_fields = {
                            'difficulty': item.get('difficulty', 2),
                            'verb': item.get('verb', 'CREATE'),
                            'goal_id': item.get('goal_id', 1),
                            'goal': item.get('goal', ''),
                            'fractions': item.get('fractions', []),
                            'problem_id': item.get('problem_id', 0)
                        }

                        # Generate correct metadata
                        correct_metadata = map_to_mastery_metadata(input_fields)
                        correct_metadata['problem_id'] = input_fields['problem_id']

                        # Update sequence metadata
                        if 'metadata' not in seq:
                            seq['metadata'] = {}
                        seq['metadata'].update(correct_metadata)

                    # Apply BBCode formatting
                    parsed = process_godot_sequences(parsed, vocabulary_list)

                    if self.verbose:
                        print(f"      ⚙️  Applied metadata mapping and BBCode formatting")

                if collect_key in parsed:
                    collected = parsed[collect_key]
                    if isinstance(collected, list):
                        all_collected.extend(collected)
                        if self.verbose:
                            print(f"      ✓ Collected {len(collected)} item(s)")
                    else:
                        all_collected.append(collected)
                        if self.verbose:
                            print(f"      ✓ Collected 1 item")
                else:
                    all_collected.append(parsed)
                    if self.verbose:
                        print(f"      ✓ Collected response")
            except json.JSONDecodeError as e:
                print(f"      ✗ JSON error: {e}")
                continue

        if self.verbose:
            print(f"  ✓ Total collected: {len(all_collected)}")

        try:
            # Special handling for godot_formatter - wrap with SequencePool structure
            if prompt_id == "godot_formatter":
                output_data = {
                    "@type": "SequencePool",
                    "sequences": all_collected
                }
            else:
                output_data = {collect_key: all_collected}

            output_path = self.output_dir / output_file
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=2)
                f.flush()  # Ensure data is written
                os.fsync(f.fileno())  # Force OS to write to disk
            if self.verbose:
                print(f"  ✓ Saved to: {output_file}")
                print(f"  ✓ Step completed successfully")
            return {"success": True, "output_file": str(output_path), "items_processed": num_to_process, "items_collected": len(all_collected)}
        except Exception as e:
            print(f"  ✗ Error saving: {e}")
            return {"success": False, "error": str(e)}

    def run_step(self, step_config: dict) -> dict:
        """Run a single pipeline step - routes to batch or item-by-item mode - routes to batch or item-by-item mode

        Args:
            step_config: {
                "name": "Question Generator",
                "prompt_id": "question_generator",
                "input_file": None or path to input file,
                "output_file": "questions.json",
                "variables": {} optional additional variables,
                "max_tokens": 8000,
                "temperature": 0.3
            }

        Returns:
            dict with result info
        """
        # Check if item-by-item mode
        processing_mode = step_config.get("processing_mode", "batch")
        if processing_mode == "item_by_item":
            return self.run_step_item_by_item(step_config)

        # Batch mode (default)
        name = step_config["name"]
        prompt_id = step_config["prompt_id"]
        input_file = step_config.get("input_file")
        output_file = step_config["output_file"]
        variables = step_config.get("variables", {})
        max_tokens = step_config.get("max_tokens", 8000)
        temperature = step_config.get("temperature", 0.3)

        if self.verbose:
            print(f"\n{'='*70}")
            print(f"STEP: {name}")
            print(f"{'='*70}")
            print(f"  Prompt ID: {prompt_id}")
            print(f"  Input: {input_file or 'None (first step)'}")
            print(f"  Output: {output_file}")

        # Build prompt
        try:
            if self.verbose:
                print(f"\n  Building prompt...")

            result = self.builder.build_prompt(
                prompt_id=prompt_id,
                input_file_path=str(input_file) if input_file else None,
                variables=variables
            )

            # Handle prefill
            if isinstance(result, tuple):
                prompt, prefill = result
                if self.verbose:
                    print(f"  ✓ Prompt built ({len(prompt):,} chars) with prefill")
            else:
                prompt = result
                prefill = None
                if self.verbose:
                    print(f"  ✓ Prompt built ({len(prompt):,} chars)")

            # Save prompt for inspection
            prompt_file = self.output_dir / f"{prompt_id}_prompt.txt"
            with open(prompt_file, 'w', encoding='utf-8') as f:
                f.write(prompt)
                if prefill:
                    f.write(f"\n\n{'='*70}\nPREFILL:\n{'='*70}\n{prefill}")

            if self.verbose:
                print(f"  ✓ Prompt saved to: {prompt_file.name}")

        except Exception as e:
            print(f"  ✗ Error building prompt: {e}")
            return {"success": False, "error": str(e)}

        # Generate response
        try:
            if self.verbose:
                print(f"\n  Generating response...")

            response = self.client.generate(
                prompt,
                prefill=prefill,
                max_tokens=max_tokens,
                temperature=temperature
            )

            if self.verbose:
                print(f"  ✓ Response received ({len(response):,} chars)")

        except Exception as e:
            print(f"  ✗ Error generating response: {e}")
            return {"success": False, "error": str(e)}

        # Extract JSON if needed
        try:
            if "```json" in response:
                json_start = response.find("```json") + 7
                json_end = response.find("```", json_start)
                response_json = response[json_start:json_end].strip()
            else:
                response_json = response.strip()

            # Validate JSON
            parsed = json.loads(response_json)

            # Save output
            output_path = self.output_dir / output_file
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(parsed, f, indent=2)
                f.flush()  # Ensure data is written
                os.fsync(f.fileno())  # Force OS to write to disk

            if self.verbose:
                print(f"  ✓ Output saved to: {output_file}")
                print(f"  ✓ Step completed successfully")

            return {
                "success": True,
                "output_file": str(output_path),
                "response_length": len(response),
                "json_length": len(response_json)
            }

        except json.JSONDecodeError as e:
            print(f"  ✗ Error parsing JSON: {e}")
            # Save raw response for debugging
            error_file = self.output_dir / f"{prompt_id}_error_response.txt"
            with open(error_file, 'w', encoding='utf-8') as f:
                f.write(response)
            print(f"  ✗ Raw response saved to: {error_file.name}")
            return {"success": False, "error": f"JSON parsing failed: {e}"}

    def run_pipeline(self, steps: list) -> dict:
        """Run a complete pipeline

        Args:
            steps: List of step configs (see run_step)

        Returns:
            dict with summary of all steps
        """
        results = []

        for i, step_config in enumerate(steps, 1):
            if self.verbose:
                print(f"\n{'#'*70}")
                print(f"# PIPELINE STEP {i}/{len(steps)}")
                print(f"{'#'*70}")

            result = self.run_step(step_config)
            results.append({
                "step": step_config["name"],
                "result": result
            })

            # Stop if step failed
            if not result.get("success"):
                print(f"\n⚠️  Pipeline stopped at step {i} due to error")
                break

            # Update input_file for next step if needed
            if i < len(steps):
                next_step = steps[i]
                if next_step.get("input_file") is None and result.get("output_file"):
                    # Auto-chain: next step takes this step's output
                    next_step["input_file"] = result["output_file"]

                    # Verify the file exists and is readable
                    output_file_path = Path(result["output_file"])
                    max_wait_time = 5  # seconds
                    wait_interval = 0.1  # seconds
                    elapsed = 0

                    while elapsed < max_wait_time:
                        if output_file_path.exists():
                            try:
                                # Try to read the file to ensure it's complete
                                with open(output_file_path, 'r', encoding='utf-8') as f:
                                    json.load(f)
                                if self.verbose:
                                    print(f"  ✓ Verified output file is ready for next step")
                                break
                            except (json.JSONDecodeError, IOError):
                                # File exists but not ready yet
                                time.sleep(wait_interval)
                                elapsed += wait_interval
                        else:
                            time.sleep(wait_interval)
                            elapsed += wait_interval

                    if elapsed >= max_wait_time:
                        print(f"  ⚠️  Warning: Output file verification timed out")
                    elif not output_file_path.exists():
                        print(f"  ✗ Error: Output file does not exist: {output_file_path}")

        # Summary
        if self.verbose:
            print(f"\n{'='*70}")
            print(f"PIPELINE SUMMARY")
            print(f"{'='*70}")
            for item in results:
                status = "✓ SUCCESS" if item["result"]["success"] else "✗ FAILED"
                print(f"{status}: {item['step']}")

            successful = sum(1 for item in results if item["result"]["success"])
            print(f"\nCompleted: {successful}/{len(steps)} steps")
            print(f"Output directory: {self.output_dir}")

        return {
            "output_dir": str(self.output_dir),
            "steps": results,
            "success": all(item["result"]["success"] for item in results)
        }


# Example pipeline configurations
EXAMPLE_PIPELINES = {
    "full": [
        {
            "name": "Question Generator",
            "prompt_id": "question_generator",
            "processing_mode": "item_by_item",  # Process each goal separately
            "input_file": "inputs/modules/module{module_number}/problem_templates.json",
            "item_key": "goals",
            "extract_fields": { 
                "goal_id": "id",
                "goal": "text",
                "difficulty_level": "difficulty_level",
                "example_questions": "example_questions",
                "variables": "variables",
                "cognitive_type": "cognitive_type"  # May not exist in all goals
            },
            "collect_key": "questions",
            "output_file": "questions.json",
            "max_tokens": 16000,
            "temperature": 1.0,
            "limit":1
        },
        {
        "name": "Interaction Designer",
        "prompt_id": "interaction_designer",
        "processing_mode": "item_by_item",
        "item_key": "questions",
        "extract_fields": {
            "question_data": None,  # Pass entire item as JSON
            "goal_id": "goal_id",    # Extract goal_id for template fetching
            "difficulty": "difficulty_level",
            "verb": "cognitive_type",
            "question_id": "question_id",
            "goal": "goal"
        
        },
        "collect_key": "sequences",
        "input_file": None,
        "output_file": "interactions.json",
        "max_tokens": 12000
        },
        {
            "name": "Remediation Generator",
            "prompt_id": "remediation_generator",
            "processing_mode": "item_by_item",  # Process each sequence separately
            "item_key": "sequences",
             "extract_fields": {
                "interactions_context": None,  # Pass entire item as JSON
                "goal_id": "goal_id"           # Extract goal_id for template fetching
             },  # Must match variable in prompt template
            "collect_key": "sequences",
            "input_file": None,  # Will be auto-set from previous step
            "output_file": "remediation.json",
            "max_tokens": 16000
        },
        {
            "name": "Godot Formatter",
            "prompt_id": "godot_formatter",
            "processing_mode": "item_by_item",  # Process each sequence separately (like test)
            "item_key": "sequences",
            "item_variable": "complete_interaction_sequences",  # Must match variable in prompt template
            "collect_key": "sequences",  # Extract sequences array from each response
            "input_file": None,  # Will be auto-set from previous step
            "output_file": "final.json",
            "max_tokens": 16000
        }
    ],

    "remediation_only": [
        {
            "name": "Remediation Generator",
            "prompt_id": "remediation_generator",
            "processing_mode": "item_by_item",
            "item_key": "sequences",
             "extract_fields": {
                "interactions_context": None,  # Pass entire item as JSON
                "goal_id": "goal_id"           # Extract goal_id for template fetching
             }, 
            "item_variable": "interactions_context",  # Must match variable in prompt template
            "collect_key": "sequences",
            "input_file": "C:\\git\\script_generator\\outputs\\pipeline_module1_pathb_20251105_171624\\interactions.json",  # Specify existing file
            "output_file": "remediation.json",
            "max_tokens": 16000
        }
    ],

    "questions_only": [
        {
            "name": "Question Generator",
            "prompt_id": "question_generator",
            "processing_mode": "item_by_item",
            "input_file": "inputs/modules/module{module_number}/problem_templates.json",
            "item_key": "goals",
            "extract_fields": { 
                "goal_id": "id",
                "goal": "text",
                "difficulty_level": "difficulty_level",
                "example_questions": "example_questions",
                "variables": "variables",
                "cognitive_type": "cognitive_type"  # May not exist in all goals
            },
            "collect_key": "questions",
            "output_file": "questions.json",
            "max_tokens": 16000,
            "temperature": 1.0,
        }
    ],

    "interactions_only": [
    {
        "name": "Interaction Designer",
        "prompt_id": "interaction_designer",
        "processing_mode": "item_by_item",
        "item_key": "sequences",
        "extract_fields": {
            "question_data": None,  # Pass entire item as JSON
            "goal_id": "goal_id",    # Extract goal_id for template fetching
            "difficulty": "difficulty_level",
            "verb": "cognitive_type",
            "question_id": "question_id",
            "goal": "goal"
        
        },
        "collect_key": "sequences",
        "input_file": "C:\\git\\script_generator\\outputs\\pipeline_module1_pathb_20251105_164511\\questions.json",
        "output_file": "interactions.json",
        "max_tokens": 12000
        }
    ],
    "godot_format_only": [
        {
            "name": "Godot Formatter",
            "prompt_id": "godot_formatter",
            "processing_mode": "item_by_item",  # Process each sequence separately (like test)
            "item_key": "sequences",
            "item_variable": "complete_interaction_sequences",  # Must match variable in prompt template
            "collect_key": "sequences",  # Extract sequences array from each response
            "input_file": "C:\\git\\script_generator\\outputs\\pipeline_module1_pathb_20251104_151523\\remediation.json",
            "output_file": "final.json",
            "max_tokens": 16000
        }
    ]

}


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run a pipeline of prompts")
    parser.add_argument("--module", type=int, help="Module number")
    parser.add_argument("--path", type=str, help="Path letter (a, b, c)")
    parser.add_argument("--pipeline", type=str,
                       help="Pipeline name (full, remediation_only) or 'custom'")
    parser.add_argument("--input", type=str, help="Input file for first step (optional)")
    parser.add_argument("--output-dir", type=str, help="Output directory (optional)")

    args = parser.parse_args()

    # Interactive prompts if arguments not provided
    module_number = args.module
    if module_number is None:
        while True:
            try:
                module_input = input("Enter module number: ").strip()
                module_number = int(module_input)
                break
            except ValueError:
                print("❌ Please enter a valid number")

    path_letter = args.path
    if path_letter is None:
        while True:
            path_input = input("Enter path letter (a/b/c): ").strip().lower()
            if path_input in ['a', 'b', 'c']:
                path_letter = path_input
                break
            else:
                print("❌ Please enter 'a', 'b', or 'c'")

    pipeline_name = args.pipeline
    if pipeline_name is None:
        print("\nAvailable pipelines:")
        for idx, name in enumerate(EXAMPLE_PIPELINES.keys(), 1):
            print(f"  {idx}. {name}")

        while True:
            pipeline_input = input(f"Select pipeline [1-{len(EXAMPLE_PIPELINES)}] or name: ").strip()

            # Check if input is a number
            if pipeline_input.isdigit():
                choice = int(pipeline_input)
                if 1 <= choice <= len(EXAMPLE_PIPELINES):
                    pipeline_name = list(EXAMPLE_PIPELINES.keys())[choice - 1]
                    break
            # Check if input is a pipeline name
            elif pipeline_input in EXAMPLE_PIPELINES:
                pipeline_name = pipeline_input
                break
            else:
                print(f"❌ Invalid choice. Enter 1-{len(EXAMPLE_PIPELINES)} or a pipeline name")

    # Get pipeline config
    if pipeline_name in EXAMPLE_PIPELINES:
        steps = EXAMPLE_PIPELINES[pipeline_name]

        # Override input file if provided
        if args.input and steps[0].get("input_file") is None:
            steps[0]["input_file"] = args.input
    else:
        print(f"❌ Unknown pipeline: {pipeline_name}")
        print(f"Available pipelines: {', '.join(EXAMPLE_PIPELINES.keys())}")
        sys.exit(1)

    # Run pipeline
    runner = PipelineRunner(
        module_number=module_number,
        path_letter=path_letter,
        output_dir=args.output_dir,
        verbose=True
    )

    result = runner.run_pipeline(steps)

    # Exit with appropriate code
    sys.exit(0 if result["success"] else 1)
