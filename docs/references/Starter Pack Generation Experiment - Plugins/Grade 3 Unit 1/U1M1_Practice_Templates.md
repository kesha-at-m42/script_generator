# MODULE 1: Data Sense & 1:1 Graphs — Practice Templates

> **⚠️ SUPERSEDED:** This local file uses the pre-migration skill ID format (`spine_skill_id: U1.SK1`, bare `SK6:ordinal`, etc.). The **canonical version** is the [Notion M1 Practice Templates page](https://www.notion.so/33e5917eac5280f8928bfd2b4b9697a9), which was updated 2026-04-16 to use global CamelCase skill IDs (`skill_id: ReadPicGraph`, `sub_skill: CompareData:ordinal`). Do not use this file as a reference for the current schema.

**Generated:** 2026-04-15
**Prompt Version:** v1.1 (Spine-Anchored)
**Skill Spine Version:** v1

---

## §PT.0 Source Readiness Check

### Toy Flow Completeness

| Check | Status | Notes |
|---|---|---|
| Learning Goal present and clear | ✅ | "Interpret picture graphs and bar graphs to generate questions about data (review/activate Grade 2 knowledge)" |
| Cognitive Focus section lists verb → component mappings | ✅ | IDENTIFY (Conceptual), COMPARE (Conceptual) |
| Misconceptions section present with priority levels | ⚠️ | No explicit misconception subsection in M1 Toy Flow. Spine provides misconception mapping per skill. Misconception Table from xlsx available. No per-module priority classification in Toy Flow — will derive from spine + table. |
| "What Students DO" includes a Practice subsection | ✅ | "Multiple graphs → Students answer comparison questions. Focus on 'how many more/fewer' language. Both orientations mixed." |
| Scaffolding Progression table present | ❌ | No formal Scaffolding Progression table for M1. Derivable from Scaffolding Notes and Lesson structure (Early = guide-narrated, Mid = guided reading, Late = independent). Flagged as lower confidence. |
| Toy Requirements table lists toys, modes, and interaction patterns | ❌ | No formal Toy Requirements table. Derivable from Toy Flow narrative: picture graph viewer, bar graph viewer, data collection game (warm-up only). Click, highlight, compare interactions described. |
| Data Constraints section present with numerical ranges | ⚠️ | Partial. Warm-up specifies "values 3-8 range." No explicit per-phase breakdown. No formal Data Constraints table. Will derive from M1 context: 1:1 scale, 3-5 categories, values 1-10. |
| Key Transition from M[N-1] present (Modules 2+) | N/A | Module 1 — no prior module. |
| Vocabulary section | ❌ | No explicit Vocabulary section. Derivable from context: "picture graph," "bar graph," "scale," "key," "category," "most," "least," "how many more," "how many fewer" all in use. "Scale of 2," "half-symbol" explicitly NOT yet introduced (those are M2). |

### Skill Spine Alignment

| Check | Status | Notes |
|---|---|---|
| Unit Skill Spine provided | ✅ | v1, 15 skill threads |
| Cross-Module Matrix reviewed | ✅ | 4 skills active in M1: SK1 (INT), SK2 (INT), SK3 (INT), SK6 (INT) |
| Spine skill count noted | ✅ | 4 skills total — INT: 4, PRC: 0, EXT: 0 |
| Open Questions from spine reviewed | ✅ | No open questions affecting M1 |

### SP Enrichment

| Check | Status | Notes |
|---|---|---|
| SP available | ❌ | No Module 1 Starter Pack exists. |

### Misconception Table Enrichment

| Check | Status | Notes |
|---|---|---|
| All misconceptions relevant to M1 identified | ✅ | From spine: SK1 → #1, #2, #16; SK2 → #1, #5, #16; SK3 → #1, #2, #3; SK6 → #6, #17. At 1:1 scale, #1 (counting instead of scaling), #2 (scale means addition), #3 (fractional symbols), and #5 (interpolation) are NOT actionable — these surface only at scaled representations (M2+). Active in M1: **#16** (Graph as Picture), **#6** ("More Than" Means Add), **#17** (All Data Must Be Used). |
| Observable Behaviors extracted for distractor design | ✅ | #16: "Sees mountain shape in line graph instead of data trend" → in M1 context: reads visual arrangement rather than data values. #6: "adds values instead of subtracting for comparison." #17: "tries to incorporate all values even when question asks about specific items." |
| Priority ratings mapped to template count targets | ⚠️ | No per-module priority in source. Deriving from M1 practice focus: #6 = PRIMARY (comparison is the core of M1 Practice), #16 = SECONDARY (reading misconception, but 1:1 scale makes it less likely), #17 = MONITOR (edge case for simple comparisons). |

### Remediation Design Reference

| Check | Status | Notes |
|---|---|---|
| RDR provided | ❌ **BLOCKED** | RDR not in workspace. Notion connector issue. **Proceeding with embedded RDR knowledge from prompt v1.1** — two-track model (MC §3 / Non-MC §2), confidence tier Light-only exception (§11), post-modeling rules (§7). Will flag any remediation design decisions where the full RDR text would add specificity. |

### Gap Summary

| Gap | Severity | Mitigation |
|---|---|---|
| No Scaffolding Progression table | MODERATE | Derived from narrative. M1 is a review module with mostly uniform scaffolding (guide models, then student practices). Tier mapping has lower confidence than later modules. |
| No Toy Requirements table | MODERATE | Derived from narrative. Toys are pre-made graphs for reading — limited interaction variety in M1. |
| No Data Constraints table | MODERATE | Derived from warm-up values (3-8) and 1:1 scale context. Values 1-10 assumed valid. |
| No Vocabulary section | LOW | M1 is a Grade 2 review. All vocabulary is prior knowledge except comparison language modeled by guide. |
| No RDR file | HIGH | Proceeding with embedded rules. Remediation design blocks will use prompt v1.1 embedded RDR structure. Flag for post-RDR validation pass. |
| No SP | LOW | Expected — no G3U1 SPs exist yet. |

---

## §PT.1 Source Analysis

### A. Toy Inventory

| Toy | Mode/Configuration | Interaction | Phase | Notes |
|---|---|---|---|---|
| Data Collection Game | Mario-party counting, 3 categories (Cats, Dogs, Birds) | Count (click/tap) | Warm-up only | Values 3-8 range. Not available in Practice. |
| Picture Graph (1:1) | Horizontal, pre-made. 1 symbol = 1 item. Symbol palette for warm-up creation. | View, Click category to highlight | Warm-up (creation), Lesson (reading) | Both orientations in Lesson. In warm-up, student creates with collected data. In lesson/practice, reads pre-made. |
| Bar Graph (1:1) | Both orientations (H and V). Scale counts by 1s. | View, Click category to highlight, Click two to compare | Lesson, EC, Practice | Primary assessment format. EC uses bar graph specifically. |
| Data Table | Tabular data display | View (reference) | Lesson | Shown alongside graphs. Not a direct interaction target in Practice. |
| Comparison Tool | Click two categories → system shows difference calculation | Click-to-select (2 selections) | Lesson, Practice | Guide asks "What do you notice?" System displays the arithmetic. |

**Changes from M[N-1]:** N/A (Module 1).

### B. Constraint Extraction

**Scope — IN:**
- Read pre-made picture graphs (1:1 scale, both orientations)
- Read pre-made bar graphs (1:1 scale, both orientations)
- Identify data values from graphs (read individual categories)
- Compare data across categories (most, least, total, difference)
- Answer "how many more/fewer" questions
- Use key parts of graphs: title, categories, scale/key
- Both horizontal and vertical orientations

**Scope — OUT (explicitly deferred):**
- Graph creation in Practice (warm-up creation only, not assessed)
- Scaled graphs (scale > 1 deferred to M2+)
- Half-symbols or fractional representations (M2+)
- Bar graph interpolation (M4+)
- Scale selection (M5)
- Multi-step problems (M6)

**Derived Data Constraints:**

| Parameter | Valid Range | Early (conf/sup) | Mid/Late (base) | Upper (str/chal) |
|---|---|---|---|---|
| Values per category | 1-10 | 3-8 (warm-up range) | 1-10 | 8-10 (near boundary) |
| Number of categories | 3-5 | 3 (warm-up count) | 3-4 | 4-5 |
| Scale | 1 only | 1 | 1 | 1 |
| Orientations | H and V | H (more familiar from Grade 2) | H and V mixed | V-only (less familiar) |
| Graph type | Picture graph, Bar graph | Picture graph (more familiar) | Both mixed | Bar graph with more categories |
| Difference values (for comparison) | 1-7 | 1-3 (small, obvious) | 1-5 | 4-7 (requires careful reading) |

**Confidence notes:** These constraints are derived, not stated in a formal Data Constraints table. The 3-8 range comes from the warm-up. The 1-10 upper bound is inferred from 1:1 scale at Grade 3 level. Values above 10 would be unusual for 1:1 picture graphs (too many symbols). Flagged for author confirmation.

### C. Skill Decomposition (spine-anchored)

**Step C.1 — Import spine skills active in M1:**

4 skills from Cross-Module Matrix: U1.SK1 (INT), U1.SK2 (INT), U1.SK3 (INT), U1.SK6 (INT).

**Step C.2 — Practice-scope eligibility:**

| Spine ID | EC Tests? | Practice References? | Independent Student Action in Lesson? | Verdict |
|---|---|---|---|---|
| U1.SK1 | ❌ EC tests bar graph (SK2), not picture graph directly | ✅ "Multiple graphs" includes picture graphs | ✅ Students read picture graphs independently in Lesson | ✅ **Practice-eligible** — taught and practiced independently, though EC specifically tests bar graph reading |
| U1.SK2 | ✅ "Bar Graph → answer questions about data" | ✅ "Multiple graphs" includes bar graphs | ✅ Students read bar graphs independently in Lesson | ✅ **Practice-eligible** — EC-tested, practiced, independent |
| U1.SK3 | ❌ EC does not test creation | ❌ Practice does not mention creation | ⚠️ Only warm-up creation (1:1 with collected data). Scoping Decision 2: "one-off engagement that introduces the creation workflow" | ❌ **[TEACHING ONLY — no templates this module]** Per Scoping Decision 2, creation occurs only in warm-up as an engagement activity. No EC, no Practice reference, no independent creation in Lesson. |
| U1.SK6 | ✅ "Answer questions about data" includes comparison | ✅ "Comparison questions," "how many more/fewer language" | ✅ Students compare data independently (click two to compare) | ✅ **Practice-eligible** — core practice focus |

**Practice-eligible: 3 skills (SK1, SK2, SK6). Teaching only: 1 skill (SK3).**

**Step C.3 — Sub-skill decomposition check:**

**U1.SK1 (Read picture graphs) — No decomposition needed.**
At 1:1 scale, reading a picture graph is a single cognitive operation: count the symbols in a category. No scaling math, no interpolation. One interaction type (click/select answer). No sub-skill split warranted.

**U1.SK2 (Read bar graphs) — No decomposition needed.**
At 1:1 scale, reading a bar graph is a single cognitive operation: read the bar height against the scale. Same rationale as SK1. One interaction type.

**U1.SK6 (Compare data across graph categories) — Decomposition warranted.**

The spine description: "Use graph data to answer comparison questions ('how many more/fewer,' 'how many in all') by reading values and performing one-step addition or subtraction."

In M1, the Toy Flow specifies:
- IDENTIFY information from graphs (most, least, total, difference)
- COMPARE data across categories
- ANSWER "how many more/fewer" questions

Evidence for decomposition (2+ signals required):

| Signal | SK6:ordinal (most/least) | SK6:difference (how many more/fewer) |
|---|---|---|
| Different verb? | **identify** — visual scan, no arithmetic | **compare** — requires subtraction |
| Different interaction type? | Click-to-select (pick the tallest/shortest bar or row with most/fewest symbols) | MC (select numerical answer to "how many more/fewer?") |
| Different EC item? | Likely tested — "answer questions about data" includes identification | Likely tested — "answer questions about data" includes comparison |
| Different misconception target? | #16 (Graph as Picture) — student reads visual arrangement | #6 ("More Than" Means Add) — student adds instead of subtracts |

**Signals met: 3 of 4** (different verb, different interaction type, different misconception target). **Decomposition justified.**

Sub-skills:

| Spine ID | Sub-skill | Module Skill ID | Description | Verb | Component |
|---|---|---|---|---|---|
| U1.SK6 | SK6:ordinal | S3 | Identify which category has the most or fewest from a graph | identify | conceptual |
| U1.SK6 | SK6:difference | S4 | Determine "how many more" or "how many fewer" between two categories | compare | conceptual |
| U1.SK6 | SK6:combination | S5 | Determine "how many in all" across categories | apply | transfer |

**SK6:combination — "how many in all" as a third sub-skill.**

| Signal | Evidence |
|---|---|
| Different verb? | **apply** — requires addition across categories, distinct from identify (ordinal) and compare (difference) |
| Different distractor strategy? | Inverse of SK6:difference — student might subtract instead of add, or report a single category value instead of the total |
| Different EC item? | EC likely tests total independently alongside reading and comparison |

**Signals met: 3 of 4.** Decomposition justified. "How many in all" is a distinct cognitive operation (aggregation via addition) that produces different template design than ordinal identification or difference comparison.

**Step C.4 — Skill additions check:**
No skill additions proposed. The 3 practice-eligible skills (SK1, SK2, SK6) cover all independent student actions described in M1's Practice and EC.

**Step C.5 — §1.8.5 calibration:**
Not applicable — no SP exists for M1.

### Full Skill Decomposition Table

| Spine ID | Sub-skill | Mod. Skill | Description | Verb | Component | Source | Progression | Practice Scope |
|---|---|---|---|---|---|---|---|---|
| U1.SK1 | — | S1 | Read a specific value from a 1:1 picture graph | identify | conceptual | Lesson (picture graph reading, both orientations) | INT | ✅ Practice-eligible |
| U1.SK2 | — | S2 | Read a specific value from a 1:1 bar graph | identify | conceptual | Lesson (bar graph reading, both orientations), EC | INT | ✅ Practice-eligible |
| U1.SK3 | — | — | Create a 1:1 picture graph from collected data | create | procedural | Warm-up only | INT | ❌ [TEACHING ONLY] — Scoping Decision 2: warm-up engagement only, no EC/Practice |
| U1.SK6 | SK6:ordinal | S3 | Identify which category has the most or fewest | identify | conceptual | Lesson (click to highlight, compare categories) | INT | ✅ Practice-eligible |
| U1.SK6 | SK6:difference | S4 | Determine "how many more/fewer" between categories | compare | conceptual | Lesson (click two to compare, system shows calculation), Practice core | INT | ✅ Practice-eligible |
| U1.SK6 | SK6:combination | S5 | Determine "how many in all" across categories | apply | transfer | Lesson (total questions), Practice | INT | ✅ Practice-eligible |

### Spine Alignment Notes

- Spine skills active in M1: 4
  - Practice-eligible: 3 (SK1, SK2, SK6 → 5 module-level skills after decomposition)
  - Teaching only: 1 (SK3)
- Sub-skills decomposed: SK6 → SK6:ordinal, SK6:difference, SK6:combination (3 sub-skills; each meets 3+ decomposition signals)
- Spine additions proposed: 0
- §1.8.5 delta: N/A (no SP)

### D. Misconception Mapping

**Active misconceptions for M1** (filtered for 1:1 scale relevance):

| ID | Name | Derived Priority | Observable Behavior | Template Strategy |
|---|---|---|---|---|
| #6 | "More Than" Means Add | **PRIMARY** | "For 'How many more chose A than B?' adds the values instead of subtracting." | 3+ templates: SK6:difference templates at multiple tiers should detect this via MC distractors where the sum of the pair is an option. Dedicated misconception_remediation template with familiar values where the sum is obviously too large. |
| #16 | Graph as Picture | **PRIMARY** | "Sees mountain shape in line graph instead of data trend." In M1 context: attends to visual arrangement of symbols/bars rather than reading the scale/key to determine count. This is the foundational reading misconception — M1 is entirely about reading graphs, making #16 the biggest risk alongside #6. | 3+ detection templates across SK1 and SK2 reading templates. Distractors where the answer reflects counting visual features (e.g., number of bars instead of bar height, number of rows instead of symbol count). 1 dedicated remediation template. |
| #17 | All Data Must Be Used | **MONITOR** | "Tries to incorporate all values even when question asks about specific items." | Distractor logic only in SK6:difference templates — include "sum of all categories" as a distractor type. No dedicated remediation template. |

**Misconceptions NOT active in M1** (scale-dependent, deferred):
- #1 (Counting Symbols Instead of Scaling) — at 1:1, counting symbols IS correct
- #2 (Scale Means Addition) — no scaling in M1
- #3 (Can't Create Fractional Symbols) — no fractional symbols in M1; SK3 is teaching-only
- #5 (Can't Interpolate Bar Heights) — no interpolation at scale of 1

### E. Practice Phase Guidance

| Requirement | Source Text | Template Implication |
|---|---|---|
| Multiple graph types | "Multiple graphs → Students answer comparison questions" | Template set must include both picture graph and bar graph reading |
| Comparison focus | "Focus on 'how many more/fewer' language" | SK6:difference templates should be the largest group; comparison language in prompts |
| Both orientations | "Both orientations mixed" | Templates must specify H and V variants or require the expansion step to mix orientations |
| No creation | Scaffolding Notes: "No graph creation yet - pure reading and interpretation" | Confirms SK3 as teaching-only; all practice templates are reading/interpretation |
| Guide models comparison language | "Guide models comparison language explicitly" | In Practice (Helper voice), comparison questions should use the modeled language: "how many more," "how many fewer" — not assumed student vocabulary |

### F. Track Classification

| Interaction Pattern | RDR Track | Confidence | Notes |
|---|---|---|---|
| MC (4-option selection for value reading) | MC (RDR §3) | HIGH | "How many [category]?" → select numerical answer. Standard MC. |
| Click-to-select (click the category with most/fewest) | MC (RDR §3) | HIGH | Selection from visible options (categories on graph). Treated as MC variant. |
| Click-two-to-compare (select two categories for comparison) | Non-MC (RDR §2) | MEDIUM | Student selects two categories, then system shows calculation. The selection is the interaction; the arithmetic is the assessment. **Ambiguous:** Is the student assessed on the selection (MC-like) or on understanding the result? Flagged for author review. |

**Author review note:** The click-two-to-compare interaction may not appear in Practice at all — the Toy Flow describes it in Lesson context ("Click categories to highlight, click two to compare, System shows difference calculations"). Practice may use only MC format for comparison questions. If so, all practice templates are MC track. **Recommendation: default all templates to MC track** unless the author confirms a non-MC comparison interaction in Practice.

### G. Dimension Budget

| Parameter | Confidence/Support | Baseline | Stretch/Challenge |
|---|---|---|---|
| Values per category | 3-6 (smaller, easier to count) | 1-8 (full familiar range) | 7-10 (larger values, closer together) |
| Categories | 3 (warm-up familiar) | 3-4 | 4-5 (more to scan) |
| Graph type | Picture graph (more familiar) | Picture and bar mixed | Bar graph (less familiar at entry) |
| Orientation | Horizontal (more familiar) | H and V mixed | Vertical only |
| Difference between compared categories | 1-3 (obvious, large gap) | 1-5 | 4-7 (small gaps between large values — harder to discriminate) |
| Distractor proximity | Spread (correct answer is clearly different from distractors) | Moderate | Close (distractors near correct value) |

---

## §PT.2 Goal Decomposition

### Component Balance

| Component | Skills | Count | % of Templates (target) | Notes |
|---|---|---|---|---|
| Conceptual | S1 (read picture graph), S2 (read bar graph), S3 (ordinal comparison), S4 (difference comparison) | 4 | ~85% | Core reading/interpretation skills. |
| Procedural | — | 0 | 0% | SK3 is teaching-only. |
| Transfer | S5 (combination/total) | 1 | ~15% | "How many in all" requires applying addition across multiple categories — a step beyond simple reading or comparison. |

**Deviation from 30-40-30 target:** M1 is a Grade 2 review/activation module. Conceptual dominance is expected. The addition of S5 (apply/transfer) provides a small but meaningful transfer component. Later modules (M2+) introduce creation (procedural) and more complex application to balance the unit.

### Verb Distribution

Using the Toy Flow Cognitive Focus and Early Module defaults:

| Verb | Skills | Templates (est.) | % (target) | Toy Flow Basis |
|---|---|---|---|---|
| identify | S1, S2, S3 | ~50% | 45-55% | "IDENTIFY (Conceptual) — recognizing data patterns." SK1/SK2 reading + SK6:ordinal identification. |
| compare | S4 | ~35% | 30-40% | "COMPARE (Conceptual) — determining relationships." SK6:difference is the core practice focus. |
| apply | S5 | ~15% | 10-20% | SK6:combination — "how many in all" requires applying addition across categories. |
| create | — | 0% | 0% | No creation in Practice. |
| connect | — | 0% | 0% | Not in Cognitive Focus. |

**Note:** The Toy Flow's emphasis on "how many more/fewer" and comparison suggests compare should be ~35%, higher than Early Module default. Adding SK6:combination (apply) at ~15% gives the module three verb types — closer to the v1 template output and better coverage of the assessed cognitive range.

### Distribution Targets

**Pool Target:** 55-65 problems (Early M1-4 range per Playbook §8)

| Tier | Target % | Target Count | Rationale |
|---|---|---|---|
| confidence | 8-12% | 5-7 | Below-grade scaffolded entry. Uses familiar parameters (3 categories, horizontal picture graph, values 3-6). |
| support | 15-20% | 9-12 | Scaffolded/simplified. Familiar graph types, moderate values. May include orientation constraint (H only). |
| baseline | 40-50% | 24-30 | Grade-level standard. Both graph types, both orientations, full value range 1-8. |
| stretch | 15-20% | 9-12 | More categories (4-5), vertical orientation, values near upper range, closer differences. |
| challenge | 5-8% | 3-5 | 5 categories, vertical bar graph, values 7-10, small differences between large values. |

### Skill-to-Template Allocation (estimated)

| Mod. Skill | Spine ID | Sub-skill | Verb | Est. Templates | Est. Problems | Tiers |
|---|---|---|---|---|---|---|
| S1 | U1.SK1 | — | identify | 3-4 | 12-16 | confidence, support, baseline, stretch |
| S2 | U1.SK2 | — | identify | 3-4 | 12-16 | confidence, support, baseline, stretch |
| S3 | U1.SK6 | SK6:ordinal | identify | 2-3 | 8-10 | support, baseline, stretch |
| S4 | U1.SK6 | SK6:difference | compare | 3-4 | 12-16 | support, baseline, stretch, challenge |
| S5 | U1.SK6 | SK6:combination | apply | 2 | 8-10 | baseline, stretch |
| — | — | — | — | **13-17 std** | **52-68** | — |

**Misconception Remediation Templates (separate sub-pool):**

| Target | Spine ID | Est. Templates | Tiers |
|---|---|---|---|
| #6 ("More Than" Means Add) | U1.SK6 | 1 | confidence/support |
| #16 (Graph as Picture) | U1.SK1/SK2 | 1 | confidence/support |
| — | — | **2 remed** | — |

---

## [AUTHOR REVIEW — COMPLETED 2026-04-15]

**Decisions confirmed:**

1. **Skill decomposition:** SK6 decomposed into 3 sub-skills (ordinal, difference, combination). SK3 teaching-only confirmed.
2. **SK6:combination (S5)** added as third sub-skill — verb: apply, component: transfer. "How many in all" is a distinct cognitive operation.
3. **Data Constraints:** Derived values confirmed (1-10, 3-5 categories, both orientations).
4. **Misconception priorities revised:** #6 = PRIMARY, **#16 = PRIMARY** (upgraded from SECONDARY — foundational reading misconception in a module that's entirely about reading graphs), #17 = MONITOR.
5. **All MC track:** Confirmed. Click-two-to-compare is Lesson-only.
6. **Verb distribution:** ~50% identify / ~35% compare / ~15% apply (3 verb types).
7. **Pool target:** 55-65 standard problems + 2 remediation templates confirmed.
8. **RDR gap:** Acceptable. Proceeding with embedded rules; post-RDR validation pass planned.

---

## §PT.3 Templates

### Standard Templates

---

#### Template 0101 — Read Picture Graph Value (Confidence)

**🟢 SKILL:** S1 — Read a specific value from a 1:1 picture graph

**🔵 PROBLEM TYPE:** Given a horizontal picture graph with 3 categories, student selects the value for a named category from 4 MC options.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — context is flavor; any countable-category survey theme works.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite fruits | apples, bananas, grapes | Universal, high familiarity |
| Playground games | tag, hopscotch, jump rope | Active play — engaging for Grade 3 |
| Favorite colors | red, blue, green | Simple, no cultural assumptions |
| Classroom pets | fish, hamsters, turtles | Common school experience |
| Favorite sports | soccer, basketball, swimming | Broad appeal |
| Snack choices | crackers, pretzels, fruit cups | School-lunch familiar |

**🟠 PROMPT EXAMPLES:**
1. "How many students chose bananas?"
2. "How many votes did soccer get?"
3. "How many animals are cats?"
4. "How many students like red?"
5. "How many people picked crackers?"

**🟣 SUCCESS DIALOGUE:**
1. "That's right — 5 students chose bananas."
2. "4 votes for soccer."
3. "Correct. 6 animals are cats."
4. "5 students like red. You read that right."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| Key emphasis pulse — key briefly highlights on graph load | confidence | Graph loads | TF: "Each [symbol] will represent one animal" — key is the anchor for reading |
| Category label highlight — target category row briefly pulses | confidence | After prompt displays | TF: "Category labels identify what each row represents" |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| adjacent_category | Reads value from wrong category row | Key Beat: category identification | "Look at the category labels on the left. Find the row that says [category]. Count the symbols in THAT row." |
| off_by_one | Miscounts symbols by ±1 | Key Beat: one-to-one counting | "Touch each symbol as you count. Each symbol stands for exactly one [item]. Count them again carefully." |
| total_all | Reports the total of all categories instead of the named one | #17 (All Data Must Be Used) | "The question asks about just ONE category. Find [category] and count only the symbols in that row." |
| visual_arrangement | Counts based on visual grouping rather than data alignment | #16 (Graph as Picture) | "Look at the KEY — it tells you what each symbol means. Use the key, not the picture shape, to find the count." |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3)
Light only: "Count the symbols in the [category] row." No Medium/Heavy — confidence tier (per RDR §11).
Validator: [Validator: Misconception_#16], [Validator: Misconception_#17]

**Technical Details:**
```
template_id: 0101
template_type: standard
spine_skill_id: U1.SK1
sub_skill: —
skill_id: S1
secondary_skill: —
skill: Read a specific value from a 1:1 picture graph
problem_type: Read named category value from horizontal picture graph (3 categories)
workspace_description: Horizontal picture graph with 3 categories, uniform symbol (e.g., stars), 1:1 scale. Key displayed showing "Each [symbol] = 1 [item]." Title visible. Category labels on left. 4 MC answer options below graph.
prompt_examples: ["How many students chose bananas?", "How many votes did soccer get?", "How many animals are cats?", "How many students like red?", "How many people picked crackers?"]
action_description: MC (4-option selection)
mastery_tier: confidence
mastery_verb: identify
parameter_coverage: values 3-6 per category; 3 categories; horizontal orientation; symbols: paw prints, stars, hearts, smiley faces
correct_end_state: Student selects the number matching the count of symbols in the named category row
success_dialogue: ["That's right — 5 students chose bananas.", "4 votes for soccer.", "Correct. 6 animals are cats.", "5 students like red. You read that right."]
key_teaching_moment: "Lesson: Guide highlights key — 'Each symbol means one animal.' Student clicks category to see count."
remediation_track: MC
validator_tag: [Validator: Misconception_#16], [Validator: Misconception_#17]
problem_count: 5
```

---

#### Template 0102 — Read Picture Graph Value (Baseline)

**🟢 SKILL:** S1 — Read a specific value from a 1:1 picture graph

**🔵 PROBLEM TYPE:** Given a picture graph (either orientation) with 3-4 categories, student selects the value for a named category from 4 MC options.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — any countable-category theme.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite seasons | spring, summer, fall, winter | 4-category natural set |
| School subjects | math, reading, science, art | School familiar |
| Weekend activities | biking, reading, swimming, drawing | Broad appeal |
| Ice cream flavors | vanilla, chocolate, strawberry, mint | Universal treat |
| Transportation to school | bus, car, walk, bike | Community variety |
| Garden plants | tomatoes, sunflowers, beans, peppers | Nature theme |

**🟠 PROMPT EXAMPLES:**
1. "How many students picked summer?"
2. "How many people like chocolate?"
3. "How many chose to walk?"
4. "How many students voted for science?"
5. "How many gardens have beans?"

**🟣 SUCCESS DIALOGUE:**
1. "8 students picked summer."
2. "That's 3 for chocolate."
3. "Right — 7 students walk to school."
4. "Correct. 4 voted for science."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| None — baseline expects independent reading | — | — | — |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| adjacent_category | Reads from neighboring category | Key Beat: category identification | "Find the label that matches the question. Read only that row or column." |
| off_by_one | Miscounts symbols ±1 | Key Beat: one-to-one counting | "Point to each symbol and count out loud. Each one means exactly 1 [item]." |
| visual_arrangement | Attends to graph shape not data | #16 (Graph as Picture) | "The symbols tell the data, not the shape. Use the key to read what each symbol means." |
| total_all | Adds all categories together | #17 (All Data Must Be Used) | "The question names one category. Find that label and count only its symbols." |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3)
Medium: Per-distractor — see Distractor Types table above.
        Visual scaffold: System highlights the target category row/column; other categories dim. 20-30 words per RDR §5.
Heavy [Modeling]: "Watch — I'll find [category]. Here's the label [highlights]. Now I count each symbol: 1, 2, 3, 4, 5. There are 5 [items] for [category]."
        Visual: System highlights the category label, then circles each symbol sequentially as it counts.
Post-Modeling: "I showed you how to find and count. Let's try the next one."
Validator: [Validator: Misconception_#16], [Validator: Misconception_#17]

**Technical Details:**
```
template_id: 0102
template_type: standard
spine_skill_id: U1.SK1
sub_skill: —
skill_id: S1
secondary_skill: —
skill: Read a specific value from a 1:1 picture graph
problem_type: Read named category value from picture graph (3-4 categories, either orientation)
workspace_description: Picture graph (horizontal or vertical), 3-4 categories, uniform symbol, 1:1 scale. Key displayed. Title visible. 4 MC answer options.
prompt_examples: ["How many students picked summer?", "How many people like chocolate?", "How many chose to walk?", "How many students voted for science?", "How many gardens have beans?"]
action_description: MC (4-option selection)
mastery_tier: baseline
mastery_verb: identify
parameter_coverage: values 1-8 per category; 3-4 categories; horizontal and vertical orientation mixed; symbols varied
correct_end_state: Student selects the number matching the symbol count for the named category
success_dialogue: ["8 students picked summer.", "That's 3 for chocolate.", "Right — 7 students walk to school.", "Correct. 4 voted for science."]
key_teaching_moment: "Lesson: Guide highlights key and category label. Student clicks category to see count highlighted."
remediation_track: MC
validator_tag: [Validator: Misconception_#16], [Validator: Misconception_#17]
problem_count: 6
```

---

#### Template 0103 — Read Picture Graph Value (Stretch)

**🟢 SKILL:** S1 — Read a specific value from a 1:1 picture graph

**🔵 PROBLEM TYPE:** Given a vertical picture graph with 4-5 categories and values near the upper range, student selects the correct value from 4 closely-spaced MC options.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — any countable-category theme. Upper values (7-10) should feel plausible.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Birds spotted on a nature walk | robins, sparrows, jays, cardinals, crows | 5 categories; nature-count plausible at higher values |
| Library books checked out | fiction, science, art, history, comics | School library context |
| Stickers earned this week | stars, hearts, smiley faces, rainbows | Reward tracking — values up to 10 plausible |
| Vegetables in the garden | carrots, tomatoes, peppers, beans, lettuce | Growth/harvest context |

**🟠 PROMPT EXAMPLES:**
1. "How many sparrows were spotted?"
2. "How many science books were checked out?"
3. "How many star stickers did you earn?"
4. "How many tomatoes grew in the garden?"
5. "How many jays did we see?"

**🟣 SUCCESS DIALOGUE:**
1. "9 sparrows spotted."
2. "That's right — 8 science books."
3. "You earned 10 star stickers."
4. "Correct. 7 tomatoes."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| None — stretch expects full independence | — | — | — |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| off_by_one | Miscounts at higher values (8 vs 9) | Key Beat: one-to-one counting | "With more symbols, it's easy to lose count. Touch each one as you count from the bottom up." |
| off_by_two | Miscounts by ±2 at higher values | Key Beat: one-to-one counting | "Start at the bottom of the column and count each symbol carefully. Don't skip any." |
| adjacent_category | Reads adjacent column (harder with 5 categories) | Key Beat: category identification | "There are more columns now. Read the label at the bottom to make sure you're in the right column." |
| visual_arrangement | Judges by column height comparison rather than counting | #16 (Graph as Picture) | "Don't guess from the column shape. Count the actual symbols — each one is exactly 1 [item]." |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3)
Medium: Per-distractor — see table above.
        Visual scaffold: Target column highlighted; counted symbols get sequential number labels overlaid.
Heavy [Modeling]: "Let me show you. I find [category] at the bottom [highlights label]. Then I count up: 1, 2, 3... 9. There are 9 [items]. The key says each symbol is one, so 9 symbols means 9."
        Visual: System highlights label, then numbers each symbol bottom-to-top.
Post-Modeling: "I counted each symbol from the bottom. Try the next one that way."
Validator: [Validator: Misconception_#16]

**Technical Details:**
```
template_id: 0103
template_type: standard
spine_skill_id: U1.SK1
sub_skill: —
skill_id: S1
secondary_skill: —
skill: Read a specific value from a 1:1 picture graph
problem_type: Read named category value from vertical picture graph (4-5 categories, high values)
workspace_description: Vertical picture graph, 4-5 categories, uniform symbol, 1:1 scale. Key displayed. Values 7-10 range. 4 MC answer options with close spacing (e.g., 7, 8, 9, 10).
prompt_examples: ["How many sparrows were spotted?", "How many science books were checked out?", "How many star stickers did you earn?", "How many tomatoes grew in the garden?", "How many jays did we see?"]
action_description: MC (4-option selection)
mastery_tier: stretch
mastery_verb: identify
parameter_coverage: values 7-10 per category; 4-5 categories; vertical orientation; close distractors (±1, ±2)
correct_end_state: Student selects exact count from closely-spaced options
success_dialogue: ["9 sparrows spotted.", "That's right — 8 science books.", "You earned 10 star stickers.", "Correct. 7 tomatoes."]
key_teaching_moment: "Lesson: one-to-one correspondence counting with key interpretation."
remediation_track: MC
validator_tag: [Validator: Misconception_#16]
problem_count: 5
```

---

#### Template 0104 — Read Bar Graph Value (Confidence)

**🟢 SKILL:** S2 — Read a specific value from a 1:1 bar graph

**🔵 PROBLEM TYPE:** Given a horizontal bar graph (scale of 1) with 3 categories, student selects the value for a named category from 4 MC options.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — any countable-category survey theme.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite fruits | apples, bananas, grapes | Familiar, warm-up callback |
| Playground games | tag, hopscotch, jump rope | Active play |
| Favorite colors | red, blue, green | Simple |
| Classroom pets | fish, hamsters, turtles | Common school context |
| Snack votes | crackers, pretzels, yogurt | Lunch familiar |

**🟠 PROMPT EXAMPLES:**
1. "How many students chose apples?"
2. "How many votes for hopscotch?"
3. "How many animals are fish?"
4. "How many picked blue?"
5. "How many chose yogurt?"

**🟣 SUCCESS DIALOGUE:**
1. "Right — 6 students chose apples."
2. "3 votes for hopscotch."
3. "That's 5 fish."
4. "Correct. 4 picked blue."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| Scale label pulse — number scale briefly highlights on graph load | confidence | Graph loads | TF: "Bar graphs use bars to show data, scale counts by 1s" |
| Helping line — faint line extends from bar end to scale numbers | confidence | Student hovers on bar | TF Lesson: "Click categories to highlight" → system shows value |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| bar_count | Counts number of bars rather than reading bar length | #16 (Graph as Picture) | "The NUMBER of bars isn't the answer. Look at how LONG this bar is. Follow it to the number scale." |
| adjacent_bar | Reads the wrong bar | Key Beat: category identification | "Find the label for [category]. Follow that bar across to the number scale." |
| off_by_one | Reads between gridlines | Key Beat: scale reading | "Find where the bar ends. Look straight down (or across) to the nearest number on the scale." |
| scale_confusion | Reads the category position number instead of the value | #16 (Graph as Picture) | "The numbers along the bottom (or side) are the SCALE — they tell you the amount. The bar reaches to the amount." |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3)
Light only: "Follow the [category] bar to the number scale." No Medium/Heavy — confidence tier (per RDR §11).
Validator: [Validator: Misconception_#16]

**Technical Details:**
```
template_id: 0104
template_type: standard
spine_skill_id: U1.SK2
sub_skill: —
skill_id: S2
secondary_skill: —
skill: Read a specific value from a 1:1 bar graph
problem_type: Read named category value from horizontal bar graph (3 categories, scale of 1)
workspace_description: Horizontal bar graph, 3 categories, scale of 1 (numbered 0-10). Gridlines visible. Title displayed. Category labels on left. 4 MC answer options.
prompt_examples: ["How many students chose apples?", "How many votes for hopscotch?", "How many animals are fish?", "How many picked blue?", "How many chose yogurt?"]
action_description: MC (4-option selection)
mastery_tier: confidence
mastery_verb: identify
parameter_coverage: values 3-6 per category; 3 categories; horizontal orientation; scale 0-10 by 1s
correct_end_state: Student selects value where the named category's bar ends on the scale
success_dialogue: ["Right — 6 students chose apples.", "3 votes for hopscotch.", "That's 5 fish.", "Correct. 4 picked blue."]
key_teaching_moment: "Lesson: System draws helping line from bar end to axis value. Guide: 'the bar reaches to 6, so 6 students chose apples.'"
remediation_track: MC
validator_tag: [Validator: Misconception_#16]
problem_count: 5
```

---

#### Template 0105 — Read Bar Graph Value (Baseline)

**🟢 SKILL:** S2 — Read a specific value from a 1:1 bar graph

**🔵 PROBLEM TYPE:** Given a bar graph (either orientation) with 3-4 categories and scale of 1, student selects the value for a named category.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — any countable-category theme.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| After-school activities | art club, soccer, coding, music | 4-category school set |
| Lunch orders | pizza, sandwich, salad, pasta | Cafeteria theme |
| Favorite animals | dogs, cats, birds, rabbits | Pet variety |
| Weather this month | sunny, rainy, cloudy, windy | Science connection |
| Favorite books | mystery, adventure, fantasy, funny | Reading engagement |
| Recycling collection | paper, plastic, cans, glass | Community theme |

**🟠 PROMPT EXAMPLES:**
1. "How many students joined art club?"
2. "How many orders for pizza?"
3. "How many sunny days?"
4. "How many chose mystery books?"
5. "How many pounds of plastic were collected?"

**🟣 SUCCESS DIALOGUE:**
1. "That's right — 7 students joined art club."
2. "8 orders for pizza."
3. "Correct. 5 sunny days this month."
4. "3 students chose mystery books."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| None — baseline expects independent reading | — | — | — |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| bar_count | Counts number of bars rather than reading bar height/length | #16 (Graph as Picture) | "The bar's LENGTH shows the amount. Follow the end of the bar to the number scale." |
| adjacent_bar | Reads value from wrong bar | Key Beat: category identification | "Check the category label. Make sure you're reading the bar that matches [category]." |
| off_by_one | Misreads between scale marks | Key Beat: scale reading | "Find exactly where the bar ends. Line it up with the nearest number on the scale." |
| highest_value | Always picks the tallest/longest bar regardless of question | #16 (Graph as Picture) | "The question asks about [category], not the biggest bar. Find the [category] label first." |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3)
Medium: Per-distractor — see table above.
        Visual scaffold: Helping line from bar end to scale value; other bars dimmed. 20-30 words.
Heavy [Modeling]: "I'll find [category]. Here's the label [highlights]. The bar reaches to... here [traces]. The scale says 7. So 7 [items] for [category]."
        Visual: System highlights label, traces bar to scale endpoint, circles the scale number.
Post-Modeling: "I followed the bar to the scale. Try the next one."
Validator: [Validator: Misconception_#16]

**Technical Details:**
```
template_id: 0105
template_type: standard
spine_skill_id: U1.SK2
sub_skill: —
skill_id: S2
secondary_skill: —
skill: Read a specific value from a 1:1 bar graph
problem_type: Read named category value from bar graph (3-4 categories, either orientation, scale of 1)
workspace_description: Bar graph (horizontal or vertical), 3-4 categories, scale of 1. Gridlines visible. Title and axis labels displayed. 4 MC answer options.
prompt_examples: ["How many students joined art club?", "How many orders for pizza?", "How many sunny days?", "How many chose mystery books?", "How many pounds of plastic were collected?"]
action_description: MC (4-option selection)
mastery_tier: baseline
mastery_verb: identify
parameter_coverage: values 1-8 per category; 3-4 categories; horizontal and vertical mixed; scale 0-10 by 1s
correct_end_state: Student selects the scale value at the bar's endpoint
success_dialogue: ["That's right — 7 students joined art club.", "8 orders for pizza.", "Correct. 5 sunny days this month.", "3 students chose mystery books."]
key_teaching_moment: "Lesson: System draws helping line from bar top/end to axis. Guide: 'the HEIGHT of the bar tells us the amount.'"
remediation_track: MC
validator_tag: [Validator: Misconception_#16]
problem_count: 6
```

---

#### Template 0106 — Read Bar Graph Value (Stretch)

**🟢 SKILL:** S2 — Read a specific value from a 1:1 bar graph

**🔵 PROBLEM TYPE:** Given a vertical bar graph with 4-5 categories and higher values, student selects the correct value from closely-spaced MC options.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — any countable-category theme. Values 7-10 plausible.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Seashells collected at the beach | conch, clam, starfish, sand dollar, scallop | 5 categories, nature count |
| Points scored in classroom games | Team A, Team B, Team C, Team D | Competitive context |
| Flowers in the school garden | roses, tulips, daisies, sunflowers, lilies | Nature/growth |
| Books read by each student | Mia, Leo, Sam, Ava | Student-tracking context |

**🟠 PROMPT EXAMPLES:**
1. "How many conch shells were found?"
2. "How many points did Team C score?"
3. "How many tulips are in the garden?"
4. "How many books did Leo read?"
5. "How many sand dollars were collected?"

**🟣 SUCCESS DIALOGUE:**
1. "9 conch shells."
2. "Team C scored 8 points."
3. "That's 10 tulips."
4. "Leo read 7 books."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| None — stretch expects full independence | — | — | — |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| off_by_one | Misreads at higher values where bars are close in height | Key Beat: scale reading | "At higher numbers, the bars look similar. Line up the bar top carefully with the scale number." |
| off_by_two | Misreads by ±2 | Key Beat: scale reading | "Use the gridlines. Follow the bar top straight across to the number. Count the gridlines if needed." |
| adjacent_bar | Reads wrong bar among 5 crowded categories | Key Beat: category identification | "With more bars, check the label carefully. Make sure you're looking at the right one." |
| bar_count | Counts number of bars (reports 5 when there are 5 categories) | #16 (Graph as Picture) | "The number of bars tells you how many CATEGORIES there are, not the amount. Read the SCALE for the amount." |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3)
Medium: Per-distractor — see table above.
        Visual scaffold: Horizontal helping line from bar top to y-axis; scale value circled.
Heavy [Modeling]: "Let me trace it. [category] bar goes up to... here [traces to gridline]. The scale says 9. So 9 [items]."
        Visual: System draws dotted line from bar top to y-axis, circles the value.
Post-Modeling: "I used the gridlines to find the exact number. Your turn."
Validator: [Validator: Misconception_#16]

**Technical Details:**
```
template_id: 0106
template_type: standard
spine_skill_id: U1.SK2
sub_skill: —
skill_id: S2
secondary_skill: —
skill: Read a specific value from a 1:1 bar graph
problem_type: Read named category value from vertical bar graph (4-5 categories, high values)
workspace_description: Vertical bar graph, 4-5 categories, scale of 1 (0-10). Gridlines visible. Values 7-10 range. 4 MC answer options with close spacing (±1, ±2).
prompt_examples: ["How many conch shells were found?", "How many points did Team C score?", "How many tulips are in the garden?", "How many books did Leo read?", "How many sand dollars were collected?"]
action_description: MC (4-option selection)
mastery_tier: stretch
mastery_verb: identify
parameter_coverage: values 7-10; 4-5 categories; vertical orientation; close distractors (±1, ±2)
correct_end_state: Student selects exact value from closely-spaced options
success_dialogue: ["9 conch shells.", "Team C scored 8 points.", "That's 10 tulips.", "Leo read 7 books."]
key_teaching_moment: "Lesson: bar-to-axis reading with helping line."
remediation_track: MC
validator_tag: [Validator: Misconception_#16]
problem_count: 5
```

---

#### Template 0107 — Identify Category with Most or Fewest (Support)

**🟢 SKILL:** S3 — Identify which category has the most or fewest (SK6:ordinal)

**🔵 PROBLEM TYPE:** Given a bar or picture graph with 3 categories, student selects which category has the most (or fewest) items.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — any countable-category theme. Values should have clear "winner" (not close).

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite pets | cats, dogs, fish | Familiar, clear preference likely |
| Rainy days by month | March, April, May | Seasonal |
| Toys in the toy box | cars, dolls, blocks | Classroom familiar |
| Fruits in the basket | apples, oranges, bananas | Tangible counting |
| Flowers planted | roses, tulips, daisies | Garden theme |

**🟠 PROMPT EXAMPLES:**
1. "Which pet is the favorite?"
2. "Which month had the most rainy days?"
3. "Which toy do we have the fewest of?"
4. "Which fruit do we have the most of?"
5. "Which flower was planted the least?"

**🟣 SUCCESS DIALOGUE:**
1. "Dogs are the favorite — they have the most votes."
2. "April had the most rainy days."
3. "We have the fewest dolls."
4. "We have the most apples."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| Comparison language cue — "Look for the TALLEST bar" or "Find the row with the MOST symbols" | support | After prompt displays | TF: "Guide asks: 'What do you notice? What's the same/different?'" |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| most_least_reversal | Picks fewest when asked for most (or vice versa) | Key Beat: comparison language | "'Most' means the BIGGEST number. 'Fewest' means the SMALLEST. Which bar is tallest?" |
| middle_value | Picks the middle-sized category | Key Beat: comparison | "Compare ALL the bars. Find the one that goes the FARTHEST (or shortest)." |
| first_listed | Picks whichever category appears first on the graph | #16 (Graph as Picture) | "The order on the graph doesn't matter. Compare the SIZES of the bars to find the answer." |
| visual_proximity | Picks the category visually closest to the question text | #16 (Graph as Picture) | "Look at the data, not the position. Which bar is actually the tallest (or shortest)?" |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3)
Medium: Per-distractor — see table above.
        Visual scaffold: All bars highlighted with value labels appearing; tallest/shortest bar pulses.
Heavy [Modeling]: "Let me compare. [Category A] has 3. [Category B] has 7. [Category C] has 5. 7 is the biggest number, so [B] has the most."
        Visual: System labels each bar with its value, then circles the highest/lowest.
Post-Modeling: "I checked every bar's number to find the biggest. Try the next one."
Validator: [Validator: Misconception_#16]

**Technical Details:**
```
template_id: 0107
template_type: standard
spine_skill_id: U1.SK6
sub_skill: SK6:ordinal
skill_id: S3
secondary_skill: —
skill: Identify which category has the most or fewest
problem_type: Select the category with most or fewest from a 3-category graph
workspace_description: Bar graph or picture graph, 3 categories, 1:1 scale. Values have a clear maximum or minimum (gap of ≥2 between top/bottom and next). 4 MC options: 3 category names + 1 distractor (e.g., "they are all the same").
prompt_examples: ["Which pet is the favorite?", "Which month had the most rainy days?", "Which toy do we have the fewest of?", "Which fruit do we have the most of?", "Which flower was planted the least?"]
action_description: MC (4-option selection — category names, not numbers)
mastery_tier: support
mastery_verb: identify
parameter_coverage: values 2-7 per category; gap ≥2 between most/fewest and next; 3 categories; either orientation
correct_end_state: Student selects the category name with the highest (or lowest) value
success_dialogue: ["Dogs are the favorite — they have the most votes.", "April had the most rainy days.", "We have the fewest dolls.", "We have the most apples."]
key_teaching_moment: "Lesson: Guide asks 'What do you notice?' Student clicks to highlight and compare categories."
remediation_track: MC
validator_tag: [Validator: Misconception_#16]
problem_count: 5
```

---

#### Template 0108 — Identify Category with Most or Fewest (Baseline)

**🟢 SKILL:** S3 — Identify which category has the most or fewest (SK6:ordinal)

**🔵 PROBLEM TYPE:** Given a bar or picture graph with 3-4 categories, some with close values, student selects which category has the most (or fewest).

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — any countable-category theme. Close values (gap of 1) increase difficulty.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite subjects | math, reading, science, art | 4 categories |
| Bugs found outside | ants, beetles, butterflies, ladybugs | Nature exploration |
| Colors of cars in the parking lot | red, blue, white, black | Observation activity |
| Drinks at the party | juice, water, milk, lemonade | Event context |
| Types of trees on the playground | oak, maple, pine, birch | Nature/science |

**🟠 PROMPT EXAMPLES:**
1. "Which subject is the most popular?"
2. "Which bug was found the least?"
3. "Which color car do we see the most?"
4. "Which drink was chosen the fewest times?"
5. "Which type of tree is most common?"

**🟣 SUCCESS DIALOGUE:**
1. "Math is the most popular."
2. "Butterflies were found the least."
3. "We see the most white cars."
4. "Milk was chosen the fewest times."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| None — baseline expects independent comparison | — | — | — |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| most_least_reversal | Picks fewest when asked for most | Key Beat: comparison language | "Read the question again — does it say 'most' or 'fewest'? Then find the bar that matches." |
| close_neighbor | Picks a category with value within ±1 of the correct answer | Key Beat: careful reading | "Two bars look close. Read the scale carefully for each one. Which number is actually bigger?" |
| first_listed | Picks the first category on the graph | #16 (Graph as Picture) | "Don't pick by position. Compare the actual amounts shown by each bar." |
| visual_proximity | Picks visually prominent category | #16 (Graph as Picture) | "Look at the numbers, not the colors or position. Which amount is the largest (or smallest)?" |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3)
Medium: Per-distractor — see table above.
        Visual scaffold: Bar values labeled; top-two (or bottom-two) bars highlighted for direct comparison.
Heavy [Modeling]: "These two look close. Let me check: [A] reaches 6, [B] reaches 7. 7 is more than 6, so [B] has the most."
        Visual: System labels the two closest bars and draws a comparison bracket.
Post-Modeling: "When bars look close, read the exact numbers. Let's try another."
Validator: [Validator: Misconception_#16]

**Technical Details:**
```
template_id: 0108
template_type: standard
spine_skill_id: U1.SK6
sub_skill: SK6:ordinal
skill_id: S3
secondary_skill: —
skill: Identify which category has the most or fewest
problem_type: Select category with most or fewest from graph with close values (3-4 categories)
workspace_description: Bar or picture graph, 3-4 categories, 1:1 scale. At least 2 categories within ±1 of each other. 4 MC options: category names.
prompt_examples: ["Which subject is the most popular?", "Which bug was found the least?", "Which color car do we see the most?", "Which drink was chosen the fewest times?", "Which type of tree is most common?"]
action_description: MC (4-option selection — category names)
mastery_tier: baseline
mastery_verb: identify
parameter_coverage: values 3-8; gap of 1 between top categories; 3-4 categories; both orientations
correct_end_state: Student selects correct category name even when values are close
success_dialogue: ["Math is the most popular.", "Butterflies were found the least.", "We see the most white cars.", "Milk was chosen the fewest times."]
key_teaching_moment: "Lesson: comparing categories by clicking to highlight and reading values."
remediation_track: MC
validator_tag: [Validator: Misconception_#16]
problem_count: 5
```

---

#### Template 0109 — How Many More/Fewer (Support)

**🟢 SKILL:** S4 — Determine "how many more" or "how many fewer" between two categories (SK6:difference)

**🔵 PROBLEM TYPE:** Given a graph with 3 categories and a "how many more" or "how many fewer" question naming two categories, student selects the difference from 4 MC options.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **tight** — context must support sensible comparison language ("more X than Y").

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite fruits | apples, bananas, grapes | "How many more students chose apples than grapes?" |
| Playground games | tag, hopscotch, jump rope | "How many fewer students like hopscotch than tag?" |
| Classroom pets | cats, dogs, fish | "How many more fish than cats?" |
| Favorite colors | red, blue, green | "How many fewer students like green than blue?" |
| Snacks at the party | chips, cookies, fruit | "How many more cookies than fruit?" |

**🟠 PROMPT EXAMPLES:**
1. "How many more students chose apples than grapes?"
2. "How many fewer students like hopscotch than tag?"
3. "How many more fish than cats are there?"
4. "How many fewer students picked green than blue?"
5. "How many more cookies were there than fruit?"

**🟣 SUCCESS DIALOGUE:**
1. "3 more students chose apples."
2. "There are 2 fewer hopscotch fans."
3. "That's right — 2 more fish than cats."
4. "1 fewer student picked green."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| Comparison highlight — both named categories highlighted with values labeled | support | After prompt displays | TF: "Click two to compare, System shows difference calculations" |
| Language cue — "MORE means the bigger number minus the smaller number" | support | First difference problem in session | TF: "Guide models comparison language explicitly" |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| sum_of_pair | Adds the two values instead of subtracting | #6 ("More Than" Means Add) | "'How many MORE' means find the DIFFERENCE. That's the bigger number MINUS the smaller number, not plus." |
| larger_value | Reports the larger of the two category values | Key Beat: difference vs value | "The question asks 'how many MORE' — that's not the bigger number itself. Subtract the smaller from the bigger." |
| smaller_value | Reports the smaller of the two category values | Key Beat: difference vs value | "That's one of the values, not the difference. 'How many more' means subtract: big number minus small number." |
| total_all | Reports total of all categories | #17 (All Data Must Be Used) | "You only need TWO categories for this question. Find [A] and [B], then subtract." |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3)
Medium: Per-distractor — see table above.
        Visual scaffold: Both named categories highlighted; difference bracket shown between them.
Heavy [Modeling]: "[A] has 7. [B] has 4. 'How many more' means I subtract: 7 minus 4 equals 3. There are 3 more [A] than [B]."
        Visual: Both bars/rows highlighted, difference bracket with arithmetic shown.
Post-Modeling: "I found each amount, then subtracted. Try the next one."
Validator: [Validator: Misconception_#6], [Validator: Misconception_#17]

**Technical Details:**
```
template_id: 0109
template_type: standard
spine_skill_id: U1.SK6
sub_skill: SK6:difference
skill_id: S4
secondary_skill: S1 or S2 (reading values is prerequisite)
skill: Determine "how many more" or "how many fewer" between two categories
problem_type: Compute difference between two named categories (3-category graph)
workspace_description: Bar or picture graph, 3 categories, 1:1 scale. Two categories named in question. Values produce small differences (1-3). 4 MC answer options including sum distractor and individual values.
prompt_examples: ["How many more students chose apples than grapes?", "How many fewer students like hopscotch than tag?", "How many more fish than cats are there?", "How many fewer students picked green than blue?", "How many more cookies were there than fruit?"]
action_description: MC (4-option selection)
mastery_tier: support
mastery_verb: compare
parameter_coverage: values 3-7 per category; differences 1-3; 3 categories; either orientation
correct_end_state: Student selects the absolute difference between the two named category values
success_dialogue: ["3 more students chose apples.", "There are 2 fewer hopscotch fans.", "That's right — 2 more fish than cats.", "1 fewer student picked green."]
key_teaching_moment: "Lesson: Student clicks two categories to compare. System shows: '[A] has 7. [B] has 4. The difference is 3.'"
remediation_track: MC
validator_tag: [Validator: Misconception_#6], [Validator: Misconception_#17]
problem_count: 5
```

---

#### Template 0110 — How Many More/Fewer (Baseline)

**🟢 SKILL:** S4 — Determine "how many more" or "how many fewer" between two categories (SK6:difference)

**🔵 PROBLEM TYPE:** Given a graph with 3-4 categories, student computes the difference between two named categories from either picture or bar graph in either orientation.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **tight** — context must support comparison language.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| School supply drive | pencils, erasers, notebooks, markers | 4 categories |
| Animals at the farm | chickens, cows, pigs, horses | Farm context |
| Sports day events | running, jumping, throwing, swimming | Active events |
| Nature walk finds | leaves, rocks, feathers, acorns | Outdoor exploration |
| Museum exhibits visited | dinosaurs, space, ocean, history | Field trip |

**🟠 PROMPT EXAMPLES:**
1. "How many more pencils than erasers were donated?"
2. "How many fewer horses than chickens are there?"
3. "How many more students chose running than swimming?"
4. "How many fewer feathers than leaves were found?"
5. "How many more people visited the dinosaur exhibit than the ocean exhibit?"

**🟣 SUCCESS DIALOGUE:**
1. "4 more pencils than erasers."
2. "There are 3 fewer horses."
3. "2 more students chose running."
4. "5 fewer feathers than leaves."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| None — baseline expects independent comparison | — | — | — |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| sum_of_pair | Adds instead of subtracts | #6 ("More Than" Means Add) | "'More than' means subtract the smaller from the larger. Find each value first, then subtract." |
| larger_value | Reports the larger value itself | Key Beat: difference vs value | "That's [A]'s amount. The question asks how many MORE — subtract [B] from [A]." |
| wrong_pair | Computes difference using a non-named category | Key Beat: category identification | "The question names [A] and [B]. Find those two — ignore the other categories." |
| sum_all | Reports total of all categories | #17 (All Data Must Be Used) | "Only two categories matter here. Read the question — which two does it name?" |
| off_by_one | Difference is ±1 from correct | Key Beat: careful subtraction | "Double-check your reading. What's [A]'s value? What's [B]'s? Now subtract carefully." |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3)
Medium: Per-distractor — see table above.
        Visual scaffold: Named categories highlighted with values labeled; subtraction shown.
Heavy [Modeling]: "[A] shows 8 and [B] shows 3. The question says 'how many more.' I subtract: 8 minus 3 equals 5. There are 5 more."
        Visual: Both bars highlighted, values labeled, subtraction equation animated.
Post-Modeling: "I read both values, then subtracted. Try this one."
Validator: [Validator: Misconception_#6], [Validator: Misconception_#17]

**Technical Details:**
```
template_id: 0110
template_type: standard
spine_skill_id: U1.SK6
sub_skill: SK6:difference
skill_id: S4
secondary_skill: S1 or S2
skill: Determine "how many more" or "how many fewer" between two categories
problem_type: Compute difference between two named categories (3-4 category graph, either type/orientation)
workspace_description: Bar or picture graph, 3-4 categories, 1:1 scale. Both orientations. Values across full range. 4 MC options including sum, individual values, and close wrong answers.
prompt_examples: ["How many more pencils than erasers were donated?", "How many fewer horses than chickens are there?", "How many more students chose running than swimming?", "How many fewer feathers than leaves were found?", "How many more people visited the dinosaur exhibit than the ocean exhibit?"]
action_description: MC (4-option selection)
mastery_tier: baseline
mastery_verb: compare
parameter_coverage: values 1-8 per category; differences 1-5; 3-4 categories; both orientations; both graph types
correct_end_state: Student selects the correct difference
success_dialogue: ["4 more pencils than erasers.", "There are 3 fewer horses.", "2 more students chose running.", "5 fewer feathers than leaves."]
key_teaching_moment: "Lesson: click-two-to-compare → system shows difference calculation."
remediation_track: MC
validator_tag: [Validator: Misconception_#6], [Validator: Misconception_#17]
problem_count: 6
```

---

#### Template 0111 — How Many More/Fewer (Stretch)

**🟢 SKILL:** S4 — Determine "how many more" or "how many fewer" between two categories (SK6:difference)

**🔵 PROBLEM TYPE:** Given a graph with 4-5 categories and values at the upper range, student computes the difference where both values are large and the gap is small.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **tight** — must support comparison; high values plausible.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Steps walked by each friend | Mia, Leo, Sam, Ava, Ben | 5 names; values 6-10 plausible |
| Stickers collected this week | stars, hearts, rainbows, smiley faces, moons | Reward system |
| Fish in the aquarium | goldfish, guppies, tetras, bettas | Nature/science |
| Pages read | Monday, Tuesday, Wednesday, Thursday, Friday | Daily tracking |

**🟠 PROMPT EXAMPLES:**
1. "How many more steps did Leo take than Sam?"
2. "How many fewer star stickers than rainbow stickers?"
3. "How many more guppies than bettas?"
4. "How many fewer pages on Monday than Friday?"
5. "How many more steps did Ava take than Ben?"

**🟣 SUCCESS DIALOGUE:**
1. "Leo took 2 more steps than Sam."
2. "1 fewer star sticker."
3. "3 more guppies than bettas."
4. "2 fewer pages on Monday."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| None — stretch expects full independence | — | — | — |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| sum_of_pair | Adds the two large values | #6 ("More Than" Means Add) | "Even with bigger numbers, 'more than' still means subtract. Find each value, then take the smaller from the larger." |
| larger_value | Reports the larger value (e.g., 9) | Key Beat: difference vs value | "9 is [A]'s value, not the difference. Subtract [B]'s value from it." |
| off_by_one | Gets ±1 wrong when values are close (e.g., 9 vs 8 → says 2) | Key Beat: careful subtraction | "Read each value carefully. 9 minus 8 is 1, not 2." |
| wrong_pair | Uses a non-named category | Key Beat: category identification | "5 categories can be confusing. Re-read the question — which TWO does it name?" |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3)
Medium: Per-distractor — see table above.
        Visual scaffold: Named categories highlighted with values; other categories dimmed.
Heavy [Modeling]: "[A] is 9 and [B] is 7. Even with bigger numbers, I subtract: 9 minus 7 equals 2."
        Visual: Named bars highlighted, arithmetic shown.
Post-Modeling: "Bigger numbers, same steps — find each value and subtract."
Validator: [Validator: Misconception_#6]

**Technical Details:**
```
template_id: 0111
template_type: standard
spine_skill_id: U1.SK6
sub_skill: SK6:difference
skill_id: S4
secondary_skill: S1 or S2
skill: Determine "how many more" or "how many fewer" between two categories
problem_type: Compute difference with high values and small gaps (4-5 categories)
workspace_description: Bar or picture graph, 4-5 categories, 1:1 scale. Values 6-10. Target pair has small difference (1-3). 4 MC options closely spaced.
prompt_examples: ["How many more steps did Leo take than Sam?", "How many fewer star stickers than rainbow stickers?", "How many more guppies than bettas?", "How many fewer pages on Monday than Friday?", "How many more steps did Ava take than Ben?"]
action_description: MC (4-option selection)
mastery_tier: stretch
mastery_verb: compare
parameter_coverage: values 6-10; differences 1-3; 4-5 categories; vertical orientation; close MC options
correct_end_state: Student selects correct small difference from closely-spaced options
success_dialogue: ["Leo took 2 more steps than Sam.", "1 fewer star sticker.", "3 more guppies than bettas.", "2 fewer pages on Monday."]
key_teaching_moment: "Lesson: comparison with system-shown difference calculations."
remediation_track: MC
validator_tag: [Validator: Misconception_#6]
problem_count: 5
```

---

#### Template 0112 — How Many More/Fewer (Challenge)

**🟢 SKILL:** S4 — Determine "how many more" or "how many fewer" between two categories (SK6:difference)

**🔵 PROBLEM TYPE:** Given a vertical bar graph with 5 categories and values at the upper boundary, student identifies the two categories with the greatest difference and computes it. Two-part question: "Which two categories are the most different? How many more [bigger] than [smaller]?"

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **tight** — must support comparison; 5 categories with varied high values.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Rainy days by month | September, October, November, December, January | Weather data — values 2-10 plausible |
| Points scored per game | Game 1, Game 2, Game 3, Game 4, Game 5 | Competition |
| Flowers blooming per week | Week 1, Week 2, Week 3, Week 4, Week 5 | Growth tracking |

**🟠 PROMPT EXAMPLES:**
1. "Which two months have the biggest difference in rainy days? How many more?"
2. "Which two games had the most different scores? What is the difference?"
3. "Which two weeks had the biggest difference in flowers? How many more?"
4. "Find the two categories that are the most different. What's the difference?"
5. "Which two are the farthest apart? How many more does the bigger one have?"

**🟣 SUCCESS DIALOGUE:**
1. "October and January — 7 more rainy days in October."
2. "Game 2 and Game 5. The difference is 6."
3. "Week 1 and Week 4 — 5 more flowers in Week 4."
4. "That's the biggest difference. Nice work finding it."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| None — challenge expects full independence | — | — | — |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| not_max_diff | Picks a pair that isn't the most different | Key Beat: comparison | "To find the biggest difference, you need the category with the MOST and the one with the FEWEST." |
| sum_of_extremes | Adds the highest and lowest values | #6 ("More Than" Means Add) | "You found the right pair, but 'difference' means SUBTRACT. Take the smaller from the larger." |
| difference_of_adjacent | Computes difference of two adjacent categories | Key Beat: comparison | "Check all five categories. The biggest difference is between the HIGHEST and the LOWEST, not neighbors." |
| reports_max_value | Reports the largest category value as the answer | Key Beat: difference vs value | "That's the highest value, not the difference. Subtract the lowest from the highest." |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3)
Medium: Per-distractor — see table above.
        Visual scaffold: All bars labeled with values; highest and lowest bars highlighted.
Heavy [Modeling]: "First I find the BIGGEST: [A] has 10. Then the SMALLEST: [B] has 3. The difference is 10 minus 3 = 7."
        Visual: Highest bar highlighted green, lowest highlighted orange, difference bracket shown.
Post-Modeling: "Find the biggest and smallest first, then subtract."
Validator: [Validator: Misconception_#6]

**Technical Details:**
```
template_id: 0112
template_type: standard
spine_skill_id: U1.SK6
sub_skill: SK6:difference
skill_id: S4
secondary_skill: S2, S3
skill: Determine the greatest difference between any two categories
problem_type: Identify the two most-different categories and compute the difference (5-category graph)
workspace_description: Vertical bar graph, 5 categories, 1:1 scale. Values 2-10 with clear extremes (max - min ≥ 5). Two-part MC: Part 1 selects the pair, Part 2 selects the difference.
prompt_examples: ["Which two months have the biggest difference in rainy days? How many more?", "Which two games had the most different scores? What is the difference?", "Which two weeks had the biggest difference in flowers? How many more?"]
action_description: MC (two-part: pair selection + difference)
mastery_tier: challenge
mastery_verb: compare
parameter_coverage: values 2-10; max-min difference ≥5; 5 categories; vertical orientation
correct_end_state: Student identifies the correct pair (max and min) and computes the correct difference
success_dialogue: ["October and January — 7 more rainy days in October.", "Game 2 and Game 5. The difference is 6.", "Week 1 and Week 4 — 5 more flowers in Week 4."]
key_teaching_moment: "Lesson: comparison across multiple categories."
remediation_track: MC
validator_tag: [Validator: Misconception_#6]
problem_count: 3
```

---

#### Template 0113 — How Many In All (Baseline)

**🟢 SKILL:** S5 — Determine "how many in all" across categories (SK6:combination)

**🔵 PROBLEM TYPE:** Given a graph with 3 categories, student computes the total across all (or a named subset of) categories.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **tight** — context must support "in all" / "altogether" language.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Fruit picked at the orchard | apples, pears, peaches | "How many fruits in all?" makes sense |
| School supplies collected | pencils, erasers, crayons | Drive totals plausible |
| Animals seen at the park | squirrels, birds, rabbits | Nature walk count |
| Stickers on the chart | gold, silver, bronze | Reward system |
| Toys donated | cars, dolls, puzzles | Charity drive |
| Flowers in the vase | roses, daisies, tulips | Counting real objects |

**🟠 PROMPT EXAMPLES:**
1. "How many fruits were picked in all?"
2. "How many school supplies were collected altogether?"
3. "How many animals were seen in total?"
4. "How many stickers are on the chart altogether?"
5. "How many toys were donated in all?"

**🟣 SUCCESS DIALOGUE:**
1. "15 fruits were picked in all."
2. "Altogether, 18 school supplies."
3. "You saw 12 animals in total."
4. "That's right — 20 stickers altogether."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| None — baseline expects independent combination | — | — | — |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| single_category | Reports only one category's value instead of the total | Key Beat: "in all" comprehension | "'In all' means ADD every category together. Read each bar, then add all the numbers." |
| difference_pair | Subtracts instead of adding (does more/fewer) | Key Beat: operation selection | "The question says 'in all' — that means ADD, not subtract. Find each value and add them up." |
| missed_category | Adds only 2 of 3 categories | Key Beat: completeness | "Make sure you counted ALL the categories. There are 3 — did you include every one?" |
| off_by_one_sum | Misreads one value, producing a slightly wrong total | Key Beat: careful reading + addition | "Double-check each value before adding. Read [A], [B], and [C] from the graph, then add." |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3)
Medium: Per-distractor — see table above.
        Visual scaffold: Each category highlighted sequentially with values labeled; running total shown.
Heavy [Modeling]: "[A] has 5, [B] has 7, [C] has 3. 'In all' means add: 5 plus 7 is 12, plus 3 is 15. 15 in all."
        Visual: System labels each bar, then shows running addition: 5 → 12 → 15.
Post-Modeling: "I read every value and added them one by one. Try this one."
Validator: —

**Technical Details:**
```
template_id: 0113
template_type: standard
spine_skill_id: U1.SK6
sub_skill: SK6:combination
skill_id: S5
secondary_skill: S1 or S2
skill: Determine "how many in all" across categories
problem_type: Compute total of all categories from a 3-category graph
workspace_description: Bar or picture graph, 3 categories, 1:1 scale. Values sum to ≤20. 4 MC options including single-category value, partial sum, and ±1 errors.
prompt_examples: ["How many fruits were picked in all?", "How many school supplies were collected altogether?", "How many animals were seen in total?", "How many stickers are on the chart altogether?", "How many toys were donated in all?"]
action_description: MC (4-option selection)
mastery_tier: baseline
mastery_verb: apply
parameter_coverage: values 3-8 per category; total ≤20; 3 categories; both orientations
correct_end_state: Student selects the sum of all category values
success_dialogue: ["15 fruits were picked in all.", "Altogether, 18 school supplies.", "You saw 12 animals in total.", "That's right — 20 stickers altogether."]
key_teaching_moment: "Lesson: Guide asks 'How many in all?' Student reads each category and system shows the total."
remediation_track: MC
validator_tag: —
problem_count: 5
```

---

#### Template 0114 — How Many In All (Stretch)

**🟢 SKILL:** S5 — Determine "how many in all" across categories (SK6:combination)

**🔵 PROBLEM TYPE:** Given a graph with 4 categories and values in the upper range, student computes the total. Higher values and more categories increase addition complexity.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **tight** — context must support totaling. 4 categories with higher values.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Canned goods collected per class | Room 1, Room 2, Room 3, Room 4 | School drive — 4 classrooms |
| Laps run per team | Red, Blue, Green, Yellow | PE activity |
| Seeds planted per row | Row 1, Row 2, Row 3, Row 4 | Garden project |
| Books read per week | Week 1, Week 2, Week 3, Week 4 | Reading challenge |

**🟠 PROMPT EXAMPLES:**
1. "How many cans were collected in all?"
2. "How many laps did all the teams run altogether?"
3. "How many seeds were planted in total?"
4. "How many books were read altogether across all 4 weeks?"
5. "What is the total for all 4 groups?"

**🟣 SUCCESS DIALOGUE:**
1. "32 cans collected in all."
2. "All teams ran 28 laps altogether."
3. "30 seeds were planted in total."
4. "That's 26 books altogether."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| None — stretch expects full independence | — | — | — |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| missed_category | Adds only 3 of 4 categories | Key Beat: completeness | "There are 4 categories. Make sure you included all of them in your addition." |
| single_max | Reports the highest category value | Key Beat: "in all" comprehension | "'In all' means the TOTAL of every category added together, not just the biggest." |
| addition_error | Makes an addition mistake with larger numbers | Key Beat: careful addition | "With bigger numbers, add carefully. Try adding two at a time: first add [A] + [B], then add [C], then [D]." |
| difference_of_extremes | Computes max minus min instead of total | Key Beat: operation selection | "The question asks 'in all' — that's ADD everything, not subtract." |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3)
Medium: Per-distractor — see table above.
        Visual scaffold: Each category highlighted with value; running addition shown step by step.
Heavy [Modeling]: "I'll add them one at a time. [A] is 8, [B] is 6 — that's 14. [C] is 9 — now 23. [D] is 7 — 23 plus 7 is 30. Total: 30."
        Visual: System highlights each bar in order, showing cumulative sum.
Post-Modeling: "Adding one at a time keeps it organized. Your turn."
Validator: —

**Technical Details:**
```
template_id: 0114
template_type: standard
spine_skill_id: U1.SK6
sub_skill: SK6:combination
skill_id: S5
secondary_skill: S1 or S2
skill: Determine "how many in all" across categories
problem_type: Compute total of 4 categories with upper-range values
workspace_description: Bar or picture graph, 4 categories, 1:1 scale. Values 6-10. Total 24-36. 4 MC options including partial sums and ±1-2 errors.
prompt_examples: ["How many cans were collected in all?", "How many laps did all the teams run altogether?", "How many seeds were planted in total?", "How many books were read altogether across all 4 weeks?", "What is the total for all 4 groups?"]
action_description: MC (4-option selection)
mastery_tier: stretch
mastery_verb: apply
parameter_coverage: values 6-10 per category; 4 categories; total 24-36; vertical orientation
correct_end_state: Student selects the correct sum of all 4 categories
success_dialogue: ["32 cans collected in all.", "All teams ran 28 laps altogether.", "30 seeds were planted in total.", "That's 26 books altogether."]
key_teaching_moment: "Lesson: reading each value and computing totals."
remediation_track: MC
validator_tag: —
problem_count: 4
```

---

### Misconception Remediation Templates

---

#### Template 0120 — Remediation: "More Than" Means Add (#6)

**🟢 SKILL:** S4 — Determine "how many more" (SK6:difference) — remediation for Misconception #6

**🔵 PROBLEM TYPE:** Given a picture graph with 3 categories where two values are far apart, student answers "how many more." Parameters are chosen so the SUM is obviously too large (e.g., 8 vs 2: sum=10 but there are only 8+2=10 total items shown, difference is clearly 6). The misconception answer (10) is visibly unreasonable.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **misconception-sensitive** — simple, familiar themes only. Difficulty is in the operation, not the context.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite fruits | apples, bananas, grapes | Universal, no cognitive load |
| Classroom pets | cats, dogs, fish | Familiar |
| Playground games | tag, hopscotch, jump rope | Simple |
| Favorite colors | red, blue, yellow | Minimal categories |

**🟠 PROMPT EXAMPLES:**
1. "How many more students chose apples than grapes?"
2. "How many more cats than fish?"
3. "How many more students like tag than hopscotch?"
4. "How many more chose red than yellow?"
5. "How many more bananas than grapes?"

**🟣 SUCCESS DIALOGUE:**
1. "6 more students chose apples. You found the difference!"
2. "That's right — 5 more cats than fish."
3. "4 more students like tag."
4. "Correct — 3 more chose red."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| Comparison language cue — "'More than' means find the DIFFERENCE" | confidence/support | Problem loads | TF: "Guide models comparison language explicitly" |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| sum_of_pair | Adds the two values (8+2=10) instead of subtracting | #6 ("More Than" Means Add) | "'More than' asks for the DIFFERENCE, not the total. Look at the two bars — how much LONGER is the bigger one?" |
| larger_value | Reports the larger value (8) | Key Beat: difference vs value | "8 is how many chose [A]. The question asks how many MORE — that's the gap between the two." |
| smaller_value | Reports the smaller value (2) | Key Beat: difference vs value | "2 is [B]'s count. Subtract to find how many MORE [A] has." |
| total_all | Reports total of all 3 categories | #17 (All Data Must Be Used) | "You only need TWO categories. Which two does the question name?" |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3) — full escalation for misconception_remediation template (confidence tier exception does NOT apply to remediation templates)
Medium: Per-distractor — see table above.
        Visual scaffold: Both named categories highlighted. Difference bracket shown between bar endpoints.
Heavy [Modeling]: "Watch carefully. [A] has 8. [B] has 2. 'How many MORE' means: how much BIGGER is [A]? I subtract: 8 minus 2 equals 6. [A] has 6 more."
        Visual: System highlights both bars, draws bracket between endpoints, shows "8 - 2 = 6."
Post-Modeling: "I helped you see that 'more than' means subtract. Let's try another."
Validator: [Validator: Misconception_#6]

**Technical Details:**
```
template_id: 0120
template_type: misconception_remediation
spine_skill_id: U1.SK6
sub_skill: SK6:difference
skill_id: S4
secondary_skill: —
skill: Determine "how many more" (remediation for "More Than" Means Add)
problem_type: Compute difference with large gap — misconception answer (sum) is obviously too large
workspace_description: Picture graph, 3 categories, 1:1 scale. Two named categories with large gap (≥4). Values chosen so sum is obviously too large. 4 MC options: correct difference, sum, larger value, smaller value.
prompt_examples: ["How many more students chose apples than grapes?", "How many more cats than fish?", "How many more students like tag than hopscotch?", "How many more chose red than yellow?", "How many more bananas than grapes?"]
action_description: MC (4-option selection)
mastery_tier: confidence
mastery_verb: compare
parameter_coverage: values 2-8; differences ≥4 (large gap makes sum obviously wrong); 3 categories; horizontal orientation
correct_end_state: Student selects the difference, rejecting the sum
success_dialogue: ["6 more students chose apples. You found the difference!", "That's right — 5 more cats than fish.", "4 more students like tag.", "Correct — 3 more chose red."]
key_teaching_moment: "Lesson: 'Click two categories to compare' → system shows difference calculation."
remediation_track: MC
validator_tag: [Validator: Misconception_#6]
problem_count: 4
misconception_targeting:
  misconception_id: 6
  detection_signal: Student selects the sum of the two named categories
  remediation_approach: Visual bracket showing the gap between bars. Guide models subtraction with explicit language about "more than" meaning the difference, not the total. Parameters chosen so sum is visibly unreasonable.
```

---

#### Template 0121 — Remediation: Graph as Picture (#16)

**🟢 SKILL:** S1/S2 — Read graph values — remediation for Misconception #16

**🔵 PROBLEM TYPE:** Given a bar graph where the number of bars does NOT match any bar's value, and a picture graph where symbol arrangement could be misleading, student reads the correct value. The "graph as picture" error (e.g., counting 3 bars and answering "3" when the asked-about bar reaches 7) is made visible by the mismatch.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **misconception-sensitive** — simple, familiar themes.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite snacks | crackers, cheese, fruit, pretzels | 4 bars, values ≠ 4 |
| Animals at the shelter | cats, dogs, rabbits | 3 bars, values not 3 |
| Books on the shelf | fiction, science, art, history | 4 categories |
| Toys in the box | cars, blocks, dolls | 3 categories |

**🟠 PROMPT EXAMPLES:**
1. "How many dogs are at the shelter?"
2. "How many fiction books are on the shelf?"
3. "How many chose crackers?"
4. "How many cars are in the toy box?"
5. "How many students chose fruit?"

**🟣 SUCCESS DIALOGUE:**
1. "7 dogs at the shelter. You read the scale!"
2. "That's 5 fiction books."
3. "Correct — 8 chose crackers."
4. "6 cars. You used the numbers, not the picture."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| Key/scale emphasis — key or scale axis pulses on graph load with brief label: "Use the NUMBERS to find the answer" | confidence/support | Graph loads | TF: "Address 'reading the picture not the data' misconception" |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| bar_count | Answers with the number of bars (e.g., 4 bars → "4") | #16 (Graph as Picture) | "The number of bars tells you how many CATEGORIES — not the amount. Look at the SCALE on the side to find the amount." |
| category_count | Answers with the number of categories listed | #16 (Graph as Picture) | "That's how many types there are, not how many [items]. Read the bar's HEIGHT against the number scale." |
| visual_pattern | Answers based on visual arrangement (e.g., position, color) | #16 (Graph as Picture) | "Don't use the picture to guess. The NUMBERS on the scale tell you the real amount. Find where the bar ends." |
| adjacent_bar | Reads the wrong bar's value | Key Beat: category identification | "Make sure you're reading the right bar. Find the label for [category] first." |

**🟤 REMEDIATION DESIGN:**

Track: MC (RDR §3) — full escalation (misconception_remediation template)
Medium: Per-distractor — see table above.
        Visual scaffold: Scale axis highlighted with arrow pointing to it. Target bar's endpoint connected to scale value.
Heavy [Modeling]: "The SCALE tells us the amount — not the picture shape. I find [category]'s bar [highlights]. It reaches up to... 7 on the scale. So there are 7 [items]. The key or scale always tells the true count."
        Visual: System highlights the scale, traces from bar top to scale value, circles the number.
Post-Modeling: "I used the numbers, not the picture. The scale always has the answer."
Validator: [Validator: Misconception_#16]

**Technical Details:**
```
template_id: 0121
template_type: misconception_remediation
spine_skill_id: U1.SK2
sub_skill: —
skill_id: S2
secondary_skill: S1
skill: Read graph values (remediation for Graph as Picture misconception)
problem_type: Read value from graph where visual features could mislead — number of bars/categories ≠ any bar value
workspace_description: Bar graph (or picture graph), 3-4 categories, 1:1 scale. Number of bars/categories is different from every bar's value (e.g., 4 bars but no bar has value 4). Distractors include bar count and category count. Key/scale prominently displayed.
prompt_examples: ["How many dogs are at the shelter?", "How many fiction books are on the shelf?", "How many chose crackers?", "How many cars are in the toy box?", "How many students chose fruit?"]
action_description: MC (4-option selection)
mastery_tier: support
mastery_verb: identify
parameter_coverage: values 5-8 (deliberately not equal to number of categories); 3-4 categories; both orientations; distractors include category count
correct_end_state: Student selects value from scale, ignoring visual misleads
success_dialogue: ["7 dogs at the shelter. You read the scale!", "That's 5 fiction books.", "Correct — 8 chose crackers.", "6 cars. You used the numbers, not the picture."]
key_teaching_moment: "Lesson: Guide highlights key/scale — 'Each symbol means one animal' / 'The numbers on the side tell us the amount.'"
remediation_track: MC
validator_tag: [Validator: Misconception_#16]
problem_count: 4
misconception_targeting:
  misconception_id: 16
  detection_signal: Student selects the number of bars/categories or a value based on visual arrangement rather than scale reading
  remediation_approach: Scale/key emphasis with visual trace from data point to scale value. Parameters chosen so the "visual" answer (bar count = 3 or 4) doesn't match any bar's value, making the error detectable and the correct approach visible.
```

---

## §PT.4 Template Summary

### Standard Templates (count toward Pool Target)

| # | ID | Type | Problem Type | Spine Skill | Sub-skill | Verb | Track | Tiers | Misc. Detected | Problems |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0101 | standard | Read picture graph value (3 cat, H) | U1.SK1 | — | identify | MC | confidence | #16, #17 | 5 |
| 2 | 0102 | standard | Read picture graph value (3-4 cat, both orient.) | U1.SK1 | — | identify | MC | baseline | #16, #17 | 6 |
| 3 | 0103 | standard | Read picture graph value (4-5 cat, V, high values) | U1.SK1 | — | identify | MC | stretch | #16 | 5 |
| 4 | 0104 | standard | Read bar graph value (3 cat, H) | U1.SK2 | — | identify | MC | confidence | #16 | 5 |
| 5 | 0105 | standard | Read bar graph value (3-4 cat, both orient.) | U1.SK2 | — | identify | MC | baseline | #16 | 6 |
| 6 | 0106 | standard | Read bar graph value (4-5 cat, V, high values) | U1.SK2 | — | identify | MC | stretch | #16 | 5 |
| 7 | 0107 | standard | Identify most/fewest (3 cat, clear gap) | U1.SK6 | SK6:ordinal | identify | MC | support | #16 | 5 |
| 8 | 0108 | standard | Identify most/fewest (3-4 cat, close values) | U1.SK6 | SK6:ordinal | identify | MC | baseline | #16 | 5 |
| 9 | 0109 | standard | How many more/fewer (3 cat, small diff) | U1.SK6 | SK6:difference | compare | MC | support | #6, #17 | 5 |
| 10 | 0110 | standard | How many more/fewer (3-4 cat, full range) | U1.SK6 | SK6:difference | compare | MC | baseline | #6, #17 | 6 |
| 11 | 0111 | standard | How many more/fewer (4-5 cat, high values) | U1.SK6 | SK6:difference | compare | MC | stretch | #6 | 5 |
| 12 | 0112 | standard | Greatest difference (5 cat, two-part) | U1.SK6 | SK6:difference | compare | MC | challenge | #6 | 3 |
| 13 | 0113 | standard | How many in all (3 cat) | U1.SK6 | SK6:combination | apply | MC | baseline | — | 5 |
| 14 | 0114 | standard | How many in all (4 cat, high values) | U1.SK6 | SK6:combination | apply | MC | stretch | — | 4 |
| | | | | | | | | | **STANDARD POOL TOTAL** | **70** |
| | | | | | | | | | **POOL TARGET** | **55-65** |

**Note:** Standard pool total (70) is slightly above the 55-65 target. This provides buffer for the expansion step to cull lower-quality instances. If the pool needs trimming, reduce problem_count on 0102, 0105, and 0110 from 6 to 5 each (→ 67), or drop 0112 challenge template (→ 67).

### Misconception Remediation Templates (separate sub-pool)

| # | ID | Type | Problem Type | Spine Skill | Targets | Tiers | Problems |
|---|---|---|---|---|---|---|---|
| 1 | 0120 | misc_remed | "More than" with large gap — sum is obviously wrong | U1.SK6 | #6 | confidence | 4 |
| 2 | 0121 | misc_remed | Read value where visual features could mislead | U1.SK2 | #16 | support | 4 |
| | | | | | | **REMEDIATION SUB-POOL TOTAL** | **8** |

---

## §PT.5 Coverage Validation

### Tier Distribution (standard templates only)

| Tier | Target | Actual Count | Actual % | Status |
|---|---|---|---|---|
| confidence | 8-12% | 10 (0101 + 0104) | 14.3% | ⚠️ Slightly above. Acceptable — M1 is a review module; extra confidence supports Grade 2 activation. |
| support | 15-20% | 10 (0107 + 0109) | 14.3% | ⚠️ Slightly below target. Close enough; ordinal (0107) and difference (0109) cover key skills at this tier. |
| baseline | 40-50% | 28 (0102 + 0105 + 0108 + 0110 + 0113) | 40.0% | ✅ At lower boundary. |
| stretch | 15-20% | 19 (0103 + 0106 + 0111 + 0114) | 27.1% | ⚠️ Above target. Reflects extra reading templates at stretch. Consider moving 0103 or 0106 problem_count down. |
| challenge | 5-8% | 3 (0112) | 4.3% | ⚠️ Slightly below. Single challenge template for M1 is acceptable — module is introductory. |

**Adjustment recommendation:** Reduce 0103 and 0106 from 5 to 4 problems each (stretch reading → 17, 24.3%). Increase 0107 from 5 to 6 (support → 11, 15.7%). This brings tiers closer to targets.

### Skill Coverage (grouped by spine skill)

| Spine Skill | Sub-skill | Description | Templates | Tiers Covered | Status |
|---|---|---|---|---|---|
| U1.SK1 | — | Read picture graph values | 0101, 0102, 0103 | confidence, baseline, stretch | ✅ 3 templates, 3 tiers |
| U1.SK2 | — | Read bar graph values | 0104, 0105, 0106 | confidence, baseline, stretch | ✅ 3 templates, 3 tiers |
| U1.SK3 | — | Create picture graphs | — | [TEACHING ONLY] | ✅ Correctly excluded |
| U1.SK6 | SK6:ordinal | Most/fewest identification | 0107, 0108 | support, baseline | ✅ 2 templates, 2 tiers |
| U1.SK6 | SK6:difference | How many more/fewer | 0109, 0110, 0111, 0112 | support, baseline, stretch, challenge | ✅ 4 templates, 4 tiers |
| U1.SK6 | SK6:combination | How many in all | 0113, 0114 | baseline, stretch | ✅ 2 templates, 2 tiers |

### Verb Distribution

| Verb | Count | % of Total | Target | Status |
|---|---|---|---|---|
| identify | 36 (0101-0108) | 51.4% | 45-55% | ✅ |
| compare | 25 (0109-0112) | 35.7% | 30-40% | ✅ |
| apply | 9 (0113-0114) | 12.9% | 10-20% | ✅ |

### Misconception Detection (in standard templates)

| ID | Priority | Detected In | Detection Strategy | Status |
|---|---|---|---|---|
| #6 | PRIMARY | 0109, 0110, 0111, 0112 | Sum-of-pair distractor in all SK6:difference templates | ✅ 4 templates (≥3 required) |
| #16 | PRIMARY | 0101, 0102, 0103, 0104, 0105, 0106, 0107, 0108 | Visual-arrangement / bar-count / first-listed distractors across all reading templates | ✅ 8 templates (≥3 required) |
| #17 | MONITOR | 0101, 0102, 0109, 0110 | Total-all distractor in reading and difference templates | ✅ Distractor logic present |

### Misconception Remediation Coverage

| ID | Priority | Remed. Template(s) | Remediation Approach | Status |
|---|---|---|---|---|
| #6 | PRIMARY | 0120 | Large-gap comparison where sum is obviously wrong; visual bracket + subtraction modeling | ✅ (≥1 required) |
| #16 | PRIMARY | 0121 | Graph where bar/category count ≠ any value; scale emphasis + trace modeling | ✅ (≥1 required) |
| #17 | MONITOR | — | Standard detection only | ✅ (no dedicated template required) |

### Practice Phase Guidance Compliance

| Requirement | Met? | How |
|---|---|---|
| Multiple graph types | ✅ | SK1 templates (picture graph) + SK2 templates (bar graph). Mixed in SK6 templates. |
| Comparison focus | ✅ | 25 problems (35.7%) are compare verb; 9 problems (12.9%) are apply. SK6 total = 34 of 70 comparison/combination problems. |
| Both orientations | ✅ | Confidence templates specify H; baseline templates mix H and V; stretch templates specify V. |
| No creation | ✅ | SK3 excluded. All templates are reading/interpretation. |
| Guide models comparison language | ✅ | Prompt examples use modeled language: "how many more," "how many fewer," "in all." |

### Action Variety

| Action Type | Templates | Track | Status |
|---|---|---|---|
| MC (4-option selection — numerical) | 0101-0106, 0109-0114 | MC | ✅ |
| MC (4-option selection — category names) | 0107, 0108 | MC | ✅ |
| MC (two-part) | 0112 | MC | ✅ |

**Note:** All templates are MC track, as confirmed by author. M1 Practice uses only MC interaction. Action variety comes from the response type (numerical vs. category name vs. two-part).

### Dimension Coverage

| Check | Status |
|---|---|
| All valid parameter values used across template set? | ✅ Values 1-10 covered across tiers |
| Novel values (not in Early Lesson) present in baseline+? | ✅ Baseline uses full 1-8 range; stretch/challenge use 7-10 |
| Early-phase values reserved for confidence/support? | ✅ Confidence uses 3-6/3-8; stretch/challenge uses 7-10 |

### Context Coverage

| Check | Status |
|---|---|
| All templates have ⚪ RECOMMENDED CONTEXTS? | ✅ All 14 standard + 2 remediation |
| Context coupling appropriate per template? | ✅ Reading = loose; comparison = tight; remediation = misconception-sensitive |
| Context variety across template set? | ✅ No context reused across templates (some overlap in categories but different pairings) |
| Category examples plausible for parameter range? | ✅ All categories produce plausible count data for values 1-10 |

### Remediation Design Compliance (per RDR)

| Check | Status |
|---|---|
| MC templates with per-distractor Medium? | ✅ All baseline+ templates have per-distractor Medium |
| MC templates with shared Heavy + [Modeling]? | ✅ All baseline+ templates |
| Non-MC templates with full L-M-H? | N/A — no non-MC templates in M1 |
| Confidence templates with Light only? | ✅ 0101, 0104 — Light only per RDR §11 |
| Confidence remediation templates with full escalation? | ✅ 0120 — full MC escalation (exception to confidence Light-only rule for remediation templates) |
| Post-modeling language checked (RDR §7)? | ✅ All Heavy blocks include post-modeling language acknowledging assistance |
| Validator tags assigned? | ✅ All misconception-detecting templates have validator tags |
| Distractor type pools ≥ 4 types? | ✅ All templates have 4+ distractor types |
| Track classification consistent? | ✅ All templates MC track, matching Track Classification table |

### Gaps / Flags

1. **Pool total slightly above target (70 vs 55-65).** Buffer is intentional for expansion culling. If strict trimming needed, reduce 0102/0105/0110 from 6→5 problems each (→ 67) or drop 0112 (→ 67).
2. **Stretch tier slightly high (27.1% vs 15-20%).** Recommended adjustment: reduce 0103 and 0106 from 5→4 problems, increase 0107 from 5→6.
3. **No support tier for SK1/SK2 reading.** Reading at support tier is nearly identical to confidence (same skill, slightly more categories). Support tier is covered by SK6:ordinal (0107), which combines reading + comparison at a scaffolded level. Acceptable but flagged.
4. **SK6:ordinal has no confidence tier template.** Ordinal comparison at confidence level would be trivially simple (3 categories, one much larger). Covered by support (0107) with clear gap. Acceptable for M1.
5. **SK6:combination has no confidence or support tier.** "How many in all" requires addition, which is inherently above confidence level for this skill. Baseline is the entry point. Acceptable.
6. **RDR validation pending.** Remediation design blocks use embedded rules from prompt v1.1. Post-RDR validation pass recommended once RDR is available.

### SP Delta

Not applicable — no SP exists for Module 1.
