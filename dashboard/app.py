"""Visual Dashboard for Prompt Engineering and Testing"""
import sys
from pathlib import Path
import json
import streamlit as st
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from core.json_utils import parse_json
from steps.question_generator import QuestionGenerator
from dashboard.module_editor import render_module_editor

# Configuration
PROMPTS_FILE = "prompts/saved_prompts.json"
OUTPUT_DIR = "output/dashboard"

def load_prompts():
    """Load saved prompts from file"""
    prompts_path = Path(PROMPTS_FILE)
    if prompts_path.exists():
        with open(prompts_path, 'r') as f:
            return json.load(f)
    return {
        "question_generator": {
            "name": "Question Generator",
            "template": """Generate {num_questions} educational questions based on these learning goals:

{learning_goals}

Return as a JSON array where each item has:
- "goal": the specific learning goal being addressed
- "prompt": the question text
- "interaction_type": one of ["Click", "Shade", "Multiple Choice", "Drag and Drop"]

Example:
[
  {{
    "goal": "Students can identify fractions",
    "prompt": "Click on the shape that shows 1/2",
    "interaction_type": "Click"
  }}
]"""
        }
    }

def save_prompts(prompts):
    """Save prompts to file"""
    prompts_path = Path(PROMPTS_FILE)
    prompts_path.parent.mkdir(parents=True, exist_ok=True)
    with open(prompts_path, 'w') as f:
        json.dump(prompts, f, indent=2)

def save_result(prompt_name, input_data, output_data):
    """Save test result"""
    output_path = Path(OUTPUT_DIR)
    output_path.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = output_path / f"{prompt_name}_{timestamp}.json"
    
    result = {
        "timestamp": timestamp,
        "prompt_name": prompt_name,
        "input": input_data,
        "output": output_data
    }
    
    with open(filename, 'w') as f:
        json.dump(result, f, indent=2)
    
    return str(filename)

# Streamlit App
st.set_page_config(page_title="Prompt Dashboard", layout="wide", page_icon="🎯")

st.title("🎯 Prompt Engineering Dashboard")
st.markdown("Edit, test, and manage your Claude prompts")

# Sidebar for navigation
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Go to:", ["Prompt Editor", "Test Prompt", "Prompt Chain", "Module Editor", "History"])
    
    st.divider()
    st.header("Quick Stats")
    if 'test_count' not in st.session_state:
        st.session_state.test_count = 0
    st.metric("Tests Run", st.session_state.test_count)

# Load prompts
if 'prompts' not in st.session_state:
    st.session_state.prompts = load_prompts()

prompts = st.session_state.prompts

# PAGE 1: Prompt Editor
if page == "Prompt Editor":
    st.header("📝 Prompt Editor")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Saved Prompts")
        prompt_names = list(prompts.keys())
        selected_prompt = st.selectbox("Select a prompt:", prompt_names)
        
        st.divider()
        
        # Add new prompt
        st.subheader("Add New Prompt")
        new_prompt_id = st.text_input("Prompt ID (no spaces):", key="new_id")
        new_prompt_name = st.text_input("Display Name:", key="new_name")
        
        if st.button("➕ Create New Prompt"):
            if new_prompt_id and new_prompt_name:
                if new_prompt_id not in prompts:
                    prompts[new_prompt_id] = {
                        "name": new_prompt_name,
                        "template": "Your prompt template here..."
                    }
                    save_prompts(prompts)
                    st.success(f"Created '{new_prompt_name}'!")
                    st.rerun()
                else:
                    st.error("Prompt ID already exists!")
    
    with col2:
        if selected_prompt:
            st.subheader(f"Edit: {prompts[selected_prompt]['name']}")
            
            # Edit prompt name
            new_name = st.text_input("Prompt Name:", 
                                    value=prompts[selected_prompt]['name'],
                                    key=f"edit_name_{selected_prompt}")
            
            # Edit prompt template
            new_template = st.text_area("Prompt Template:", 
                                       value=prompts[selected_prompt]['template'],
                                       height=400,
                                       key=f"edit_template_{selected_prompt}",
                                       help="Use {variable_name} for placeholders")
            
            col_save, col_delete = st.columns(2)
            
            with col_save:
                if st.button("💾 Save Changes", type="primary", use_container_width=True):
                    prompts[selected_prompt]['name'] = new_name
                    prompts[selected_prompt]['template'] = new_template
                    save_prompts(prompts)
                    st.success("✓ Prompt saved!")
            
            with col_delete:
                if st.button("🗑️ Delete Prompt", use_container_width=True):
                    if len(prompts) > 1:
                        del prompts[selected_prompt]
                        save_prompts(prompts)
                        st.success("Prompt deleted!")
                        st.rerun()
                    else:
                        st.error("Cannot delete the last prompt!")
            
            # Show variables in template
            st.divider()
            st.subheader("Variables Found")
            import re
            variables = re.findall(r'\{(\w+)\}', new_template)
            if variables:
                st.write(", ".join([f"`{{{v}}}`" for v in set(variables)]))
            else:
                st.info("No variables found. Use {variable_name} syntax.")

# PAGE 2: Test Prompt
elif page == "Test Prompt":
    st.header("🧪 Test Prompt")
    
    # Select prompt to test
    prompt_names = list(prompts.keys())
    selected_prompt = st.selectbox("Select prompt to test:", prompt_names)
    
    if selected_prompt:
        prompt_data = prompts[selected_prompt]
        st.subheader(f"Testing: {prompt_data['name']}")
        
        # Show prompt template
        with st.expander("📄 View Prompt Template", expanded=False):
            st.code(prompt_data['template'], language="text")
        
        # Extract variables
        import re
        variables = re.findall(r'\{(\w+)\}', prompt_data['template'])
        unique_vars = list(set(variables))
        
        st.divider()
        st.subheader("Input Parameters")
        
        # Create input fields for each variable
        input_values = {}
        for var in unique_vars:
            if var == "num_questions":
                input_values[var] = st.number_input(f"{var}:", 
                                                    min_value=1, 
                                                    max_value=20, 
                                                    value=5)
            elif var == "learning_goals":
                input_values[var] = st.text_area(f"{var}:", 
                                                 height=150,
                                                 value="- Students can identify fractions\n- Students can compare fractions")
            else:
                input_values[var] = st.text_area(f"{var}:", height=100)
        
        # Show final prompt
        st.divider()
        st.subheader("Final Prompt Preview")
        try:
            final_prompt = prompt_data['template'].format(**input_values)
            with st.expander("👁️ Preview (click to expand)", expanded=False):
                st.code(final_prompt, language="text")
        except KeyError as e:
            st.error(f"Missing variable: {e}")
            final_prompt = None
        
        st.divider()
        
        # Test with Claude
        col1, col2 = st.columns([1, 3])
        with col1:
            max_tokens = st.number_input("Max Tokens:", min_value=100, max_value=4000, value=2000)
        
        if st.button("🚀 Run Test with Claude", type="primary", use_container_width=True):
            if final_prompt:
                with st.spinner("Calling Claude API..."):
                    try:
                        # Initialize Claude client
                        client = ClaudeClient()
                        
                        # Generate response
                        response = client.generate(final_prompt, max_tokens=max_tokens)
                        
                        # Update test count
                        st.session_state.test_count += 1
                        
                        # Display results
                        st.success("✓ Response received!")
                        
                        col_a, col_b = st.columns(2)
                        
                        with col_a:
                            st.metric("Input Tokens", client.get_stats()['input_tokens'])
                        with col_b:
                            st.metric("Output Tokens", client.get_stats()['output_tokens'])
                        
                        st.divider()
                        st.subheader("📤 Claude's Response")
                        
                        # Try to parse as JSON
                        try:
                            parsed = parse_json(response)
                            st.json(parsed)
                            
                            # Save result
                            saved_path = save_result(selected_prompt, input_values, parsed)
                            st.info(f"💾 Result saved to: `{saved_path}`")
                        except:
                            st.text_area("Raw Response:", value=response, height=300)
                            
                            # Save result
                            saved_path = save_result(selected_prompt, input_values, response)
                            st.info(f"💾 Result saved to: `{saved_path}`")
                        
                    except Exception as e:
                        st.error(f"Error: {e}")

# PAGE 3: Prompt Chain
elif page == "Prompt Chain":
    st.header("🔗 Prompt Chain Builder")
    st.markdown("Create multi-step workflows where outputs feed into subsequent prompts")
    
    # Initialize chain state
    if 'chain_steps' not in st.session_state:
        st.session_state.chain_steps = []
    if 'chain_results' not in st.session_state:
        st.session_state.chain_results = []
    
    # Chain builder
    st.subheader("Build Your Chain")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.write("**Add Step to Chain:**")
        prompt_names = list(prompts.keys())
        step_prompt = st.selectbox("Select prompt:", prompt_names, key="chain_add")
        
        if st.button("➕ Add Step"):
            st.session_state.chain_steps.append({
                "prompt_id": step_prompt,
                "prompt_name": prompts[step_prompt]['name']
            })
            st.rerun()
        
        if st.button("🗑️ Clear Chain"):
            st.session_state.chain_steps = []
            st.session_state.chain_results = []
            st.rerun()
    
    with col2:
        if st.session_state.chain_steps:
            st.write("**Current Chain:**")
            for i, step in enumerate(st.session_state.chain_steps):
                col_a, col_b = st.columns([4, 1])
                with col_a:
                    st.write(f"{i+1}. {step['prompt_name']} (`{step['prompt_id']}`)")
                with col_b:
                    if st.button("❌", key=f"remove_{i}"):
                        st.session_state.chain_steps.pop(i)
                        st.rerun()
        else:
            st.info("No steps in chain yet. Add prompts to build your workflow.")
    
    # Execute chain
    if st.session_state.chain_steps:
        st.divider()
        st.subheader("Configure & Execute")
        
        # First step inputs
        first_step = st.session_state.chain_steps[0]
        first_prompt_data = prompts[first_step['prompt_id']]
        
        st.write(f"**Step 1 Inputs:** {first_step['prompt_name']}")
        
        import re
        first_vars = re.findall(r'\{(\w+)\}', first_prompt_data['template'])
        unique_first_vars = list(set(first_vars))
        
        initial_inputs = {}
        for var in unique_first_vars:
            if var == "num_questions":
                initial_inputs[var] = st.number_input(f"{var}:", min_value=1, max_value=20, value=5, key="chain_input_num")
            elif var == "learning_goals":
                initial_inputs[var] = st.text_area(f"{var}:", height=100, 
                                                   value="- Students can identify fractions\n- Students can compare fractions",
                                                   key="chain_input_goals")
            else:
                initial_inputs[var] = st.text_area(f"{var}:", height=100, key=f"chain_input_{var}")
        
        # Variable mapping for subsequent steps
        st.divider()
        st.subheader("Variable Mapping")
        st.markdown("Map outputs to inputs for subsequent steps")
        
        variable_mappings = []
        
        for i in range(1, len(st.session_state.chain_steps)):
            step = st.session_state.chain_steps[i]
            prompt_data = prompts[step['prompt_id']]
            step_vars = list(set(re.findall(r'\{(\w+)\}', prompt_data['template'])))
            
            st.write(f"**Step {i+1}: {step['prompt_name']}**")
            
            mapping = {}
            for var in step_vars:
                col_a, col_b, col_c = st.columns([2, 1, 2])
                with col_a:
                    st.write(f"`{{{var}}}`")
                with col_b:
                    st.write("⬅️")
                with col_c:
                    source = st.selectbox(
                        f"Source for {var}:",
                        ["Previous output", "Custom value"],
                        key=f"map_{i}_{var}"
                    )
                    if source == "Custom value":
                        custom_val = st.text_input("Value:", key=f"custom_{i}_{var}")
                        mapping[var] = {"type": "custom", "value": custom_val}
                    else:
                        mapping[var] = {"type": "previous_output", "value": None}
            
            variable_mappings.append(mapping)
        
        # Execute button
        st.divider()
        max_tokens = st.number_input("Max Tokens per step:", min_value=100, max_value=4000, value=2000, key="chain_tokens")
        
        if st.button("🚀 Execute Chain", type="primary", use_container_width=True):
            st.session_state.chain_results = []
            client = ClaudeClient()
            
            try:
                # Execute each step
                for i, step in enumerate(st.session_state.chain_steps):
                    with st.spinner(f"Executing Step {i+1}/{len(st.session_state.chain_steps)}: {step['prompt_name']}..."):
                        prompt_data = prompts[step['prompt_id']]
                        
                        # Prepare inputs
                        if i == 0:
                            # First step uses initial inputs
                            step_inputs = initial_inputs
                        else:
                            # Subsequent steps use mappings
                            step_inputs = {}
                            mapping = variable_mappings[i-1]
                            
                            for var, source in mapping.items():
                                if source['type'] == 'custom':
                                    step_inputs[var] = source['value']
                                else:
                                    # Use previous output
                                    prev_result = st.session_state.chain_results[i-1]
                                    if isinstance(prev_result['output'], str):
                                        step_inputs[var] = prev_result['output']
                                    else:
                                        step_inputs[var] = json.dumps(prev_result['output'], indent=2)
                        
                        # Format prompt
                        final_prompt = prompt_data['template'].format(**step_inputs)
                        
                        # Call Claude
                        response = client.generate(final_prompt, max_tokens=max_tokens)
                        
                        # Try to parse JSON
                        try:
                            parsed_output = parse_json(response)
                        except:
                            parsed_output = response
                        
                        # Store result
                        st.session_state.chain_results.append({
                            "step": i + 1,
                            "prompt_name": step['prompt_name'],
                            "inputs": step_inputs,
                            "output": parsed_output
                        })
                
                st.success(f"✓ Chain executed successfully! {len(st.session_state.chain_steps)} steps completed.")
                
                # Show results
                st.divider()
                st.subheader("Chain Results")
                
                for result in st.session_state.chain_results:
                    with st.expander(f"Step {result['step']}: {result['prompt_name']}", expanded=True):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.subheader("Inputs")
                            st.json(result['inputs'])
                        
                        with col2:
                            st.subheader("Output")
                            st.json(result['output'])
                
                # Show stats
                stats = client.get_stats()
                st.divider()
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Total Steps", len(st.session_state.chain_steps))
                with col_b:
                    st.metric("Input Tokens", stats['input_tokens'])
                with col_c:
                    st.metric("Output Tokens", stats['output_tokens'])
                
            except Exception as e:
                st.error(f"Error executing chain: {e}")
        
        # Show previous results if any
        if st.session_state.chain_results:
            st.divider()
            if st.button("💾 Save Chain Results"):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                chain_output = {
                    "timestamp": timestamp,
                    "chain_steps": st.session_state.chain_steps,
                    "results": st.session_state.chain_results
                }
                
                output_path = Path(OUTPUT_DIR)
                output_path.mkdir(parents=True, exist_ok=True)
                filename = output_path / f"chain_{timestamp}.json"
                
                with open(filename, 'w') as f:
                    json.dump(chain_output, f, indent=2)
                
                st.success(f"💾 Chain results saved to: `{filename}`")

# PAGE 4: Module Editor
elif page == "Module Editor":
    render_module_editor()

# PAGE 5: History
elif page == "History":
    st.header("📊 Test History")
    
    output_path = Path(OUTPUT_DIR)
    
    if output_path.exists():
        result_files = sorted(output_path.glob("*.json"), reverse=True)
        
        if result_files:
            st.info(f"Found {len(result_files)} test results")
            
            # Display recent results
            for i, file_path in enumerate(result_files[:10]):
                with open(file_path, 'r') as f:
                    result = json.load(f)
                
                with st.expander(f"🕐 {result['timestamp']} - {result['prompt_name']}", expanded=(i==0)):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("Input")
                        st.json(result['input'])
                    
                    with col2:
                        st.subheader("Output")
                        st.json(result['output'])
                    
                    if st.button(f"Delete", key=f"delete_{i}"):
                        file_path.unlink()
                        st.success("Deleted!")
                        st.rerun()
        else:
            st.info("No test results yet. Run some tests!")
    else:
        st.info("No test results yet. Run some tests!")

# Footer
st.divider()
st.caption("💡 Tip: Edit prompts, test them with Claude, and track your results all in one place!")
