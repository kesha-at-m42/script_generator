## unknown · unknown
**Status:** TBD
> Just realizing you put dialogue only. Do we put these vocab tags in the prompt too? Or they won’t show there (I might have changed some in previous reviews in the prompt…) @Kesha Bagadia
> They don’t show up in prompts, no
> Actually, I lied. We can “bold”.
> So do we leave a vocab tag on them in the prompt to bold it in the prompt? I don’t think I want to switch back to all caps. I think that’s a good emphasis and shouldn’t be tied to vocab.
> Yes, it’s okay to leave vocab tags on them if we want to agree that {} in dialogue is VOCAB treatment (blue highlighted word) and {} in prompts and options is BOLD treatment.
> if we want bold treatment AND vocab treatment in dialogue, we need a new way to tag that.
> tagging @Faina Atamas here, we should have this discussion sometime next week
**Issue:** This is a formatting/tagging convention discussion, not a content quality issue introduced by any AI pipeline step.
**Step:** `none`  [high]
**Reasoning:** The thread discusses whether vocab tags ({}) should appear in prompts and how they render differently in dialogue vs prompts. This is a human editorial decision about markup conventions, not an AI-generated content error. No pipeline step is responsible for choosing tagging conventions — they follow whatever markup exists in their input.
**Fix:** This requires a human editorial decision and documentation update, not a pipeline fix.
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

Issue: This is a formatting/tagging convention discussion, not a content quality issue introduced by any AI pipeline step.
Beat: {}

Responsible step: `none` — `steps/prompts/none.py`

Please read `steps/prompts/none.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```

## s2_2_reading_bar_height · General section-level comment about vocabulary formatting
**Status:** TBD
> Another note - generating these removed the all CAPS from the starter pack. This was our vocab sign in the SP. I am comparing them so I am catching those spots (and maybe we are moving to the brackets in SPs anyway?), but just wanted you to know
> We do need to ensure if we are using the brackets in SPs that they are preserved in the scripts (and not replaced by normal text like our all CAPS was replaced by normal text)
> This is hard and would need some iteration since the starter packs are intentionally less structured and deterministically preservable than scripts (it’s easier to preserve intent than EXACT content since it is run through AI). I am 78% sure that with the new starter packs, since they are much more structured, it won’t be a problem.
**Issue:** ALL CAPS vocabulary markers from starter pack were converted to normal text instead of being preserved or converted to bracket notation
**Step:** `starterpack_parser`  [medium]
**Reasoning:** The starterpack_parser is responsible for extracting structured metadata from module starter packs and passing spec content to downstream steps. If ALL CAPS vocabulary markers were present in the starter pack but not preserved in any form in the generated script, this suggests the parser either stripped the formatting or failed to flag vocabulary terms for special handling. However, this could also be a section_structurer issue if it received the vocab markers but chose not to preserve them.
**Fix:** Ensure starterpack_parser preserves vocabulary markers (either ALL CAPS or brackets) and passes them through to section_structurer for inclusion in generated dialogue and prompts
**Prompt file:** `steps/prompts/starterpack_parser.py`

**Paste into chat to fix:**
```
Reviewer comment on `s2_2_reading_bar_height` (General section-level comment about vocabulary formatting):
  "Another note - generating these removed the all CAPS from the starter pack. This was our vocab sign in the SP. I am comparing them so I am catching those spots (and maybe we are moving to the brackets in SPs anyway?), but just wanted you to know"
  "We do need to ensure if we are using the brackets in SPs that they are preserved in the scripts (and not replaced by normal text like our all CAPS was replaced by normal text)"
  "This is hard and would need some iteration since the starter packs are intentionally less structured and deterministically preservable than scripts (it’s easier to preserve intent than EXACT content since it is run through AI). I am 78% sure that with the new starter packs, since they are much more structured, it won’t be a problem."

Issue: ALL CAPS vocabulary markers from starter pack were converted to normal text instead of being preserved or converted to bracket notation
Beat: {}

Responsible step: `starterpack_parser` — `steps/prompts/starterpack_parser.py`

Please read `steps/prompts/starterpack_parser.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```

## s3_4_three_scale_toggle_same_data · Section-level comment about scale toggle interaction
**Status:** For CATs
> I think they will be getting “error” feedback on the graph too - like “these symbols all can’t fit in this graphing space”
> Is there a UX specced out for this?
> There is… Brian made it… do I know if it made it to dev docs or engineering, no clue
> let me investigate
> (she is yet to investigate. @Kesha Bagadia do investigate)
**Issue:** Reviewer is concerned that students may receive error feedback when toggling to scale 1 because 40 symbols cannot fit in the graphing space, and is asking whether UX specs exist for this constraint.
**Step:** `section_structurer`  [high]
**Reasoning:** The comment raises a UX/design question about whether the graph can physically accommodate 40 symbols at scale 1, not a content quality issue with generated dialogue or remediation. The section_structurer is responsible for scene descriptions and the initial specification of how tangibles behave. If the graph cannot display 40 symbols, this is a structural/spec issue that should have been caught during initial beat design, not a tone or remediation problem.
**Fix:** Verify that the picture_graph tangible can display up to 40 symbols at scale 1, or add a scene beat describing graceful overflow handling (scrolling, wrapping, etc.) before the first scale toggle prompt.
**Prompt file:** `steps/prompts/section_structurer.py`

**Paste into chat to fix:**
```
Reviewer comment on `s3_4_three_scale_toggle_same_data` (Section-level comment about scale toggle interaction):
  "I think they will be getting “error” feedback on the graph too - like “these symbols all can’t fit in this graphing space”"
  "Is there a UX specced out for this?"
  "There is… Brian made it… do I know if it made it to dev docs or engineering, no clue"
  "let me investigate"
  "(she is yet to investigate. @Kesha Bagadia do investigate)"

Issue: Reviewer is concerned that students may receive error feedback when toggling to scale 1 because 40 symbols cannot fit in the graphing space, and is asking whether UX specs exist for this constraint.
Beat: {}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```

## s3_7_reading_totals · validator[selected=5] - incorrect-attempt dialogue for student selecting 5 (the axis interval)
**Status:** IN PROCESS
> it focused on something that wasn’t the error listed in the SP (true it does match scale of 5, but not as likely as an error)
**Issue:** The incorrect-attempt feedback addresses selecting the axis interval (5) when the spec indicates a more likely error is a different mistake
**Step:** `remediation_generator`  [high]
**Reasoning:** The remediation_generator creates all incorrect-validator dialogue and determines which distractors to address and how. The reviewer notes that while 5 does match the scale interval, it's not the most likely error according to the starter pack. This is a distractor prioritization decision made during remediation generation.
**Fix:** Review the starter pack to identify the actual common error pattern and either remove the 5 distractor or deprioritize its remediation in favor of more likely mistakes
**Prompt file:** `steps/prompts/remediation_generator.py`

**Paste into chat to fix:**
```
Reviewer comment on `s3_7_reading_totals` (validator[selected=5] - incorrect-attempt dialogue for student selecting 5 (the axis interval)):
  "it focused on something that wasn’t the error listed in the SP (true it does match scale of 5, but not as likely as an error)"

Issue: The incorrect-attempt feedback addresses selecting the axis interval (5) when the spec indicates a more likely error is a different mistake
Beat: {}

Responsible step: `remediation_generator` — `steps/prompts/remediation_generator.py`

Please read `steps/prompts/remediation_generator.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```
