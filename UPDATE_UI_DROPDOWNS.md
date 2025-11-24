# Update UI to Add Dropdowns

## Changes to make in `ui/app.py`:

### 1. Update Configuration (line 27-29)

**Replace:**
```python
PROMPTS_DIR = project_root / "inputs" / "prompts"
OUTPUTS_DIR = project_root / "outputs"
SAVED_PIPELINES_FILE = Path(__file__).parent / "saved_pipelines.json"
```

**With:**
```python
PROMPTS_DIR = project_root / "steps" / "prompts"
FORMATTING_DIR = project_root / "steps" / "formatting"
OUTPUTS_DIR = project_root / "outputs"
SAVED_PIPELINES_FILE = Path(__file__).parent / "saved_pipelines.json"
```

### 2. Add Helper Function (after line 57, before sidebar)

**Add this new function:**
```python
def get_available_formatters():
    """Scan formatting directory and return available formatters"""
    formatters = {}
    if FORMATTING_DIR.exists():
        for ff in FORMATTING_DIR.glob("*.py"):
            if ff.stem != "__init__":
                try:
                    import importlib.util
                    spec = importlib.util.spec_from_file_location(ff.stem, ff)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    # Find all functions in the module
                    for name, obj in module.__dict__.items():
                        if callable(obj) and not name.startswith("_"):
                            display_name = f"{ff.stem}.{name}"
                            formatters[display_name] = f"{ff.stem}.{name}"
                except Exception as e:
                    st.error(f"Error loading {ff.stem}: {e}")
    return formatters
```

### 3. Update Sidebar Available Steps (replace lines 83-94)

**Replace:**
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

**With:**
```python
st.markdown("### 📁 Available Steps")

st.markdown("**AI Prompts:**")
if PROMPTS_DIR.exists():
    prompt_files = [pf.stem for pf in PROMPTS_DIR.glob("*.py") if pf.stem != "__init__"]
    if prompt_files:
        for pf in prompt_files:
            st.caption(f"• {pf}")
    else:
        st.caption("No prompts")
else:
    st.caption("Directory not found")

st.markdown("**Formatters:**")
formatters = get_available_formatters()
if formatters:
    for display_name in formatters.keys():
        st.caption(f"• {display_name}")
else:
    st.caption("No formatters")
```

### 4. Update AI Step Input (replace lines 237-241)

**Replace:**
```python
if step_type == "AI Step":
    st.markdown("##### AI Step")
    step_name = st.text_input("Step Name", key="ai_step_name")
    prompt_name = st.text_input("Prompt Name", key="ai_prompt_name",
                               help="e.g., interaction_generator")
```

**With:**
```python
if step_type == "AI Step":
    st.markdown("##### AI Step")

    # Get available prompts
    available_prompts = []
    if PROMPTS_DIR.exists():
        available_prompts = [pf.stem for pf in PROMPTS_DIR.glob("*.py") if pf.stem != "__init__"]

    if available_prompts:
        prompt_name = st.selectbox(
            "Select Prompt",
            options=available_prompts,
            key="ai_prompt_name"
        )
    else:
        st.warning("No prompts found in steps/prompts/")
        prompt_name = st.text_input("Prompt Name", key="ai_prompt_name")

    step_name = st.text_input("Step Name (optional)", key="ai_step_name",
                              placeholder=prompt_name if prompt_name else "")
```

### 5. Update Formatting Step Input (replace lines 265-269)

**Replace:**
```python
else:  # Formatting Step
    st.markdown("##### Formatting Step")
    step_name = st.text_input("Step Name", key="format_step_name")
    function = st.text_input("Function", key="format_function",
                            help="e.g., script_formatter.format_interactions_to_markdown")
```

**With:**
```python
else:  # Formatting Step
    st.markdown("##### Formatting Step")

    # Get available formatters
    formatters = get_available_formatters()

    if formatters:
        selected_formatter = st.selectbox(
            "Select Formatter",
            options=list(formatters.keys()),
            key="format_function_select"
        )
        function = formatters[selected_formatter]
    else:
        st.warning("No formatters found in steps/formatting/")
        function = st.text_input("Function", key="format_function")

    step_name = st.text_input("Step Name (optional)", key="format_step_name",
                              placeholder=function if function else "")
```

### 6. Update Edit Prompts Tab (replace lines 297-298)

**Replace:**
```python
if PROMPTS_DIR.exists():
    prompt_files = [pf.stem for pf in PROMPTS_DIR.glob("*.py") if pf.stem != "__init__"]
```

**With:**
```python
if PROMPTS_DIR.exists():
    prompt_files = [pf.stem for pf in PROMPTS_DIR.glob("*.py") if pf.stem != "__init__"]
else:
    prompt_files = []
```

## That's it!

After these changes, you'll have:
- ✅ Dropdown for AI prompts
- ✅ Dropdown for formatting functions
- ✅ Sidebar showing available steps
- ✅ No more manual typing!
