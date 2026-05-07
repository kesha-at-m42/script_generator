## s1_0_transition_into_exit_check · beats[0] (dialogue)
**Status:** done
> Delete this transition - it appears at the end of lesson
**Issue:** Transition dialogue appears at end of lesson where it should not exist
**Step:** `section_structurer`  [high]
**Reasoning:** The section_structurer is responsible for creating the initial section structure, including determining where transition sections should appear and what dialogue they contain. This transition section was incorrectly placed at the end of the lesson (before exit check) when it should not exist at this location. The dialogue_rewriter only modifies existing dialogue for voice/style, it does not control section placement or structural decisions.
**Fix:** Remove this transition section entirely from the lesson structure
**Prompt file:** `steps/prompts/section_structurer.py`

**Paste into chat to fix:**
```
Reviewer comment on `s1_0_transition_into_exit_check` (beats[0] (dialogue)):
  "Delete this transition - it appears at the end of lesson"

Issue: Transition dialogue appears at end of lesson where it should not exist
Beat: {"type": "dialogue", "text": "You made bar graphs with scale of 10. You read values at the lines and between the lines. Let's see what you know.", "notion_flag": "suggested", "_notion_block_id": "34f5917e-ac52-8189-a51d-f865005e213d"}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```

## s1_3_create_bar_graph_with_mixed · dialogue beat before prompt
**Status:** IN PROGRESS
> This seems too tied to a specific error that the student might not have made
> Or it needs to be done for all 4 as the guide talks through them
**Issue:** The dialogue references 'Some values are at the lines, some are between' which assumes a specific error pattern the student hasn't made yet, or should be explained for all four values during guided instruction.
**Step:** `section_structurer`  [high]
**Reasoning:** The section_structurer generates initial dialogue beats and is responsible for their content and instructional approach. This dialogue assumes student confusion about gridline alignment before the student has attempted the task, or fails to provide comprehensive guidance for all four data points. The dialogue_rewriter only fixes voice/style issues, not instructional design problems.
**Fix:** Either remove the gridline reference and let remediation handle it if students struggle, or restructure as guided instruction walking through all four values explicitly.
**Prompt file:** `steps/prompts/section_structurer.py`

**Paste into chat to fix:**
```
Reviewer comment on `s1_3_create_bar_graph_with_mixed` (dialogue beat before prompt):
  "This seems too tied to a specific error that the student might not have made"
  "Or it needs to be done for all 4 as the guide talks through them"

Issue: The dialogue references 'Some values are at the lines, some are between' which assumes a specific error pattern the student hasn't made yet, or should be explained for all four values during guided instruction.
Beat: {}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```
