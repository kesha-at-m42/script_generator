"""
Prompt V2 - Simplified prompt class and builder with caching support

Key improvements:
1. Clean Prompt class instead of dictionaries
2. Simplified doc loading with fallback chain: module/path -> module -> docs
3. Auto-loading prompts from prompts folder
4. Prompt caching support for 90% cost reduction
5. Variable substitution in all text fields
6. Support for both list and dict format in module_ref
"""

from pathlib import Path
from typing import List, Dict, Optional, Union
from datetime import datetime
import sys
import importlib


class Prompt:
    """Represents a prompt with its components"""

    def __init__(
        self,
        role: str = None,
        instructions: str = None,
        doc_refs: List[str] = None,
        examples: List[Dict] = None,
        output_structure: str = None,
        prefill: str = None,
        module_ref: Union[List[str], Dict[str, str]] = None,
        template_ref: Union[List[str], Dict[str, str]] = None,
        # Caching settings
        cache_docs: bool = True,
        cache_ttl: str = "5m",
        # API parameters (defaults, can be overridden by pipeline)
        temperature: float = None,
        max_tokens: int = None,
        stop_sequences: List[str] = None
    ):
        """
        Args:
            role: System role/identity for Claude (supports variable substitution)
            instructions: The actual task to perform (supports variable substitution)
            doc_refs: List of documentation file names to reference
            examples: List of example outputs with format [{"description": "...", "output": "..."}]
            output_structure: Expected output schema/format (supports variable substitution)
            prefill: Template for prefilling assistant response (supports variable substitution)
            module_ref: Fields to fetch from modules.py. Can be:
                        - List of field paths: ["vocabulary", "phases.0.phase_name"]
                        - Dict mapping variable names to paths: {"phase_name": "phases.0.phase_name"}
            template_ref: Fields to fetch from problem templates (supports list or dict)
            cache_docs: Enable prompt caching for doc_refs (default: True)
            cache_ttl: Cache time-to-live: "5m" or "1h" (default: "5m")
            temperature: Sampling temperature 0.0-1.0 (default: None = use pipeline default)
            max_tokens: Maximum tokens to generate (default: None = use pipeline default)
            stop_sequences: Custom stop sequences (default: None)
        """
        self.role = role
        self.instructions = instructions or ""
        self.doc_refs = doc_refs or []
        self.examples = examples or []
        self.output_structure = output_structure
        self.prefill = prefill

        # Normalize module_ref and template_ref to dict format
        if isinstance(module_ref, list):
            # Convert list to dict where key = value (simple format)
            self.module_ref = {field: field for field in module_ref}
        elif isinstance(module_ref, set):
            # Handle set format with colon syntax: {"vocabulary", "phase:phases.0"}
            self.module_ref = {}
            for item in module_ref:
                if ':' in item:
                    # Parse "var:path" format
                    var, path = item.split(':', 1)
                    self.module_ref[var] = path
                else:
                    # Simple field reference
                    self.module_ref[item] = item
        elif isinstance(module_ref, dict):
            self.module_ref = module_ref
        else:
            self.module_ref = {}

        if isinstance(template_ref, list):
            self.template_ref = {field: field for field in template_ref}
        elif isinstance(template_ref, dict):
            self.template_ref = template_ref
        else:
            self.template_ref = {}

        # Caching settings
        self.cache_docs = cache_docs
        self.cache_ttl = cache_ttl

        # API parameters
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.stop_sequences = stop_sequences or []

    def to_dict(self) -> Dict:
        """Convert to dictionary for backwards compatibility"""
        return {
            "role": self.role,
            "instructions": self.instructions,
            "doc_refs": self.doc_refs,
            "examples": self.examples,
            "output_structure": self.output_structure,
            "prefill": self.prefill,
            "module_ref": self.module_ref,
            # "template_ref": self.template_ref,
            "cache_docs": self.cache_docs,
            "cache_ttl": self.cache_ttl,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stop_sequences": self.stop_sequences
        }


class PromptBuilderV2:
    """Builds prompts with automatic prompt loading, variable resolution, and caching support"""

    def __init__(self, module_number: int = None, path_letter: str = None, verbose: bool = False):
        self.module_number = module_number
        self.path_letter = path_letter
        self.verbose = verbose

        # Import path_manager
        from path_manager import get_project_paths, get_module_paths

        # Base directories
        paths = get_project_paths()
        self.project_root = paths['project_root']
        self.docs_dir = paths['docs']
        self.modules_dir = paths['modules']
        self.prompts_dir = paths['prompts']

        # Build module paths
        if module_number is not None and path_letter:
            self.module_path = f"module{module_number}/path{path_letter.lower()}"
            self.module_only_path = f"module{module_number}"
        else:
            self.module_path = None
            self.module_only_path = None

        # Add prompts directory to Python path for imports
        if str(self.prompts_dir) not in sys.path:
            sys.path.insert(0, str(self.prompts_dir))

    def build(self, prompt_name: str, variables: Dict = None, input_content: str = None, save_prompt_to: str = None) -> Dict:
        """Build complete prompt with caching support

        Args:
            prompt_name: Name of the prompt (e.g., "godot_formatter")
            variables: Optional dict of variables to substitute in instructions
            input_content: Content to use as <input> in system prompt (from pipeline input_file)
            save_prompt_to: Optional path to save the prompt to (for debugging/review)

        Returns:
            Dict with {system, user_message, prefill, api_params}
        """
        if variables is None:
            variables = {}

        if self.verbose:
            print(f"\n{'='*70}")
            print(f"Building prompt: {prompt_name}")
            print(f"{'='*70}")

        # Load prompt definition
        prompt = self._load_prompt(prompt_name)

        # Auto-fetch module data if specified
        if self.module_number and prompt.module_ref:
            variables = self._fetch_module_data(prompt.module_ref, variables)

        # # Auto-fetch template data if specified
        # if self.module_number and prompt.template_ref:
        #     goal_id = variables.get("goal_id")
        #     if goal_id:
        #         # Convert to int if string
        #         if isinstance(goal_id, str):
        #             try:
        #                 goal_id = int(goal_id)
        #             except ValueError:
        #                 if self.verbose:
        #                     print(f"  [WARN] goal_id '{goal_id}' is not a valid integer")
        #                 goal_id = None

        #         if goal_id:
        #             variables = self._fetch_template_data(prompt.template_ref, goal_id, variables)
        #     elif self.verbose:
        #         print(f"  [WARN] template_ref specified but goal_id not found in variables")

        # Build system blocks (for caching)
        # Order: Role -> Reference Docs -> Task Instructions -> Examples -> Output Structure (all static)
        system_blocks = []

        # 1. Role & Context (static)
        if prompt.role:
            role_text = self._substitute_variables(prompt.role, variables)
            system_blocks.append(
                self._create_block(
                    text=role_text,
                    block_type="role",
                    purpose="Establishes AI role and task context"
                )
            )

        # 2. Reference Documentation (static, cacheable)
        if prompt.doc_refs:
            doc_blocks = self._load_docs_as_blocks(prompt.doc_refs)
            system_blocks.extend(doc_blocks)

        # 3. Task Instructions (static, cacheable)
        if prompt.instructions:
            instructions_text = self._substitute_variables(prompt.instructions, variables)
            system_blocks.append(
                self._create_block(
                    text=instructions_text,
                    block_type="instructions",
                    purpose="Step-by-step task instructions"
                )
            )

        # 4. Examples (static, cacheable)
        if prompt.examples:
            examples_text = self._format_examples(prompt.examples, variables)
            system_blocks.append(
                self._create_block(
                    text=f"<examples>\n{examples_text}\n</examples>",
                    block_type="examples",
                    purpose="Demonstration of expected output format"
                )
            )

        # 5. Output Structure (static, cacheable)
        if prompt.output_structure:
            structure_text = self._substitute_variables(prompt.output_structure, variables)
            system_blocks.append(
                self._create_block(
                    text=f"<output_structure>\n{structure_text}\n</output_structure>",
                    block_type="output_schema",
                    purpose="Defines expected output structure"
                )
            )

        # 6. Add cache_control to last block (if caching enabled)
        # All system blocks are now static and cacheable
        if prompt.cache_docs and system_blocks:
            cache_control = {"type": "ephemeral"}
            if prompt.cache_ttl == "1h":
                cache_control["ttl"] = "1h"
            system_blocks[-1]["cache_control"] = cache_control

        # 7. Build user message (dynamic - just the input data)
        # User message contains ONLY the input content that changes per request
        if input_content:
            user_message = f"<input>\n{input_content}\n</input>"
        else:
            user_message = ""

        # 8. Handle prefill
        final_prefill = None
        if prompt.prefill:
            final_prefill = self._substitute_variables(prompt.prefill, variables).rstrip()

        # 9. API parameters
        api_params = {}
        if prompt.temperature is not None:
            api_params["temperature"] = prompt.temperature
        if prompt.max_tokens is not None:
            api_params["max_tokens"] = prompt.max_tokens
        if prompt.stop_sequences:
            api_params["stop_sequences"] = prompt.stop_sequences

        if self.verbose:
            print(f"  [OK] Built prompt with {len(system_blocks)} system blocks")
            if final_prefill:
                print(f"  [OK] Prefill: {len(final_prefill)} chars")
        # Save prompt to file if requested
        if save_prompt_to:
            self._save_prompt_to_file(
                save_path=save_prompt_to,
                prompt_name=prompt_name,
                system_blocks=system_blocks,
                user_message=user_message,
                prefill=final_prefill,
                api_params=api_params
            )

        return {
            "system": system_blocks,
            "user_message": user_message,
            "prefill": final_prefill,
            "api_params": api_params
        }

    def _format_examples(self, examples: List[Dict], variables: Dict) -> str:
        """Format examples with variable substitution"""
        formatted = []

        for i, example in enumerate(examples, 1):
            example_text = f"Example {i}:\n"
            if "description" in example:
                desc = self._substitute_variables(example["description"], variables)
                example_text += f"{desc}\n\n"
            if "output" in example:
                output = self._substitute_variables(example["output"], variables)
                example_text += output
            formatted.append(example_text)

        return "\n\n---\n\n".join(formatted)

    def _load_prompt(self, prompt_name: str) -> Prompt:
        """Load prompt definition from prompts folder

        Looks for a constant named {PROMPT_NAME}_PROMPT in {prompt_name}.py
        Example: godot_formatter.py should contain GODOT_FORMATTER_PROMPT
        """
        if self.verbose:
            print(f"  Loading prompt definition: {prompt_name}")

        try:
            # Import the module
            module = importlib.import_module(prompt_name)

            # Build expected constant name (e.g., "godot_formatter" -> "GODOT_FORMATTER_PROMPT")
            constant_name = f"{prompt_name.upper()}_PROMPT"

            # Get the prompt object
            if hasattr(module, constant_name):
                prompt = getattr(module, constant_name)
                if self.verbose:
                    print(f"  [OK] Loaded {constant_name}")
                return prompt
            else:
                raise AttributeError(f"Prompt file '{prompt_name}.py' does not contain '{constant_name}'")

        except ImportError as e:
            raise FileNotFoundError(f"Could not find prompt file: {prompt_name}.py") from e

    def _load_docs_as_blocks(self, doc_refs: List[str]) -> List[Dict]:
        """Load documentation as separate blocks for granular caching

        Each doc becomes its own system block for efficient caching.
        Fallback chain: module/path -> module -> docs

        Returns:
            List of system blocks (dicts with type and text)
        """
        blocks = []

        for doc_ref in doc_refs:
            content = self._load_single_doc(doc_ref)
            if content:
                tag = Path(doc_ref).stem
                blocks.append(
                    self._create_block(
                        text=f"<{tag}>\n{content}\n</{tag}>",
                        block_type="reference_doc",
                        block_name=doc_ref,
                        purpose="Reference documentation"
                    )
                )
            elif self.verbose:
                print(f"  [WARN] Doc not found: {doc_ref}")

        return blocks

    def _create_block(self, text: str, block_type: str, block_name: str = None,
                      cacheable: bool = True, purpose: str = None,
                      add_context_header: bool = True) -> Dict:
        """Create a block with semantic metadata and optional context header

        Args:
            text: The actual text content of the block
            block_type: Type of block (role|reference_doc|input|examples|output_schema|instructions)
            block_name: Optional name for the block (e.g., filename for docs)
            cacheable: Whether this block should be cacheable (default: True)
            purpose: Optional human-readable description of block purpose
            add_context_header: Whether to add a contextual header to the text (default: True)

        Returns:
            Dict with type, text, and metadata fields
        """
        # Add contextual header to help Claude understand block structure
        final_text = text
        if add_context_header:
            header = self._get_context_header(block_type, block_name)
            if header:
                final_text = f"{header}\n\n{text}"

        block = {
            "type": "text",
            "text": final_text,
            "metadata": {
                "block_type": block_type,
                "cacheable": cacheable
            }
        }

        if block_name:
            block["metadata"]["block_name"] = block_name
        if purpose:
            block["metadata"]["purpose"] = purpose

        return block

    def _get_context_header(self, block_type: str, block_name: str = None) -> str:
        """Generate contextual header for a block

        Args:
            block_type: Type of block
            block_name: Optional name (e.g., filename for docs)

        Returns:
            Header string or empty string if no header needed
        """
        if block_type == "role":
            return "# ROLE & CONTEXT"
        elif block_type == "reference_doc":
            if block_name:
                return f"# REFERENCE DOCUMENTATION: {block_name}"
            return "# REFERENCE DOCUMENTATION"
        elif block_type == "input":
            return "# INPUT DATA"
        elif block_type == "examples":
            return "# EXAMPLES"
        elif block_type == "output_schema":
            return "# OUTPUT STRUCTURE"
        elif block_type == "instructions":
            return "# TASK INSTRUCTIONS"
        else:
            return ""

    def _load_docs(self, doc_refs: List[str]) -> str:
        """Load documentation with fallback chain (legacy method)

        Returns combined string for backwards compatibility.
        Use _load_docs_as_blocks for caching support.
        """
        sections = []

        for doc_ref in doc_refs:
            content = self._load_single_doc(doc_ref)
            if content:
                tag = Path(doc_ref).stem
                sections.append(f"<{tag}>\n{content}\n</{tag}>")
            elif self.verbose:
                print(f"  [WARN] Doc not found: {doc_ref}")

        return "\n\n".join(sections)

    def _load_single_doc(self, doc_ref: str) -> Optional[str]:
        """Load a single doc with fallback chain"""
        from path_manager import resolve_doc_path

        if self.verbose:
            print(f"    Resolving doc: {doc_ref}")

        resolved_path = resolve_doc_path(
            doc_ref,
            module_number=self.module_number,
            path_letter=self.path_letter,
            required=False
        )

        if resolved_path and resolved_path.exists():
            with open(resolved_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if self.verbose:
                print(f"    [OK] Loaded from: {resolved_path}")
            return content

        if self.verbose:
            print(f"    [WARN] Not found: {doc_ref}")
        return None

    def _fetch_module_data(self, module_ref_mapping: Dict[str, str], variables: Dict) -> Dict:
        """Fetch module data fields using module_utils

        Args:
            module_ref_mapping: Dict mapping variable names to field paths
                                e.g., {"phase_name": "phases.0.phase_name", "vocab": "vocabulary"}
            variables: Existing variables dict to update
        """
        from path_manager import get_project_paths

        paths = get_project_paths()
        utils_path = paths['utils']
        if str(utils_path) not in sys.path:
            sys.path.insert(0, str(utils_path))

        from module_utils import get_module_field

        if self.verbose:
            print(f"  [FETCH] Fetching module data: {list(module_ref_mapping.keys())}")

        for var_name, field_path in module_ref_mapping.items():
            # Skip if already provided
            if var_name in variables:
                if self.verbose:
                    print(f"     --> Skipping '{var_name}' (already provided)")
                continue

            try:
                field_value = get_module_field(self.module_number, field_path, required=False)
                if field_value is not None:
                    variables[var_name] = field_value
                    if self.verbose:
                        if field_path != var_name:
                            print(f"     [OK] Fetched '{var_name}' from '{field_path}'")
                        else:
                            print(f"     [OK] Fetched '{var_name}'")
                else:
                    if self.verbose:
                        print(f"     [WARN] Field '{field_path}' not found")
            except Exception as e:
                print(f"     [ERROR] Error fetching '{field_path}': {e}")

        return variables

    def _fetch_template_data(self, template_ref_fields: List[str], goal_id: int, variables: Dict) -> Dict:
        """Fetch problem template data fields"""
        from path_manager import get_project_paths

        paths = get_project_paths()
        utils_path = paths['utils']
        if str(utils_path) not in sys.path:
            sys.path.insert(0, str(utils_path))

        from problem_template_utils import get_fields_by_reference

        if self.verbose:
            print(f"  [FETCH] Fetching template data: {template_ref_fields}")

        try:
            fetched_fields = get_fields_by_reference(
                self.module_number,
                goal_id,
                template_ref_fields,
                required=False
            )

            for field_name, field_value in fetched_fields.items():
                if field_name in variables:
                    if self.verbose:
                        print(f"     --> Skipping '{field_name}' (already provided)")
                    continue

                if field_value is not None:
                    variables[field_name] = field_value
                    if self.verbose:
                        print(f"     [OK] Fetched '{field_name}'")
                else:
                    if self.verbose:
                        print(f"     [WARN] Field '{field_name}' not found")

        except Exception as e:
            print(f"     [ERROR] Error fetching template fields: {e}")

        return variables

    def run(self, prompt_name: str, variables: Dict = None, input_content: str = None, model: str = None, save_prompt_to: str = None) -> str:
        """Build and execute a prompt in one call

        Args:
            prompt_name: Name of the prompt to run
            variables: Variables for substitution
            input_content: Content to use as <input> in system prompt
            model: Claude model to use (e.g., "claude-opus-4-5-20251101"). If None, uses default

        Returns:
            Claude's response text
        """
        # Import here to avoid circular dependency
        import sys
        from pathlib import Path

        # Add core directory to path if needed
        core_dir = Path(__file__).parent
        if str(core_dir) not in sys.path:
            sys.path.insert(0, str(core_dir))

        from claude_client import ClaudeClient

        # Build the prompt using existing build() method
        built_prompt = self.build(prompt_name, variables, input_content=input_content, save_prompt_to=save_prompt_to)

        # Create client and execute
        client = ClaudeClient()

        response = client.generate(
            system=built_prompt['system'],
            user_message=built_prompt['user_message'],
            prefill=built_prompt.get('prefill'),
            model=model,
            **built_prompt['api_params']
        )

        if self.verbose:
            stats = client.get_stats()
            print(f"\n{'='*70}")
            print(f"USAGE STATS")
            print(f"{'='*70}")
            for key, value in stats.items():
                print(f"  {key}: {value}")

        return response

    def _substitute_variables(self, text: str, variables: Dict) -> str:
        """Safely substitute variables in text

        Handles templates that contain literal braces (like JSON examples)
        and variables with special characters like {phases[0]}.
        Uses direct string replacement instead of .format() to avoid parsing issues.
        """
        if not variables or not text:
            return text

        result = text

        # Sort keys by length (longest first) to handle overlapping variable names
        sorted_keys = sorted(variables.keys(), key=len, reverse=True)

        for key in sorted_keys:
            # Replace {key} with the actual value
            placeholder = '{' + key + '}'
            if placeholder in result:
                # Convert value to string
                value = variables[key]
                if isinstance(value, (list, dict)):
                    import json
                    value_str = json.dumps(value, ensure_ascii=False)
                else:
                    value_str = str(value)

                result = result.replace(placeholder, value_str)

        return result

    def _get_blocks_by_type(self, blocks: List[Dict], block_type: str) -> List[Dict]:
        """Get all blocks of a specific type

        Args:
            blocks: List of system blocks
            block_type: Type to filter by (e.g., 'reference_doc', 'role', 'examples')

        Returns:
            List of blocks matching the specified type
        """
        return [b for b in blocks
                if b.get("metadata", {}).get("block_type") == block_type]

    def _get_cached_blocks(self, blocks: List[Dict]) -> List[Dict]:
        """Get all blocks with cache_control

        Args:
            blocks: List of system blocks

        Returns:
            List of blocks that have cache_control applied
        """
        return [b for b in blocks if "cache_control" in b]

    def _save_prompt_to_file(self, save_path: str, prompt_name: str, system_blocks: list, user_message: str, prefill: str, api_params: dict):
          """Save the complete prompt to a file in human-readable format

          Args:
              save_path: Path to save the prompt file
              prompt_name: Name of the prompt
              system_blocks: List of system blocks
              user_message: User message content
              prefill: Prefill content (if any)
              api_params: API parameters
          """
          try:
              save_path = Path(save_path)
              save_path.parent.mkdir(parents=True, exist_ok=True)

              with open(save_path, 'w', encoding='utf-8') as f:
                  f.write(f"# Prompt: {prompt_name}\n")
                  f.write(f"# Generated: {datetime.now().isoformat()}\n")
                  f.write("="*70 + "\n\n")

                  # Write API parameters
                  f.write("## API Parameters\n")
                  for key, value in api_params.items():
                      f.write(f"- {key}: {value}\n")
                  f.write("\n" + "="*70 + "\n\n")

                  # Write system blocks
                  f.write("## System Prompt\n\n")
                  for i, block in enumerate(system_blocks, 1):
                      metadata = block.get("metadata", {})
                      block_type = metadata.get("block_type", "unknown")
                      block_name = metadata.get("block_name", "")
                      purpose = metadata.get("purpose", "")

                      # Block header with type
                      header = f"### Block {i}"
                      if block_type != "unknown":
                          header += f": {block_type.replace('_', ' ').title()}"
                      if block_name:
                          header += f" ({block_name})"

                      f.write(f"{header}\n")

                      # Purpose and cacheable status
                      if purpose:
                          f.write(f"Purpose: {purpose}\n")
                      if metadata.get("cacheable"):
                          f.write(f"Cacheable: Yes\n")

                      # Cache control indicator
                      if 'cache_control' in block:
                          f.write(f"*[CACHED: {block['cache_control']}]*\n")

                      f.write(f"\n{block['text']}\n\n")
                      f.write("-"*70 + "\n\n")

                  # Write user message
                  f.write("## User Message\n\n")
                  f.write(user_message)
                  f.write("\n\n" + "="*70 + "\n\n")

                  # Write prefill if exists
                  if prefill:
                      f.write("## Prefill\n\n")
                      f.write(prefill)
                      f.write("\n\n")

              if self.verbose:
                  print(f"  [SAVE] Saved prompt to: {save_path}")

          except Exception as e:
              if self.verbose:
                  print(f"  [WARN] Failed to save prompt: {e}")


# Test it
if __name__ == "__main__":
    print("PromptBuilderV2 Test")
    print("="*70)

    # Test loading a prompt
    builder = PromptBuilderV2(module_number=1, path_letter='b', verbose=True)

    try:
        result = builder.run('test', variables={'name': 'Hazel'})
        print("\n" + "="*70)
        print("RESPONSE:")
        print("="*70)
        print(result)
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()