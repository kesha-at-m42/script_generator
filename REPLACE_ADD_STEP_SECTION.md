# Replace "Add Step" Section in ui/app.py

## Find and Replace Lines 232-291

**Find this entire section (lines 232-291):**
```python
    with col2:
        st.subheader("Add Step")

        step_type = st.radio("Step Type", ["AI Step", "Formatting Step"], key="new_step_type")

        if step_type == "AI Step":
            st.markdown("##### AI Step")
            step_name = st.text_input("Step Name", key="ai_step_name")
            prompt_name = st.text_input("Prompt Name", key="ai_prompt_name",
                                       help="e.g., interaction_generator")

            st.markdown("**Variables** (JSON)")
            variables_json = st.text_area("Variables", value="{}", key="ai_variables", height=100)

            output_file = st.text_input("Output File", key="ai_output_file",
                                       help="e.g., interactions.json")

            if st.button("➕ Add AI Step"):
                try:
                    variables = json.loads(variables_json) if variables_json else {}
                    new_step = {
                        "name": step_name or prompt_name,
                        "type": "ai",
                        "prompt_name": prompt_name,
                        "variables": variables,
                        "output_file": output_file
                    }
                    st.session_state.pipeline_steps.append(new_step)
                    st.success(f"Added: {step_name or prompt_name}")
                    st.rerun()
                except json.JSONDecodeError as e:
                    st.error(f"Invalid JSON in variables: {e}")

        else:  # Formatting Step
            st.markdown("##### Formatting Step")
            step_name = st.text_input("Step Name", key="format_step_name")
            function = st.text_input("Function", key="format_function",
                                    help="e.g., script_formatter.format_interactions_to_markdown")

            st.markdown("**Arguments** (JSON)")
            args_json = st.text_area("Arguments", value="{}", key="format_args", height=100)

            output_file = st.text_input("Output File", key="format_output_file",
                                       help="e.g., script.md")

            if st.button("➕ Add Formatting Step"):
                try:
                    args = json.loads(args_json) if args_json else {}
                    new_step = {
                        "name": step_name or function,
                        "type": "formatting",
                        "function": function,
                        "function_args": args,
                        "output_file": output_file
                    }
                    st.session_state.pipeline_steps.append(new_step)
                    st.success(f"Added: {step_name or function}")
                    st.rerun()
                except json.JSONDecodeError as e:
                    st.error(f"Invalid JSON in arguments: {e}")
```

**Replace with:**
```python
    with col2:
        st.subheader("Add Step")

        step_type = st.radio("Step Type", ["AI Step", "Formatting Step"], key="new_step_type")

        if step_type == "AI Step":
            st.markdown("##### AI Step")

            # Get available prompts
            available_prompts = []
            if PROMPTS_DIR.exists():
                available_prompts = [pf.stem for pf in PROMPTS_DIR.glob("*.py") if pf.stem != "__init__"]

            if available_prompts:
                prompt_name = st.selectbox(
                    "Prompt",
                    options=available_prompts,
                    key="ai_prompt_select"
                )
            else:
                st.warning("⚠️ No prompts found in steps/prompts/")
                prompt_name = None

            description = st.text_area("Description", key="ai_description", height=80,
                                      placeholder="What does this step do?")

            output_file = st.text_input("Output File", key="ai_output_file",
                                       placeholder="e.g., interactions.json")

            if st.button("➕ Add AI Step", disabled=not prompt_name):
                new_step = {
                    "name": prompt_name,
                    "type": "ai",
                    "prompt_name": prompt_name,
                    "description": description,
                    "variables": {},
                    "output_file": output_file
                }
                st.session_state.pipeline_steps.append(new_step)
                st.success(f"✅ Added: {prompt_name}")
                st.rerun()

        else:  # Formatting Step
            st.markdown("##### Formatting Step")

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
                selected_formatter = st.selectbox(
                    "Formatter",
                    options=list(formatters.keys()),
                    key="format_select"
                )
                function = formatters[selected_formatter]
            else:
                st.warning("⚠️ No formatters found in steps/formatting/")
                function = None

            description = st.text_area("Description", key="format_description", height=80,
                                      placeholder="What does this step do?")

            output_file = st.text_input("Output File", key="format_output_file",
                                       placeholder="e.g., script.md")

            if st.button("➕ Add Formatting Step", disabled=not function):
                new_step = {
                    "name": function,
                    "type": "formatting",
                    "function": function,
                    "description": description,
                    "function_args": {},
                    "output_file": output_file
                }
                st.session_state.pipeline_steps.append(new_step)
                st.success(f"✅ Added: {function}")
                st.rerun()
```

## Also Update Configuration (Lines 27-29)

**Find:**
```python
PROMPTS_DIR = project_root / "inputs" / "prompts"
OUTPUTS_DIR = project_root / "outputs"
SAVED_PIPELINES_FILE = Path(__file__).parent / "saved_pipelines.json"
```

**Replace with:**
```python
PROMPTS_DIR = project_root / "steps" / "prompts"
FORMATTING_DIR = project_root / "steps" / "formatting"
OUTPUTS_DIR = project_root / "outputs"
SAVED_PIPELINES_FILE = Path(__file__).parent / "saved_pipelines.json"
```

## Update Step Display (Lines 208-223)

**Find:**
```python
                with st.expander(f"Step {idx + 1}: {step.get('name', 'Unnamed')}", expanded=False):
                    step_type = step.get("type", "ai")

                    if step_type == "ai":
                        st.write(f"**Type:** AI Step")
                        st.write(f"**Prompt:** `{step.get('prompt_name')}`")
                        if step.get("variables"):
                            st.write(f"**Variables:** {step['variables']}")
                    else:
                        st.write(f"**Type:** Formatting Step")
                        st.write(f"**Function:** `{step.get('function')}`")
                        if step.get("function_args"):
                            st.write(f"**Arguments:** {step['function_args']}")

                    st.write(f"**Output File:** {step.get('output_file', 'None')}")
```

**Replace with:**
```python
                with st.expander(f"Step {idx + 1}: {step.get('name', 'Unnamed')}", expanded=False):
                    step_type = step.get("type", "ai")

                    if step_type == "ai":
                        st.write(f"**Type:** AI Step")
                        st.write(f"**Prompt:** `{step.get('prompt_name')}`")
                    else:
                        st.write(f"**Type:** Formatting Step")
                        st.write(f"**Function:** `{step.get('function')}`")

                    if step.get("description"):
                        st.write(f"**Description:** {step['description']}")

                    st.write(f"**Output File:** {step.get('output_file', 'None')}")
```

## That's it!

Now you'll have:
- ✅ Dropdowns for prompts and formatters
- ✅ Description field instead of variables/arguments
- ✅ Cleaner, simpler UI
