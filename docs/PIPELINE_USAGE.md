# Two-Step Pipeline: Questions → Sequences

## Overview

This pipeline converts learning goals into interactive educational sequences in two steps:

**Step 1: Question Generator** → Generates educational questions with metadata  
**Step 2: Sequence Generator** → Converts questions into guided step-by-step interactions

## Architecture

```
Learning Goals
     ↓
┌────────────────────────────────┐
│  Step 1: QuestionGenerator     │
│  - Reads: difficulty_levels.md │
│  - Reads: question_types.md    │
│  - Output: questions.json      │
└────────────────────────────────┘
     ↓ (questions with metadata)
┌────────────────────────────────┐
│  Step 2: SequenceGenerator     │
│  - Reads: guide_design.md      │
│  - Input: Step 1 output        │
│  - Output: sequences.json      │
└────────────────────────────────┘
     ↓
Interactive Sequences
```

## Step 1: Question Generator

**Input:**
```json
{
  "learning_goals": "- Students can partition shapes\n- Students can identify fractions",
  "num_questions": 5,
  "grade_level": 3
}
```

**Reference Docs:**
- `inputs/docs/difficulty_levels.md` - Defines difficulty 0-4
- `inputs/docs/question_types.md` - Defines procedural/conceptual/transfer

**Output:**
```json
{
  "metadata": {
    "total_questions": 5,
    "distribution": {...}
  },
  "questions": [
    {
      "id": 1,
      "goal": "Students can partition shapes into equal parts",
      "prompt": "Divide the rectangle into 4 equal parts",
      "interaction_type": "Shade",
      "difficulty_level": 1,
      "question_type": "procedural",
      "cognitive_verb": "partition"
    },
    ...
  ]
}
```

## Step 2: Sequence Generator

**Input:**
- Takes the **entire output from Step 1** (questions + metadata)
- Loads character template from `inputs/docs/guide_design.md`

**Output:**
```json
{
  "sequences": [
    {
      "problem_id": 1,
      "difficulty": 1,
      "verb": "partition",
      "goal": "Students can partition shapes into equal parts",
      "steps": [
        {
          "dialogue": "Hi! Today we're going to work on dividing shapes...",
          "prompt": null,
          "visual": null,
          "expected_student_input": "next button"
        },
        {
          "dialogue": "Great! Now I'll show you a rectangle...",
          "prompt": "Click to divide this rectangle into 4 equal parts",
          "visual": [
            {
              "id": "rect1",
              "type": "horizontal_rectangle_bar",
              "state": "empty",
              "description": "A blank rectangle"
            }
          ],
          "expected_student_input": "click to partition"
        },
        ...
      ],
      "valid_visual": [...],
      "student_attempts": {...}
    },
    ...
  ]
}
```

## Usage

### Run Full Pipeline

```bash
python tests/test_full_pipeline.py
```

This will:
1. Generate questions from learning goals
2. Convert questions to interactive sequences
3. Save both outputs to `outputs/` folder
4. Display summary of results

### Run Individual Steps

**Step 1 only:**
```bash
python steps/question_generator.py
```

**Step 2 only (with sample data):**
```bash
python steps/sequence_generator.py
```

### Use in Code

```python
from core.pipeline import Pipeline
from core.claude_client import ClaudeClient
from steps.question_generator import QuestionGenerator
from steps.sequence_generator import SequenceGenerator

client = ClaudeClient()

# Create pipeline
pipeline = Pipeline("questions_to_sequences", save_intermediate=True)
pipeline.add_step(QuestionGenerator(client))
pipeline.add_step(SequenceGenerator(client))

# Execute
results = pipeline.execute({
    "learning_goals": "- Students can add fractions",
    "num_questions": 5,
    "grade_level": 4,
    "questions_per_goal": 3  # For step 2
})

# Get final sequences
sequences = pipeline.get_final_output()
```

## Configuration Files

### Required Files

1. **`inputs/docs/difficulty_levels.md`** (Step 1)
   - Defines 5 difficulty levels (0-4)
   - Targets, purposes, allowed question types

2. **`inputs/docs/question_types.md`** (Step 1)
   - Defines 3 cognitive types (procedural, conceptual, transfer)
   - Verbs, descriptions, targets

3. **`inputs/docs/guide_design.md`** (Step 2)
   - Character/tutor personality
   - Voice characteristics
   - Dialogue style guidelines

### Edit Framework Files

All framework files are **direct markdown** - just edit and run:

```bash
# Edit difficulty levels
code inputs/docs/difficulty_levels.md

# Edit question types  
code inputs/docs/question_types.md

# Edit character template
code inputs/docs/guide_design.md
```

Changes take effect immediately on next run!

## Output Files

Pipeline saves intermediate outputs:

```
outputs/
├── question_generator_20251013_195045.json    # Step 1 output
└── sequence_generator_20251013_195102.json    # Step 2 output
```

**File naming:** `{step_name}_{timestamp}.json`

## Validation

Both steps include validation:

**Step 1 validates:**
- Difficulty levels are 0-4
- Question types are procedural/conceptual/transfer
- Auto-fixes hallucinated values

**Step 2 validates:**
- Required fields present (problem_id, goal, steps)
- Steps array has 3-6 items
- Each step has dialogue
- Final visual state defined

Warnings printed during execution if issues found.

## Token Usage

Approximate token usage per run:

- **Step 1 (Questions):** ~1,500-2,000 tokens
- **Step 2 (Sequences):** ~6,000-8,000 tokens
- **Total Pipeline:** ~8,000-10,000 tokens

## Troubleshooting

**"guide_design.md not found":**
- Create `inputs/docs/guide_design.md` with character template
- Or step will use default character template

**"Invalid difficulty_level":**
- Step 1 auto-fixes to difficulty 2
- Check difficulty_levels.md is correct

**"Only 2 steps (recommended 3-6)":**
- Step 2 warning - LLM generated too few steps
- Check character template encourages detailed scaffolding

**Pipeline fails between steps:**
- Check Step 1 output format matches Step 2 input expectations
- Run steps individually to isolate issue
