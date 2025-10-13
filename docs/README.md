# 📚 Complete Guide - Script Generator

## 🚀 Quick Start

### Launch the Module Editor:
```bash
# Windows: Double-click
run_module_editor.bat

# Mac/Linux/Git Bash:
./run_module_editor.sh

# Manual:
streamlit run dashboard/run_module_editor.py
```

### Launch Full Dashboard:
```bash
streamlit run dashboard/app.py
```

---

## 📝 Module Editor Guide

### Features:
- ✅ Visual form editor for module data
- ✅ Dropdown to select modules
- ✅ Add/edit/delete modules
- ✅ Save all changes with one click
- ✅ Export individual modules as JSON

### Where is the Save Button?
**Tab 8: "Save & Export"** - Big blue "Save Changes" button

### Quick Workflow:
1. **Select** module from dropdown
2. **Edit** fields in tabs 1-7
3. **Save** in tab 8 by clicking "Save Changes"
4. **Verify** changes in `inputs/modules.py`

### Important:
- Changes stay in memory until you click "Save Changes"
- All widget keys are unique per module (fields update when switching)
- New modules won't persist until you save

---

## 🗂️ Working with Module Data

### Direct Python Access (Recommended):
```python
from inputs.modules import module_1, module_2, MODULES

# Use specific module
print(module_1['module_name'])
print(module_1['vocabulary'])

# Or select dynamically
module = MODULES[1]  # Get module by number

# Loop through all
for num, mod in MODULES.items():
    print(f"Module {num}: {mod['module_name']}")
```

### No Parser Needed!
- All modules in `inputs/modules.py`
- Just import and use directly
- No JSON parsing, no file I/O overhead

---

## 🎯 Pipeline System

### Basic Pipeline:
```python
from core.pipeline import Pipeline
from core.claude_client import ClaudeClient
from steps.question_generator import QuestionGenerator
from steps.answer_generator import AnswerGenerator
from steps.quiz_formatter import QuizFormatter

# Create pipeline
client = ClaudeClient()
pipeline = Pipeline("my_quiz")

# Add steps
pipeline.add_step(QuestionGenerator(client))
pipeline.add_step(AnswerGenerator(client))
pipeline.add_step(QuizFormatter(format_type="html"))

# Execute
results = pipeline.execute({
    "learning_goals": "Students can identify fractions",
    "num_questions": 5
})

# Save
pipeline.save_results()
output_file = save_to_file(pipeline.get_final_output(), "quiz.html", "output")
```

### Using Module Data in Pipeline:
```python
from inputs.modules import MODULES

module = MODULES[1]

pipeline_input = {
    "learning_goals": "\n".join(f"- {g}" for g in module["learning_goals"]),
    "module_name": module["module_name"],
    "grade_level": module["grade_level"],
    "num_questions": 5
}

pipeline.execute(pipeline_input)
```

---

## 📊 Dashboard Features

### Page 1: Prompt Editor
- Edit and save prompt templates
- Changes automatically apply to pipeline steps
- Stored in `prompts/saved_prompts.json`

### Page 2: Test Prompt
- Test prompts with custom input
- See token usage
- View raw and parsed output

### Page 3: Prompt Chain
- Chain multiple prompts together
- Each step uses previous output
- Save chain results

### Page 4: Module Editor
- Visual form for module data
- Add/edit/delete modules
- Save to `inputs/modules.py`

### Page 5: History
- View past test results
- Token usage statistics
- Rerun previous tests

---

## 🏗️ Creating New Pipeline Steps

```python
from core.pipeline import Step
from core.claude_client import ClaudeClient

class MyCustomStep(Step):
    def __init__(self, client: ClaudeClient):
        super().__init__("My Custom Step")
        self.client = client
    
    def execute(self, input_data: dict) -> dict:
        # Your logic here
        prompt = f"Do something with: {input_data['text']}"
        
        response = self.client.generate(
            prompt=prompt,
            model="claude-3-5-sonnet-20241022"
        )
        
        return {
            "output": response,
            "processed": True
        }
```

---

## 📁 Project Structure

```
script_generator/
├── core/                      # Core utilities
│   ├── claude_client.py       # API client
│   ├── pipeline.py            # Pipeline system
│   ├── json_utils.py          # JSON parsing
│   └── file_utils.py          # File I/O
│
├── dashboard/                 # Streamlit UI
│   ├── app.py                 # Main dashboard
│   └── module_editor.py       # Module form editor
│
├── steps/                     # Pipeline steps
│   ├── question_generator.py
│   ├── answer_generator.py
│   └── quiz_formatter.py
│
├── inputs/
│   └── modules.py             # Module data (Python dict)
│
├── prompts/
│   └── saved_prompts.json     # Prompt templates
│
├── output/                    # Generated files
│   ├── pipelines/             # Pipeline results (JSON)
│   └── *.html                 # Quiz outputs
│
└── tests/                     # Test scripts
    └── demo_*.py              # Demo scripts
```

---

## 🎨 Module Data Structure

```python
module_1 = {
    "module_name": "Introduction to Fractions",
    "module_number": 1,
    "grade_level": 3,
    "path_variant": "B",
    
    "learning_goals": [
        "Goal 1",
        "Goal 2"
    ],
    
    "vocabulary": ["term1", "term2"],
    
    "standards": {
        "building_on": ["2.G.A.3"],
        "addressing": ["3.G.A.2"],
        "building_toward": ["3.NF.A.2"]
    },
    
    "core_concepts": ["Concept 1", "Concept 2"],
    
    "goals": [
        {
            "id": 1,
            "text": "Detailed goal description",
            "content_categories": ["category1", "category2"],
            "examples": ["Example question 1", "Example question 2"]
        }
    ],
    
    "misconceptions": [
        {
            "misconception": "Common error",
            "correction": "Correct understanding"
        }
    ]
}
```

---

## 🔧 Common Tasks

### Add a New Module:
1. Open editor: `streamlit run dashboard/run_module_editor.py`
2. Click "➕ New Module"
3. Fill in the fields
4. Go to Tab 8, click "Save Changes"

### Edit Existing Module:
1. Select module from dropdown
2. Edit any fields
3. Go to Tab 8, click "Save Changes"

### Create a New Pipeline:
```python
from core.pipeline import Pipeline
from core.claude_client import ClaudeClient

pipeline = Pipeline("my_pipeline")
pipeline.add_step(MyStep1(client))
pipeline.add_step(MyStep2(client))
results = pipeline.execute(input_data)
```

### Add a New Prompt:
1. Open dashboard: `streamlit run dashboard/app.py`
2. Go to "Prompt Editor" page
3. Create new prompt or edit existing
4. Save - automatically available to pipeline steps

---

## 💡 Tips & Best Practices

### Module Editor:
- **Keys are unique per module** - fields update instantly when switching
- **Changes aren't auto-saved** - must click "Save Changes"
- **Export before major edits** - use "Export Module" for JSON backup
- **Use Git** - commit changes: `git commit -m "Updated module 1"`

### Pipeline Development:
- **Test steps individually** first before chaining
- **Use dashboard** to test prompts before coding
- **Check token usage** - shown in pipeline results
- **Save intermediate results** - useful for debugging

### Data Management:
- **Keep modules in one file** (`inputs/modules.py`) - easier to manage
- **Use direct imports** - no parsing overhead
- **Version control** - commit modules.py changes

---

## 🐛 Troubleshooting

### Editor fields don't update when switching modules:
✅ **Fixed** - All widget keys now include module number

### Can't find save button:
✅ **Tab 8: "Save & Export"** - Look for big blue button

### New module not in modules.py:
✅ **Expected** - Must click "Save Changes" to persist

### Streamlit command not found:
```bash
# Activate virtual environment first
source venv/Scripts/activate  # Git Bash
# OR
venv\Scripts\activate.bat     # Windows CMD
```

### Import errors:
```python
# Add this at top of script
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
```

---

## 📚 Quick Reference Commands

```bash
# Run module editor
streamlit run dashboard/run_module_editor.py

# Run full dashboard
streamlit run dashboard/app.py

# Test module data
python tests/demo_multiple_modules.py

# Test pipeline
python tests/test_module_direct.py

# View quick reference
python docs/QUICK_REFERENCE.py
```

---

## 🎯 Summary

**This system provides:**
- ✅ Visual module data editor with dropdown selector
- ✅ Direct Python access to module data (no parsing)
- ✅ Multi-step pipeline for chaining AI operations
- ✅ Dashboard for prompt management and testing
- ✅ Automatic prompt loading in pipeline steps
- ✅ Complete documentation in one place

**Everything you need to build, test, and deploy educational content generation workflows!**
