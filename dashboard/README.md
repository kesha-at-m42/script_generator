# Dashboard

Visual interface for prompt engineering and testing with Claude.

## Features

- **📝 Prompt Editor**: Create, edit, and manage prompt templates
- **🧪 Test Prompt**: Test prompts with Claude API in real-time
- **📊 History**: View and manage past test results

## Quick Start

From the project root directory:

```bash
# Windows
run_dashboard.bat

# Linux/Mac
./run_dashboard.sh

# Or manually
streamlit run dashboard/app.py
```

The dashboard will open automatically at `http://localhost:8501`

## File Structure

```
dashboard/
├── app.py              # Main Streamlit application
└── __init__.py         # Package initialization
```

## Data Storage

- **Prompts**: Saved to `prompts/saved_prompts.json`
- **Test Results**: Saved to `output/dashboard/`

## Usage

### 1. Edit Prompts

- Navigate to "Prompt Editor"
- Select an existing prompt or create a new one
- Use `{variable_name}` syntax for dynamic values
- Click "Save Changes" to persist edits

### 2. Test Prompts

- Navigate to "Test Prompt"
- Select a prompt to test
- Fill in the variable values
- Click "Run Test with Claude"
- Results are automatically saved

### 3. View History

- Navigate to "History"
- View past test runs with inputs and outputs
- Delete old results if needed

## Tips

- All prompt edits are saved to disk and persist across sessions
- Test results include timestamps for tracking
- Use the Preview feature before running expensive API calls
