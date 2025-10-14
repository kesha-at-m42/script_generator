# Script Generator System - Technical Summary

## Overview
Python-based educational content generation system using Claude API (Anthropic) with a multi-step pipeline architecture for chaining AI operations.

## Core Architecture

### 1. Pipeline System (`core/pipeline.py`)
- **Base Class:** `Step` - abstract base for all pipeline steps
- **Orchestrator:** `Pipeline` - chains steps together, passes data between them
- **Execution Flow:** Each step receives input dict, processes it, returns output dict
- **Results:** Saved as JSON to `output/pipelines/` with timestamps

### 2. API Client (`core/claude_client.py`)
- Wrapper around Anthropic API
- Tracks token usage (input/output tokens)
- Handles model selection (claude-opus-4, claude-3-5-sonnet)
- Uses `.env` file for API key: `ANTHROPIC_API_KEY=...`

### 3. Utility Modules
- `core/json_utils.py` - Extracts JSON from Claude responses (handles markdown code blocks)
- `core/file_utils.py` - File I/O operations (save_json, load_json, save_to_file)

## Pipeline Steps

### QuestionGenerator (`steps/question_generator.py`)
**Input:**
```python
{
    "learning_goals": "- Goal 1\n- Goal 2",  # String with line-separated goals
    "num_questions": 5,                       # Number of questions to generate
    "module_name": "Module Name",             # Optional
    "grade_level": 3                          # Required for appropriate difficulty
}
```

**Output:**
```python
{
    "questions": [
        {
            "goal": "Goal text",
            "prompt": "Question text",
            "interaction_type": "Click|Shade|Multiple Choice|Multiple Select|Drag and Drop|Input|True/False",
            "difficulty_level": 0-4,              # 0=Support, 1=Confidence, 2=Baseline, 3=Stretch, 4=Challenge
            "question_type": "procedural|conceptual|transfer",  # Cognitive focus
            "cognitive_verb": "identify|compare|partition|apply|...",  # Main action verb
            "context": "Visual description"       # Optional setup/scenario
        },
        ...
    ]
}
```

**Prompt Source:** Loads from `prompts/saved_prompts.json` (key: "question_generator")

**Difficulty Framework:** Uses `inputs/difficulty_levels.py`
- **Level 0 (Support):** Easiest wins, 90%+ success rate, confidence building
- **Level 1 (Confidence):** Slightly challenging, 75-85% success rate, strong scaffolding
- **Level 2 (Baseline):** Core mastery assessment, 65-75% success rate
- **Level 3 (Stretch):** Deeper reasoning, 50-60% success rate
- **Level 4 (Challenge):** Above-grade, 30-50% success rate, multi-step
- **Note:** Levels 2-4 count toward mastery; Levels 0-1 are support only

**Question Type Framework:** Uses `inputs/question_types.py`
- **Procedural:** Skill execution (verbs: create, construct, partition, divide)
- **Conceptual:** Understanding & reasoning (verbs: identify, compare, explain, recognize)
- **Transfer:** Application in new contexts (verbs: apply, connect, predict, extend)

### AnswerGenerator (`steps/answer_generator.py`)
**Input:** Output from QuestionGenerator (receives `questions` array)

**Output:**
```python
{
    "questions": [
        {
            "goal": "...",
            "prompt": "...",
            "interaction_type": "...",
            "answer": "Correct answer",
            "explanation": "Why this is correct",
            "hint": "Optional hint"
        },
        ...
    ]
}
```

**Prompt Source:** Loads from `prompts/saved_prompts.json` (key: "answer_generator")

### QuizFormatter (`steps/quiz_formatter.py`)
**Input:** Output from AnswerGenerator

**Output:** HTML or Markdown formatted quiz (string)

**Note:** No LLM call - pure formatting logic

## Data Storage

### Module Data (`inputs/modules.py`)
**Format:** Python dictionary (not JSON - direct import)

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
        "building_on": ["standard1"],
        "addressing": ["standard2"],
        "building_toward": ["standard3"]
    },
    
    "core_concepts": ["concept1"],
    
    "goals": [  # Detailed/deconstructed goals
        {
            "id": 1,
            "text": "Detailed goal description",
            "content_categories": ["category1"],
            "examples": ["Example question 1"]
        }
    ],
    
    "misconceptions": [
        {
            "misconception": "Common error",
            "correction": "Correct understanding"
        }
    ]
}

# Dictionary for dynamic access
MODULES = {1: module_1, 2: module_2}
```

**Usage:**
```python
from inputs.modules import module_1, MODULES
# Direct access - no parsing needed
print(module_1['module_name'])
```

### Prompt Templates (`prompts/saved_prompts.json`)
```json
{
    "question_generator": {
        "name": "Question Generator",
        "template": "Generate {num_questions} questions based on: {learning_goals}..."
    },
    "answer_generator": {
        "name": "Answer Generator", 
        "template": "For each question, provide answer and explanation..."
    }
}
```

Pipeline steps automatically load their templates from this file.

## Example Usage

### Complete Pipeline with Question Metadata
```python
from core.claude_client import ClaudeClient
from core.pipeline import Pipeline
from steps.question_generator import QuestionGenerator
from steps.answer_generator import AnswerGenerator
from steps.quiz_formatter import QuizFormatter
from inputs.modules import module_1

# Initialize
client = ClaudeClient()
pipeline = Pipeline("my_quiz")

# Add steps
pipeline.add_step(QuestionGenerator(client))
pipeline.add_step(AnswerGenerator(client))
pipeline.add_step(QuizFormatter(format_type="html"))

# Prepare input from module data
pipeline_input = {
    "learning_goals": "\n".join(f"- {goal['text']}" for goal in module_1['goals']),
    "module_name": module_1['module_name'],
    "grade_level": module_1['grade_level'],  # Required for difficulty calibration
    "num_questions": 8  # Recommend 8+ for good difficulty/type variety
}

# Execute
results = pipeline.execute(pipeline_input)

# Questions now include metadata
questions = results  # or results.get('questions') depending on step output
for q in questions:
    print(f"Level {q['difficulty_level']} ({q['question_type']}): {q['prompt']}")

# Save
pipeline_file = pipeline.save_results()  # JSON to output/pipelines/
html_file = save_to_file(pipeline.get_final_output(), "quiz.html", "output")

# Check usage and distribution
stats = client.get_stats()
print(f"Total tokens: {stats['total_tokens']}")

# Analyze question distribution
mastery_qs = [q for q in questions if q['difficulty_level'] >= 2]
print(f"Mastery questions: {len(mastery_qs)}/{len(questions)}")
```

## Project Structure
```
script_generator/
├── core/
│   ├── claude_client.py      # API wrapper
│   ├── pipeline.py            # Pipeline orchestration
│   ├── json_utils.py          # JSON parsing utilities
│   └── file_utils.py          # File I/O
│
├── steps/                     # Pipeline steps
│   ├── question_generator.py
│   ├── answer_generator.py
│   └── quiz_formatter.py
│
├── inputs/
│   ├── modules.py             # Module data (Python dict)
│   ├── difficulty_levels.py   # Difficulty framework (0-4)
│   └── question_types.py      # Question type framework (procedural/conceptual/transfer)
│
├── prompts/
│   └── saved_prompts.json     # Prompt templates
│
├── output/
│   ├── pipelines/             # Pipeline results (JSON)
│   └── *.html                 # Generated quizzes
│
└── tests/
    ├── test_module_direct.py  # Complete example
    └── test_complete_pipeline.py
```

## Key Implementation Details

### Step Base Class
```python
class Step(ABC):
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def execute(self, input_data: dict) -> dict:
        """Process input and return output"""
        pass
```

### Pipeline Execution
```python
def execute(self, initial_input: dict) -> dict:
    current_data = initial_input
    for step in self.steps:
        print(f"▶ Step {i+1}/{total}: {step.name}")
        step_output = step.execute(current_data)
        current_data = step_output  # Pass to next step
        self.results.append(step_output)
    return current_data
```

### Prompt Loading Pattern
```python
# In QuestionGenerator.__init__()
def _load_prompt_template(self):
    prompts_file = Path("prompts/saved_prompts.json")
    with open(prompts_file, 'r') as f:
        prompts = json.load(f)
    return prompts.get("question_generator", {}).get("template", "")
```

### JSON Extraction Strategy
Claude often wraps JSON in markdown code blocks:
```python
# json_utils.py tries multiple strategies:
1. Extract from ```json ... ``` blocks
2. Extract from ``` ... ``` blocks
3. Try raw response as JSON
4. Search for {...} or [...] patterns
```

## Environment Setup
```bash
# .env file
ANTHROPIC_API_KEY=sk-ant-...

# Virtual environment
python -m venv venv
source venv/Scripts/activate  # Git Bash
venv\Scripts\activate.bat     # Windows CMD

# Dependencies
pip install anthropic python-dotenv streamlit
```

## Testing
```bash
# Complete pipeline with module data
python tests/test_module_direct.py

# Basic pipeline without modules  
python tests/test_complete_pipeline.py
```

## Important Notes

1. **No Parser Class:** Module data is Python dict, imported directly (no JSON parsing)
2. **Step Chaining:** Each step's output becomes next step's input
3. **Dynamic Prompts:** Prompts auto-generated from framework definitions (edit framework files, regenerate prompt)
4. **Structured Output:** Questions returned with metadata object (distribution summary)
5. **Token Tracking:** ClaudeClient tracks all API usage
6. **Error Handling:** JSON extraction has multiple fallback strategies
7. **State Management:** Pipeline saves intermediate results for debugging

## Framework-Driven Architecture

### Simple 2-Level Runtime Injection
The system uses a **2-level architecture** with runtime data injection:

```
┌─────────────────────────────────────────┐
│ LEVEL 1: Framework Files (Variable Data)│
│  - inputs/difficulty_levels.py         │
│  - inputs/question_types.py            │
└─────────────────────────────────────────┘
                  │
                  │ Loaded at runtime
                  ▼
┌─────────────────────────────────────────┐
│ LEVEL 2: Hard-coded Prompt (Structure)  │
│  - steps/question_generator.py         │
│  - Defines format & requirements       │
└─────────────────────────────────────────┘
```

**To update question generation behavior:**
1. Edit `inputs/difficulty_levels.py` or `inputs/question_types.py`
2. Run question generation - changes take effect immediately
3. No regeneration step needed!

**Example: Change difficulty distribution:**
```python
# In inputs/difficulty_levels.py
DIFFICULTY_DISTRIBUTION = {
    "target_percentages": {
        0: 5,   # Reduce support questions (was 10)
        1: 10,  # Reduce confidence (was 15)
        2: 35,  # Increase baseline (was 30)
        3: 30,  # Increase stretch (was 25)
        4: 20   # Same
    }
}
```

Save the file and run: `python tests/test_question_types.py`

The framework data is loaded fresh each time at runtime and injected into the static prompt template.

### Structured Output Format
Questions are returned in a structured format with metadata:

```python
{
  "metadata": {
    "total_questions": 8,
    "distribution": {
      "by_difficulty": {"0": 1, "1": 1, "2": 2, "3": 2, "4": 2},
      "by_question_type": {"procedural": 2, "conceptual": 4, "transfer": 2},
      "by_interaction_type": {"Click": 1, "Shade": 1, ...}
    }
  },
  "questions": [ ... ]
}
```

**Benefits:**
- **Simple:** Only 2 levels to understand
- **Fast:** Edit and test immediately
- **Async-friendly:** Edit framework files while testing
- **Self-documenting:** Metadata shows actual distribution achieved
- **Easy validation:** Compare metadata against target distributions

## Extending the System

### Create New Step
```python
class MyCustomStep(Step):
    def __init__(self, client: ClaudeClient):
        super().__init__("My Step Name")
        self.client = client
    
    def execute(self, input_data: dict) -> dict:
        # Your logic here
        response = self.client.generate(prompt="...", model="...")
        return {"output": response}
```

### Add to Pipeline
```python
pipeline.add_step(MyCustomStep(client))
```

### Add Prompt Template
Edit `prompts/saved_prompts.json`:
```json
{
    "my_step": {
        "name": "My Step",
        "template": "Your prompt template here..."
    }
}
```

---

**This system is designed for chaining AI operations where each step processes and enhances the previous step's output, particularly for educational content generation.**
