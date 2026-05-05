## unknown · unknown
> Just realizing you put dialogue only. Do we put these vocab tags in the prompt too? Or they won’t show there (I might have changed some in previous reviews in the prompt…) @Kesha Bagadia
> They don’t show up in prompts, no
> Actually, I lied. We can “bold”.
> So do we leave a vocab tag on them in the prompt to bold it in the prompt? I don’t think I want to switch back to all caps. I think that’s a good emphasis and shouldn’t be tied to vocab.
> Yes, it’s okay to leave vocab tags on them if we want to agree that {} in dialogue is VOCAB treatment (blue highlighted word) and {} in prompts and options is BOLD treatment.
> if we want bold treatment AND vocab treatment in dialogue, we need a new way to tag that.
> tagging @Faina Atamas here, we should have this discussion sometime next week
**Issue:** Discussion about vocab tag formatting conventions in prompts vs dialogue, not a content quality issue
**Step:** `none`  [high]
**Reasoning:** This thread is a design discussion between reviewers about formatting conventions for vocab tags ({}) in different beat types (dialogue vs prompts). No beat content is provided, no AI-generated content is being critiqued, and no pipeline step is responsible. This is a product/formatting specification question, not a content generation issue.
**Fix:** No pipeline fix needed — this is a formatting specification discussion to be resolved by the product team
**Prompt file:** `steps/prompts/none.py`

**Paste into chat to fix:**
```
Reviewer comment on `unknown` (unknown):
  "Just realizing you put dialogue only. Do we put these vocab tags in the prompt too? Or they won’t show there (I might have changed some in previous reviews in the prompt…) @Kesha Bagadia"
  "They don’t show up in prompts, no"
  "Actually, I lied. We can “bold”."
  "So do we leave a vocab tag on them in the prompt to bold it in the prompt? I don’t think I want to switch back to all caps. I think that’s a good emphasis and shouldn’t be tied to vocab."
  "Yes, it’s okay to leave vocab tags on them if we want to agree that {} in dialogue is VOCAB treatment (blue highlighted word) and {} in prompts and options is BOLD treatment."
  "if we want bold treatment AND vocab treatment in dialogue, we need a new way to tag that."
  "tagging @Faina Atamas here, we should have this discussion sometime next week"

Issue: Discussion about vocab tag formatting conventions in prompts vs dialogue, not a content quality issue
Beat: {}

Responsible step: `none` — `steps/prompts/none.py`

Please read `steps/prompts/none.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```

## s2_2_reading_bar_height · beats[4] (dialogue)
> Another note - generating these removed the all CAPS from the starter pack. This was our vocab sign in the SP. I am comparing them so I am catching those spots (and maybe we are moving to the brackets in SPs anyway?), but just wanted you to know
> We do need to ensure if we are using the brackets in SPs that they are preserved in the scripts (and not replaced by normal text like our all CAPS was replaced by normal text)
> This is hard and would need some iteration since the starter packs are intentionally less structured and deterministically preservable than scripts (it’s easier to preserve intent than EXACT content since it is run through AI). I am 78% sure that with the new starter packs, since they are much more structured, it won’t be a problem.
**Issue:** All-caps vocabulary markers (HEIGHT, ENDS) from the starter pack were converted to lowercase with bracket formatting ({height}) during generation.
**Step:** `section_structurer`  [high]
**Reasoning:** The pipeline history shows section_structurer produced the beat with all-caps 'HEIGHT' and 'ENDS', which were then converted to lowercase with brackets in later formatting steps. Section_structurer is responsible for interpreting the starter pack content and establishing the initial vocabulary treatment. The conversion from all-caps to brackets represents a systematic formatting decision made during initial structure generation, not a rewriting issue.
**Fix:** Update section_structurer to preserve bracket-formatted vocabulary markers from starter packs instead of converting all-caps to brackets.
**Prompt file:** `steps/prompts/section_structurer.py`
**Input prompt for this section:** `tracked_scripts\u1\m3\lesson\step_05_section_structurer\prompts\s2_2_reading_bar_height.md`

**Paste into chat to fix:**
```
Reviewer comment on `s2_2_reading_bar_height` (beats[4] (dialogue)):
  "Another note - generating these removed the all CAPS from the starter pack. This was our vocab sign in the SP. I am comparing them so I am catching those spots (and maybe we are moving to the brackets in SPs anyway?), but just wanted you to know"
  "We do need to ensure if we are using the brackets in SPs that they are preserved in the scripts (and not replaced by normal text like our all CAPS was replaced by normal text)"
  "This is hard and would need some iteration since the starter packs are intentionally less structured and deterministically preservable than scripts (it’s easier to preserve intent than EXACT content since it is run through AI). I am 78% sure that with the new starter packs, since they are much more structured, it won’t be a problem."

Issue: All-caps vocabulary markers (HEIGHT, ENDS) from the starter pack were converted to lowercase with bracket formatting ({height}) during generation.
Beat: {"type": "dialogue", "text": "In a bar graph, you read the {height}, where the bar ENDS on the axis. Look at Slides. What's the {height} of the Slides bar? Where does it end?", "id": "s2_2_reading_bar_height_b4", "_notion_block_id": "3485917e-ac52-8135-ab14-d5dfa0ea4853"}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`
Input prompt used: `tracked_scripts\u1\m3\lesson\step_05_section_structurer\prompts\s2_2_reading_bar_height.md`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```

## s3_4_three_scale_toggle_same_data · beats[3].validator[0] (correct).beats[0] (scene)
> I think they will be getting “error” feedback on the graph too - like “these symbols all can’t fit in this graphing space”
> Is there a UX specced out for this?
> There is… Brian made it… do I know if it made it to dev docs or engineering, no clue
> let me investigate
> (she is yet to investigate. @Kesha Bagadia do investigate)
**Issue:** The reviewer is concerned that students may receive UX error feedback when toggling to scale of 1 because 40 symbols cannot fit in the graphing space.
**Step:** `section_structurer`  [high]
**Reasoning:** The scene beat describes the graph transformation when toggling to scale of 1, showing Olivia going from 8 to 40 symbols. The section_structurer is responsible for scene descriptions and ensuring they match the lesson spec and are physically feasible. This is a design/feasibility issue about whether the described transformation can actually be rendered in the UI, not a content quality or tone issue.
**Fix:** Verify with UX/engineering whether 40 symbols can fit in the graph space, and if not, adjust the scene description or data values to stay within renderable limits.
**Prompt file:** `steps/prompts/section_structurer.py`
**Input prompt for this section:** `tracked_scripts\u1\m3\lesson\step_05_section_structurer\prompts\s3_4_three_scale_toggle_same_data.md`

**Paste into chat to fix:**
```
Reviewer comment on `s3_4_three_scale_toggle_same_data` (beats[3].validator[0] (correct).beats[0] (scene)):
  "I think they will be getting “error” feedback on the graph too - like “these symbols all can’t fit in this graphing space”"
  "Is there a UX specced out for this?"
  "There is… Brian made it… do I know if it made it to dev docs or engineering, no clue"
  "let me investigate"
  "(she is yet to investigate. @Kesha Bagadia do investigate)"

Issue: The reviewer is concerned that students may receive UX error feedback when toggling to scale of 1 because 40 symbols cannot fit in the graphing space.
Beat: {"type": "scene", "method": "animate", "tangible_id": "picture_graph_books", "params": {"event": "scale_toggle_transform", "status": "confirmed", "description": "Graph animates: symbols multiply. Olivia goes from 8 symbols to 40, Liam from 7 to 35, Noah from 5 to 25, Emma from 4 to 20. Key updates to Each symbol = 1."}, "id": "s3_4_three_scale_toggle_same_data_b3_v0_b0", "notion_flag": "updated", "_notion_block_id": "34c5917e-ac52-8113-9c67-e3997927d630"}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`
Input prompt used: `tracked_scripts\u1\m3\lesson\step_05_section_structurer\prompts\s3_4_three_scale_toggle_same_data.md`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```
