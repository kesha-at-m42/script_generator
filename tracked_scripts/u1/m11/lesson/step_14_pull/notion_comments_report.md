## s2_3_mixed_concrete_dots_bridge · beats[2] (dialogue)
> Pictures? This should probably say arrays since that vocabulary has already been introduced
> @Andrea Caldas
> No… an ice cube tray is not technically an array, so we can’t refer to both as arrays. Here it is about connecting that other things can be in an array formation even if they look different. It doesn’t have to be “pictures” but we need to keep it generic to represent the 2 images/representations. Or just “look at these” and not refer to them by any specific name at all
**Issue:** Dialogue uses 'pictures' to refer to visual representations when 'arrays' would be more pedagogically consistent with previously introduced vocabulary.
**Step:** `section_structurer`  [high]
**Reasoning:** This is a top-level dialogue beat containing the initial lesson content. The word choice ('pictures' vs 'arrays') is a content decision about how to refer to the visual representations, not a tone/voice issue. The section_structurer generates initial dialogue wording and is responsible for pedagogical vocabulary choices. The dialogue_rewriter only fixes voice/style violations, not content-level word choice decisions.
**Fix:** Revise dialogue to use 'arrays' or a generic phrase like 'look at these' instead of 'pictures' to maintain vocabulary consistency.
**Prompt file:** `steps/prompts/section_structurer.py`

**Paste into chat to fix:**
```
Reviewer comment on `s2_3_mixed_concrete_dots_bridge` (beats[2] (dialogue)):
  "Pictures? This should probably say arrays since that vocabulary has already been introduced"
  "@Andrea Caldas"
  "No… an ice cube tray is not technically an array, so we can’t refer to both as arrays. Here it is about connecting that other things can be in an array formation even if they look different. It doesn’t have to be “pictures” but we need to keep it generic to represent the 2 images/representations. Or just “look at these” and not refer to them by any specific name at all"

Issue: Dialogue uses 'pictures' to refer to visual representations when 'arrays' would be more pedagogically consistent with previously introduced vocabulary.
Beat: {"type": "dialogue", "text": "Check out these two pictures. On the left, an ice cube tray. On the right, a dot array. Same number of rows. Same number of columns. Whether you're looking at ice cubes or dots, it's the same array. 2 rows of 6.", "id": "s2_3_mixed_concrete_dots_bridge_b2", "_notion_block_id": "33b5917e-ac52-8147-adb6-f9f867e05461"}

Responsible step: `section_structurer` — `steps/prompts/section_structurer.py`

Please read `steps/prompts/section_structurer.py` and identify the specific rule or instruction that should have prevented this. Then suggest a targeted fix to that rule.
```
