"""
Pipeline - Core pipeline functionality

Provides Step class and run_pipeline function for chaining prompts together.
"""
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict
import sys

# Add core directory to path
core_dir = Path(__file__).parent
if str(core_dir) not in sys.path:
    sys.path.insert(0, str(core_dir))

from prompt_builder import PromptBuilderV2


class Step:
      """A single step in a pipeline"""

      def __init__(
          self,
          prompt_name: str,
          variables: Dict = None,
          input_file: str = None,
          output_file: str = None
      ):
          """
          Args:
              prompt_name: Name of the prompt to run
              variables: Static variables for this step
              input_file: Path to input file to load (supports auto-chaining from previous step)
              output_file: Path to save output file (enables human-in-loop editing)
          """
          self.prompt_name = prompt_name
          self.variables = variables or {}
          self.input_file = input_file
          self.output_file = output_file


def run_pipeline(
      steps: List[Step],
      initial_variables: Dict = None,
      module_number: int = None,
      path_letter: str = None,
      output_dir: str = None,
      verbose: bool = True
  ) -> Dict:
      """Run a pipeline of steps with file I/O support

      Args:
          steps: List of Step objects to execute
          initial_variables: Variables available to all steps
          module_number: Module number for context
          path_letter: Path letter for context
          output_dir: Directory for output files (default: outputs/pipeline_TIMESTAMP)
          verbose: Enable verbose logging

      Returns:
          Dict with final_output and metadata
      """
      if initial_variables is None:
          initial_variables = {}

      # Create output directory
      if output_dir is None:
          timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
          output_dir = f"outputs/pipeline_{timestamp}"

      output_dir_path = Path(output_dir)
      output_dir_path.mkdir(parents=True, exist_ok=True)

      builder = PromptBuilderV2(module_number, path_letter, verbose)

      # Project root for path resolution
      project_root = Path(__file__).parent.parent

      last_output = None
      last_output_file = None

      if verbose:
          print(f"\n{'='*70}")
          print(f"RUNNING PIPELINE")
          print(f"Steps: {len(steps)}")
          print(f"Output Directory: {output_dir_path}")
          print(f"{'='*70}")

      for i, step in enumerate(steps, 1):
          if verbose:
              print(f"\n[STEP {i}/{len(steps)}] {step.prompt_name}")

          step_vars = initial_variables.copy()
          step_vars.update(step.variables)

          # Auto-chain: If input_file is None, use previous step's output_file
          input_file = step.input_file
          if input_file is None and last_output_file is not None:
              input_file = last_output_file
              if verbose:
                  print(f"  [AUTO-CHAIN] Using previous output: {input_file}")
                  
          # Load input file if specified
          input_content = None
          if input_file:
              input_path = _resolve_input_path(input_file, output_dir_path, project_root)
              if verbose:
                  print(f"  [LOAD] Reading: {input_path}")
              try:
                  with open(input_path, 'r', encoding='utf-8') as f:
                      input_content = f.read()
                  if verbose:
                      print(f"  [OK] Loaded {len(input_content)} chars")
              except Exception as e:
                  print(f"  [ERROR] Failed to load input file: {e}")
                  raise
          # Run the prompt with input_content passed separately
          output = builder.run(step.prompt_name, step_vars, input_content=input_content)
          last_output = output

          # Save output file if specified
          if step.output_file:
              output_path = output_dir_path / step.output_file
              output_path.parent.mkdir(parents=True, exist_ok=True)

              with open(output_path, 'w', encoding='utf-8') as f:
                  f.write(output)

              last_output_file = step.output_file

              if verbose:
                  print(f"  [SAVE] Wrote {len(output)} chars to: {step.output_file}")

      if verbose:
          print(f"\n{'='*70}")
          print(f"PIPELINE COMPLETE")
          print(f"{'='*70}")

      return {
          'final_output': last_output,
          'output_dir': str(output_dir_path),
          'last_output_file': last_output_file
      }

def _resolve_input_path(input_file: str, output_dir: Path, project_root: Path) -> Path:
    """Resolve input file path with fallback chain

    Resolution order:
    1. Absolute path → use as-is
    2. Relative to output_dir (for chained files)
    3. Relative to project root
    4. As-is (will fail if not found)
    """
    input_path = Path(input_file)

    # 1. Absolute path
    if input_path.is_absolute():
        return input_path

    # 2. Relative to output_dir (chained files)
    output_relative = output_dir / input_file
    if output_relative.exists():
        return output_relative

    # 3. Relative to project root
    project_relative = project_root / input_file
    if project_relative.exists():
        return project_relative

    # 4. Use as-is (will error if doesn't exist)
    return input_path
