## s1_1_scale_progression_pattern_type_pattern · Initial scene setup showing all four bar graphs (scales 1, 2, 5, 10) simultaneously
**Status**: IN PROGRESS
> We want EACH of the graphs to highlight as she does the count for each (scale of 1 and 2) - then maybe 5 and 10 together for them to check. Following the dialogue, not flashing the answer.
**Issue:** All four graphs appear at once instead of appearing sequentially with highlights as the guide counts the lines on each scale
**Step:** `section_structurer`  [high]
**Reasoning:** The section_structurer is responsible for creating scene beats that describe tangible changes on screen. The reviewer wants sequential highlighting of each graph as the guide discusses it, but the structurer created four separate 'add' beats that all fire before any dialogue. The structurer should have either: (1) created interleaved scene/dialogue beats to highlight each graph as it's discussed, or (2) created a single add beat followed by highlight beats synchronized with dialogue about each scale.
**Fix:** Restructure the scene beats to add all graphs first, then create highlight beats interleaved with dialogue that counts lines for scale 1, then scale 2, then both 5 and 10 together for student verification
**Prompt file:** `steps/prompts/section_structurer.py`

**Paste into chat to fix:**
```
Reviewer comment on `s1_1_scale_progression_pattern_type_pattern` (Initial scene setup showing all four bar graphs (scales 1, 2, 5, 10) simultaneously):
  "We want EACH of the graphs to highlight as she does the count for each (scale of 1 and 2) - then maybe 5 and 10 together for them to check. Following the dialogue, not flashing the answer."

Issue: All four graphs appear at once instead of appearing sequentially with highlights as the guide counts the lines on each scale
Beat: {}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```

## s2_1_orientation_transfer_type_d_representation · Initial scene beats adding vertical and horizontal bar graphs
**Status**: IN PROGRESS
> We don’t want these visual cues here - that’s what we are asking the student to click and identify
**Issue:** Scene descriptions explicitly mention visual cues (bar positions between gridlines) that students are being asked to identify themselves
**Step:** `section_structurer`  [high]
**Reasoning:** The scene beat descriptions in beats b0 and b1 state 'Category B bar reaches 35, positioned between 30 and 40 gridlines' — this is a visual cue that reveals the answer before students attempt the task. The section_structurer generates all scene descriptions and is responsible for ensuring they don't give away information students need to discover. This is a scene description accuracy/appropriateness issue, not a dialogue or remediation issue.
**Fix:** Remove the specific positional cues from scene descriptions; describe only what appears without revealing the answer location
**Prompt file:** `steps/prompts/section_structurer.py`

**Paste into chat to fix:**
```
Reviewer comment on `s2_1_orientation_transfer_type_d_representation` (Initial scene beats adding vertical and horizontal bar graphs):
  "We don’t want these visual cues here - that’s what we are asking the student to click and identify"

Issue: Scene descriptions explicitly mention visual cues (bar positions between gridlines) that students are being asked to identify themselves
Beat: {}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```

## s2_1_orientation_transfer_type_d_representation · Two sequential prompts asking student to click Category B in vertical graph, then horizontal graph
**Status**: IN PROGRESS
> @Kesha Bagadia I think this needs to be regenerated because it has the 2 paths again when what we want is a student to select BOTH this time (not just 1 of the 2 like we adjusted for another problem). Can this be set up more like a multi select, but the multi select parts are the parts of the two graphs?
> Also, just a note if you do rerun it (and I can change it again later after regeneration….) I don’t want this to be Category A that is the answer again so I switched the letters around so A is 20, B is 40 and C is 35.
**Issue:** Section uses two separate single-selection prompts instead of one multi-select prompt where student must select the same category in both graphs simultaneously
**Step:** `section_structurer`  [high]
**Reasoning:** The section_structurer creates the initial prompt structure and interaction design. The reviewer wants a single multi-select prompt targeting both graphs at once, but the structurer generated two sequential single-selection prompts (beats b3 and b6). This is a fundamental interaction design decision made during initial section structuring, not a content quality issue that downstream steps would address.
**Fix:** Regenerate section with a single prompt beat using multi-select tool that targets both bar_graph_vertical and bar_graph_horizontal, requiring student to select Category B in both graphs before validation
**Prompt file:** `steps/prompts/section_structurer.py`

**Paste into chat to fix:**
```
Reviewer comment on `s2_1_orientation_transfer_type_d_representation` (Two sequential prompts asking student to click Category B in vertical graph, then horizontal graph):
  "@Kesha Bagadia I think this needs to be regenerated because it has the 2 paths again when what we want is a student to select BOTH this time (not just 1 of the 2 like we adjusted for another problem). Can this be set up more like a multi select, but the multi select parts are the parts of the two graphs?"
  "Also, just a note if you do rerun it (and I can change it again later after regeneration….) I don’t want this to be Category A that is the answer again so I switched the letters around so A is 20, B is 40 and C is 35."

Issue: Section uses two separate single-selection prompts instead of one multi-select prompt where student must select the same category in both graphs simultaneously
Beat: {}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```

## s3_1_real_world_connection_type_c · scene beat showing three scenario images labeled A, B, C
**Status**: IN PROGRESS
> Can this be multi-choice/select and not labeled A, B, C? I’m not remembering exactly what we said would apply in these situations…
**Issue:** The prompt uses letter labels (A, B, C) which violates the no-letter-labels rule from the spec.
**Step:** `section_structurer`  [high]
**Reasoning:** The section_structurer created the initial scene beat with letter labels in the image descriptions ('A: Counting money... B: Measuring height... C: Counting items'). The dialogue_rewriter only processes dialogue beats, not scene beats, so it would not have touched this tangible description. The letter labels appear in the scene description and are referenced throughout the prompt and validator logic.
**Fix:** Remove letter labels from the scenario images and use visual differentiation or position-based selection instead.
**Prompt file:** `steps/prompts/section_structurer.py`

**Paste into chat to fix:**
```
Reviewer comment on `s3_1_real_world_connection_type_c` (scene beat showing three scenario images labeled A, B, C):
  "Can this be multi-choice/select and not labeled A, B, C? I’m not remembering exactly what we said would apply in these situations…"

Issue: The prompt uses letter labels (A, B, C) which violates the no-letter-labels rule from the spec.
Beat: {}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```

## s3_1_real_world_connection_type_c · prompt beat asking students to select which situations work well with scale of 10
**Status**: IN PROGRESS
> If we remove A, B and C from the images, we do have to figure out how to refer to them here though
**Issue:** Prompt options use letter labels (A, B, C) which violates dialogue_rewriter rules, and if images lose labels, prompt becomes unworkable without alternative reference method
**Step:** `section_structurer`  [high]
**Reasoning:** The section_structurer created the prompt beat with options ['A', 'B', 'C'] that directly reference letter labels from the spec. The dialogue_rewriter is responsible for removing letter labels from dialogue beats, but this is a prompt beat with structured options, not dialogue. The structurer should have anticipated that letter labels would be removed from images and designed a prompt mechanism that doesn't depend on them (e.g., clickable images, descriptive option text like 'Counting money in stacks of 10').
**Fix:** Redesign prompt to use descriptive option text or make images themselves selectable, eliminating dependency on letter labels
**Prompt file:** `steps/prompts/section_structurer.py`

**Paste into chat to fix:**
```
Reviewer comment on `s3_1_real_world_connection_type_c` (prompt beat asking students to select which situations work well with scale of 10):
  "If we remove A, B and C from the images, we do have to figure out how to refer to them here though"

Issue: Prompt options use letter labels (A, B, C) which violates dialogue_rewriter rules, and if images lose labels, prompt becomes unworkable without alternative reference method
Beat: {}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```
