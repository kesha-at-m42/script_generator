# Updated Project Structure

## New Organization

```
script_generator/
├── steps/                        # 🆕 All pipeline steps
│   ├── prompts/                  # AI steps (call Claude)
│   │   ├── interaction_generator.py
│   │   ├── warmup_generator.py
│   │   └── ...
│   └── formatting/               # Deterministic steps (no API)
│       ├── script_formatter.py
│       └── ...
│
├── ui/                           # UI files
│   ├── app.py
│   └── saved_pipelines.json
│
├── config/                       # Configuration
│   └── pipelines.py
│
├── core/                         # Core engine
├── utils/                        # Utilities
├── outputs/                      # Pipeline outputs
└── scripts/                      # CLI scripts
```

## Changes to Make in `ui/app.py`

### 1. Update Configuration (around line 26-28):

Replace:
```python
PROMPTS_DIR = project_root / "inputs" / "prompts"
OUTPUTS_DIR = project_root / "outputs"
SAVED_PIPELINES_FILE = Path(__file__).parent / "saved_pipelines.json"
```

With:
```python
PROMPTS_DIR = project_root / "steps" / "prompts"
FORMATTING_DIR = project_root / "steps" / "formatting"
OUTPUTS_DIR = project_root / "outputs"
SAVED_PIPELINES_FILE = Path(__file__).parent / "saved_pipelines.json"
```

### 2. Update Sidebar (around line 83-94):

Replace:
```python
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
```

With:
```python
st.markdown("### 📁 Available Steps")
st.caption("**AI Prompts:**")
if PROMPTS_DIR.exists():
    prompt_files = list(PROMPTS_DIR.glob("*.py"))
    if prompt_files:
        for pf in prompt_files:
            prompt_name = pf.stem
            if prompt_name != "__init__":
                st.caption(f"• {prompt_name}")
    else:
        st.caption("No prompts found")

st.caption("**Formatting:**")
if FORMATTING_DIR.exists():
    format_files = list(FORMATTING_DIR.glob("*.py"))
    if format_files:
        for ff in format_files:
            format_name = ff.stem
            if format_name != "__init__":
                st.caption(f"• {format_name}")
    else:
        st.caption("No formatters found")
```

### 3. Update "Add Step" section (around line 236-262):

Replace the AI Step input with dropdown:
```python
if step_type == "AI Step":
    st.markdown("##### AI Step")
    step_name = st.text_input("Step Name", key="ai_step_name")
    prompt_name = st.text_input("Prompt Name", key="ai_prompt_name",
                               help="e.g., interaction_generator")
```

With:
```python
if step_type == "AI Step":
    st.markdown("##### AI Step")

    # Get available prompts
    available_prompts = []
    if PROMPTS_DIR.exists():
        available_prompts = [pf.stem for pf in PROMPTS_DIR.glob("*.py") if pf.stem != "__init__"]

    prompt_name = st.selectbox(
        "Select Prompt",
        options=available_prompts,
        key="ai_prompt_name"
    )
    step_name = st.text_input("Step Name (optional)", key="ai_step_name",
                              placeholder=prompt_name if prompt_name else "")
```

### 4. Update Formatting Step section (around line 264-290):

Replace:
```python
else:  # Formatting Step
    st.markdown("##### Formatting Step")
    step_name = st.text_input("Step Name", key="format_step_name")
    function = st.text_input("Function", key="format_function",
                            help="e.g., script_formatter.format_interactions_to_markdown")
```

With:
```python
else:  # Formatting Step
    st.markdown("##### Formatting Step")

    # Get available formatters
    available_formatters = []
    formatter_functions = {}
    if FORMATTING_DIR.exists():
        for ff in FORMATTING_DIR.glob("*.py"):
            if ff.stem != "__init__":
                # Import the module and find functions
                import importlib.util
                spec = importlib.util.spec_from_file_location(ff.stem, ff)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Find all functions in the module
                for name, obj in module.__dict__.items():
                    if callable(obj) and not name.startswith("_"):
                        display_name = f"{ff.stem}.{name}"
                        available_formatters.append(display_name)
                        formatter_functions[display_name] = f"{ff.stem}.{name}"

    if available_formatters:
        selected_formatter = st.selectbox(
            "Select Formatter",
            options=available_formatters,
            key="format_function_select"
        )
        function = formatter_functions[selected_formatter]
    else:
        st.warning("No formatters found in steps/formatting/")
        function = st.text_input("Function", key="format_function",
                                help="e.g., script_formatter.format_interactions_to_markdown")

    step_name = st.text_input("Step Name (optional)", key="format_step_name",
                              placeholder=function if function else "")
```

## Updated Run Commands

```bash
# Run UI
streamlit run ui/app.py

# Prompts are now in: steps/prompts/
# Formatters are now in: steps/formatting/
```

## Migration Notes

- Old `inputs/prompts/` → `steps/prompts/`
- Old `utils/script_formatter.py` → `steps/formatting/script_formatter.py`
- Update `config/pipelines.py` to use new paths
