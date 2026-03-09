# script_generator

A pipeline system for generating interactive lesson scripts using Claude. Scripts are
structured JSON consumed by a learning product runtime.

---

## How It Works

Content moves through three phases before reaching the product.

### 1. Preproduction

Before any pipeline runs, the curriculum and design teams produce the inputs the
pipeline depends on. This is a multi-step human process, not automated.

```
curriculum documents
        |
        v
unit decomposition
        |
        v
module map  (modules chunked to curriculum standards, one concept per module)
        |
        +---> toy_specs.md        (tangibles and their interaction surfaces)
        |
        +---> guide_design.md     (voice, tone, values the script must hold)
        |
        v
starter packs  (units/unit{N}/_starter_packs/module_{N}.json)
```

**Starter packs** are the connective tissue between curriculum and pipeline. They encode
everything a module needs: what tangibles exist, what misconceptions to address, what
vocabulary is in play, what the one core concept is, and what constraints scope the lesson.
They are built from curriculum documents, toy specs, and the module map.

**Toy specs** (`units/unit{N}/toy_specs.md`) describe every tangible available for that
unit — what it looks like, what modes it supports, what interaction surfaces it exposes.
These come from UX preproduction.

**Guide design** (`docs/guide_design.md`) holds the voice and values the script must
embody — how the guide speaks, what to avoid, how to handle correct and incorrect
student responses.

---

### 2. Content Authoring

With preproduction in place, content authors write module spec files in plain markdown.
Each spec describes the interactions for one lesson phase.

```
units/
  unit1/
    toy_specs.md
    _starter_packs/
      module_1.json
      module_2.json
    module1/
      warmup.md       <- what the warmup does, beat by beat in plain language
      lesson.md       <- the main lesson interactions
      exitcheck.md    <- mastery check
      practice.md     <- extended practice
      synthesis.md    <- consolidation interactions
    module2/
      warmup.md
      ...
```

Spec files describe pedagogical intent, not schema. The pipeline handles translation.

---

### 3. Generation Pipeline

The pipeline transforms a spec file into a structured JSON array of sections.

```
spec (.md)
    |
    v  [AI] script_generator / section_structurer
    |
    v  section array  [{ id, type, scene, steps }]
    |
    v  [FORMATTING] filter_sections
    |
    v  [AI] remediation_generator  (batch: one call per section)
    |
    v  [FORMATTING] remediation_merger
    |
    v  full section array  (correct + incorrect validator states)
    |
    v  [AI] dialogue_rewriter  (optional voice pass)
    |
    v  [FORMATTING] dialogue_merger
    |
    v  final section array
    |
    v  [FORMATTING] push -> Notion
```

**AI steps** call Claude with a prompt built from the spec, starter pack fields,
toy specs, and guide design. **Formatting steps** are deterministic Python functions
with no API calls.

Each pipeline run creates a versioned output directory:
```
outputs/unit1/warmup_generator_module_2/
  v0/
    step_01_script_generator/
    step_02_filter_sections/
    step_03_remediation_generator/
    step_04_merge_remediation/
    step_05_push/        <- push.json (notion url)
    step_06_pull/        <- pull.json (edited content, after review)
```

---

### 4. Review and Editing

After generation, the script is pushed to Notion for human review. Writers improve
dialogue voice; teachers validate pedagogical intent and visual alignment. Changes
are pulled back as a versioned file.

See `docs/references/script_editing_process.md` for the full workflow.

```bash
# Push to Notion (runs as step 5 in pipeline; can also run standalone)
python cli/push_to_notion.py outputs/unit1/warmup_generator_module_2/v0/step_05_push/push.json

# Pull after editing -> saves to step_06_pull/pull.json in the same version
python cli/push_to_notion.py outputs/unit1/warmup_generator_module_2/v0/step_05_push/push.json --pull
```

---

### 5. Output Format and Product Ingestion

The pipeline produces a JSON array of **sections**. Each section is a self-contained sub-sequence — one concept. A section may contain
multiple student actions, one, or none (transitions, demonstrations, bridging narration). The product executes them as a
beat-by-beat student journey.

#### Section

```json
{
  "id": "s5_1_scale_toggle",
  "type": "main",
  "scene": ["data_table"],
  "steps": [ [ beat, beat, beat ] ]
}
```

| Field | Meaning |
|-------|---------|
| `id` | Unique slug. Format: `s{major}_{minor}_{name}` or `s{major}_{name}`. Used for analytics and goto targets. |
| `type` | `main` (interactive), `transition` (dialogue-only), `remediation` (remediation path). |
| `scene` | Tangible IDs already visible when the section begins. Product ensures these are loaded. |
| `steps` | Groups of beats. Executed in order. Steps within a section are separated by a visual pause. |

#### Beat Types

**dialogue** — guide speaks to the student.
```json
{ "type": "dialogue", "text": "Here's data you know — and a graph with scale of 2." }
```
Product action: display text / play TTS.

---

**scene** — workspace command.
```json
{
  "type": "scene",
  "method": "add",
  "tangible_id": "picture_graph_pets",
  "tangible_type": "picture_graph",
  "params": { "mode": "reading", "scale": 2, "categories": [...], "values": [...] }
}
```

| `method` | Product action |
|----------|---------------|
| `add` | Instantiate and show tangible |
| `remove` | Destroy tangible |
| `show` / `hide` | Toggle visibility |
| `update` | Mutate props on existing tangible |
| `animate` | Trigger named animation event |
| `lock` / `unlock` | Disable / enable student interaction |

`tangible_type` maps to a product component class. `params` are concrete values — no
placeholders. The `description` field in params is human-readable context, not rendered.

---

**prompt** — student interaction gate. Blocks execution until resolved.
```json
{
  "type": "prompt",
  "text": "Toggle the scale to 1. What happens to the graph?",
  "tool": "click_component",
  "target": "picture_graph_pets.scale_toggle",
  "validator": [ ... ]
}
```

| Tool | Student action |
|------|---------------|
| `click_component` | Tap a specific component on a tangible |
| `multiple_choice` | Select one from a list |
| `multi_select` | Select one or more |
| `drag_item` | Drag to a target |
| `build_graph` | Place symbols to construct a graph |
| `input_number` | Enter or adjust a numeric value |

---

**validator** — declarative state machine. Evaluated top-to-bottom; first match executes.
```json
{
  "condition": { "selected": "Scale of 2" },
  "description": "Student selected Scale of 2 — correct",
  "is_correct": true,
  "steps": [ [ beat, beat ] ]
}
```

| Condition shape | Meaning |
|----------------|---------|
| `{}` | Always matches — use as fallback or any-response-advances |
| `{ "selected": "value" }` | MC/multi-select answer equals value |
| `{ "incorrect_count": N }` | Student has failed this prompt N times |
| `{ "and": [...] }` | All sub-conditions must match |
| `{ "or": [...] }` | Any sub-condition must match |

`is_correct: true` closes the gate and advances to the next section.
`is_correct: false` re-presents the prompt (attempt count increments).

---

**current_scene** — reference snapshot of workspace state at this point. Not rendered.
The product may use it for state reconciliation or QA; it is not required for execution.

---

#### Execution Model

```
load section array
for each section in order:
    ensure section.scene tangibles are loaded
    for each step in section.steps:
        for each beat in step:
            dialogue      -> speak / display
            scene         -> execute workspace command
            prompt        -> present, wait for input
                            evaluate validator conditions in order
                            first match -> execute state.steps
                            is_correct: true  -> next section
                            is_correct: false -> re-present prompt
            current_scene -> skip
```

#### Architecture Mapping

| Script concept | Architecture equivalent |
|---------------|------------------------|
| `section` | Screen / node in a lesson graph |
| `section.type` | Node type |
| `scene` (field) | Scene preload / prop state at entry |
| `scene` (beat) | World state mutation command |
| `dialogue` beat | NPC speech event |
| `prompt` beat | Input gate |
| `validator` | Condition-response table / state machine transitions |
| `validator condition` | Guard clause |
| `validator state.steps` | Transition payload |
| `tangible_id` | Entity / prop instance ID |
| `tangible_type` | Component / prefab class |
| `tool` | Input handler type |
| `is_correct` | Whether interaction closes the gate |
| `current_scene` | State snapshot — optional reconciliation data |

`tangible_type` and `tool` are the two extension points where product-specific
component mappings are required.

---

## Setup

**Prerequisites:** Python 3.8+, Anthropic API key, Notion API key (optional)

```bash
git clone <repo>
cd script_generator
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
pip install -r requirements.txt

# Configure
cp .env.example .env
# Set: ANTHROPIC_API_KEY, NOTION_API_KEY, NOTION_PARENT_PAGE_ID
```

---

## CLI Reference

**Run a pipeline:**
```bash
python cli/run_pipeline.py -p warmup_generator -u 1 -m 2
```

**Rerun a specific step:**
```bash
python cli/rerun.py warmup_generator --start-from 5 --end-at 5 --unit 1 --module 2
```

**Push to / pull from Notion:**
```bash
python cli/push_to_notion.py outputs/unit1/warmup_generator_module_2/v0/step_05_push/push.json
python cli/push_to_notion.py outputs/unit1/warmup_generator_module_2/v0/step_05_push/push.json --pull
```

---

## Key Directories

| Path | Contents |
|------|----------|
| `units/unit{N}/` | Spec files, toy specs, starter packs per unit |
| `config/pipelines.json` | Pipeline definitions |
| `steps/prompts/` | AI prompt steps |
| `steps/formatting/` | Deterministic formatting steps |
| `core/` | Pipeline orchestration, Claude client, prompt builder |
| `utils/` | Shared utilities |
| `docs/` | Design and reference documentation |
| `outputs/` | Generated content (gitignored) |

---

## Documentation

| Doc | What it covers |
|-----|---------------|
| `docs/guide_design.md` | Voice, tone, and values for the script guide |
| `docs/references/lesson_script_schema_guide.md` | Full schema reference |
| `docs/references/script_editing_process.md` | Writer and teacher editing workflows |
| `docs/remediation_design_ref.md` | Remediation system design |
