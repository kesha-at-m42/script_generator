# M1 Practice Templates — v1.1 Reconciliation Edits

**Date:** 2026-04-15 (updated 2026-04-16)
**Purpose:** Specific edits to apply to the existing v1 M1 Practice Templates in Notion. Brings spine-anchored improvements from v1.1 into the teacher-reviewed v1 without replacing it.

> **⚠️ Global Skill ID Update (2026-04-16):** After this doc was written, the skill ID system was redesigned to use global descriptive names instead of unit-scoped numbers. All references below use the original format (`S1`–`S5`, `U1.SK1`–`U1.SK6`, `SK6:ordinal`, etc.). The Notion page and Skill Spine database have been updated to the new format:
> - `S1` / `U1.SK1` → `ReadPicGraph`
> - `S2` / `U1.SK2` → `ReadBarGraph`
> - `S3`–`S5` / `U1.SK6` → `CompareData` (with sub-skills `CompareData:ordinal`, `CompareData:difference`, `CompareData:combination`)
> - `spine_skill_id` field removed; `skill_id` now holds the global name directly
> - The Notion Skill Spine database "Spine ID" property uses these global names

**Changes:**
- A. Three new templates (0113, 0114, 0115)
- B. Spine metadata fields on all existing templates
- C. Track classification table (add to backbone)
- D. Updated §PT.4 Summary table
- E. Updated §PT.5 Coverage Validation

---

## A. NEW TEMPLATES

Insert these after Template 0112 (before the Misconception Remediation Templates section).

---

### Template 0113 — In All / Total — Picture Graph (Confidence)

**🟢 SKILL:** S5 — Solve "in all / total" combination problems
**Spine:** U1.SK6 → sub-skill SK6:combination

**🔵 PROBLEM TYPE:** Given a picture graph with 3 categories and Data Table visible, student finds the total of two named categories.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **tight** — "in all / combined" needs categories where combining quantities makes sense (counts of the same unit).

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite fruits | apples, bananas, grapes | Combining "fruit votes" is natural |
| Stickers earned | stars, hearts, smiley faces | Countable rewards; simple |
| Books read this week | Maya, Leo, Priya | Name-based; combining "books read" is natural |
| Playground animals spotted | birds, squirrels, butterflies | Nature/outdoor; combining sightings |
| Art supplies used | crayons, markers, colored pencils | Classroom creative theme |

**🟠 PROMPT EXAMPLES:**
1. "How many students chose apples and grapes in all?"
2. "How many stickers did Maya and Leo earn combined?"
3. "How many birds and squirrels were spotted total?"
4. "How many votes did crayons and markers get in all?"
5. "How many people picked bananas and grapes combined?"

**🟣 SUCCESS DIALOGUE:**
1. "9 in all. Apples had 5, grapes had 4. You added them."
2. "Right — 7 combined."
3. "11 total. You found the sum."
4. "Correct. 8 in all."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold Type | Tier | Trigger | Reference |
|---|---|---|---|
| Data Table visible | confidence | Always present at confidence tier | SP §1.5.3 |
| Two-category highlight | confidence | Question loads — system highlights the two named categories | Lesson 3.3 |
| Key emphasis pulse | confidence | Graph loads — key briefly pulses | SP §1.5.1 |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| difference_of_pair | Subtracts the two values instead of adding | #6 (inverse) | "'In all' means COMBINE — add them together. [A] has [X], [B] has [Y]. [X] plus [Y] = the total." |
| all_categories | Sums all 3 categories shown, not just the two named | #17 | "The question names only [A] and [B]. Don't add [C]. Just these two." |
| single_value | Selects one value without combining | Key Beat: Two-value combination (3.3) | "You found one group. But 'in all' means you must add the two amounts together." |
| off_by_one | Computes sum but off by 1 | Key Beat: Addition accuracy (3.3) | "Recount. [A] has [X], [B] has [Y]. [X] plus [Y] equals exactly [answer]." |

**🟤 REMEDIATION DESIGN:**

Track: MC — confidence tier `[Pedagogical_Override]` per RDR §11 confidence builder exception; overrides §3 MC no-Light rule.
Light only: "Count the symbols for [A] and [B]. Add those two numbers together." No Medium/Heavy — confidence tier.
Validator: —

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0113 |
| template_type | standard |
| skill_id | S5 |
| spine_skill_id | U1.SK6 |
| sub_skill | SK6:combination |
| skill | Solve "in all / total" combination problems (add) |
| problem_type | "How many A and B in all?" from a picture graph |
| workspace_description | Picture Graph (Mode 1: Reading). Horizontal orientation. 3 categories. Key: "Each [symbol] = 1 [item]." Values per category: 3–6. Data Table visible. Two categories highlighted by prompt. MC distractors: correct sum, difference of two values (#6 inverse), sum of ALL categories (#17), one individual value. |
| action_description | Multiple choice (4 options) |
| mastery_tier | confidence |
| mastery_verb | apply |
| parameter_coverage | Values: 3, 4, 5, 6. Categories: 3. Orientation: horizontal only. Graph type: picture graph. Data Table: visible. |
| correct_end_state | Student selects the correct sum of the two named categories. |
| key_teaching_moment | Lesson 3.3: "'In all' means COMBINE — add the amounts together." System highlights both rows. Guide: "[A] has [X] symbols, [B] has [Y] symbols. Add them." |
| remediation_track | MC — confidence `[Pedagogical_Override]` per RDR §11; overrides §3 no-Light rule |
| validator_tag | — |
| problem_count | 4 |

---

### Template 0114 — Inferential Combination: "How many did NOT choose X?" (Stretch)

**🟢 SKILL:** S5 — Solve "in all / total" combination problems
**Spine:** U1.SK6 → sub-skill SK6:combination

**🔵 PROBLEM TYPE:** Given a graph with 3–4 categories, student answers a question like "How many students did NOT choose [category]?" Student must infer which categories to combine (all except the named one), then add them. The question never explicitly names the categories to add — the student reasons about which ones to include.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **tight** — the "not X" phrasing must make contextual sense. Works best with surveys/votes where "not choosing X" is a natural question. The excluded category should be one with a middling value (not the obvious most or least) so the answer isn't trivially the "total minus the biggest."

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite fruits | apples, bananas, grapes, oranges | "How many did NOT pick apples?" — natural survey question |
| Votes for class pet | fish, hamster, bird, turtle | "How many students did NOT vote for hamster?" |
| Favorite colors | red, blue, green, yellow | "How many did NOT choose blue?" — universal |
| After-school activities | reading, sports, drawing, music | "How many students are NOT in sports?" |
| Lunch choices | pizza, salad, sandwich, soup | "How many did NOT pick pizza?" — cafeteria familiar |

**🟠 PROMPT EXAMPLES:**
1. "How many students did NOT choose apples?"
2. "How many votes were NOT for hamster?"
3. "How many students did NOT pick blue?"
4. "How many people are NOT in sports?"
5. "How many students did NOT choose pizza?"

**🟣 SUCCESS DIALOGUE:**
1. "15 students did not choose apples. You added bananas, grapes, and oranges — everyone except apples."
2. "Right — 12 votes were not for hamster. You combined the other three."
3. "18 did not pick blue. You figured out which ones to add."
4. "Correct — 11 are not in sports."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold Type | Tier | Trigger | Reference |
|---|---|---|---|
| (none at stretch tier) | — | — | — |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| total_all | Sums ALL categories including the excluded one | #17 | "Careful — the question says NOT [X]. That means don't count [X]'s votes. Add only the others." |
| excluded_value_only | Selects the value of the excluded category (reads "NOT X" as "X") | Key Beat: Question reading (3.4a) | "That's how many DID choose [X]. The question asks how many did NOT. You need the other categories." |
| total_minus_wrong | Subtracts the excluded category from one other category instead of from total | Key Beat: Multi-value combination (3.3) | "You subtracted from just one group. 'Not [X]' means ALL the other groups combined." |
| off_by_one | Correct categories, correct operation, off by 1 | Key Beat: Addition accuracy (3.3) | "You found the right groups. Recount: [A] + [B] + [C] = [answer]." |
| includes_excluded | Adds most categories correctly but accidentally includes the excluded one too | #17 variant | "Check — did you include [X]? The question says NOT [X], so leave that one out." |

**🟤 REMEDIATION DESIGN:**

**RDR §3 (MC Track):**

- **Medium per-distractor (see table above)**
- **Heavy [Modeling]:** "The question says 'NOT [X].' That means I need everyone EXCEPT [X]. Let me find the other categories: [A] has [val], [B] has [val], [C] has [val]. I add those: [val] + [val] + [val] = [total]. I did NOT count [X] — that's the one to leave out."
- **Post-Modeling (RDR §7):** "When you see 'not,' figure out which groups to leave out, then add the rest."
- **Validator tags:** [Validator: Misconception_#17]

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0114 |
| template_type | standard |
| skill_id | S5 |
| spine_skill_id | U1.SK6 |
| sub_skill | SK6:combination |
| skill | Solve inferential combination problems — "how many did NOT choose X?" |
| problem_type | "How many did NOT choose [category]?" from a graph with 3–4 categories |
| workspace_description | Bar Graph (Mode 1: Reading). Mixed orientation. 3–4 categories. Axis 0–10 by 1s. Values: 3–8 per category. The excluded category has a middling value (not the max or min) to prevent students from shortcutting via "total minus the biggest." Data Table NOT visible. MC distractors: correct sum of non-excluded categories, total of ALL categories (#17), value of excluded category, total minus wrong category, off-by-one. |
| action_description | Multiple choice (4 options) |
| mastery_tier | stretch |
| mastery_verb | apply |
| parameter_coverage | Values: 3, 4, 5, 6, 7, 8. Categories: 3–4. Orientation: mixed. Graph type: bar graph. Data Table: hidden. |
| correct_end_state | Student selects the correct sum of all categories EXCEPT the named one. |
| key_teaching_moment | Extends Lesson 3.3 ("in all" = add) + Lesson 3.4a (selective data use) to inferential contexts. Student must determine WHICH categories to combine rather than being told. The "not" framing inverts the selective data use skill — instead of "use only these two," it's "use all EXCEPT this one." |
| remediation_track | MC (per RDR §3) |
| validator_tag | [Validator: Misconception_#17] |
| problem_count | 4 |

---

### Template 0115 — Greatest Difference Pair (Challenge)

**🟢 SKILL:** S4 (primary) + S1 or S2 (secondary) — Identify the category pair with the greatest difference, then compute it.
**Spine:** U1.SK6 → sub-skill SK6:difference (primary), SK1 or SK2 (reading step)

**🔵 PROBLEM TYPE:** Given a graph with 4–5 categories, student first identifies which two categories have the greatest difference (Part A), then computes the difference (Part B). Two sequential submissions.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **tight** — needs enough categories that the "greatest difference" is not visually obvious. Values should be arranged so at least two plausible pairs compete for greatest difference.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Books read by students | Ava, Dan, Kenji, Mia, Leo | 5 names; diverse |
| Votes for class pet | fish, hamster, turtle, bird, rabbit | 5 animals; school-themed |
| Favorite sports | soccer, basketball, swimming, running, tennis | 5 sports; universal |
| Trees counted in park | oak, maple, pine, birch, elm | Nature/science; 5 types |
| Snack votes | pretzels, crackers, fruit, cheese, yogurt | 5 snack options; school-lunch familiar |

**🟠 PROMPT EXAMPLES:**
1. "Part A: Which TWO categories have the BIGGEST difference? Click on both."
2. "Part B: What IS the difference between those two categories?"

**🟣 SUCCESS DIALOGUE:**
1. "Part A: Right — Leo and Dan have the biggest gap."
2. "Part B: The difference is 5. Leo read 8, Dan read 3."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold Type | Tier | Trigger | Reference |
|---|---|---|---|
| Part A answer locks before Part B | challenge | After Part A submission, selected pair highlights and stays visible | Sequential submission design |
| (no other scaffolds at challenge tier) | — | — | — |

**🔴 DISTRACTOR TYPES:**

**Part A (click-to-select two categories):**

N/A — Click-to-select interaction. Error patterns:
- Selects the two highest values (not necessarily the greatest difference) — Key Beat: Difference vs magnitude confusion
- Selects the pair that *looks* most different (e.g., tallest and shortest bars) but where axis reading reveals closer values — #16 adjacent
- Selects adjacent categories (position-based, not value-based) — Key Beat: Reading data not position

**Part B (MC for the difference):**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| sum_of_pair | Adds the two selected values instead of subtracting | #6 | "You found the right pair. Now COMPARE them — that means subtract, not add." |
| difference_of_wrong_pair | Computes the difference of a different pair | Key Beat: Multi-pair comparison (2.3–2.4) | "Make sure you're using the values for the two categories you picked." |
| second_largest_difference | Computes the difference of the second-best pair | Key Beat: Full comparison (2.3–2.4) | "Close — but there's a pair with an even bigger gap. Check all the values." |
| off_by_one | Correct pair, correct operation, off by 1 | Key Beat: Subtraction accuracy (3.1–3.2) | "Almost. Recount carefully: [X] minus [Y] equals exactly [answer]." |

**🟤 REMEDIATION DESIGN:**

**Per-Step Escalation (same pattern as 0111):**

RDR §1.2 escalation applies independently to each part:
- **Part A** (identify pair): Non-MC track (click-to-select). Light: "Which two bars are the farthest apart on the scale?" Medium: "Read each bar's value. The biggest difference is between the bar with the MOST and the bar with the LEAST." Visual: values appear next to each bar. Heavy [Modeling]: "I'll read each value. [A]=3, [B]=7, [C]=5, [D]=4, [E]=8. The biggest and smallest are 8 and 3. That's [E] and [A] — difference of 5."
- **Part B** (compute difference): MC track. Medium per-distractor — see table above. Heavy [Modeling]: "I selected [E] with [X] and [A] with [Y]. To find the difference: [X] minus [Y] = [difference]."
- **Post-Modeling (RDR §7):** "That's how you find the greatest difference — read every value, find the pair that's farthest apart, then subtract."
- **Maximum remediation interactions per problem:** 6 (3 per part).
- **Validator tags:** [Validator: Misconception_#6]

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0115 |
| template_type | standard |
| skill_id | S4 |
| secondary_skill | S1 or S2 |
| spine_skill_id | U1.SK6 |
| sub_skill | SK6:difference |
| skill | Identify the category pair with the greatest difference, then compute it |
| problem_type | Two-part: Part A = select pair with greatest difference; Part B = compute the difference |
| workspace_description | Bar Graph (Mode 1: Reading). Vertical orientation. 4–5 categories. Axis 0–10 by 1s. Values chosen so two plausible "greatest difference" pairs compete (e.g., values 3, 4, 5, 7, 8 — the greatest difference pair is 3 and 8, but 4 and 8 or 3 and 7 are close seconds). Data Table NOT visible. Part A: click-to-select two categories. Part B: MC for the difference. |
| action_description | Two sequential submissions: click-to-select pair, then MC |
| mastery_tier | challenge |
| mastery_verb | compare |
| parameter_coverage | Values: 3, 4, 5, 6, 7, 8, 9, 10. Categories: 4–5. Orientation: vertical. Graph type: bar graph. |
| correct_end_state | Student correctly identifies the pair with the greatest difference AND computes the difference. |
| key_teaching_moment | Builds on Lesson 2.3–2.4 (comparing all bars) + Lesson 3.1–3.2 (compute difference). Extends taught skills to a novel task: systematic comparison across all pairs, not just a named pair. |
| remediation_track | Mixed: Part A = Non-MC (per RDR §2), Part B = MC (per RDR §3) |
| validator_tag | [Validator: Misconception_#6] |
| problem_count | 2 |

---

## B. SPINE METADATA — Add to All Existing Templates

Add these two fields to the Technical Details table of every existing template. Insert them after `skill_id` and before `skill`.

| Template | spine_skill_id | sub_skill |
|----------|---------------|-----------|
| 0101 | U1.SK1 | — |
| 0102 | U1.SK1 | — |
| 0103 | U1.SK2 | — |
| 0104 | U1.SK2 | — |
| 0105 | U1.SK6 | SK6:ordinal |
| 0106 | U1.SK6 | SK6:ordinal |
| 0107 | U1.SK6 | SK6:difference |
| 0108 | U1.SK6 | SK6:difference |
| 0109 | U1.SK6 | SK6:difference |
| 0110 | U1.SK6 | SK6:combination |
| 0111 | U1.SK6 | SK6:difference (primary) / SK6:combination (secondary) |
| 0112 | U1.SK1 + U1.SK2 | — |
| 0120 | U1.SK2 | — |
| 0121 | U1.SK6 | SK6:difference |
| 0122 | U1.SK6 | SK6:difference |

Also add a **Spine** line to the header block of each template, directly after the 🟢 SKILL line. Format:

```
**Spine:** U1.SK1
```
or for sub-skills:
```
**Spine:** U1.SK6 → sub-skill SK6:ordinal
```

---

## C. TRACK CLASSIFICATION TABLE — Add to Backbone (§PT.2)

Insert after the Distribution Targets section in the backbone. This makes the MC vs Non-MC decision explicit before template generation.

### Track Classification

*Every interaction pattern in M1's practice templates classified per RDR §2–3.*

| Interaction Pattern | Track | Rationale |
|---|---|---|
| Read a value from a graph → MC (4 options) | MC (RDR §3) | Per-distractor branching enables targeted misconception detection. Each wrong answer reveals a specific error type. |
| Find most/least → click-to-select category | Non-MC (RDR §2) | Student clicks a category, not a number. System detects *that* it's wrong but not *how* — generic L-M-H escalation. |
| How many more/fewer → MC (4 options) | MC (RDR §3) | Sum-instead-of-difference (#6) is the primary distractor. Per-distractor Medium is essential for distinguishing #6 from other errors. |
| In all / total → MC (4 options) | MC (RDR §3) | Difference-instead-of-sum (#6 inverse) and all-categories (#17) are distinct error types needing per-distractor responses. |
| Two-step: combine then compare → 2× sequential MC | MC (RDR §3) | Each step has its own distractor pool. Per-step escalation per RDR §1.2. |
| Cross-graph-type → MC (4 options) | MC (RDR §3) | Wrong-graph and swapped-category errors are distinct distractor types. |
| Greatest difference pair → click-to-select + MC | Mixed: Part A = Non-MC (RDR §2), Part B = MC (RDR §3) | Part A is a selection task; Part B is arithmetic with distractors. |

---

## D. UPDATED §PT.4 — Template Summary

Replace the existing §PT.4 with this version. Changes: +3 templates (0113, 0114, 0115), spine_skill_id column, sub_skill column, track column, updated totals.

### Standard Templates (count toward Pool Total)

| # | ID | Problem Type | Verb | Tier | Skill | Spine | Sub-skill | Track | Misc. Detected | Problems |
|---|------|--------------------------------------|----------|------------|-------|-------|-----------|-------|----------------|----------|
| 1 | 0101 | Read picture graph value | identify | confidence | S1 | SK1 | — | MC | — | 6 |
| 2 | 0102 | Read picture graph value | identify | baseline | S1 | SK1 | — | MC | #16 | 6 |
| 3 | 0103 | Read bar graph value | identify | confidence | S2 | SK2 | — | MC | — | 6 |
| 4 | 0104 | Read bar graph value | identify | baseline | S2 | SK2 | — | MC | #16 | 6 |
| 5 | 0105 | Most/least — picture graph | compare | support | S3 | SK6 | :ordinal | Non-MC | — | 4 |
| 6 | 0106 | Most/least — bar graph | compare | baseline | S3 | SK6 | :ordinal | Non-MC | #16 | 5 |
| 7 | 0107 | How many more/fewer — PG | compare | support | S4 | SK6 | :difference | MC | #6 | 4 |
| 8 | 0108 | How many more/fewer — BG | compare | baseline | S4 | SK6 | :difference | MC | #6, #17 | 7 |
| 9 | 0109 | How many more/fewer — 4-5 cats | compare | stretch | S4 | SK6 | :difference | MC | #6, #17 | 4 |
| 10 | 0110 | In all / total — BG | apply | baseline | S5 | SK6 | :combination | MC | #6 inv., #17 | 5 |
| 11 | 0111 | Two-step: combine then compare | apply | stretch | S4+S5 | SK6 | :diff / :comb | MC (2×) | #6 | 3 |
| 12 | 0112 | Cross-graph-type reading | identify | stretch | S1+S2 | SK1+SK2 | — | MC | — | 2 |
| 13 | 0113 | In all / total — PG | apply | confidence | S5 | SK6 | :combination | MC | — | 4 |
| 14 | 0114 | "Not X" inferential combination | apply | stretch | S5 | SK6 | :combination | MC | #17 | 4 |
| 15 | 0115 | Greatest difference pair | compare | challenge | S4 | SK6 | :difference | Mixed | #6 | 2 |
| | | | | | | | | **STANDARD POOL TOTAL** | | **68** |

### Misconception Remediation Templates (separate sub-pool)

| # | ID | Problem Type | Targets | Tier | Track | Problems |
|---|------|----------------------------------------|---------|------------|-------|----------|
| 1 | 0120 | Read bar value — visual mismatch | #16 | confidence | MC | 3 |
| 2 | 0121 | How many more/fewer — 5 categories | #17 | support | MC | 3 |
| 3 | 0122 | How many more/fewer — sum vs difference | #6 | confidence | MC | 3 |
| | | | | **REMEDIATION SUB-POOL TOTAL** | | **9** |

**Grand Total:** 68 standard + 9 remediation = **77 problems across 18 templates**

---

## E. UPDATED §PT.5 — Coverage Validation

Replace with this version. Key changes: updated tier/skill/verb distributions, +challenge tier, S5 coverage broadened, new templates reflected.

### Tier Distribution (standard templates only)

| Tier | Count | % | Notes |
|------|-------|---|-------|
| confidence | 16 | 24% | S1, S2, S5 entry points. Adequate pool breadth for warm-up draws. |
| support | 8 | 12% | S3, S4 entry points. Algorithm tunes session-level draw rate. |
| baseline | 30 | 44% | Core of the pool. S1, S2, S3, S4, S5 all represented. |
| stretch | 12 | 18% | S4 (multi-cat), S5 (multi-cat), S1+S2 (cross-graph), S4+S5 (two-step). |
| challenge | 2 | 3% | S4 greatest-difference pair. Novel task beyond taught scope. |

### Skill Coverage

| Skill | Spine | Description | Templates | Tiers Covered | Problems | % |
|-------|-------|-------------|-----------|---------------|----------|---|
| S1 | SK1 | Read picture graph value | 0101, 0102, 0112 | conf, base, stretch | 14 | 21% |
| S2 | SK2 | Read bar graph value | 0103, 0104, 0112 | conf, base, stretch | 14 | 21% |
| S3 | SK6:ordinal | Most/least | 0105, 0106 | support, base | 9 | 13% |
| S4 | SK6:difference | How many more/fewer | 0107, 0108, 0109, 0111, 0115 | sup, base, stretch, challenge | 20 | 29% |
| S5 | SK6:combination | In all / total | 0110, 0111, 0113, 0114 | conf, base, stretch | 16 | 24% (was 12% in v1) |

> S4 remains the highest-share skill (29%) per SP §1.8.5's "highest-demand exit skill" note. S5 now has its own tier progression (confidence → baseline → stretch), up from 1 dedicated template in v1.

### Verb Distribution

| Verb | Count | % |
|------|-------|---|
| identify | 28 | 41% |
| compare | 22 | 32% |
| apply | 18 | 26% |

### Misconception Detection Coverage (standard templates)

| ID | Priority | Detected In | Detection Strategy | Status |
|----|----------|-------------|-------------------|--------|
| 16 | PRIMARY | 0102, 0104, 0106 | MC distractor = visually prominent category value | ✅ (3 templates) |
| 17 | SECONDARY | 0108, 0109, 0110, 0114 | MC distractor = total of all categories | ✅ (4 templates — +1 from v1) |
| 6 | ADDRESSED | 0107, 0108, 0109, 0110, 0111, 0113, 0115 | MC distractor = sum instead of difference (S4) or difference instead of sum (S5) | ✅ (7 templates — +2 from v1) |

### Misconception Remediation Coverage (dedicated templates)

| ID | Priority | Remed. Template | Remediation Approach | Status |
|----|----------|-----------------|---------------------|--------|
| 16 | PRIMARY | 0120 | Visual mismatch bars + helping line animation + Data Table verification | ✅ |
| 17 | SECONDARY | 0121 | 5-category graph + category dimming + selective data prompt | ✅ |
| 6 | ADDRESSED | 0122 | Large-gap values where sum is implausibly large + explicit "compare = subtract" | ✅ |

### Action Variety

| Action Type | Templates | Status |
|-------------|-----------|--------|
| Multiple choice | 0101–0104, 0107–0114, 0120–0122 | ✅ |
| Click to select category | 0105, 0106 | ✅ |
| Sequential MC (two-step) | 0111 | ✅ |
| Click-to-select + MC (two-part) | 0115 | ✅ (new) |

### Practice Phase Guidance Compliance

| Requirement | Met? | How |
|-------------|------|-----|
| S4 weighted most heavily | ✅ | S4 has 20 problems (29%) — highest single-skill share |
| Both orientations | ✅ | Horizontal: 0101, 0105, 0107, 0113. Vertical: 0103, 0115. Mixed: 0102, 0104, 0106, 0108–0112, 0114. |
| Both graph types in same problem | ✅ | 0112 (cross-graph-type reading) |
| "How many more/fewer" language | ✅ | 0107, 0108, 0109, 0111, 0115 |
| "In all / total" language | ✅ | 0110, 0113 |
| Inferential "not X" combination | ✅ | 0114 (extends "in all" to inferential contexts) |
| MC interaction type | ✅ | Majority MC. 0105, 0106 click-to-select. 0115 mixed. |
| Data Table visibility scaffolding | ✅ | Visible in confidence/support. Hidden in baseline+. |
| No creation in Practice | ✅ | All templates are reading/interpreting. |
| "All data" distractors | ✅ | 0108, 0109, 0110, 0114 (#17 inverted — "all including excluded"), 0121 |

### Gaps / Flags

- ℹ️ **S3 has no stretch tier.** Most/least only appears at support and baseline. A stretch variant (most/least with 5 categories and close values) would improve coverage breadth. Acceptable for M1; monitor whether S3 stretch is needed based on student data.
- ℹ️ **No support tier for S1/S2.** Graph reading is a review skill — confidence entry is appropriate. If data shows students struggling, a support-tier template with guided key reading could be added.
- ℹ️ **Challenge tier is small (2 problems).** Intentional for M1 review module. 0115 is a novel extension task. If students consistently reach challenge, more can be added.
- ✅ All PRIMARY/HIGH misconceptions have dedicated remediation templates.
- ✅ All ADDRESSED misconceptions have dedicated remediation templates (per design decision 2026-04-15).
- ✅ All MC templates have per-distractor Medium remediation directions.
- ✅ S5 now has full tier progression (confidence → baseline → stretch), resolving v1's single-template coverage gap.

### SP Delta

*Differences between Toy Flow and SP that affected template design:*

- Toy Flow lacked Data Constraints, Toy Requirements, Vocabulary, and Scaffolding tables. SP §1.5 provided all values and configurations used in templates.
- Toy Flow listed misconceptions without priority. SP §1.4 classified #16 as PRIMARY and #17 as SECONDARY, which determined remediation template allocation.
- SP §1.8.5 Distribution Targets (S1 30%, S2 30%, S3 30%, S4 10%) were adjusted: S3 broken out as separate skill, S4 elevated per SP's own "highest-demand" note.
- SP §1.8.5 4-skill decomposition expanded to 5 skills (S3 most/least separated from S1/S2) based on decomposition framework analysis.

### Spine Delta (v1.1 reconciliation, 2026-04-15)

*Changes made to align v1 templates with the Unit 1 Skill Spine:*

- SK6 ("Compare data across graph categories") decomposed into three sub-skills: SK6:ordinal (S3), SK6:difference (S4), SK6:combination (S5). All three map to existing v1 skills — no reclassification needed, only metadata added.
- SK3 ("Create picture graphs") confirmed as TEACHING ONLY — not eligible for practice templates. Three-check: EC tests it? No. Practice subsection references it? No. Independent student action in Lesson? No (warmup only).
- spine_skill_id and sub_skill fields added to all templates for cross-module skill tracking.
- Templates 0113 (S5 confidence), 0114 (S5 stretch), 0115 (S4 challenge) added to broaden tier coverage for S5 and introduce challenge tier.
- Track classification table added to backbone for consistency checking.
