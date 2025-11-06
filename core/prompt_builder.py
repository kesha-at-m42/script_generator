"""
Prompt Builder - Centralized prompt management system

Each prompt has 5 components:
1. role - System role/identity for Claude
2. docs - Reference documentation to include
3. examples - Example outputs to guide Claude
4. structure - Required output structure/schema
5. instructions - What to do (the actual task)
"""

from logging import config
from pathlib import Path
from typing import Dict, List, Optional
import sys

# Add prompts directory to path for imports
prompts_path = Path(__file__).parent.parent / "inputs" / "prompts"
if str(prompts_path) not in sys.path:
    sys.path.insert(0, str(prompts_path))


class PromptBuilder:
    """Builds prompts from structured components"""

    def __init__(self, module_number: int = None, path_letter: str = None, verbose: bool = False):
        self.docs_dir = Path(__file__).parent.parent / "inputs" / "docs"
        self.modules_dir = Path(__file__).parent.parent / "inputs" / "modules"
        self.prompts_dir = Path(__file__).parent.parent / "inputs" / "prompts"
        self.module_number = module_number
        self.path_letter = path_letter
        self.verbose = verbose
        
        # Build module path like "module1/pathb" for accessing module-specific docs
        if module_number is not None and path_letter:
            self.module_path = f"module{module_number}/path{path_letter.lower()}"
        else:
            self.module_path = None
    
    def build_prompt(self, prompt_id: str, input_file_path: str = None, variables: Dict = None):
        """Build a complete prompt from components

        Args:
            prompt_id: ID of the prompt to build (e.g., "remediation_generator")
            input_file_path: Optional path to input file from previous pipeline step
            variables: Optional dict of variables to substitute in template

        Returns:
            tuple: (prompt_text, prefill_text) or just prompt_text if no prefill
        """

        # Load prompt config
        config = self._get_prompt_config(prompt_id)

        # Initialize variables dict
        if variables is None:
            variables = {}

        # Auto-load input file if specified
        if input_file_path and config.get("input_variable"):
            input_var = config["input_variable"]
            if input_var not in variables:  # Don't override if already provided
                try:
                    with open(input_file_path, 'r', encoding='utf-8') as f:
                        variables[input_var] = f.read()
                    if self.verbose:
                        print(f"  📄 Loaded input file: {input_file_path} -> {input_var}")
                except Exception as e:
                    print(f"⚠️  Warning: Could not load input file {input_file_path}: {e}")

        # Auto-fetch module data if MODULE_REF is specified
        if self.module_number and config.get("module_ref"):
            variables = self._auto_fetch_module_data(config["module_ref"], variables)

         # Auto-fetch problem template data if PROBLEM_TEMPLATE_REF is specified
        if self.module_number and config.get("problem_template_ref"):
            # Require goal_id in variables for problem template fetching
            goal_id = variables.get("goal_id")
            if goal_id:
                # Convert to int if it's a string
                if isinstance(goal_id, str):
                    try:
                        goal_id = int(goal_id)
                    except ValueError:
                        if self.verbose:
                            print(f"  ⚠️ goal_id '{goal_id}' is not a valid integer")
                        goal_id = None

                if goal_id:
                    variables = self._auto_fetch_problem_template_data(
                        config["problem_template_ref"],
                        goal_id,
                        variables
                    )
            elif self.verbose:
                print(f"  ⚠️ PROBLEM_TEMPLATE_REF specified but goal_id not found in variables")
        
        # Build sections
        sections = []
        
        # 1. Role (if present)
        if config.get("role"):
            sections.append(f"<role>\n{config['role']}\n</role>")
        
        # 2. Documentation references
        if config.get("docs"):
            docs_content = self._load_docs(config["docs"])
            if self.verbose:
                print("Adding document to prompt...")
            sections.append(docs_content)
        
        # 3. Examples
        if config.get("examples"):
            examples_content = self._format_examples(config["examples"])
            sections.append(f"<examples>\n{examples_content}\n</examples>")
        
        # 4. Output structure
        if config.get("structure"):
            sections.append(f"<required_output_format>\n{config['structure']}\n</required_output_format>")
        
        # 5. Instructions (the actual task)
        instructions = config.get("instructions", "")

        # Safe formatting: instructions may contain many literal braces (JSON examples).
        # To avoid KeyError when calling str.format on those literals, escape all
        # braces first, then un-escape only the placeholders we actually provide in
        # `variables` so that only those are substituted.
        if variables:
            # Escape all braces to treat them as literals
            instr_escaped = instructions.replace('{', '{{').replace('}', '}}')

            # Un-escape placeholders that we will provide so format can substitute them
            for key in variables.keys():
                instr_escaped = instr_escaped.replace('{{' + key + '}}', '{' + key + '}')

            try:
                instructions = instr_escaped.format(**variables)
            except KeyError as e:
                print(f"⚠️  Warning: Missing variable in template: {e}")
                print(f"    Available variables: {list(variables.keys())}")
                raise ValueError(f"Template formatting failed: missing variable {e}")
        sections.append(instructions)
        
        final_prompt = "\n\n".join(sections)
        if self.verbose:
            print("Final prompt length:", len(final_prompt))

        # Return with prefill if specified
        prefill = config.get("prefill")
        if prefill:
            # Format prefill with variables if needed
            try:
                prefill = prefill.format(**variables)
                if self.verbose:
                    print(f"Using prefill: {prefill}")
                return final_prompt, prefill
            except KeyError as e:
                if self.verbose:
                    print(f"⚠️  Prefill has missing variable {e}, skipping prefill")
                # Return without prefill if variables are missing
                return final_prompt
        return final_prompt
    
    def _auto_fetch_module_data(self, module_ref_fields: List[str], variables: Dict) -> Dict:
        """Auto-fetch module data fields using module_utils"""
        import sys
        from pathlib import Path
        
        # Add utils directory to path if needed
        utils_path = Path(__file__).parent.parent / "utils"
        if str(utils_path) not in sys.path:
            sys.path.insert(0, str(utils_path))
        
        from module_utils import get_module_field
        
        # Handle case where module_ref_fields might not be a list
        if not isinstance(module_ref_fields, list):
            if self.verbose:
                print(f"  ⚠️ MODULE_REF is not a list, got: {type(module_ref_fields)}")
            return variables

        if self.verbose:
            print(f"  📦 Auto-fetching module data for fields: {module_ref_fields}")

        for field_name in module_ref_fields:
            # Skip if already provided in variables
            if field_name in variables:
                if self.verbose:
                    print(f"     ↪ Skipping '{field_name}' (already provided)")
                continue

            try:
                # Fetch from modules.py
                field_value = get_module_field(self.module_number, field_name, required=False)
                if field_value is not None:
                    variables[field_name] = field_value
                    if self.verbose:
                        print(f"     ✓ Fetched '{field_name}' from module {self.module_number}")
                else:
                    if self.verbose:
                        print(f"     ⚠️ Field '{field_name}' not found in module {self.module_number}")
            except Exception as e:
                print(f"     ✗ Error fetching '{field_name}': {e}")
        
        return variables
    
    def _auto_fetch_problem_template_data(self, problem_template_ref_fields: List[str], goal_id: int, variables: Dict) -> Dict:
        """Auto-fetch problem template data fields using problem_template_utils"""
        import sys
        from pathlib import Path

        # Add utils directory to path if needed
        utils_path = Path(__file__).parent.parent / "utils"
        if str(utils_path) not in sys.path:
            sys.path.insert(0, str(utils_path))

        from problem_template_utils import get_fields_by_reference

        # Handle case where problem_template_ref_fields might not be a list
        if not isinstance(problem_template_ref_fields, list):
            if self.verbose:
                print(f"  ⚠️ PROBLEM_TEMPLATE_REF is not a list, got: {type(problem_template_ref_fields)}")
            return variables

        if self.verbose:
            print(f"  📦 Auto-fetching problem template data for fields: {problem_template_ref_fields}")

        try:
            # Fetch all fields at once using get_fields_by_reference
            fetched_fields = get_fields_by_reference(
                self.module_number,
                goal_id,
                problem_template_ref_fields,
                required=False
            )

            # Add fetched fields to variables (skip if already provided)
            for field_name, field_value in fetched_fields.items():
                if field_name in variables:
                    if self.verbose:
                        print(f"     ↪ Skipping '{field_name}' (already provided)")
                    continue

                if field_value is not None:
                    variables[field_name] = field_value
                    if self.verbose:
                        print(f"     ✓ Fetched '{field_name}' from module {self.module_number}, goal {goal_id}")
                else:
                    if self.verbose:
                        print(f"     ⚠️ Field '{field_name}' not found in problem template")

        except Exception as e:
            print(f"     ✗ Error fetching problem template fields: {e}")

        return variables

    def _get_prompt_config(self, prompt_id: str) -> Dict:
        """Get prompt configuration by ID"""

        if self.verbose:
            print(f"\nDEBUG: Requested prompt_id = '{prompt_id}'")

        # Map prompt IDs to their config methods (don't call them yet!)
        config_methods = {
            "question_generator": self._question_generator_config,
            "interaction_designer": self._interaction_designer_config,
            "remediation_generator": self._remediation_generator_config,
            "godot_formatter": self._godot_formatter_config,
        }

        # Only call the specific config method we need
        if prompt_id in config_methods:
            if self.verbose:
                print(f"DEBUG: Loading config for '{prompt_id}'")
            return config_methods[prompt_id]()  # ← Note the () here - call it now
        else:
            print(f"⚠️  WARNING: Unknown prompt_id '{prompt_id}'")
            return {}
    
    def _load_docs(self, doc_refs: List[str], required: bool = False) -> str:
        """Load documentation files with module-specific override support

        Args:
            doc_refs: List of document references (file paths or embedded dicts)
            required: If True, raises error when doc not found. If False, logs warning.
                     Default is False - docs are optional unless explicitly required.
        """
        sections = []
        missing_docs = []

        for doc_ref in doc_refs:
            if isinstance(doc_ref, dict):
                # Embedded doc content
                title = doc_ref.get("title", "Reference")
                content = doc_ref.get("content", "")
                sections.append(f"<{title.lower().replace(' ', '_')}>\n{content}\n</{title.lower().replace(' ', '_')}>")
            else:
                # File reference - check for module-specific version first
                content = self._load_doc_with_module_fallback(doc_ref)
                if content:
                    tag = Path(doc_ref).stem
                    sections.append(f"<{tag}>\n{content}\n</{tag}>")
                else:
                    missing_docs.append(doc_ref)

        # Handle missing docs
        if missing_docs:
            error_msg = f"Missing documentation files: {', '.join(missing_docs)}"
            if required:
                raise FileNotFoundError(error_msg)
            else:
                if self.verbose:
                    print(f"⚠️  {error_msg} (skipping)")

        return "\n\n".join(sections)
    
    def _load_doc_with_module_fallback(self, doc_ref: str) -> Optional[str]:
        """Load doc with module-specific override, fallback to base

        Priority:
        1. Module-specific: inputs/modules/module{num}/path{letter}/{doc_ref}
        2. Base: inputs/docs/{doc_ref}
        """
        # Try module-specific first
        if self.module_path:
            module_path = self.modules_dir / self.module_path / doc_ref
            if self.verbose:
                print(f"  Checking module-specific doc: {module_path}")
            if module_path.exists():
                with open(module_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if self.verbose:
                    print(f"  📘 Loaded module-specific: {self.module_path}/{doc_ref} ({len(content)} chars)")
                    print(f"     Preview: {content[:200]}")
                return content

        # Fallback to base
        base_path = self.docs_dir / doc_ref
        if self.verbose:
            print(f"  Checking base doc: {base_path}")
        if base_path.exists():
            with open(base_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if self.verbose:
                print(f"  📗 Loaded base: {doc_ref} ({len(content)} chars)")
                print(f"     Preview: {content[:200]}")
            return content

        # Doc not found - will be handled by _load_docs
        return None
    
    def _format_examples(self, examples: List[Dict]) -> str:
        """Format example outputs"""
        formatted = []
        
        for i, example in enumerate(examples, 1):
            example_text = f"Example {i}:\n"
            if "description" in example:
                example_text += f"{example['description']}\n\n"
            example_text += example.get("output", "")
            formatted.append(example_text)
        
        return "\n\n---\n\n".join(formatted)
    
    # ========================================================================
    # PROMPT CONFIGURATIONS
    # ========================================================================
    
    def _question_generator_config(self) -> Dict:
        """Question Generator prompt configuration"""
        from question_generator import (
            QUESTION_GENERATOR_ROLE,
            QUESTION_GENERATOR_DOCS,
            QUESTION_GENERATOR_EXAMPLES,
            QUESTION_GENERATOR_STRUCTURE,
            QUESTION_GENERATOR_INSTRUCTIONS,
            QUESTION_GENERATOR_MODULE_REF,
            QUESTION_GENERATOR_PREFILL
        )
        
        return {
            "role": QUESTION_GENERATOR_ROLE,
            "docs": QUESTION_GENERATOR_DOCS,
            "examples": QUESTION_GENERATOR_EXAMPLES,
            "structure": QUESTION_GENERATOR_STRUCTURE,
            "instructions": QUESTION_GENERATOR_INSTRUCTIONS,
            "module_ref": QUESTION_GENERATOR_MODULE_REF,
            "prefill": QUESTION_GENERATOR_PREFILL
        }
    
    def _interaction_designer_config(self) -> Dict:
        """Interaction Designer prompt configuration"""
        from interaction_designer import (
            INTERACTION_DESIGNER_ROLE,
            INTERACTION_DESIGNER_DOCS,
            INTERACTION_DESIGNER_EXAMPLES,
            INTERACTION_DESIGNER_STRUCTURE,
            INTERACTION_DESIGNER_INSTRUCTIONS,
            INTERACTION_DESIGNER_TEMPLATE_REF 
        )

        return {
            "role": INTERACTION_DESIGNER_ROLE,
            "docs": INTERACTION_DESIGNER_DOCS,
            "examples": INTERACTION_DESIGNER_EXAMPLES,
            "structure": INTERACTION_DESIGNER_STRUCTURE,
            "instructions": INTERACTION_DESIGNER_INSTRUCTIONS,
            "problem_template_ref": INTERACTION_DESIGNER_TEMPLATE_REF
        }

    
    def _remediation_generator_config(self) -> Dict:
        """Remediation Generator prompt configuration"""
        from remediation_generator import (
            REMEDIATION_GENERATOR_ROLE,
            REMEDIATION_GENERATOR_DOCS,
            REMEDIATION_GENERATOR_EXAMPLES,
            REMEDIATION_GENERATOR_STRUCTURE,
            REMEDIATION_GENERATOR_INSTRUCTIONS,
            REMEDIATION_GENERATOR_TEMPLATE_REF
        )

        return {
            "role": REMEDIATION_GENERATOR_ROLE,
            "docs": REMEDIATION_GENERATOR_DOCS,
            "examples": REMEDIATION_GENERATOR_EXAMPLES,
            "structure": REMEDIATION_GENERATOR_STRUCTURE,
            "instructions": REMEDIATION_GENERATOR_INSTRUCTIONS,
            "problem_template_ref": REMEDIATION_GENERATOR_TEMPLATE_REF
        }
    
    def _godot_formatter_config(self) -> Dict:
        """Godot Formatter prompt configuration"""
        from godot_formatter import (
            GODOT_FORMATTER_ROLE,
            GODOT_FORMATTER_DOCS,
            GODOT_FORMATTER_EXAMPLES,
            GODOT_FORMATTER_STRUCTURE,
            GODOT_FORMATTER_INSTRUCTIONS
        )
        
        return {
            "role": GODOT_FORMATTER_ROLE,
            "docs": GODOT_FORMATTER_DOCS,
            "examples": GODOT_FORMATTER_EXAMPLES,
            "structure": GODOT_FORMATTER_STRUCTURE,
            "instructions": GODOT_FORMATTER_INSTRUCTIONS
        }
    
    def build_remediation_generator_prompt(self, interactions_context: str = None, input_file_path: str = None) -> str:
        """Build prompt for remediation generation

        Args:
            interactions_context: Direct context string (legacy)
            input_file_path: Path to interactions.json file (new method)

        Returns:
            Prompt string (or tuple with prefill if specified)
        """
        variables = {}
        if interactions_context:
            variables["interactions_context"] = interactions_context

        return self.build_prompt(
            "remediation_generator",
            input_file_path=input_file_path,
            variables=variables if variables else None
        )


# Test it
if __name__ == "__main__":
    import json

    # Ask user for module number and path letter
    try:
        module_number = int(input("Enter module number: "))
    except Exception:
        print("Invalid module number. Using 1.")
        module_number = 1
    path_letter = input("Enter path letter (e.g., 'a', 'b'): ").strip() or "a"

    # Ask for interactions file path
    interactions_file = input("Enter path to interactions JSON file (or press Enter to skip): ").strip()
    if not interactions_file:
        print("No interactions file provided. Testing with empty context.")
        interactions_context = "{}"
    else:
        try:
            with open(interactions_file, 'r', encoding='utf-8') as f:
                interactions_context = f.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            interactions_context = "{}"

    builder = PromptBuilder(module_number=module_number, path_letter=path_letter, verbose=True)

    print("=" * 70)
    print(f"Testing prompt builder for module {module_number} path {path_letter}")
    print("=" * 70)

    # Build a remediation generator prompt
    print("\nBuilding remediation_generator prompt...")

    # Method 1: Using input_file_path (NEW - recommended)
    if interactions_file:
        print("  Using new method: input_file_path")
        result = builder.build_prompt(
            prompt_id="remediation_generator",
            input_file_path=interactions_file
        )
    # Method 2: Using variables dict (OLD - still supported)
    else:
        print("  Using legacy method: variables dict")
        result = builder.build_prompt(
            prompt_id="remediation_generator",
            variables={"interactions_context": interactions_context}
        )

    # Handle prefill if returned
    if isinstance(result, tuple):
        prompt, prefill = result
        print(f"\n✓ Prompt built successfully with prefill!")
        print(f"  Prompt length: {len(prompt)} characters")
        print(f"  Prefill: {prefill[:100]}...")
    else:
        prompt = result
        print(f"\n✓ Prompt built successfully!")
        print(f"  Total length: {len(prompt)} characters")

    print("\nFirst 500 characters:")
    print(prompt[:500])