## s1_1_reading_bar_heights_worked_example · beats[0] (scene)
> This data needs to be updated to reflect the warmup
**Issue:** Scene description references 'Warmup' data but the actual bar values do not match the warmup section data.
**Step:** `section_structurer`  [high]
**Reasoning:** This is the opening scene beat of the section, created by section_structurer when converting the lesson spec into the initial structure. The description claims the data comes from the Warmup, but the reviewer indicates the bar values need updating to actually reflect warmup data. Scene beat content and accuracy is section_structurer's responsibility.
**Fix:** Update bar_values in the scene params to match the actual data from the warmup section.
**Prompt file:** `steps/prompts/section_structurer.py`

**Paste into chat to fix:**
```
Reviewer comment on `s1_1_reading_bar_heights_worked_example` (beats[0] (scene)):
  "This data needs to be updated to reflect the warmup"

Issue: Scene description references 'Warmup' data but the actual bar values do not match the warmup section data.
Beat: {"type": "scene", "method": "add", "tangible_id": "bar_graph_colors", "tangible_type": "bar_graph", "params": {"mode": "reading", "orientation": "vertical", "categories": ["Red", "Blue", "Green", "Yellow"], "axis_range": [0, 60], "axis_interval": 10, "bar_values": {"Red": 40, "Blue": 30, "Green": 50, "Yellow": 20}, "highlight_categories": ["Red"], "description": "Vertical bar graph appears. Favorite Colors data from Warmup. Red=40, Blue=30, Green=50, Yellow=20. Axis labeled 0 to 60 in intervals of 10. All 4 bars pre-filled."}, "id": "s1_1_reading_bar_heights_worked_example_b0", "_notion_block_id": "34f5917e-ac52-8137-8b50-fb04f8205c8a", "notion_flag": "updated"}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```

## s1_4_your_turn_create_bar_guided · beats[3].validator[0] (correct).beats[1] (dialogue)
> I feel like the pipeline overdid it with the repetition of on correct and heavy remediation dialogues - so many are “right” for on correct and “let me show you” for heavy remediation
**Issue:** On-correct dialogue opens with repetitive 'Right' across multiple prompts instead of varying the positive signal
**Step:** `dialogue_rewriter`  [high]
**Reasoning:** This is on-correct feedback dialogue that opens with 'Right.' The dialogue_rewriter is responsible for enforcing voice/style rules on dialogue beats, including the requirement that on_correct beats open with a brief positive signal. While it correctly ensures a positive signal exists, it should vary the opening across multiple prompts to avoid the repetitive pattern the reviewer flagged.
**Fix:** Dialogue_rewriter should vary on-correct opening signals across a section (e.g., 'Right', 'Yes', 'Exactly', 'That's it') to prevent monotonous repetition
**Prompt file:** `steps/prompts/dialogue_rewriter.py`

**Paste into chat to fix:**
```
Reviewer comment on `s1_4_your_turn_create_bar_guided` (beats[3].validator[0] (correct).beats[1] (dialogue)):
  "I feel like the pipeline overdid it with the repetition of on correct and heavy remediation dialogues - so many are “right” for on correct and “let me show you” for heavy remediation"

Issue: On-correct dialogue opens with repetitive 'Right' across multiple prompts instead of varying the positive signal
Beat: {"type": "dialogue", "text": "Right. 10, 20, 30. The bar ends at 30 on the axis. 30 votes for Swings. You completed the scale of 10 bar graph.", "notion_flag": "suggested", "_notion_block_id": "34f5917e-ac52-8134-80e9-cd23533c274b"}

Responsible step: `dialogue_rewriter` — `steps/prompts/dialogue_rewriter.py`

Please read `steps/prompts/dialogue_rewriter.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```

## s2_5_mixed_values_at_lines_between · beats[3].validator[2] (incorrect[2]).beats[1] (dialogue)
> This uses 0 and 5s logic that they haven’t learned yet
> I adjusted and accepted suggestions, just another instance for you to be aware of (they are going to find those patterns in a later module). I left parts of them throughout the script, but didn’t fully rely on “ends in 0s” and “ends in 5s” logic
**Issue:** The remediation dialogue teaches a pattern (values ending in 0 are at lines, values ending in 5 are halfway between) that students have not yet learned in the curriculum.
**Step:** `remediation_generator`  [high]
**Reasoning:** This is an incorrect-validator dialogue beat (second attempt remediation). The remediation_generator is responsible for all content inside validator[is_correct=false] states. It introduced instructional content that assumes prior knowledge students don't have, violating the curriculum sequence by teaching the 0s/5s pattern prematurely.
**Fix:** Regenerate the remediation to guide students using skip counting and visual positioning without relying on the ends-in-0/ends-in-5 pattern.
**Prompt file:** `steps/prompts/remediation_generator.py`

**Paste into chat to fix:**
```
Reviewer comment on `s2_5_mixed_values_at_lines_between` (beats[3].validator[2] (incorrect[2]).beats[1] (dialogue)):
  "This uses 0 and 5s logic that they haven’t learned yet"
  "I adjusted and accepted suggestions, just another instance for you to be aware of (they are going to find those patterns in a later module). I left parts of them throughout the script, but didn’t fully rely on “ends in 0s” and “ends in 5s” logic"

Issue: The remediation dialogue teaches a pattern (values ending in 0 are at lines, values ending in 5 are halfway between) that students have not yet learned in the curriculum.
Beat: {"type": "dialogue", "text": "Let's break this down. Count by 10s to find the days that stop at the axis lines. Monday is 40 and Wednesday is 50 so those stop at the exact lines. The others are Tuesday at 35 and Thursday at 25. Those end in 5, so they're halfway between axis lines. Set each bar where it belongs.", "notion_flag": "suggested", "_notion_block_id": "34f5917e-ac52-81b3-b720-d6e0358d7c50"}

Responsible step: `remediation_generator` — `steps/prompts/remediation_generator.py`

Please read `steps/prompts/remediation_generator.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```
