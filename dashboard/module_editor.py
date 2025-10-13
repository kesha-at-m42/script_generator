"""
Module Data Editor - Visual form editor for module data
"""
import streamlit as st
import json
import ast
from pathlib import Path

def load_all_modules():
    """Load all modules from modules.py"""
    modules_path = Path(__file__).parent.parent / "inputs" / "modules.py"
    with open(modules_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse the file to extract all module_X dictionaries
    modules = {}
    tree = ast.parse(content)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id.startswith('module_'):
                    module_data = ast.literal_eval(node.value)
                    module_num = module_data.get('module_number', 0)
                    if module_num:
                        modules[module_num] = module_data
    return modules

def save_modules_file(all_modules_data):
    """Save all modules back to modules.py"""
    modules_path = Path(__file__).parent.parent / "inputs" / "modules.py"
    
    # Build content with all modules
    content = '"""\nModule Data - All Modules\n"""\n\n'
    
    module_vars = []
    for module_num in sorted(all_modules_data.keys()):
        module_data = all_modules_data[module_num]
        var_name = f"module_{module_num}"
        module_vars.append(var_name)
        
        content += f"{var_name} = {json.dumps(module_data, indent=4)}\n\n"
    
    # Add MODULES dictionary
    content += "# Dictionary of all modules for easy lookup\n"
    content += "MODULES = {\n"
    for module_num in sorted(all_modules_data.keys()):
        content += f"    {module_num}: module_{module_num},\n"
    content += "}\n\n"
    
    # Add __all__
    content += "# Export for easy import\n"
    content += f"__all__ = {module_vars + ['MODULES']}\n"
    
    with open(modules_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return modules_path

def render_module_editor():
    """Render the module editor form"""
    st.title("📝 Module Data Editor")
    st.markdown("Visual editor for module data - no code editing needed!")
    
    # Load all modules
    if 'all_modules' not in st.session_state:
        st.session_state.all_modules = load_all_modules()
    
    if not st.session_state.all_modules:
        st.error("Could not load modules from inputs/modules.py")
        return
    
    # Module selector
    col1, col2 = st.columns([3, 1])
    with col1:
        module_numbers = sorted(st.session_state.all_modules.keys())
        module_options = [
            f"Module {num}: {st.session_state.all_modules[num]['module_name']}"
            for num in module_numbers
        ]
        
        selected_option = st.selectbox(
            "Select Module to Edit",
            options=module_options,
            key="module_selector"
        )
        
        # Extract module number from selection
        selected_num = int(selected_option.split(":")[0].replace("Module ", ""))
        
        # Store selected module number in session state
        if 'current_module_num' not in st.session_state or st.session_state.current_module_num != selected_num:
            st.session_state.current_module_num = selected_num
    
    with col2:
        st.markdown("###  ")  # Spacing
        if st.button("➕ New Module", use_container_width=True):
            # Create new module with next number
            new_num = max(st.session_state.all_modules.keys()) + 1
            st.session_state.all_modules[new_num] = {
                "module_name": f"New Module {new_num}",
                "module_number": new_num,
                "grade_level": 3,
                "path_variant": "A",
                "learning_goals": [],
                "vocabulary": [],
                "standards": {"building_on": [], "addressing": [], "building_toward": []},
                "core_concepts": [],
                "goals": [],
                "misconceptions": []
            }
            st.session_state.current_module_num = new_num
            st.rerun()
    
    # Get reference to current module
    module = st.session_state.all_modules[st.session_state.current_module_num]
    
    # Module summary
    st.divider()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Modules", len(st.session_state.all_modules))
    with col2:
        st.metric("Learning Goals", len(module.get('learning_goals', [])))
    with col3:
        st.metric("Vocabulary Terms", len(module.get('vocabulary', [])))
    with col4:
        st.metric("Detailed Goals", len(module.get('goals', [])))
    
    st.divider()
    
    # Create tabs for different sections
    tabs = st.tabs([
        "📋 Basic Info",
        "🎯 Learning Goals",
        "📚 Vocabulary",
        "📊 Standards",
        "💡 Core Concepts",
        "🎓 Detailed Goals",
        "⚠️ Misconceptions",
        "💾 Save & Export"
    ])
    
    # ========================================================================
    # TAB 1: BASIC INFO
    # ========================================================================
    with tabs[0]:
        st.subheader("Basic Module Information")
        
        col1, col2 = st.columns(2)
        with col1:
            module["module_name"] = st.text_input(
                "Module Name",
                value=module.get("module_name", ""),
                key=f"module_name_{st.session_state.current_module_num}"
            )
            module["module_number"] = st.number_input(
                "Module Number",
                value=module.get("module_number", 1),
                min_value=1,
                key=f"module_number_{st.session_state.current_module_num}"
            )
        
        with col2:
            module["grade_level"] = st.number_input(
                "Grade Level",
                value=module.get("grade_level", 1),
                min_value=1,
                max_value=12,
                key=f"grade_level_{st.session_state.current_module_num}"
            )
            module["path_variant"] = st.text_input(
                "Path Variant",
                value=module.get("path_variant", "A"),
                key=f"path_variant_{st.session_state.current_module_num}"
            )
    
    # ========================================================================
    # TAB 2: LEARNING GOALS
    # ========================================================================
    with tabs[1]:
        st.subheader("Learning Goals (Verbatim)")
        
        # Display existing goals
        if "learning_goals" not in module:
            module["learning_goals"] = []
        
        for i, goal in enumerate(module["learning_goals"]):
            col1, col2 = st.columns([9, 1])
            with col1:
                module["learning_goals"][i] = st.text_area(
                    f"Goal {i+1}",
                    value=goal,
                    key=f"learning_goal_{st.session_state.current_module_num}_{i}",
                    height=80
                )
            with col2:
                if st.button("🗑️", key=f"delete_lg_{st.session_state.current_module_num}_{i}"):
                    module["learning_goals"].pop(i)
                    st.rerun()
        
        # Add new goal
        if st.button("➕ Add Learning Goal", key=f"add_lg_{st.session_state.current_module_num}"):
            module["learning_goals"].append("")
            st.rerun()
    
    # ========================================================================
    # TAB 3: VOCABULARY
    # ========================================================================
    with tabs[2]:
        st.subheader("Key Vocabulary")
        
        if "vocabulary" not in module:
            module["vocabulary"] = []
        
        # Display as editable list
        vocab_text = st.text_area(
            "Vocabulary (one per line)",
            value="\n".join(module["vocabulary"]),
            height=200,
            key=f"vocabulary_text_{st.session_state.current_module_num}"
        )
        module["vocabulary"] = [v.strip() for v in vocab_text.split("\n") if v.strip()]
        
        st.caption(f"Total: {len(module['vocabulary'])} terms")
    
    # ========================================================================
    # TAB 4: STANDARDS
    # ========================================================================
    with tabs[3]:
        st.subheader("Curriculum Standards")
        
        if "standards" not in module:
            module["standards"] = {
                "building_on": [],
                "addressing": [],
                "building_toward": []
            }
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Building On**")
            building_on = st.text_area(
                "Standards (one per line)",
                value="\n".join(module["standards"].get("building_on", [])),
                height=150,
                key=f"standards_building_on_{st.session_state.current_module_num}"
            )
            module["standards"]["building_on"] = [s.strip() for s in building_on.split("\n") if s.strip()]
        
        with col2:
            st.markdown("**Addressing**")
            addressing = st.text_area(
                "Standards (one per line)",
                value="\n".join(module["standards"].get("addressing", [])),
                height=150,
                key=f"standards_addressing_{st.session_state.current_module_num}"
            )
            module["standards"]["addressing"] = [s.strip() for s in addressing.split("\n") if s.strip()]
        
        with col3:
            st.markdown("**Building Toward**")
            building_toward = st.text_area(
                "Standards (one per line)",
                value="\n".join(module["standards"].get("building_toward", [])),
                height=150,
                key=f"standards_building_toward_{st.session_state.current_module_num}"
            )
            module["standards"]["building_toward"] = [s.strip() for s in building_toward.split("\n") if s.strip()]
    
    # ========================================================================
    # TAB 5: CORE CONCEPTS
    # ========================================================================
    with tabs[4]:
        st.subheader("Core Concepts")
        
        if "core_concepts" not in module:
            module["core_concepts"] = []
        
        concepts_text = st.text_area(
            "Core Concepts (one per line)",
            value="\n".join(module["core_concepts"]),
            height=150,
            key=f"core_concepts_text_{st.session_state.current_module_num}"
        )
        module["core_concepts"] = [c.strip() for c in concepts_text.split("\n") if c.strip()]
    
    # ========================================================================
    # TAB 6: DETAILED GOALS
    # ========================================================================
    with tabs[5]:
        st.subheader("Detailed/Deconstructed Goals")
        
        if "goals" not in module:
            module["goals"] = []
        
        # Display existing goals
        for i, goal in enumerate(module["goals"]):
            with st.expander(f"Goal {goal.get('id', i+1)}: {goal.get('text', '')[:50]}..."):
                col1, col2 = st.columns([9, 1])
                
                with col1:
                    goal["id"] = st.number_input(
                        "Goal ID",
                        value=goal.get("id", i+1),
                        min_value=1,
                        key=f"goal_id_{st.session_state.current_module_num}_{i}"
                    )
                    
                    goal["text"] = st.text_area(
                        "Goal Text",
                        value=goal.get("text", ""),
                        height=100,
                        key=f"goal_text_{st.session_state.current_module_num}_{i}"
                    )
                    
                    # Content categories
                    categories_text = st.text_input(
                        "Content Categories (comma-separated)",
                        value=", ".join(goal.get("content_categories", [])),
                        key=f"goal_categories_{st.session_state.current_module_num}_{i}"
                    )
                    goal["content_categories"] = [c.strip() for c in categories_text.split(",") if c.strip()]
                    
                    # Examples
                    examples_text = st.text_area(
                        "Example Questions (one per line)",
                        value="\n".join(goal.get("examples", [])),
                        height=100,
                        key=f"goal_examples_{st.session_state.current_module_num}_{i}"
                    )
                    goal["examples"] = [e.strip() for e in examples_text.split("\n") if e.strip()]
                
                with col2:
                    if st.button("🗑️", key=f"delete_goal_{st.session_state.current_module_num}_{i}"):
                        module["goals"].pop(i)
                        st.rerun()
        
        # Add new goal
        if st.button("➕ Add Detailed Goal", key=f"add_goal_{st.session_state.current_module_num}"):
            new_id = max([g.get("id", 0) for g in module["goals"]], default=0) + 1
            module["goals"].append({
                "id": new_id,
                "text": "",
                "content_categories": [],
                "examples": []
            })
            st.rerun()
    
    # ========================================================================
    # TAB 7: MISCONCEPTIONS
    # ========================================================================
    with tabs[6]:
        st.subheader("Common Misconceptions")
        
        if "misconceptions" not in module:
            module["misconceptions"] = []
        
        # Display existing misconceptions
        for i, misc in enumerate(module["misconceptions"]):
            with st.expander(f"Misconception {i+1}: {misc.get('misconception', '')[:40]}..."):
                col1, col2 = st.columns([9, 1])
                
                with col1:
                    misc["misconception"] = st.text_area(
                        "Misconception",
                        value=misc.get("misconception", ""),
                        height=80,
                        key=f"misc_{st.session_state.current_module_num}_{i}"
                    )
                    
                    misc["correction"] = st.text_area(
                        "Correction",
                        value=misc.get("correction", ""),
                        height=80,
                        key=f"correction_{st.session_state.current_module_num}_{i}"
                    )
                
                with col2:
                    if st.button("🗑️", key=f"delete_misc_{st.session_state.current_module_num}_{i}"):
                        module["misconceptions"].pop(i)
                        st.rerun()
        
        # Add new misconception
        if st.button("➕ Add Misconception", key=f"add_misc_{st.session_state.current_module_num}"):
            module["misconceptions"].append({
                "misconception": "",
                "correction": ""
            })
            st.rerun()
    
    # ========================================================================
    # TAB 8: SAVE & EXPORT
    # ========================================================================
    with tabs[7]:
        st.subheader("Save & Export")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 💾 Save All Modules")
            st.caption("Saves all modules to modules.py")
            if st.button("Save Changes", type="primary", use_container_width=True):
                try:
                    # Module is already a reference to the dict in session state, so it's already updated
                    # Just save all modules
                    saved_path = save_modules_file(st.session_state.all_modules)
                    st.success(f"✅ Saved all modules to {saved_path}")
                    st.success(f"📄 File: {saved_path.name}")
                    st.balloons()
                except Exception as e:
                    st.error(f"❌ Error saving: {e}")
                    st.exception(e)
        
        with col2:
            st.markdown("### 📥 Export Module")
            st.caption("Download current module as JSON")
            json_str = json.dumps(module, indent=2)
            st.download_button(
                label="Download JSON",
                data=json_str,
                file_name=f"module_{module.get('module_number', 1)}.json",
                mime="application/json",
                use_container_width=True
            )
        
        with col3:
            st.markdown("### 🗑️ Delete Module")
            st.caption("Remove this module completely")
            if len(st.session_state.all_modules) > 1:
                if st.button("Delete Module", type="secondary", use_container_width=True):
                    current_num = st.session_state.current_module_num
                    if st.session_state.get('confirm_delete') == current_num:
                        # Actually delete
                        del st.session_state.all_modules[current_num]
                        st.session_state.confirm_delete = None
                        # Switch to first available module
                        st.session_state.current_module_num = min(st.session_state.all_modules.keys())
                        st.success(f"✅ Module {current_num} deleted")
                        st.rerun()
                    else:
                        # Ask for confirmation
                        st.session_state.confirm_delete = current_num
                        st.warning("⚠️ Click again to confirm deletion")
            else:
                st.warning("⚠️ Cannot delete the last module")
        
        # Preview
        st.markdown("### 👁️ Preview")
        with st.expander("View Current Data"):
            st.json(module)


if __name__ == "__main__":
    render_module_editor()
