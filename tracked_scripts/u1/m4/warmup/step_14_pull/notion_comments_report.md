## s1_1_data_collection_game · section heading
> Update all warmup parts once the game is solidified
**Issue:** Reviewer flagged this warmup section for updates pending finalization of the data collection game design.
**Step:** `section_structurer`  [high]
**Reasoning:** The comment indicates the entire warmup section needs revision once the game mechanics are finalized. The section_structurer is responsible for the initial structure, scene descriptions, dialogue content, and factual accuracy of all beats in this transition section. Since the issue affects the whole section's design rather than specific voice/tone or remediation concerns, it falls to the step that created the initial content.
**Fix:** Regenerate the entire section after the data collection game specifications are finalized to ensure alignment with final game mechanics and values.
**Prompt file:** `steps/prompts/section_structurer.py`

**Paste into chat to fix:**
```
Reviewer comment on `s1_1_data_collection_game` (section heading):
  "Update all warmup parts once the game is solidified"

Issue: Reviewer flagged this warmup section for updates pending finalization of the data collection game design.
Beat: {}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```

## s1_1_data_collection_game · beats[2] (scene)
> Depending on amount of time required to count all of these items, consider reducing to 3 categories (values likes 60, 20, 50)
**Issue:** The data collection game uses four categories with values that may take too long to count; reviewer suggests reducing to three categories with simpler values like 60, 20, 50.
**Step:** `section_structurer`  [high]
**Reasoning:** The section_structurer is responsible for the initial scene descriptions and the specific values used in tangibles. This beat defines the categories (Red, Blue, Green, Yellow Minis) and their target values (20, 40, 30, 50). The reviewer's concern is about the pedagogical design choice of using four categories rather than three, which is a structural decision made during initial section generation, not a tone/voice issue that dialogue_rewriter would handle or a remediation issue.
**Fix:** Modify the section_structurer prompt or spec to use three categories with values 60, 20, 50 instead of four categories with values 20, 40, 30, 50.
**Prompt file:** `steps/prompts/section_structurer.py`
**Input prompt for this section:** `tracked_scripts\u1\m4\warmup\step_05_section_structurer\prompts\s1_1_data_collection_game.md`

**Paste into chat to fix:**
```
Reviewer comment on `s1_1_data_collection_game` (beats[2] (scene)):
  "Depending on amount of time required to count all of these items, consider reducing to 3 categories (values likes 60, 20, 50)"

Issue: The data collection game uses four categories with values that may take too long to count; reviewer suggests reducing to three categories with simpler values like 60, 20, 50.
Beat: {"type": "scene", "method": "animate", "tangible_id": "data_collection_game_minis", "params": {"event": "count_items", "status": "confirmed", "description": "Student counts items across categories. Results: Red Minis 20, Blue Minis 40, Green Minis 30, Yellow Minis 50. Values display as multiples of 10 with clear differences."}, "id": "s1_1_data_collection_game_b2", "_notion_block_id": "3485917e-ac52-8131-9760-c67a136a67c6"}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`
Input prompt used: `tracked_scripts\u1\m4\warmup\step_05_section_structurer\prompts\s1_1_data_collection_game.md`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```

## s4_1_bridge_lesson · beats[0] (scene)
> This will be the same data from above and not a new data set
**Issue:** The bar graph uses the same Favorite Colors dataset that was shown in the previous section, not a new dataset as the lesson structure requires.
**Step:** `section_structurer`  [high]
**Reasoning:** The section_structurer is responsible for creating scene beats and ensuring they match the lesson spec requirements. This is a bridge/transition section that should introduce new data for the upcoming lesson, but instead reuses the previous section's Favorite Colors data. This is a structural content error in the initial scene generation, not a tone or dialogue issue.
**Fix:** The section_structurer should generate a scene beat with a different dataset appropriate for the bridge lesson context.
**Prompt file:** `steps/prompts/section_structurer.py`
**Input prompt for this section:** `tracked_scripts\u1\m4\warmup\step_05_section_structurer\prompts\s4_1_bridge_lesson.md`

**Paste into chat to fix:**
```
Reviewer comment on `s4_1_bridge_lesson` (beats[0] (scene)):
  "This will be the same data from above and not a new data set"

Issue: The bar graph uses the same Favorite Colors dataset that was shown in the previous section, not a new dataset as the lesson structure requires.
Beat: {"type": "scene", "method": "add", "tangible_id": "bar_graph_colors", "tangible_type": "bar_graph", "params": {"mode": "reading", "orientation": "vertical", "categories": ["Red", "Blue", "Yellow", "Green"], "axis_range": [0, 60], "scale": 10, "description": "Vertical bar graph appears. Favorite Colors data with scale of 10. Red=30, Blue=50, Yellow=60, Green=40."}, "id": "s4_1_bridge_lesson_b0", "_notion_block_id": "3485917e-ac52-81db-9d0c-ce54804a306c"}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`
Input prompt used: `tracked_scripts\u1\m4\warmup\step_05_section_structurer\prompts\s4_1_bridge_lesson.md`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```
