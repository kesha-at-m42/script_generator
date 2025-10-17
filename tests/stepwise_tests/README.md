# Stepwise Pipeline Tests

This directory contains **modular, independent tests** for each step of the content generation pipeline. Each test can be run standalone with JSON file inputs/outputs, making development and debugging easier.

## Pipeline Overview

```
Questions JSON
    ↓
[Test 1] Interaction Designer ← Claude API (temp: 0.7)
    ↓
Sequences JSON (main flow)
    ↓
[Test 2] Remediation Generator ← Claude API (temp: 0.3)
    ↓
Remediation JSON (with error paths)
    ↓
[Test 3] Godot Formatter ← Deterministic (no AI)
    ↓
Godot Sequences JSON (production-ready)
```

## Test Files

### `test_1_interaction_designer.py`
**Input:** Questions JSON with learning goals  
**Output:** Sequences JSON with workspace/workspace_context schema  
**Purpose:** Generate main instruction flow (Part 1 + Part 2 structure)

**Run:**
```bash
python tests/stepwise_tests/test_1_interaction_designer.py inputs/questions.json
```

**Schema Generated:**
- Part 1 steps: `dialogue` + `workspace` (array of tangibles)
- Part 2 steps: `dialogue` + `prompt` + `interaction_tool` + `workspace_context` + `correct_answer`
- Success path: `success_path.steps[0].dialogue`

**Key Features:**
- Uses Claude API (temperature: 0.7 for creativity)
- Max tokens: 8000
- Validates Part 1/Part 2 structure
- Checks that visual field is omitted (not null)

---

### `test_2_remediation_generator.py`
**Input:** Sequences JSON (from test_1)  
**Output:** Remediation JSON with error paths  
**Purpose:** Add error handling with Light/Medium/Heavy scaffolding

**Run:**
```bash
python tests/stepwise_tests/test_2_remediation_generator.py outputs/test_interaction_YYYYMMDD_HHMMSS/sequences.json
```

**Schema Generated:**
- Adds `student_attempts` object with error paths
- Each error path has 3 steps:
  - Light: `scaffolding_level="light"`, `workspace_context`, `visual=null`
  - Medium: `scaffolding_level="medium"`, `workspace_context`, `visual.effects[]`
  - Heavy: `scaffolding_level="heavy"`, `workspace_context`, `visual.effects[]` (more detailed)

**Key Features:**
- Uses Claude API (temperature: 0.3 for structured output)
- Max tokens: 16000
- Validates 3 steps per error path (L→M→H progression)
- Checks visual effects present for medium/heavy, null for light

---

### `test_3_godot_formatter.py`
**Input:** Remediation JSON (from test_2)  
**Output:** Godot Sequences JSON (production-ready)  
**Purpose:** Transform to Godot-processable schema

**Run:**
```bash
python tests/stepwise_tests/test_3_godot_formatter.py outputs/test_remediation_YYYYMMDD_HHMMSS/remediation.json
```

**Transformations Applied:**
- Adds `@type` annotations for Godot type system
- Flattens steps structure (no nesting)
- Maps interaction tools to validator types
- Embeds visual effects as `[event:...]` tags in dialogue
- Converts scaffolding levels to remediation IDs (light/medium/heavy)

**Key Features:**
- **Deterministic** (no AI, pure JSON transformation)
- Instant execution
- Maps types: `rectangle_bar` → `RectangleBar`, `square` → `Square`, etc.
- Compatible with `problem_pool.json` schema

---

## Running the Complete Pipeline

### Option 1: Run Tests Sequentially
```bash
# Step 1: Generate sequences
python tests/stepwise_tests/test_1_interaction_designer.py inputs/questions.json

# Step 2: Add error paths (use output path from step 1)
python tests/stepwise_tests/test_2_remediation_generator.py outputs/test_interaction_20251017_152028/sequences.json

# Step 3: Transform to Godot format (use output path from step 2)
python tests/stepwise_tests/test_3_godot_formatter.py outputs/test_remediation_20251017_152122/remediation.json
```

### Option 2: Use Combined Test (Steps 1+2 only)
```bash
python tests/stepwise_tests/test_interaction_remediation.py inputs/questions.json
```

### Option 3: Full Pipeline (All 3 steps)
*Coming soon: `test_full_pipeline.py` to chain all steps automatically*

---

## Schema Evolution

### Our Schema (AI-Generated)
```json
{
  "sequences": [{
    "problem_id": 1,
    "steps": [
      {
        "dialogue": "...",
        "workspace": [{"id": "rect_1", "type": "rectangle_bar", ...}]
      },
      {
        "dialogue": "...",
        "prompt": "...",
        "interaction_tool": "click_sections",
        "workspace_context": {"tangibles_present": ["rect_1"]},
        "correct_answer": [1]
      }
    ],
    "student_attempts": {
      "success_path": {...},
      "error_path_generic": {
        "steps": [
          {"scaffolding_level": "light", "dialogue": "...", "visual": null},
          {"scaffolding_level": "medium", "dialogue": "...", "visual": {"effects": [...]}},
          {"scaffolding_level": "heavy", "dialogue": "...", "visual": {"effects": [...]}}
        ]
      }
    }
  }]
}
```

### Godot Schema (Production-Ready)
```json
{
  "@type": "SequencePool",
  "sequences": [{
    "@type": "Sequence",
    "problem_id": 1,
    "steps": [
      {
        "@type": "Step",
        "workspace": {
          "@type": "WorkspaceData",
          "tangibles": [{"@type": "RectangleBar", "id": "rect_1", ...}]
        },
        "dialogue": "..."
      },
      {
        "@type": "Step",
        "dialogue": "..."
      },
      {
        "@type": "Step",
        "prompt": {
          "@type": "Prompt",
          "text": "...",
          "tool": "click_sections",
          "validator": {"@type": "SelectSectionsValidator", "answer": [1]},
          "remediations": [
            {
              "@type": "Remediation",
              "id": "light",
              "step": {"@type": "Step", "dialogue": "..."}
            },
            {
              "@type": "Remediation",
              "id": "medium",
              "step": {"@type": "Step", "dialogue": "[event:highlight_pulse_sections] ..."}
            },
            {
              "@type": "Remediation",
              "id": "heavy",
              "step": {"@type": "Step", "dialogue": "[event:demo_shade_section] ..."}
            }
          ]
        }
      },
      {
        "@type": "Step",
        "dialogue": "Success!"
      }
    ]
  }]
}
```

---

## Validation

Each test includes comprehensive validation:

### Test 1 Validation
- ✓ Part 1 steps have `workspace` field
- ✓ Part 2 steps have `workspace_context`, `interaction_tool`, `correct_answer`
- ✓ `visual` field is omitted (not set to null)
- ✓ Success path present

### Test 2 Validation
- ✓ Each error path has 3 steps (L/M/H)
- ✓ Scaffolding levels correct: light → medium → heavy
- ✓ Light steps have `visual=null`
- ✓ Medium/heavy steps have `visual.effects` array
- ✓ `workspace_context` present in all error steps

### Test 3 Validation
- ✓ All objects have `@type` annotations
- ✓ Tangibles mapped to Godot class names
- ✓ Validators have correct `@type` based on interaction tool
- ✓ Remediations have `id` field (light/medium/heavy)
- ✓ Visual effects embedded as `[event:...]` tags

---

## Output Structure

Each test creates timestamped output directories:

```
outputs/
├── test_interaction_20251017_152028/
│   ├── sequences_raw.txt          # Raw Claude API response
│   ├── sequences.json              # Parsed sequences (input for test 2)
│   └── validation_report.json     # Validation results
│
├── test_remediation_20251017_152122/
│   ├── remediation_raw.txt        # Raw Claude API response
│   ├── remediation.json            # With error paths (input for test 3)
│   └── validation_report.json     # Validation results
│
└── test_godot_20251017_153413/
    ├── godot_sequences.json        # Final Godot format (ready for game)
    └── validation_report.json     # Validation results
```

---

## Terminology

### Our Internal Schema
- **tangibles**: Physical objects in the workspace (rectangles, circles, number lines)
- **workspace**: Array of tangibles (Part 1 setup)
- **workspace_context**: Metadata about tangibles (Part 2 reference)
- **visual effects**: Animations/highlights for remediation

### Reference Documentation (visual_guide.md)
- **shapes**: Visual objects
- **rectangle bars**: Horizontal/vertical bars
- **visual design**: Animation and layout

*Note: Claude successfully interprets both terminologies. We kept "tangibles/workspace" for clarity in prompts despite visual_guide.md using "shapes".*

---

## Next Steps

1. **Test with more questions**: Run with different learning goals and difficulty levels
2. **Add more validator types**: Extend `create_validator()` in test_3 for new interaction tools
3. **Create full pipeline test**: Chain all 3 steps in one command
4. **Add formatter step**: Convert to human-readable markdown scripts for review

---

## Debugging Tips

### Common Issues

**Test 1: Template escaping errors**
- Symptom: `KeyError: '"dialogue"'`
- Fix: Double braces `{{}}` in INSTRUCTIONS section of prompts (handled in interaction_designer.py)

**Test 2: Validation failures**
- Symptom: "Expected 3 steps, got X"
- Check: Claude may have skipped scaffolding levels
- Fix: Review remediation_system.md for clearer error pattern definitions

**Test 3: Missing @type annotations**
- Symptom: Validation issues with @type fields
- Fix: Check `map_type_to_godot()` function has all type mappings

### Running with Debug Output

Add debug prints in any test file:
```python
# After loading input
print(json.dumps(input_data, indent=2)[:500])

# After Claude response
print(f"Response preview: {response[:500]}")

# After transformation
print(json.dumps(output_data, indent=2)[:500])
```

---

## Credits

**Pipeline Architecture:** Modular stepwise testing approach  
**Schema Design:** Workspace/visual separation, Part 1/Part 2 structure  
**Godot Integration:** @type annotations, flattened steps, event tags
