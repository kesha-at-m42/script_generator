# Engineering Questions — Unit 1 Script Architecture

Questions from the script pipeline team. Answers needed to correctly generate and validate lesson JSON for Unit 1 (M7–M12).

---

## 1. Tool vs Workspace — Where Is the Boundary?

**What we currently understand:**
- `workspace_specs.toys` = the tangibles on screen (picture_graph, bar_graph, equal_groups, etc.)
- `prompt.tool` = the interaction mechanism the student uses to respond (click_category, multiple_choice, drag_to_sort, etc.)

**Questions:**

- Is `tool` strictly a student input mechanism, or does it encompass the visual widget that enables that input (e.g. a palette, a selector UI)?
- When a student interacts with a toy (e.g. clicking a bar on a bar_graph), is the `tool` (click_category) rendered *inside* the toy, *alongside* it, or is it a separate overlay layer?
- Is there a concept of an "active tool" separate from the workspace — something that gets mounted when a prompt beat fires and unmounted after the student responds?

---

## 2. Palettes — Where Do They Live?

Several interactions involve a palette of selectable/placeable items. It's unclear whether the palette belongs to the toy, the tool, or is a separate component.

| Context | Palette type | Current `tool` value | Open question |
|---|---|---|---|
| `picture_graph` (creating mode) | Symbol palette (icons to choose from) | `click_symbol` | Is the palette defined on the toy params, or is it a separate workspace component? |
| `equation_builder` | Tile palette (number/operator tiles) | *(methods C/D per M8 spec)* | How does the tile palette get configured — by the toy params or by the prompt? |
| `dropdown_fillin` | Option palette (fill choices per blank) | `select_fill_option` | Are options defined on the toy (sentence frame) or on the prompt beat? |
| `sorting_area` | Draggable item set | `drag_to_sort` | Where is the set of draggable items declared? On the toy or the prompt? |

**Core question:** Is a palette always owned by the toy (declared in `scene` beat params when the toy is added), or can the prompt beat itself supply a palette at interaction time?

---

## 3. Word Problems — Hosting Architecture

`word_problem_area` is described as a container that hosts other toys (bar graphs, arrays, equal groups) and response components (multiple choice, dropdown_fillin, equation builder).

**Questions:**

- In the script JSON, does a `word_problem_area` have a `children` or `hosted_toys` field listing what it contains?
- Can a prompt beat target a toy hosted *inside* a `word_problem_area`, or does the prompt always target the `word_problem_area` itself?
- What does the `tangible_id` look like for a hosted toy — is it `word_problem_area_1.bar_graph` or something else?
- Can a `word_problem_area` host a `multiple_choice` response (i.e. the MC options appear inline in the word problem frame rather than as a standalone overlay)?

---

## 4. Changing Interaction Mode Mid-Section

Some toys support multiple modes (e.g. `picture_graph` has reading mode and creating mode; `equal_groups` has highlight mode and build mode).

**Questions:**

- Can a toy change modes *within* a section, or does mode change require removing and re-adding the toy?
- If mid-section mode change is supported, is it an `update` scene beat with a `mode` param, or a different mechanism?
- Example: M7 Lesson has `equal_groups` used first in highlight mode (Guide demonstrates), then in build mode (student constructs). Is that two separate sections, or one section with a mode transition beat?

**Proposed pattern (confirm or correct):**
```json
{ "type": "scene", "method": "update", "tangible_id": "equal_groups_1", "params": { "mode": "build" } }
```

---

## 5. Tool vs Scene Beat — Confirm the Boundary

The glossary currently states:
> Highlighting, animating, and revealing are always **scene beats**, never tools. Do not use `highlight` or `animate` as a tool value.

**Confirm:** Is this correct across all Unit 1 toys? Specifically:
- `equal_groups` highlight mode — is the highlighting triggered by a `scene` beat (animate), never by the `tool` field?
- `arrays` row/column toggle — is switching between row and column interpretation a student-initiated `tool` action, or a `scene` beat the Guide controls?

---

## 6. `drag_to_sort` — Not Yet Specced

`drag_to_sort` is listed as pending spec in the glossary. For M9+ lessons that involve sorting activities:

- What is the expected JSON shape for `sorting_area` + `drag_to_sort`?
- What does the validator look like — does it check final zone placement, order, or both?
- Is the draggable content (items to sort) defined on the toy at `add` time, or supplied by the prompt?

---

*Last updated: 2026-04-02*
*Contact: script pipeline team*
