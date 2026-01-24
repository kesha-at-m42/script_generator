"""
Pipeline UI - Streamlit-based interface for pipeline management
Run with: streamlit run pipeline_ui.py
"""

import streamlit as st
import sys
import json
from pathlib import Path
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "core"))

from core.pipeline import Step, run_pipeline, run_single_step
from core.prompt_builder import Prompt
from path_manager import get_project_paths
import importlib

 # Import output utilities
from ui.utils.output import (
    capture_console_output_streaming,
    display_unified_output
)

# Note: All pipelines are now centralized in config/pipelines.json

# Configuration
paths = get_project_paths()
PROMPTS_DIR = paths['prompts']
FORMATTING_DIR = paths['formatting']
OUTPUTS_DIR = paths['outputs']
PIPELINES_FILE = paths['project_root'] / "config" / "pipelines.json"

# Claude Models Configuration
CLAUDE_MODELS = {
    "claude-sonnet-4-5-20250929": "Sonnet 4.5 - Best balance of speed, cost, and intelligence",
    "claude-opus-4-5-20251101": "Opus 4.5 - Most capable model for complex tasks",
    "claude-3-5-sonnet-20241022": "Sonnet 3.5 - Fast and capable for most tasks",
    "claude-3-5-haiku-20241022": "Haiku 3.5 - Fastest and most cost-effective for simple tasks",
}
DEFAULT_MODEL = "claude-sonnet-4-5-20250929"


st.set_page_config(
    page_title="Pipeline Manager",
    page_icon="🔧",
    layout="wide"
)

# Helper functions for saving/loading pipelines
def load_saved_pipelines():
    """Load pipelines from centralized JSON file"""
    if PIPELINES_FILE.exists():
        with open(PIPELINES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_pipeline_to_file(name: str, steps: list):
    """Save a pipeline to the centralized JSON file"""
    pipelines = load_saved_pipelines()
    pipelines[name] = steps
    with open(PIPELINES_FILE, 'w', encoding='utf-8') as f:
        json.dump(pipelines, f, indent=2)

def delete_saved_pipeline(name: str):
    """Delete a pipeline from the centralized JSON file"""
    pipelines = load_saved_pipelines()
    if name in pipelines:
        del pipelines[name]
        with open(PIPELINES_FILE, 'w', encoding='utf-8') as f:
            json.dump(pipelines, f, indent=2)

# Initialize session state
if "pipeline_steps" not in st.session_state:
    st.session_state.pipeline_steps = []
if "current_prompt" not in st.session_state:
    st.session_state.current_prompt = None
if "execution_result" not in st.session_state:
    st.session_state.execution_result = None
if "interactive_step" not in st.session_state:
    st.session_state.interactive_step = 0
if "interactive_outputs" not in st.session_state:
    st.session_state.interactive_outputs = []
if "interactive_action" not in st.session_state:
    st.session_state.interactive_action = None
if "pipeline_output_dir" not in st.session_state:
    st.session_state.pipeline_output_dir = None
if "edit_step_idx" not in st.session_state:
    st.session_state.edit_step_idx = None
if "pipeline_name" not in st.session_state:
    st.session_state.pipeline_name = None


# Sidebar - Configuration
with st.sidebar:
    st.title("⚙️ Pipeline Configuration")

    module_number = st.number_input("Module Number", min_value=1, max_value=10, value=1)
    path_letter = st.text_input("Path Letter", value="c", max_chars=1)

    st.divider()

    verbose = st.checkbox("Verbose Logging", value=True)
    parse_json = st.checkbox("Parse JSON Output", value=True)
    interactive = st.checkbox("Interactive Mode (step-by-step)", value=False,
                             help="Pause after each step for review")

    st.divider()

    st.markdown("### 📁 Available Prompts")
    if PROMPTS_DIR.exists():
        prompt_files = list(PROMPTS_DIR.glob("*.py"))
        if prompt_files:
            for pf in prompt_files:
                prompt_name = pf.stem
                if prompt_name != "__init__":
                    st.caption(f"• {prompt_name}")
        else:
            st.caption("No prompts found")
    else:
        st.caption("Prompts directory not found")


# Main Content
st.title("🔧 Pipeline Manager")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📚 Module Viewer", "✏️ Edit Prompts", "📋 Pipeline Steps", "▶️ Run Pipeline"])

# TAB 1: Module Viewer
with tab1:
    st.header("📚 Module Viewer")
    st.caption("View and explore module data from modules.py")

    # Import modules
    modules_file = project_root / "modules" / "modules.py"

    if modules_file.exists():
        try:
            # Import the modules file
            import importlib.util
            spec = importlib.util.spec_from_file_location("modules", modules_file)
            modules_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modules_module)

            # Find all module_N variables
            available_modules = {}
            for name, obj in modules_module.__dict__.items():
                if name.startswith("module_") and isinstance(obj, dict):
                    module_num = name.split("_")[1]
                    if module_num.isdigit():
                        available_modules[int(module_num)] = obj

            if available_modules:
                # Module selector
                selected_module_num = st.selectbox(
                    "Select Module",
                    options=sorted(available_modules.keys()),
                    format_func=lambda x: f"Module {x}: {available_modules[x].get('module_name', 'Unnamed')}"
                )

                if selected_module_num:
                    module_data = available_modules[selected_module_num]

                    st.divider()

                    # Helper function to display data recursively
                    def display_data(data, level=0):
                        indent = "  " * level

                        if isinstance(data, dict):
                            for key, value in data.items():
                                if isinstance(value, (dict, list)):
                                    st.markdown(f"{indent}**{key}:**")
                                    display_data(value, level + 1)
                                else:
                                    st.markdown(f"{indent}**{key}:** `{value}`")

                        elif isinstance(data, list):
                            for idx, item in enumerate(data):
                                if isinstance(item, (dict, list)):
                                    st.markdown(f"{indent}**[{idx}]:**")
                                    display_data(item, level + 1)
                                else:
                                    st.markdown(f"{indent}• `{item}`")
                        else:
                            st.markdown(f"{indent}`{data}`")

                    # Display all fields
                    st.subheader(f"Module {selected_module_num}: {module_data.get('module_name', 'Unnamed')}")

                    # Show field paths helper
                    with st.expander(" Field Path Reference", expanded=False):
                        st.caption("Use these paths in module_ref to access fields:")
                        st.code("""
                        Examples:
                        - module_name → "module_name"
                        - vocabulary → "vocabulary"
                        - phase → "phases.0"
                        - phase.phase_name → "phases.0.phase_name"
                        - phases[1].variables[0] → "phases.1.variables.0"
                        """)

                    # Display module data
                    for key, value in module_data.items():
                        with st.expander(f"**{key}**", expanded=(key in ["module_name", "vocabulary", "phases"])):
                            display_data(value)

                    st.divider()

                    # JSON view
                    with st.expander("📄 Raw JSON View", expanded=False):
                        st.json(module_data)

            else:
                st.warning("No modules found in modules.py")

        except Exception as e:
            st.error(f"Failed to load modules.py: {e}")
            st.exception(e)
    else:
        st.error(f"modules.py not found at: {modules_file}")

# TAB 2: Edit Prompts
with tab2:
    st.header("Edit Prompts")
    st.caption("Visual editor for creating and editing prompts with all fields")

    # Show success message if prompt was just saved
    if "prompt_saved_message" in st.session_state:
        st.success(st.session_state.prompt_saved_message)
        del st.session_state.prompt_saved_message

    # Helper function to highlight variables in text
    def highlight_variables(text):
        """Return markdown with variables highlighted"""
        import re
        if not text:
            return ""
        # Find all {{variable}} patterns
        highlighted = re.sub(r'\{\{([^}]+)\}\}', r'`{{\1}}`', text)
        return highlighted

    # Field tooltips
    FIELD_TOOLTIPS = {
        "role": "System role/identity for Claude. Defines who Claude is and how it should behave for this step.",
        "instructions": "The main task instructions. This is where you describe what Claude should do, how it should reference documents and how to fill in the output structure. Supports variable substitution with {{variable}}.",
        "doc_refs": "List of documentation files stored in input docs or module and path specific folders to include as context. Doc Refs should be entered on separate lines.",
        "module_ref": "Fields to fetch from modules.py. Maps variable names to field paths.",
        "output_structure": "Expected JSON schema or format for the output. Helps Claude understand the required output structure.",
        "prefill": "Template for prefilling Claude's response. Useful for ensuring consistent output format and reducing unnecessary rewriting.",
        "examples": "(WIP) List of example inputs/outputs to guide Claude.",
        "template_ref": "(WIP) Fields to fetch from problem templates (similar to module_ref).",
        "cache_docs": "Enable prompt caching for static doc_refs to reduce API costs (90% savings).",
        "cache_ttl": "Cache time-to-live: '5m' for 5 minutes or '1h' for 1 hour.",
        "temperature": "Sampling temperature 0.0-1.0. Higher = more creative, lower = more focused.",
        "max_tokens": "Maximum tokens to generate in the response.",
        "stop_sequences": "Custom sequences that stop generation when encountered."
    }

    # Select prompt to edit
    col_select, col_new = st.columns([3, 1])

    with col_select:
        if PROMPTS_DIR.exists():
            prompt_files = [pf.stem for pf in PROMPTS_DIR.glob("*.py") if pf.stem != "__init__"]
            if prompt_files:
                selected_prompt_name = st.selectbox("Select Prompt", ["-- New Prompt --"] + prompt_files, key="visual_prompt_select")
            else:
                selected_prompt_name = "-- New Prompt --"
                st.warning("No prompts found. Create a new one below.")
        else:
            st.error("Prompts directory not found!")
            selected_prompt_name = None

    with col_new:
        st.write("")
        st.write("")
        if st.button("📂 Load", use_container_width=True):
            if selected_prompt_name and selected_prompt_name != "-- New Prompt --":
                # Load the prompt
                prompt_file = PROMPTS_DIR / f"{selected_prompt_name}.py"
                try:
                    # Import the prompt module
                    import importlib.util
                    spec = importlib.util.spec_from_file_location(selected_prompt_name, prompt_file)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    # Find the Prompt object
                    prompt_obj = None
                    for name, obj in module.__dict__.items():
                        if hasattr(obj, '__class__') and obj.__class__.__name__ == 'Prompt':
                            prompt_obj = obj
                            break

                    if prompt_obj:
                        # Store in session state
                        st.session_state.edit_prompt_name = selected_prompt_name
                        st.session_state.edit_role = prompt_obj.role or ""
                        st.session_state.edit_instructions = prompt_obj.instructions or ""
                        st.session_state.edit_doc_refs = "\n".join(prompt_obj.doc_refs) if prompt_obj.doc_refs else ""

                        # Convert module_ref to list of tuples for visual editor
                        if isinstance(prompt_obj.module_ref, dict):
                            st.session_state.edit_module_ref_items = list(prompt_obj.module_ref.items())
                        elif isinstance(prompt_obj.module_ref, (list, set)):
                            # Handle both list and set formats
                            items = []
                            for field in prompt_obj.module_ref:
                                # Check if it's in "var:path" format
                                if ':' in str(field):
                                    var, path = field.split(':', 1)
                                    items.append((var, path))
                                else:
                                    # Simple field reference
                                    items.append((field, field))
                            st.session_state.edit_module_ref_items = items
                        else:
                            st.session_state.edit_module_ref_items = []

                        st.session_state.edit_output_structure = prompt_obj.output_structure or ""
                        st.session_state.edit_prefill = prompt_obj.prefill or ""
                        st.session_state.edit_examples = str(prompt_obj.examples) if prompt_obj.examples else "[]"
                        st.session_state.edit_template_ref = str(prompt_obj.template_ref) if prompt_obj.template_ref else "{}"
                        st.session_state.edit_cache_docs = prompt_obj.cache_docs
                        st.session_state.edit_cache_ttl = prompt_obj.cache_ttl or "5m"
                        st.session_state.edit_temperature = prompt_obj.temperature if prompt_obj.temperature is not None else 1.0
                        st.session_state.edit_max_tokens = prompt_obj.max_tokens if prompt_obj.max_tokens else 8000
                        st.session_state.edit_stop_sequences = "\n".join(prompt_obj.stop_sequences) if prompt_obj.stop_sequences else ""
                        st.success(f"Loaded {selected_prompt_name}")
                        st.rerun()
                    else:
                        st.error("No Prompt object found in file")
                except Exception as e:
                    st.error(f"Failed to load prompt: {e}")
            else:
                # Initialize new prompt
                st.session_state.edit_prompt_name = "new_prompt"
                st.session_state.edit_role = ""
                st.session_state.edit_instructions = ""
                st.session_state.edit_doc_refs = ""
                st.session_state.edit_module_ref_items = []
                st.session_state.edit_output_structure = ""
                st.session_state.edit_prefill = ""
                st.session_state.edit_examples = "[]"
                st.session_state.edit_template_ref = "{}"
                st.session_state.edit_cache_docs = True
                st.session_state.edit_cache_ttl = "5m"
                st.session_state.edit_temperature = 1.0
                st.session_state.edit_max_tokens = 8000
                st.session_state.edit_stop_sequences = ""
                st.success("Initialized new prompt")
                st.rerun()

    # Only show editor if prompt is loaded
    if "edit_prompt_name" in st.session_state:
        st.divider()

        # Prompt name
        prompt_name_input = st.text_input("Prompt Name", value=st.session_state.edit_prompt_name,
                                        help="Name of the prompt file (without .py extension). Spaces will be replaced with underscores.")

        # Update session state when name changes
        if prompt_name_input != st.session_state.edit_prompt_name:
            st.session_state.edit_prompt_name = prompt_name_input

        st.divider()

        st.subheader("Main Fields")

        # Role
        st.markdown(f"**Role** ")
        st.caption(FIELD_TOOLTIPS["role"])
        st.text_area("Role", height=100, key="edit_role", label_visibility="collapsed")
        if st.session_state.edit_role:
            import re
            # Match {variable} patterns that would be substituted by prompt_builder
            # Matches: {vocabulary}, {phase}, {animation_events}, etc.
            role_vars = re.findall(r'\{(\w+(?:\[\d+\])?)\}', st.session_state.edit_role)
            if role_vars:
                st.markdown(f"**Variables used:** {', '.join([f'`{{{v}}}`' for v in role_vars])}")

        # Instructions
        st.markdown(f"**Instructions** ")
        st.caption(FIELD_TOOLTIPS["instructions"])
        st.text_area("Instructions", height=400, key="edit_instructions", label_visibility="collapsed")
        if st.session_state.edit_instructions:
            import re
            # Match {variable} patterns that would be substituted by prompt_builder
            vars_found = re.findall(r'\{(\w+(?:\[\d+\])?)\}', st.session_state.edit_instructions)
            if vars_found:
                st.markdown(f"**Variables used:** {', '.join([f'`{{{v}}}`' for v in vars_found])}")

            # Document Upload and Management (must be BEFORE doc_refs widget)
            with st.expander("📤 Manage Documents", expanded=False):
                col_upload, col_list = st.columns([1, 1])

                with col_upload:
                    st.markdown("**Upload New Documents**")
                    uploaded_files = st.file_uploader(
                        "Choose files",
                        accept_multiple_files=True,
                        type=['txt', 'md', 'json', 'py', 'csv', 'xml', 'yaml', 'yml'],
                        key="doc_uploader",
                        label_visibility="collapsed"
                    )

                    if uploaded_files:
                        if st.button("💾 Save Uploaded Files"):
                            docs_dir = project_root / "docs"
                            docs_dir.mkdir(parents=True, exist_ok=True)

                            uploaded_names = []
                            for uploaded_file in uploaded_files:
                                file_path = docs_dir / uploaded_file.name
                                with open(file_path, "wb") as f:
                                    f.write(uploaded_file.getbuffer())
                                uploaded_names.append(uploaded_file.name)

                            # Update doc_refs BEFORE widget creation
                            if "edit_doc_refs" in st.session_state:
                                current_refs = st.session_state.edit_doc_refs.strip()
                                if current_refs:
                                    existing_refs = set(line.strip() for line in current_refs.split('\n') if line.strip())
                                else:
                                    existing_refs = set()

                                for name in uploaded_names:
                                    existing_refs.add(name)

                                st.session_state.edit_doc_refs = '\n'.join(sorted(existing_refs))

                            st.success(f"✅ Uploaded {len(uploaded_names)} file(s) and added to doc_refs")
                            st.rerun()

                with col_list:
                    st.markdown("**Available Documents**")
                    docs_dir = project_root / "docs"
                    if docs_dir.exists():
                        doc_files = sorted([f.name for f in docs_dir.iterdir() if f.is_file()])
                        if doc_files:
                            for doc in doc_files:
                                st.caption(f"📄 {doc}")
                        else:
                            st.caption("No documents yet")
                    else:
                        st.caption("docs directory not found")

            # Doc Refs
            st.markdown(f"**Doc Refs** ")
            st.caption(FIELD_TOOLTIPS["doc_refs"])
            st.text_area("Doc Refs (one per line)", height=80, key="edit_doc_refs",
                        label_visibility="collapsed")

        # Module Ref - Visual Editor
        st.markdown(f"**Module Ref** ")
        st.caption(FIELD_TOOLTIPS["module_ref"])

        # Initialize if not exists
        if "edit_module_ref_items" not in st.session_state:
            st.session_state.edit_module_ref_items = []

        # Display module ref items
        module_ref_items_updated = []
        for idx, (var_name, field_path) in enumerate(st.session_state.edit_module_ref_items):
            col1, col2, col3 = st.columns([2, 3, 1])
            with col1:
                var = st.text_input("Variable", value=var_name, key=f"modref_var_{idx}",
                                   placeholder="phase_name", label_visibility="collapsed")
            with col2:
                path = st.text_input("Path", value=field_path, key=f"modref_path_{idx}",
                                    placeholder="phases.0.phase_name", label_visibility="collapsed")
            with col3:
                st.write("")
                if st.button("🗑️", key=f"modref_del_{idx}"):
                    continue  # Skip this item

            if var and path:
                module_ref_items_updated.append((var, path))

        st.session_state.edit_module_ref_items = module_ref_items_updated

        if st.button("➕ Add Module Ref Variable"):
            st.session_state.edit_module_ref_items.append(("", ""))
            st.rerun()

        # Advanced fields in expander
        with st.expander("⚙️ Advanced Fields", expanded=False):

            # Output Structure
            st.markdown(f"**Output Structure** ")
            st.caption(FIELD_TOOLTIPS["output_structure"])
            st.text_area("Output Structure", height=200, key="edit_output_structure",
                        label_visibility="collapsed")

            # Prefill
            st.markdown(f"**Prefill** ")
            st.caption(FIELD_TOOLTIPS["prefill"])
            st.text_area("Prefill", height=80, key="edit_prefill", label_visibility="collapsed")

            # Examples
            st.markdown(f"**Examples** ")
            st.caption(FIELD_TOOLTIPS["examples"])
            st.text_area("Examples (list of dicts)", height=150, key="edit_examples",
                        label_visibility="collapsed")

            # Template Ref
            st.markdown(f"**Template Ref** ")
            st.caption(FIELD_TOOLTIPS["template_ref"])
            st.text_area("Template Ref (dict format)", height=80, key="edit_template_ref",
                        label_visibility="collapsed")

            st.divider()
            st.markdown("**Caching Settings**")

            col_cache1, col_cache2 = st.columns(2)
            with col_cache1:
                cache_docs_input = st.checkbox("Cache Docs", value=st.session_state.edit_cache_docs,
                                              help=FIELD_TOOLTIPS["cache_docs"])
            with col_cache2:
                cache_ttl_input = st.selectbox("Cache TTL", ["5m", "1h"],
                                              index=0 if st.session_state.edit_cache_ttl == "5m" else 1,
                                              help=FIELD_TOOLTIPS["cache_ttl"])

            st.divider()
            st.markdown("**API Parameters**")

            col_api1, col_api2 = st.columns(2)
            with col_api1:
                temperature_input = st.slider("Temperature", 0.0, 1.0,
                                             float(st.session_state.edit_temperature), 0.1,
                                             help=FIELD_TOOLTIPS["temperature"])
            with col_api2:
                max_tokens_input = st.number_input("Max Tokens", min_value=100, max_value=200000,
                                                  value=int(st.session_state.edit_max_tokens), step=1000,
                                                  help=FIELD_TOOLTIPS["max_tokens"])

            st.text_area("Stop Sequences (one per line)", height=60,
                        key="edit_stop_sequences", help=FIELD_TOOLTIPS["stop_sequences"])

        st.divider()

        # Save button
        col_save1, col_save2 = st.columns([3, 1])
        with col_save2:
            if st.button("💾 Save Prompt", type="primary", use_container_width=True):
                try:
                    # Get values from session state
                    prompt_name = st.session_state.edit_prompt_name
                    filename = prompt_name.replace(" ", "_")
                    role = st.session_state.edit_role
                    instructions = st.session_state.edit_instructions
                    doc_refs_text = st.session_state.edit_doc_refs
                    output_structure = st.session_state.edit_output_structure
                    prefill = st.session_state.edit_prefill
                    examples = st.session_state.edit_examples
                    template_ref = st.session_state.edit_template_ref
                    cache_docs = st.session_state.edit_cache_docs
                    cache_ttl = st.session_state.edit_cache_ttl
                    temperature = st.session_state.edit_temperature
                    max_tokens = st.session_state.edit_max_tokens
                    stop_sequences_text = st.session_state.edit_stop_sequences

                    # Parse inputs
                    doc_refs_list = [line.strip() for line in doc_refs_text.split('\n') if line.strip()]
                    stop_sequences_list = [line.strip() for line in stop_sequences_text.split('\n') if line.strip()]

                    # Build module_ref dict from items
                    module_ref_dict = {var: path for var, path in st.session_state.edit_module_ref_items if var and path}

                    # Generate Python file content
                    file_content = f'''"""
{prompt_name} - AI Prompt
"""

import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

{prompt_name.upper()}_PROMPT = Prompt(
    role="""{role}""",

    instructions="""
{instructions}
""",

    doc_refs={doc_refs_list},

    output_structure="""
{output_structure}
""",

    prefill="""{prefill}""",

    examples={examples},

    module_ref={module_ref_dict},

    template_ref={template_ref},

    cache_docs={cache_docs},
    cache_ttl="{cache_ttl}",
    temperature={temperature},
    max_tokens={max_tokens},
    stop_sequences={stop_sequences_list}
)
'''

                    # Save to file
                    output_path = PROMPTS_DIR / f"{filename}.py"
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(file_content)

                    st.rerun()
                    st.success(f"✅ Saved {filename}.py")

                except Exception as e:
                    st.error(f"Failed to save: {e}")
                    st.exception(e)

# TAB 3: Pipeline Steps
with tab3:
    st.header("Load Pipeline")

    # Load pipeline section
    st.subheader("📦 Load Pipeline")

    # Get all available pipelines from centralized JSON
    all_pipelines = load_saved_pipelines()

    if all_pipelines:
        col_load1, col_load2, col_load3 = st.columns([3, 1, 1])

        with col_load1:
            selected_pipeline_name = st.selectbox(
                "Select a pipeline to load",
                options=[""] + list(all_pipelines.keys()),
                format_func=lambda x: "-- Select --" if x == "" else x
            )

        with col_load2:
            st.write("")  # Spacer
            st.write("")  # Spacer
            if st.button("📥 Load", use_container_width=True):
                if selected_pipeline_name:
                    # Load pipeline directly from JSON
                    st.session_state.pipeline_steps = all_pipelines[selected_pipeline_name]
                    st.session_state.pipeline_name = selected_pipeline_name
                    st.success(f"✅ Loaded '{selected_pipeline_name}' with {len(st.session_state.pipeline_steps)} steps")
                    st.rerun()
                else:
                    st.warning("Please select a pipeline first")

        with col_load3:
            st.write("")  # Spacer
            st.write("")  # Spacer
            if selected_pipeline_name:
                if st.button("🗑️ Delete", use_container_width=True):
                    delete_saved_pipeline(selected_pipeline_name)
                    st.success(f"Deleted '{selected_pipeline_name}'")
                    st.rerun()

    # Save current pipeline section
    if st.session_state.pipeline_steps:
        st.markdown("##### 💾 Save Current Pipeline")

        # Show currently loaded pipeline
        if st.session_state.pipeline_name:
            st.info(f"📁 Loaded from: **{st.session_state.pipeline_name}**")

        col_save1, col_save2 = st.columns([3, 1])

        with col_save1:
            # Pre-fill with loaded pipeline name if exists
            default_name = st.session_state.pipeline_name if st.session_state.pipeline_name else ""
            save_name = st.text_input("Pipeline Name",
                                     value=default_name,
                                     key="save_pipeline_name",
                                     placeholder="my_pipeline",
                                     help="Change name to save as new pipeline, or keep same name to update")

            # Detect if name changed (will create new pipeline)
            if st.session_state.pipeline_name and save_name and save_name != st.session_state.pipeline_name:
                st.caption(f"⚠️ Will create new pipeline '{save_name}' (original '{st.session_state.pipeline_name}' will remain)")

        with col_save2:
            st.write("")  # Spacer
            st.write("")  # Spacer

            # Show appropriate button label
            is_rename = st.session_state.pipeline_name and save_name and save_name != st.session_state.pipeline_name
            button_label = "💾 Save As" if is_rename else "💾 Save"

            if st.button(button_label, use_container_width=True):
                if save_name:
                    save_pipeline_to_file(save_name, st.session_state.pipeline_steps)
                    st.session_state.pipeline_name = save_name
                    st.success(f"✅ Saved pipeline as '{save_name}'")
                    st.rerun()
                else:
                    st.warning("Please enter a pipeline name")

        # Delete current pipeline button
        if st.session_state.pipeline_name:
            col_del1, col_del2 = st.columns([3, 1])
            with col_del2:
                if st.button("🗑️ Delete Pipeline", use_container_width=True, type="secondary"):
                    delete_saved_pipeline(st.session_state.pipeline_name)
                    st.success(f"🗑️ Deleted '{st.session_state.pipeline_name}'")
                    st.session_state.pipeline_name = None
                    st.rerun()

    st.divider()

    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("Current Pipeline")

        if not st.session_state.pipeline_steps:
            st.info("No steps added yet. Add a step below or load a pipeline above.")
        else:
            for idx, step in enumerate(st.session_state.pipeline_steps):
                with st.expander(f"Step {idx + 1}: {step.get('name', 'Unnamed')}", expanded=False):
                    step_type = step.get("type", "ai")

                    if step_type == "ai":
                        st.write(f"**Type:** AI Step")
                        st.write(f"**Prompt:** `{step.get('prompt_name')}`")

                        # Display model if set
                        model = step.get('model')
                        if model:
                            model_desc = CLAUDE_MODELS.get(model, model)
                            st.write(f"**Model:** {model_desc}")
                        else:
                            st.write(f"**Model:** Default ({DEFAULT_MODEL})")
                    else:
                        st.write(f"**Type:** Formatting Step")
                        st.write(f"**Function:** `{step.get('function')}`")

                    if step.get("description"):
                        st.write(f"**Description:** {step['description']}")

                    st.write(f"**Output File:** {step.get('output_file', 'None')}")

                    col_up, col_down, col_edit, col_delete = st.columns(4)

                    with col_up:
                        if st.button(f"⬆️", key=f"up_{idx}", disabled=(idx == 0), help="Move up"):
                            # Swap with previous step
                            st.session_state.pipeline_steps[idx], st.session_state.pipeline_steps[idx-1] =                                 st.session_state.pipeline_steps[idx-1], st.session_state.pipeline_steps[idx]
                            # Update edit_step_idx if in edit mode
                            if st.session_state.edit_step_idx == idx:
                                st.session_state.edit_step_idx = idx - 1
                            elif st.session_state.edit_step_idx == idx - 1:
                                st.session_state.edit_step_idx = idx
                            st.rerun()

                    with col_down:
                        if st.button(f"⬇️", key=f"down_{idx}", disabled=(idx == len(st.session_state.pipeline_steps) - 1), help="Move down"):
                            # Swap with next step
                            st.session_state.pipeline_steps[idx], st.session_state.pipeline_steps[idx+1] =                                 st.session_state.pipeline_steps[idx+1], st.session_state.pipeline_steps[idx]
                            # Update edit_step_idx if in edit mode
                            if st.session_state.edit_step_idx == idx:
                                st.session_state.edit_step_idx = idx + 1
                            elif st.session_state.edit_step_idx == idx + 1:
                                st.session_state.edit_step_idx = idx
                            st.rerun()

                    with col_edit:
                        if st.button(f"✏️ Edit", key=f"edit_{idx}"):
                            st.session_state.edit_step_idx = idx
                            st.rerun()

                    with col_delete:
                        if st.button(f"🗑️ Delete", key=f"delete_{idx}"):
                            st.session_state.pipeline_steps.pop(idx)
                            st.session_state.edit_step_idx = None  # Clear edit mode if deleting
                            st.rerun()

    with col2:
        # Determine if we're in edit mode
        editing = st.session_state.edit_step_idx is not None

        if editing:
            st.subheader("✏️ Edit Step")
            edit_step = st.session_state.pipeline_steps[st.session_state.edit_step_idx]
            step_type_default = "AI Step" if edit_step.get("type") == "ai" else "Formatting Step"

            # Cancel button
            if st.button("❌ Cancel Edit"):
                st.session_state.edit_step_idx = None
                st.rerun()
        else:
            st.subheader("➕ Add Step")
            step_type_default = "AI Step"

        step_type = st.radio("Step Type", ["AI Step", "Formatting Step"],
                            key="step_type_radio",
                            index=0 if step_type_default == "AI Step" else 1)

        if step_type == "AI Step":
            st.markdown("##### AI Step Configuration")

            # Get available prompts
            available_prompts = []
            if PROMPTS_DIR.exists():
                available_prompts = [pf.stem for pf in PROMPTS_DIR.glob("*.py") if pf.stem != "__init__"]

            if available_prompts:
                # Pre-populate if editing
                default_prompt = None
                if editing and edit_step.get("type") == "ai":
                    default_prompt = edit_step.get("prompt_name")
                    if default_prompt in available_prompts:
                        default_idx = available_prompts.index(default_prompt)
                    else:
                        default_idx = 0
                else:
                    default_idx = 0

                prompt_name = st.selectbox(
                    "Prompt",
                    options=available_prompts,
                    index=default_idx,
                    key="edit_ai_prompt_select" if editing else "ai_prompt_select"
                )
            else:
                st.warning("⚠️ No prompts found in steps/prompts/")
                prompt_name = None

            # Pre-populate description if editing
            default_desc = ""
            if editing and edit_step.get("type") == "ai":
                default_desc = edit_step.get("description", "")

            description = st.text_area("Description",
                                      value=default_desc,
                                      key="edit_ai_description" if editing else "ai_description",
                                      height=80,
                                      placeholder="What does this step do?")

            # Pre-populate output file if editing
            default_output = ""
            if editing and edit_step.get("type") == "ai":
                default_output = edit_step.get("output_file", "")

            output_file = st.text_input("Output File",
                                       value=default_output,
                                       key="edit_ai_output_file" if editing else "ai_output_file",
                                       placeholder="e.g., interactions.json")

            # Model selection
            model_options = list(CLAUDE_MODELS.keys())
            model_display_names = [CLAUDE_MODELS[model] for model in model_options]

            # Pre-populate model if editing
            default_model_idx = 0
            if editing and edit_step.get("type") == "ai":
                edit_model = edit_step.get("model")
                if edit_model and edit_model in model_options:
                    default_model_idx = model_options.index(edit_model)

            selected_model_idx = st.selectbox(
                "Claude Model",
                options=range(len(model_options)),
                format_func=lambda i: model_display_names[i],
                index=default_model_idx,
                key="edit_ai_model_select" if editing else "ai_model_select",
                help="Choose which Claude model to use for this step"
            )
            selected_model = model_options[selected_model_idx]

            # Add or Update button
            button_label = "💾 Save Changes" if editing else "➕ Add AI Step"
            if st.button(button_label, disabled=not prompt_name, key="save_ai_step"):
                step_data = {
                    "name": prompt_name,
                    "type": "ai",
                    "prompt_name": prompt_name,
                    "description": description,
                    "variables": {},
                    "output_file": output_file,
                    "model": selected_model
                }

                if editing:
                    st.session_state.pipeline_steps[st.session_state.edit_step_idx] = step_data
                    st.success(f"✅ Updated: {prompt_name}")
                    st.session_state.edit_step_idx = None
                else:
                    st.session_state.pipeline_steps.append(step_data)
                    st.success(f"✅ Added: {prompt_name}")
                st.rerun()

        else:  # Formatting Step
            st.markdown("##### Formatting Step Configuration")

            # Get available formatters
            formatters = {}
            if FORMATTING_DIR.exists():
                for ff in FORMATTING_DIR.glob("*.py"):
                    if ff.stem != "__init__":
                        try:
                            import importlib.util
                            spec = importlib.util.spec_from_file_location(ff.stem, ff)
                            module = importlib.util.module_from_spec(spec)
                            spec.loader.exec_module(module)

                            for name, obj in module.__dict__.items():
                                if callable(obj) and not name.startswith("_"):
                                    display_name = f"{ff.stem}.{name}"
                                    formatters[display_name] = f"{ff.stem}.{name}"
                        except:
                            pass

            if formatters:
                # Pre-populate if editing
                default_formatter_idx = 0
                if editing and edit_step.get("type") == "formatting":
                    edit_function = edit_step.get("function")
                    formatter_list = list(formatters.keys())
                    if edit_function in formatter_list:
                        default_formatter_idx = formatter_list.index(edit_function)

                selected_formatter = st.selectbox(
                    "Formatter",
                    options=list(formatters.keys()),
                    index=default_formatter_idx,
                    key="edit_format_select" if editing else "format_select"
                )
                function = formatters[selected_formatter]
            else:
                st.warning("⚠️ No formatters found in steps/formatting/")
                function = None

            # Pre-populate description if editing
            default_desc = ""
            if editing and edit_step.get("type") == "formatting":
                default_desc = edit_step.get("description", "")

            description = st.text_area("Description",
                                      value=default_desc,
                                      key="edit_format_description" if editing else "format_description",
                                      height=80,
                                      placeholder="What does this step do?")

            # Pre-populate output file if editing
            default_output = ""
            if editing and edit_step.get("type") == "formatting":
                default_output = edit_step.get("output_file", "")

            output_file = st.text_input("Output File",
                                       value=default_output,
                                       key="edit_format_output_file" if editing else "format_output_file",
                                       placeholder="e.g., script.md")

            # Add or Update button
            button_label = "💾 Save Changes" if editing else "➕ Add Formatting Step"
            if st.button(button_label, disabled=not function, key="save_format_step"):
                step_data = {
                    "name": function,
                    "type": "formatting",
                    "function": function,
                    "description": description,
                    "function_args": {},
                    "output_file": output_file
                }

                if editing:
                    st.session_state.pipeline_steps[st.session_state.edit_step_idx] = step_data
                    st.success(f"✅ Updated: {function}")
                    st.session_state.edit_step_idx = None
                else:
                    st.session_state.pipeline_steps.append(step_data)
                    st.success(f"✅ Added: {function}")
                st.rerun()

# TAB 4: Run Pipeline
with tab4:
    st.header("Run Pipeline")

    if not st.session_state.pipeline_steps:
        st.warning("⚠️ No steps in pipeline. Add steps in the 'Pipeline Steps' tab first.")
    else:
        st.subheader("Pipeline Summary")

        #Show pipeline overview
        st.write(f"**Total Steps:** {len(st.session_state.pipeline_steps)}")
        st.write(f"**Module:** {module_number}")
        st.write(f"**Path:** {path_letter}")

        st.divider()

        # Show step sequence
        st.markdown("##### Execution Order")
        for idx, step in enumerate(st.session_state.pipeline_steps, 1):
            step_type = "🤖 AI" if step.get("type") == "ai" else "⚙️ Format"
            st.write(f"{idx}. {step_type} - {step.get('name')} → `{step.get('output_file', 'N/A')}`")

        st.divider()

        # Get output directory (reuse in interactive mode, otherwise let pipeline.py create it)
        if interactive and st.session_state.pipeline_output_dir is not None:
        # Reuse existing directory for subsequent steps in interactive mode
            actual_output_dir = st.session_state.pipeline_output_dir
        else:
        # Let pipeline.py create the directory
            actual_output_dir = None

        # Show progress if interactive mode is active
        if interactive and st.session_state.interactive_step > 0:
            st.markdown(f"### Step {st.session_state.interactive_step}/{len(st.session_state.pipeline_steps)}")
            st.progress(st.session_state.interactive_step / len(st.session_state.pipeline_steps))

        # Start or Continue button
        if not interactive:
            # Non-interactive mode
            if st.session_state.execution_result:
                button_label = "🔄 Re-run Pipeline"
            else:
                button_label = "🚀 Start Pipeline"
        else:
            # Interactive mode
            if st.session_state.interactive_step == 0:
                button_label = "🚀 Start Pipeline"
            elif st.session_state.interactive_step >= len(st.session_state.pipeline_steps):
                button_label = "🔄 Start Pipeline"
            else:
                button_label = f"▶️ Continue to Step {st.session_state.interactive_step + 1}"

        if st.button(button_label, type="primary") or st.session_state.interactive_action == "proceed":
            st.session_state.interactive_action = None

            # Reset state if re-running
            if not interactive and st.session_state.execution_result:
                st.session_state.execution_result = None
                st.rerun()
            elif interactive and st.session_state.interactive_step >= len(st.session_state.pipeline_steps):
                st.session_state.interactive_step = 0
                st.session_state.interactive_outputs = []
                st.session_state.pipeline_output_dir = None
                st.session_state.execution_result = None
                st.rerun()

            if not interactive:
                # Original non-interactive execution
                try:
                    steps = []
                    for step_config in st.session_state.pipeline_steps:
                        if step_config["type"] == "ai":
                            step = Step(
                                prompt_name=step_config["prompt_name"],
                                variables=step_config.get("variables"),
                                output_file=step_config.get("output_file")
                            )
                        else:
                            step = Step(
                                function=step_config["function"],
                                function_args=step_config.get("function_args"),
                                output_file=step_config.get("output_file")
                            )
                        steps.append(step)

                    #Create console output container with real-time streaming
                    with st.expander("Console Output", expanded = True):
                        console_display = st.empty()

                        with capture_console_output_streaming(console_display) as console_buffer:
                            result = run_pipeline(
                                steps=steps,
                                pipeline_name=st.session_state.pipeline_name,
                                module_number=module_number,
                                path_letter=path_letter,
                                output_dir=actual_output_dir,
                                verbose=verbose,
                                parse_json_output=parse_json
                            )

                        captured_output = console_buffer.getvalue()
                        st.session_state.execution_result = result
                        st.session_state.console_output = captured_output

                        # Display completion message
                        st.success("✅ Pipeline completed successfully!")

                except Exception as e:
                    st.error(f"❌ Pipeline failed: {str(e)}")
                    st.exception(e)

            else:
                # Interactive mode - execute one step
                current_step_idx = st.session_state.interactive_step

                if current_step_idx < len(st.session_state.pipeline_steps):
                    step_config = st.session_state.pipeline_steps[current_step_idx]

                    with st.spinner(f"Executing step {current_step_idx + 1}..."):
                        # Get previous step's output file for auto-chaining
                        previous_output_file = None
                        if st.session_state.interactive_outputs:
                            last_result = st.session_state.interactive_outputs[-1]['result']
                            previous_output_file = last_result.get('last_output_file')

                        # Convert step_config to Step object
                        if step_config["type"] == "ai":
                            step = Step(
                                prompt_name=step_config["prompt_name"],
                                variables=step_config.get("variables", {}),
                                input_file=previous_output_file,
                                output_file=step_config.get("output_file")
                            )
                        else:
                            step = Step(
                                function=step_config["function"],
                                function_args=step_config.get("function_args", {}),
                                input_file=previous_output_file,
                                output_file=step_config.get("output_file")
                            )
                        # Create console output container for real-time streaming
                        st.subheader(f"Executing Step {current_step_idx + 1}: {step_config.get('name', 'Unknown')}")
                        
                        console_display = st.empty()
                        # Capture console output with real-time streaming
                        with capture_console_output_streaming(console_display) as output_buffer:
                            result = run_single_step(
                                step=step,
                                module_number=module_number,
                                path_letter=path_letter,
                                output_dir=actual_output_dir,
                                verbose=verbose,
                                parse_json_output=parse_json
                            )

                        console_output = output_buffer.getvalue()

                        # Store output directory for subsequent steps
                        if st.session_state.interactive_step == 0 and actual_output_dir is None:
                            st.session_state.pipeline_output_dir = result.get('output_dir')

                        step_output = {
                            'result': result,
                            'console': console_output,
                            'step_name': step_config.get('name', 'Unknown'),
                            'step_type': step_config.get('type', 'unknown')
                        }

                        st.session_state.interactive_outputs.append(step_output)
                        st.session_state.interactive_step += 1

                    st.rerun()

        # Show step output and decision buttons (interactive mode)
        if interactive and st.session_state.interactive_outputs:
            st.divider()

            # Show latest step output
            latest = st.session_state.interactive_outputs[-1]

            st.subheader(f"✅ Step {len(st.session_state.interactive_outputs)}: {latest['step_name']}")

            # Use unified output display
            if latest['result'].get('output_dir'):
                output_dir = Path(latest['result']['output_dir'])
                display_unified_output(
                    output_dir=output_dir,
                    console_output=None,
                    show_all_files=True,
                    result=latest['result'],
                    button_key_prefix=f"step_{len(st.session_state.interactive_outputs)}"
                )

            st.divider()
        
            # Check if pipeline is complete
            if st.session_state.interactive_step >= len(st.session_state.pipeline_steps):
                st.success("🎉 Pipeline Completed!")

        # Show results
        if st.session_state.execution_result:
              st.divider()
              st.subheader("Results")

              result = st.session_state.execution_result
              output_path = Path(result.get("output_dir"))

              # Use unified output display
              display_unified_output(
                  output_dir=output_path,
                  console_output=None,
                  show_all_files=True,
                  result=result,
                  button_key_prefix="final_result"
              )


# Footer
st.divider()
st.caption("Pipeline Manager - Built with Streamlit")
