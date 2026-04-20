# MODULE 1: Data Sense & 1:1 Graphs — Practice Templates

*Continues from §PT.0–PT.2 (Backbone). This file contains §PT.3 (Templates), §PT.4 (Summary), and §PT.5 (Validation).*

---

## §PT.3 Templates

### Standard Templates

---

#### Template 0101 — Read Picture Graph Value (Confidence)

**🟢 SKILL:** S1 — Read a specific value from a picture graph (1:1 scale)

**🔵 PROBLEM TYPE:** Given a horizontal picture graph with 3 categories, student reads a specific category's value.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — context is flavor; any countable-category survey theme works.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite fruits | apples, bananas, grapes, oranges, strawberries | Universal, high familiarity |
| Playground games | tag, hopscotch, jump rope, swings, hide-and-seek | Active play — engaging for Grade 2 |
| Favorite colors | red, blue, green, yellow, purple | Simple, no cultural assumptions |
| Classroom pets | fish, hamsters, turtles, birds | Common school experience |
| Favorite sports | soccer, basketball, swimming, running | Broad appeal |
| Snack choices | crackers, pretzels, fruit cups, cheese, yogurt | School-lunch familiar |

**🟠 PROMPT EXAMPLES:**
1. "How many students chose bananas?"
2. "How many votes did soccer get?"
3. "How many animals are cats?"
4. "How many students like red?"
5. "How many people picked pizza?"

**🟣 SUCCESS DIALOGUE:**
1. "6 students chose bananas."
2. "That's right — 4 votes for soccer."
3. "8 animals are cats. You read that from the graph."
4. "Correct. 5 students like red."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| Key emphasis pulse | confidence | Graph loads — key briefly pulses | SP §1.5.1: "Key on every graph" |
| Data Table cross-highlight | confidence | Student selects answer — system highlights matching table row | SP §1.5.3 |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| other_category_value | Reads a different category's value | Key Beat: Category identification (1.1) | "Find [category name] first, then count its symbols." |
| total_all | Adds all categories together | Key Beat: Selective reading (1.4) | "The question asks about one category, not all of them." |
| off_by_one | Miscounts symbols (±1) | Key Beat: Symbol counting (1.1) | "Count each symbol carefully. Start from the left." |
| visual_impression | Picks the largest/smallest value instead of named category | #16 | "Look for the name [category] first, then read its value." |

**🟤 REMEDIATION DESIGN:**

Track: MC — confidence tier `[Pedagogical_Override]` per RDR §11 confidence builder exception; overrides §3 MC no-Light rule.
Light only: "Count the symbols for [category name]." No Medium/Heavy — confidence tier.
Validator: —

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0101 |
| template_type | standard |
| skill_id | S1 |
| skill | Read a specific value from a picture graph (1:1 scale) |
| problem_type | Read a named category's value from a horizontal picture graph |
| workspace_description | Picture Graph (Mode 1: Reading). Horizontal orientation. 3 categories with varied contexts (favorite foods, animals, sports, etc.). Key: "Each [symbol] = 1 [item]." Values per category: 3, 4, 5, or 6. Data Table visible alongside. One category highlighted by the prompt. |
| action_description | Multiple choice (4 options: correct value + 3 other category values) |
| mastery_tier | confidence |
| mastery_verb | identify |
| parameter_coverage | Values: 3, 4, 5, 6. Categories: 3. Orientation: horizontal only. Graph type: picture graph only. Data Table: visible. |
| correct_end_state | Student selects the correct numerical value for the named category. |
| key_teaching_moment | Lesson 1.1–1.5: Count symbols in a row. Key always visible: "Each [symbol] = 1 [item]." Guide: "How many [symbols] are in that row?" |
| remediation_track | MC — confidence `[Pedagogical_Override]` per RDR §11; overrides §3 no-Light rule |
| validator_tag | — |
| problem_count | 6 |

---

#### Template 0102 — Read Picture Graph Value (Baseline)

**🟢 SKILL:** S1 — Read a specific value from a picture graph (1:1 scale)

**🔵 PROBLEM TYPE:** Given a picture graph (either orientation) with 3–4 categories, student reads a specific category's value.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — context is flavor; any countable-category survey theme works.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite seasons | spring, summer, fall, winter | 4 categories available; universal |
| Birds in the park | robins, sparrows, blue jays, ducks | Nature/outdoor theme |
| After-school activities | reading, drawing, biking, playing outside | Varied interests |
| Favorite drinks | water, juice, milk, lemonade | Simple, inclusive |
| Weekend activities | park, library, swimming, movies, biking | Engaging for Grade 2 |
| Garden flowers | sunflowers, tulips, daisies, roses | Observation/nature theme |

**🟠 PROMPT EXAMPLES:**
1. "How many students chose grapes?"
2. "How many votes did swimming get?"
3. "How many birds are in the park?"
4. "How many people picked winter?"
5. "How many students like green?"

**🟣 SUCCESS DIALOGUE:**
1. "7 students chose grapes."
2. "Right — 9 votes for swimming."
3. "3 birds. You read the graph."
4. "Correct. 8 people picked winter."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| Key emphasis pulse | baseline | Graph loads — key briefly pulses | SP §1.5.1 |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| visually_prominent | Selects value of the tallest/longest bar instead of named category | #16 | Highlight the named category label. "Find [category name] first. Now count its symbols." Visual: category label pulses. |
| other_category | Reads a different (non-prominent) category's value | Key Beat: Category identification (1.1) | "That's the value for [wrong category]. The question asks about [correct category]." |
| off_by_one | Miscounts symbols (±1 from correct) | Key Beat: Symbol counting (1.1) | "Count each symbol one at a time. How many do you get?" |
| adjacent_value | Selects value numerically close to correct but from no category | Key Beat: Precise reading (1.4) | "Check — does that number match any row on the graph?" |

**🟤 REMEDIATION DESIGN:**

Track: MC (per RDR §3)
Medium: Per-distractor — see Distractor Types table above.
        Visual scaffold: Named category label highlighted/pulsing. 20-30 words per RDR §5.
Heavy [Modeling]: "Let me show you. We're looking for [category]. Here it is — [highlights row]. Now count the symbols: 1, 2, 3... [count]. That's [value] [items]."
        Visual: System highlights category row, counts symbols with animation.
Post-Modeling: "That's how you read a picture graph — find the name, then count."
Validator: [Validator: Misconception_#16]

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0102 |
| template_type | standard |
| skill_id | S1 |
| skill | Read a specific value from a picture graph (1:1 scale) |
| problem_type | Read a named category's value from a picture graph (either orientation) |
| workspace_description | Picture Graph (Mode 1: Reading). Mixed orientation (horizontal or vertical). 3–4 categories. Key: "Each [symbol] = 1 [item]." Values per category: 3–8 range. Data Table NOT visible. MC distractors drawn from distractor type pool — must include one `visually_prominent` option (catches #16). |
| action_description | Multiple choice (4 options: correct value + 3 from distractor pool) |
| mastery_tier | baseline |
| mastery_verb | identify |
| parameter_coverage | Values: 3, 4, 5, 6, 7, 8. Categories: 3–4. Orientation: mixed. Graph type: picture graph. Data Table: hidden. |
| correct_end_state | Student selects the correct numerical value for the named category. |
| key_teaching_moment | Lesson 1.4–1.5: Read values from vertical/horizontal picture graphs. Guide: "Use the key — count the symbols." |
| remediation_track | MC (per RDR §3) |
| validator_tag | [Validator: Misconception_#16] |
| problem_count | 6 |

---

#### Template 0103 — Read Bar Graph Value (Confidence)

**🟢 SKILL:** S2 — Read a specific value from a bar graph (1:1 scale)

**🔵 PROBLEM TYPE:** Given a vertical bar graph with 3 categories, student reads a specific category's value.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — context is flavor; any countable-category theme works with bar graphs.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Books read this week | Maya, Leo, Priya | Name-based categories; relatable |
| Ways to get to school | walk, bus, car, bike | Transportation theme |
| Fruit picked at the farm | apples, peaches, strawberries | Seasonal/outdoor |
| Favorite animals | cats, dogs, birds, fish | High familiarity |
| Rainy day activities | puzzles, reading, drawing, building | Indoor play |
| Votes for class mascot | bear, owl, dolphin, fox | School community theme |

**🟠 PROMPT EXAMPLES:**
1. "How many books did Maya read?"
2. "How many votes did cats get?"
3. "How many students walk to school?"
4. "How many apples were picked?"
5. "How many people chose blue?"

**🟣 SUCCESS DIALOGUE:**
1. "Maya read 5 books."
2. "Right — 4 votes for cats."
3. "6 students walk to school."
4. "Correct. 3 apples were picked."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| Helping line animation | confidence | System fires on student's first bar click | SP §1.5.2; Lesson 2.1 |
| Data Table cross-highlight | confidence | Student selects answer — system highlights matching table row | SP §1.5.3 |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| other_category_value | Reads a different category's bar | Key Beat: Bar identification (2.1) | "Find the bar for [category name]. Where does it end on the scale?" |
| visual_impression | Picks tallest/shortest bar's value, not named category | #16 | "Look for [category name] at the bottom first." |
| off_by_one | Reads between tick marks or miscounts | Key Beat: Axis reading (2.1) | "Look where the bar ends — right at a tick mark." |
| axis_misread | Reads the axis number at the wrong position | Key Beat: Helping line technique (2.1) | "Trace from the top of the [category] bar straight across to the number." |

**🟤 REMEDIATION DESIGN:**

Track: MC — confidence tier `[Pedagogical_Override]` per RDR §11 confidence builder exception; overrides §3 MC no-Light rule.
Light only: "Find the bar for [category name]. Read the number on the side." No Medium/Heavy — confidence tier.
Validator: —

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0103 |
| template_type | standard |
| skill_id | S2 |
| skill | Read a specific value from a bar graph (1:1 scale) |
| problem_type | Read a named category's value from a vertical bar graph |
| workspace_description | Bar Graph (Mode 1: Reading). Vertical orientation. 3 categories. Axis 0–8 by 1s, tick marks at each whole number. Values per category: 3, 4, 5, or 6. Data Table visible alongside. |
| action_description | Multiple choice (4 options: correct value + 3 other category values) |
| mastery_tier | confidence |
| mastery_verb | identify |
| parameter_coverage | Values: 3, 4, 5, 6. Categories: 3. Orientation: vertical only. Graph type: bar graph. Data Table: visible. |
| correct_end_state | Student selects the correct numerical value for the named category. |
| key_teaching_moment | Lesson 2.1: System draws helping line from bar top to axis. Guide: "The HEIGHT of the bar tells us the amount." |
| remediation_track | MC — confidence `[Pedagogical_Override]` per RDR §11; overrides §3 no-Light rule |
| validator_tag | — |
| problem_count | 6 |

---

#### Template 0104 — Read Bar Graph Value (Baseline)

**🟢 SKILL:** S2 — Read a specific value from a bar graph (1:1 scale)

**🔵 PROBLEM TYPE:** Given a bar graph (either orientation) with 3–4 categories, student reads a specific category's value.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — context is flavor; any countable-category theme works with bar graphs.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite ice cream flavors | vanilla, chocolate, strawberry, mint | High engagement; 4 categories available |
| Animals at the shelter | dogs, cats, rabbits, birds | Community/caring theme |
| Books read by students | Aiden, Sofia, Marcus, Lily | Name-based; use diverse names |
| Favorite seasons | spring, summer, fall, winter | Universal |
| Things in the toy box | blocks, cars, dolls, puzzles, crayons | Familiar objects |
| Trees in the schoolyard | oak, maple, pine, birch | Nature/science connection |

**🟠 PROMPT EXAMPLES:**
1. "How many students picked fall?"
2. "How many books did Aiden read?"
3. "How many votes did soccer get?"
4. "How many dogs are at the shelter?"
5. "How many people chose vanilla?"

**🟣 SUCCESS DIALOGUE:**
1. "4 students picked fall."
2. "Aiden read 7 books."
3. "Right — 8 votes for soccer."
4. "5 dogs at the shelter."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| Axis tick marks visible | all | Always present per toy spec | SP §1.5.2 |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| tallest_bar_value | Selects value of tallest/longest bar instead of named category | #16 | Highlight named bar. "Look at [category]'s bar. Where does it end on the scale?" Visual: helping line animation from bar to axis. |
| other_category | Reads correct axis position but for wrong bar | Key Beat: Bar identification (2.1) | "That's the value for [wrong category]. Find the bar labeled [correct category]." |
| off_by_one | Reads between tick marks (±1) | Key Beat: Axis reading (2.1) | "Look exactly where the bar ends. It lines up with one of the numbers." Visual: helping line to axis. |
| axis_origin_error | Counts from 1 instead of reading axis value directly | Key Beat: Helping line technique (2.1) | "Read the number straight across from the top of the bar." |

**🟤 REMEDIATION DESIGN:**

Track: MC (per RDR §3)
Medium: Per-distractor — see Distractor Types table above.
        Visual scaffold: Helping line animation from named bar's top to axis value (SP §1.5.2). 20-30 words.
Heavy [Modeling]: "Let me show you. We need [category]'s value. Here's the [category] bar — [highlights]. I trace from the top straight across to the number scale: [value]. That's how many."
        Visual: System highlights bar, animates helping line to axis, circles the number.
Post-Modeling: "Now you've seen how to read the value from the scale."
Validator: [Validator: Misconception_#16]

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0104 |
| template_type | standard |
| skill_id | S2 |
| skill | Read a specific value from a bar graph (1:1 scale) |
| problem_type | Read a named category's value from a bar graph (either orientation) |
| workspace_description | Bar Graph (Mode 1: Reading). Mixed orientation. 3–4 categories. Axis 0–10 by 1s. Values per category: 3–8 range. Data Table NOT visible. MC distractors drawn from distractor pool — must include one `tallest_bar_value` option (catches #16). |
| action_description | Multiple choice (4 options: correct value + 3 from distractor pool) |
| mastery_tier | baseline |
| mastery_verb | identify |
| parameter_coverage | Values: 3, 4, 5, 6, 7, 8. Categories: 3–4. Orientation: mixed. Graph type: bar graph. Data Table: hidden. |
| correct_end_state | Student selects the correct numerical value for the named category. |
| key_teaching_moment | Lesson 2.1–2.2: Helping line technique + axis reading. Guide: "Look at where the bar ENDS on the scale." |
| remediation_track | MC (per RDR §3) |
| validator_tag | [Validator: Misconception_#16] |
| problem_count | 6 |

---

#### Template 0105 — Find Most/Least in Picture Graph (Support)

**🟢 SKILL:** S3 — Identify the most or least/fewest category from a graph

**🔵 PROBLEM TYPE:** Given a picture graph with 3 categories, student clicks the category with the most or fewest.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — any survey/preference theme works; "most/fewest" applies universally.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite snacks | popcorn, pretzels, fruit cups | 3 categories; values should have clear most/least |
| Zoo animals | lions, penguins, birds | Nature/field trip theme |
| Favorite fruits | apples, grapes, watermelon | Universal |
| Art supplies used | crayons, markers, colored pencils | Classroom creative theme |
| Recess games | tag, swings, slides | Active play |
| Lunch choices | pizza, salad, sandwich | School cafeteria |

**🟠 PROMPT EXAMPLES:**
1. "Which snack got the MOST votes?"
2. "Which animal is the FEWEST at the zoo?"
3. "Click on the category with the LEAST."
4. "Which fruit is the MOST popular?"
5. "Which color got the FEWEST votes?"

**🟣 SUCCESS DIALOGUE:**
1. "Popcorn got the most — 6 votes."
2. "Right — birds are the fewest with 3."
3. "That's the least. Only 4."
4. "Apples are the most popular."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| Data Table visible | support | Always present at support tier | SP §1.5.3 |
| Values display on hover | support | Student hovers over category — value appears | SP §1.5.1: "hover → values display" |

**🔴 DISTRACTOR TYPES:**

N/A — Click-to-select interaction. System detects *that* the student clicked wrong, not *how*. Error patterns grounded in key teaching moments:
- Clicks opposite extreme (most when asked fewest) — Key Beat: Most/least distinction (Lesson 1.1–1.2)
- Clicks middle-value category — Key Beat: Full comparison across categories (Lesson 2.4)
- Clicks based on visual position (first/last row) rather than data value — Key Beat: Reading data not position (Lesson 1.1)
- Confuses "fewest" vocabulary — Key Beat: Comparison vocabulary (Lesson 2.4: "most," "least," "fewer," "fewest")

**🟤 REMEDIATION DESIGN:**

Track: Non-MC (per RDR §2) — click-to-select interaction
Light: "Look at ALL the rows. Which one has the [most/fewest] symbols?" 10-20 words, no visual.
Medium: "Count the symbols in each row. [Category A] has [X], [Category B] has [Y], [Category C] has [Z]. Which number is the [biggest/smallest]?"
        Visual scaffold: Values appear next to each category row.
Heavy [Modeling]: "Let me show you. I'll count each row. [Category A]: 1, 2, 3 — that's [X]. [Category B]: 1, 2, 3, 4, 5 — that's [Y]. [Category C]: 1, 2, 3, 4 — that's [Z]. [Y] is the [most/least], so [Category B] is the answer."
        Visual: System counts each row with animation, circles the correct one.
Post-Modeling: "Now you've seen how to compare — count each row and find the [biggest/smallest]."
Validator: —

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0105 |
| template_type | standard |
| skill_id | S3 |
| skill | Identify the most or least/fewest category from a graph |
| problem_type | Click the category with the most or fewest from a picture graph |
| workspace_description | Picture Graph (Mode 1: Reading). Horizontal orientation. 3 categories. Key: "Each [symbol] = 1." Values: 3–6 range with clear most/least (difference ≥ 2). Data Table visible. |
| action_description | Click to select category |
| mastery_tier | support |
| mastery_verb | compare |
| parameter_coverage | Values: 3, 4, 5, 6. Categories: 3. Orientation: horizontal. Graph type: picture graph. Data Table: visible. |
| correct_end_state | Student clicks the correct most or fewest category. |
| key_teaching_moment | Lesson 1.1–1.2: "Click on the category with the MOST/LEAST." Visual comparison across all rows. Guide: "Which row has the [most/fewest] symbols?" |
| remediation_track | Non-MC (per RDR §2) |
| validator_tag | — |
| problem_count | 4 |

---

#### Template 0106 — Find Most/Least in Bar Graph (Baseline)

**🟢 SKILL:** S3 — Identify the most or least/fewest category from a graph

**🔵 PROBLEM TYPE:** Given a bar graph (either orientation) with 4 categories, student clicks the category with the most or fewest.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — any survey/count theme works; "most/fewest" applies to any category set.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite seasons | spring, summer, fall, winter | 4 categories; universal |
| Books read by students | Dan, Mia, Kenji, Ava | Name-based; use diverse names |
| Favorite sports | soccer, basketball, swimming, running | Broad appeal |
| Pets at home | dogs, cats, fish, hamsters | Common experience |
| Lunch table choices | table A, table B, table C, table D | Abstract but relatable |
| Things collected outside | leaves, rocks, shells, pinecones | Nature/exploration |

**🟠 PROMPT EXAMPLES:**
1. "Which season is the MOST popular?"
2. "Who read the FEWEST books?"
3. "Click on the sport with the LEAST votes."
4. "Which pet do the MOST students have?"
5. "Which snack got the FEWEST votes?"

**🟣 SUCCESS DIALOGUE:**
1. "Summer is the most popular — 9 votes."
2. "Dan read the fewest — only 3 books."
3. "That's the least. You compared all the bars."
4. "Dogs — the most students have dogs."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| Axis tick marks visible | all | Always present per toy spec | SP §1.5.2 |

**🔴 DISTRACTOR TYPES:**

N/A — Click-to-select interaction. Error patterns grounded in key teaching moments:
- Clicks visually prominent bar regardless of question (#16)
- Clicks bar closest in height to another (miscompares) — Key Beat: Full comparison (Lesson 2.3–2.4)
- Clicks based on position rather than value — Key Beat: Reading bar height not position (Lesson 2.1)
- Confuses most/least vocabulary — Key Beat: Comparison vocabulary (Lesson 2.4)

**🟤 REMEDIATION DESIGN:**

**RDR §2 (Non-MC Track):**

- **Light (10–20 words):** "Look at all the bars. Which one goes the farthest?"
- **Medium (20–30 words + visual scaffold):** Highlight all bars with contrasting colors. Say: "These are all the bars. The LONGEST bar is the MOST. The SHORTEST bar is the LEAST. Which is longer — this one or this one?" Point to two bars.
- **Heavy [Modeling] (30–60 words):** "I'm going to compare ALL the bars carefully. Bar 1 is here. Bar 2 is here — shorter. Bar 3 is here — shorter. Bar 4 is here — this is the longest! The longest bar is the MOST. So [Category 4] is the MOST."
- **Post-Modeling (RDR §7):** "That's how comparing works — count each one and find the biggest."

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0106 |
| template_type | standard |
| skill_id | S3 |
| skill | Identify the most or least/fewest category from a graph |
| problem_type | Click the category with the most or fewest from a bar graph |
| workspace_description | Bar Graph (Mode 1: Reading). Mixed orientation. 4 categories. Axis 0–10 by 1s. Values: 3–8 range. Ensure at least two values are close (differ by 1) so student must read carefully. Data Table NOT visible. |
| action_description | Click to select category |
| mastery_tier | baseline |
| mastery_verb | compare |
| parameter_coverage | Values: 3, 4, 5, 6, 7, 8. Categories: 4. Orientation: mixed. Graph type: bar graph. Data Table: hidden. |
| correct_end_state | Student clicks the correct most or fewest category. |
| key_teaching_moment | Lesson 2.2a–2.4: Compare bar heights to find most/fewest. Guide: "Which bar is the [tallest/shortest]?" |
| remediation_track | Non-MC (per RDR §2) |
| validator_tag | [Validator: Misconception_#16] |
| problem_count | 5 |

---

#### Template 0107 — How Many More/Fewer — Picture Graph (Support)

**🟢 SKILL:** S4 — Solve "how many more/fewer" comparison problems

**🔵 PROBLEM TYPE:** Given a picture graph with 3 categories, student solves a "how many more" or "how many fewer" question.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — "how many more/fewer" works with any two-category comparison from a survey.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite pets | cats, dogs, birds, fish | Values should differ by 2-4 for support tier |
| Favorite colors | blue, green, red, yellow | Simple, universal |
| Lunch choices | pizza, salad, soup | 3-category graph |
| Playground activities | swings, slides, climbing | Outdoor play |
| Bedtime stories read | fairy tales, animal stories, adventures | Literacy connection |
| Favorite weather | sunny, rainy, snowy | 3 categories; seasonal |

**🟠 PROMPT EXAMPLES:**
1. "How many MORE students chose cats than birds?"
2. "How many FEWER votes did green get than blue?"
3. "How many MORE people picked pizza than salad?"
4. "How many FEWER animals are birds than dogs?"
5. "How many MORE students like summer than fall?"

**🟣 SUCCESS DIALOGUE:**
1. "3 more. Cats got 6, birds got 3. The difference is 3."
2. "2 fewer. Green got 4, blue got 6."
3. "Right — 2 more chose pizza."
4. "3 fewer birds than dogs."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold Type | Tier | Trigger | Reference |
|---|---|---|---|
| Two-category highlight | support | Question loads — system highlights the two named categories | SP §1.7 Lesson 3.1: system highlights Blue and Yellow bars |
| Data Table visible | support | Always present at support tier | SP §1.5.3 |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| sum_of_pair | Adds instead of subtracts | #6 | Emphasize: "Compare means SUBTRACT. First category is [X], second is [Y]. [X] take away [Y] gives the difference." |
| single_value | Selects one value without operating | Key Beat: Two-value comparison (3.1) | "This is just one group. The question asks about TWO groups. Find the difference." |
| off_by_one | Gets the magnitude wrong by 1 | Key Beat: Subtraction accuracy (3.1–3.2) | "Recount carefully. First has [X], second has [Y]. Count on your fingers from [Y] to [X]." |
| wrong_category_pair | Uses one correct category but pairs it with the wrong one | Key Beat: Question reading (3.4a) | "The question asks about [A] and [B]. You compared [A] with [C] instead." |

**🟤 REMEDIATION DESIGN:**

**RDR §3 (MC Track):**

- **Medium per-distractor (see table above)**
- **Heavy [Modeling]:** "I see [A] has [X] symbols, [B] has [Y] symbols. To find 'how many more,' I compare by subtracting. [X] minus [Y] equals [difference]. That's the answer."
- **Post-Modeling (RDR §7):** "That's how comparing works — subtract to find the difference."
- **Validator tags:** [Validator: Misconception_#6]

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0107 |
| template_type | standard |
| skill_id | S4 |
| skill | Solve "how many more/fewer" comparison problems (subtract) |
| problem_type | "How many more/fewer A than B?" from a picture graph |
| workspace_description | Picture Graph (Mode 1: Reading). Horizontal orientation. 3 categories. Key: "Each [symbol] = 1." Values: 3–6, with the two compared categories differing by 1–3. Data Table visible. MC distractors: correct difference, sum of two values (#6 detection), one individual value, off-by-one. |
| action_description | Multiple choice (4 options) |
| mastery_tier | support |
| mastery_verb | compare |
| parameter_coverage | Values: 3, 4, 5, 6. Categories: 3. Orientation: horizontal. Graph type: picture graph. Data Table: visible. |
| correct_end_state | Student selects the correct difference. |
| key_teaching_moment | Lesson 3.1: "This is a COMPARISON question. 'How many more' means we COMPARE. We find the DIFFERENCE by subtracting." System highlights both bars. Guide: "Blue has 8. Yellow has 6. Subtract." |
| remediation_track | MC (per RDR §3) |
| validator_tag | [Validator: Misconception_#6] |
| problem_count | 4 |

---

#### Template 0108 — How Many More/Fewer — Bar Graph (Baseline)

**🟢 SKILL:** S4 — Solve "how many more/fewer" comparison problems

**🔵 PROBLEM TYPE:** Given a bar graph (either orientation) with 3–4 categories, student solves a "how many more" or "how many fewer" question.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — any two-category comparison from a bar graph survey.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Books read by students | Ava, Dan, Kenji, Sofia | Name-based; use diverse names |
| Favorite colors | red, blue, green, yellow | Simple, universal |
| Favorite seasons | spring, summer, fall, winter | 4 categories for 3–4 cat range |
| Pets at home | dogs, cats, fish, hamsters | Common experience |
| Ways to school | walk, bus, car, bike | Transportation |
| Instruments played | piano, guitar, drums, flute | Arts connection |

**🟠 PROMPT EXAMPLES:**
1. "How many MORE books did Ava read than Dan?"
2. "How many FEWER students chose red than blue?"
3. "How many MORE votes did spring get than winter?"
4. "How many FEWER people picked fish than dogs?"
5. "How many MORE students walk than bike?"

**🟣 SUCCESS DIALOGUE:**
1. "5 more. Ava read 8, Dan read 3. The difference is 5."
2. "3 fewer. Red got 5, blue got 8."
3. "Right — 4 more for spring."
4. "2 fewer people picked fish."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold Type | Tier | Trigger | Reference |
|---|---|---|---|
| Axis tick marks visible | all | Always present | SP §1.5.2 |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| sum_of_pair | Adds instead of subtracts the two named categories | #6 | "Compare means SUBTRACT. Read both bars: [A] is [X], [B] is [Y]. [X] minus [Y] = the difference." |
| all_categories | Sums or operates on all 3–4 bars shown | #17 | "Stop! This question only names [A] and [B]. Ignore the other bars. Compare only these two." |
| single_value | Selects one bar value without comparison | Key Beat: Two-value comparison (3.1) | "This is just one category. You need to compare TWO. Find the difference." |
| wrong_pair | Compares a different pair than named | Key Beat: Question reading (3.4a) | "The question asks about [A] and [B]. Not [C] and [D]. Find the right bars." |
| off_by_one | Computes the difference but off by 1 | Key Beat: Subtraction accuracy (3.1–3.2) | "Recount both bars carefully. [X] minus [Y] equals exactly [answer]." |

**🟤 REMEDIATION DESIGN:**

**RDR §3 (MC Track):**

- **Medium per-distractor (see table above)**
- **Heavy [Modeling]:** "I read both bars carefully. [A] has [X]. [B] has [Y]. To compare, I subtract. [X] minus [Y] equals [difference]. That's how many more/fewer."
- **Post-Modeling (RDR §7):** "There you go — subtract to compare. That's the approach for these problems."
- **Validator tags:** [Validator: Misconception_#6], [Validator: Misconception_#17]

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0108 |
| template_type | standard |
| skill_id | S4 |
| skill | Solve "how many more/fewer" comparison problems (subtract) |
| problem_type | "How many more/fewer A than B?" from a bar graph |
| workspace_description | Bar Graph (Mode 1: Reading). Mixed orientation. 3–4 categories. Axis 0–10 by 1s. Values: 3–8, compared categories differ by 2–5. Data Table NOT visible. MC distractors: correct difference, sum of two values (#6), total of all categories (#17), one individual value. |
| action_description | Multiple choice (4 options) |
| mastery_tier | baseline |
| mastery_verb | compare |
| parameter_coverage | Values: 3, 4, 5, 6, 7, 8. Categories: 3–4. Orientation: mixed. Graph type: bar graph. Data Table: hidden. |
| correct_end_state | Student selects the correct difference. |
| key_teaching_moment | Lesson 3.1–3.2: Compare = subtract. System highlights both named bars. Guide: "[Larger] minus [smaller] = difference." Lesson 3.4a: "Which categories do you need?" (selective data use — only the two named categories matter). |
| remediation_track | MC (per RDR §3) |
| validator_tag | [Validator: Misconception_#6], [Validator: Misconception_#17] |
| problem_count | 7 |

---

#### Template 0109 — How Many More/Fewer — Stretch (4–5 Categories)

**🟢 SKILL:** S4 — Solve "how many more/fewer" comparison problems

**🔵 PROBLEM TYPE:** Given a graph with 4–5 categories, student answers "how many more/fewer" with more distractor categories present.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **loose** — same as other comparison templates but with 4–5 categories to increase distractor load.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Pets at the pet store | dogs, cats, fish, birds, lizards | 5 categories; lots of distractors |
| Favorite seasons | spring, summer, fall, winter | 4 categories |
| Favorite colors | red, blue, green, yellow, purple | 5 categories; universal |
| Books read by students | Kai, Nia, Sam, Ava, Leo | Name-based with 5 names |
| School supplies used | pencils, markers, crayons, erasers, scissors | Classroom familiar |
| Types of trees in the park | oak, maple, pine, birch, elm | Nature/science |

**🟠 PROMPT EXAMPLES:**
1. "How many FEWER students have fish than dogs?"
2. "How many MORE people chose summer than spring?"
3. "How many FEWER votes did lizards get than cats?"
4. "How many MORE books did the winner read than the person in last?"
5. "How many FEWER students like yellow than the most popular color?"

**🟣 SUCCESS DIALOGUE:**
1. "3 fewer. Dogs have 7, fish have 4. The difference is 3."
2. "4 more. Summer got 9, spring got 5."
3. "Right — 8 fewer."
4. "3 more books."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold Type | Tier | Trigger | Reference |
|---|---|---|---|
| (none at stretch tier) | — | — | — |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| sum_of_pair | Adds the two named categories instead of subtracting | #6 | "Compare means SUBTRACT, not add. [A] is [X], [B] is [Y]. [X] minus [Y] = [difference]." |
| all_categories_total | Sums all 4–5 categories shown | #17 | "You used every bar! But the question asks only about [A] and [B]. Which two do you need?" |
| all_categories_partial | Sums 3–4 categories (subset of all) | #17 variant | "You're using too many categories. Focus on just [A] and [B]. Dim the others in your mind." |
| single_value | Picks one bar value without comparing | Key Beat: Two-value comparison (3.1) | "This is only one group. You must COMPARE two groups. Find the difference." |
| wrong_pair | Compares different categories than named | Key Beat: Question reading (3.4a) | "Read the question again. It asks about [A] and [B], not [C] and [D]." |

**🟤 REMEDIATION DESIGN:**

**RDR §3 (MC Track):**

- **Medium per-distractor (see table above)**
- **Heavy [Modeling]:** "I see many categories, but the question asks only about [A] and [B]. I'll focus on those two. [A] has [X], [B] has [Y]. I subtract: [X] minus [Y] = [difference]. Done."
- **Post-Modeling (RDR §7):** "That's the approach — focus on just the two categories the question names."
- **Validator tags:** [Validator: Misconception_#6], [Validator: Misconception_#17]

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0109 |
| template_type | standard |
| skill_id | S4 |
| skill | Solve "how many more/fewer" comparison problems (subtract) |
| problem_type | "How many more/fewer A than B?" from a graph with 4–5 categories |
| workspace_description | Bar Graph or Picture Graph (Mode 1: Reading). Mixed orientation. 4–5 categories. Values: 4–10 range, compared categories differ by 2–6. Data Table NOT visible. MC distractors: correct difference, sum of two named values (#6), total of all categories (#17), value of an unnamed category. |
| action_description | Multiple choice (4 options) |
| mastery_tier | stretch |
| mastery_verb | compare |
| parameter_coverage | Values: 4, 5, 6, 7, 8, 9, 10. Categories: 4–5. Orientation: mixed. Graph type: mixed. Data Table: hidden. |
| correct_end_state | Student selects the correct difference. |
| key_teaching_moment | Lesson 3.1–3.2 + 3.4a: Compare = subtract + selective data use. Same technique as S4 baseline but with more categories requiring stronger question-reading skills. |
| remediation_track | MC (per RDR §3) |
| validator_tag | [Validator: Misconception_#6], [Validator: Misconception_#17] |
| problem_count | 4 |

---

#### Template 0110 — In All / Total (Baseline)

**🟢 SKILL:** S5 — Solve "in all / total" combination problems

**🔵 PROBLEM TYPE:** Given a bar graph with 3–4 categories, student finds the total of two named categories.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **tight** — "in all / combined" needs categories where combining quantities makes sense (counts of the same unit).

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Books read by students | Ben, Cara, Dex, Mia | Name-based; combining "books read" is natural |
| Votes for class activities | red, blue, yellow, green | Combining vote counts makes sense |
| Pets owned by students | cats, dogs, fish, birds | "How many pets in all" is natural |
| Stickers collected | star, heart, smiley, animal | Countable items; combining works |
| Flowers in the garden | sunflowers, tulips, daisies, roses | Combining "total flowers" is natural |

**🟠 PROMPT EXAMPLES:**
1. "How many books did Ben and Cara read in all?"
2. "How many votes did red and yellow get combined?"
3. "How many students chose cats or dogs in all?"
4. "How many pets do fish and bird owners have total?"
5. "How many people picked spring and fall combined?"

**🟣 SUCCESS DIALOGUE:**
1. "11 books in all. Ben read 5, Cara read 6."
2. "Right — 9 combined. Red got 4, yellow got 5."
3. "13 in all. You added the two amounts."
4. "7 pets total."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold Type | Tier | Trigger | Reference |
|---|---|---|---|
| Axis tick marks visible | all | Always present | SP §1.5.2 |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| difference_of_pair | Subtracts the two values instead of adding | #6 (inverse) | "'In all' means COMBINE — add them together. [A] has [X], [B] has [Y]. [X] plus [Y] = the total." |
| all_categories | Sums all 3–4 bars shown, not just the two named | #17 | "The question names only [A] and [B]. Don't add the other bars. Just these two." |
| single_value | Selects one value without combining | Key Beat: Two-value combination (3.3) | "You found one group. But 'in all' means you must add the two amounts together." |
| off_by_one | Computes sum but off by 1 | Key Beat: Addition accuracy (3.3) | "Recount. [A] has [X], [B] has [Y]. [X] plus [Y] equals exactly [answer]." |
| wrong_operation_on_pair | Multiplies or uses another operation | Key Beat: Operation selection (3.1 vs 3.3) | "'In all' means ADD. Not multiply. [X] plus [Y] = [sum]." |

**🟤 REMEDIATION DESIGN:**

**RDR §3 (MC Track):**

- **Medium per-distractor (see table above)**
- **Heavy [Modeling]:** "'In all' means COMBINE. [A] has [X], [B] has [Y]. I add: [X] plus [Y] equals [total]. That's how many in all."
- **Post-Modeling (RDR §7):** "That's how 'in all' works — add the two amounts together."
- **Validator tags:** [Validator: Misconception_#6], [Validator: Misconception_#17]

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0110 |
| template_type | standard |
| skill_id | S5 |
| skill | Solve "in all / total" combination problems (add) |
| problem_type | "How many A and B in all?" from a bar graph |
| workspace_description | Bar Graph (Mode 1: Reading). Mixed orientation. 3–4 categories. Axis 0–10 by 1s. Values: 3–8. Data Table NOT visible. MC distractors: correct sum, difference of the two values (#6 inverse), sum of ALL categories (#17), one individual value. |
| action_description | Multiple choice (4 options) |
| mastery_tier | baseline |
| mastery_verb | apply |
| parameter_coverage | Values: 3, 4, 5, 6, 7, 8. Categories: 3–4. Orientation: mixed. Graph type: bar graph. Data Table: hidden. |
| correct_end_state | Student selects the correct sum of the two named categories. |
| key_teaching_moment | Lesson 3.3: "'In all' means COMBINE — add the amounts together." System highlights both bars. Guide: "Yellow has [X], Red has [Y]. Add them: [X] plus [Y] = [total]." |
| remediation_track | MC (per RDR §3) |
| validator_tag | [Validator: Misconception_#6], [Validator: Misconception_#17] |
| problem_count | 5 |

---

#### Template 0111 — Two-Step: Combine Then Compare (Stretch)

**🟢 SKILL:** S4 (primary) + S5 (secondary) — Two-step problem (stretch variant)

**🔵 PROBLEM TYPE:** Student first combines two categories (S5), then compares that total to a third category (S4). Sequential submissions.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **tight** — context must support combining two categories and then comparing to a third. Categories need to be logically groupable (e.g., two similar things combined vs. a third).

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Pets at the pet store | cats, dogs, birds, fish | "cats and dogs combined vs. birds" is natural |
| Books read by students | Ava, Ben, Dan, Mia | "Ava and Ben combined vs. Dan" works with names |
| Favorite seasons | spring, summer, fall, winter | Combine any two, compare to third |
| Stickers collected | stars, hearts, animals, smiley faces | Combinable countable items |
| Votes for games | tag, hide-and-seek, hopscotch, jump rope | Combine two game votes, compare to third |

**🟠 PROMPT EXAMPLES:**
1. "How many MORE students chose cats and dogs combined than birds?"
2. "How many FEWER votes did red and green get together than blue?"
3. "How many MORE books did Ava and Ben read in all compared to Dan?"
4. "How many FEWER pets do fish and lizard owners have combined compared to dog owners?"
5. "How many MORE students like summer and spring together than winter?"

**🟣 SUCCESS DIALOGUE:**
1. "Step 1: 5 + 4 = 9 combined. Step 2: 9 − 3 = 6 more."
2. "Right. You combined first, then compared."
3. "7 more. You added, then subtracted."
4. "2 fewer combined."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold Type | Tier | Trigger | Reference |
|---|---|---|---|
| Step 1 total displayed after submission | all | After Step 1 answer — correct total appears on screen | SP §1.7 Lesson 3.3b–3.4c |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| first_step_only | Student stops after Step 1 and submits the combined total as the final answer | Key Beat: Two-step sequencing (3.3b) | "You found the combined total, but the question has a second step. Use that total to compare with [C]." |
| second_step_wrong_op | Student adds instead of subtracts in Step 2 (#6 pattern continuing) | #6 | "Step 1 was COMBINE (add). Step 2 is COMPARE — that means SUBTRACT. Take your sum and subtract [C]'s value." |
| sum_all_three | Student sums all three named categories | #17-adjacent | "Don't add all three. Step 1: add [A] and [B]. Step 2: compare that total to [C] by subtracting." |
| single_value | Selects one category value without either operation | Key Beat: Multi-value reading (3.1) | "This is a two-step problem. First combine, then compare." |
| reversed_steps | Student compares first, then adds the result | Key Beat: Step ordering (3.3b–3.4c) | "The order matters. Read the question: combine FIRST, then compare." |

**🟤 REMEDIATION DESIGN:**

**RDR §3 (MC Track) — Per-Step Escalation:**

RDR §1.2 escalation applies independently to each step:
- **Step 1** (combine): Up to 3 attempts with L-M-H per the MC track (Medium per-distractor, then shared Heavy). If system takeover after attempt 3, system provides the correct total and displays it on screen before moving to Step 2.
- **Step 2** (compare): Independent L-M-H escalation. The Step 1 total is visible on screen regardless of how Step 1 resolved.
- **Maximum remediation interactions per problem:** 6 (3 per step). If both steps require system takeover, the problem is marked as fully modeled.

- **Medium per-distractor (see table above)**
- **Heavy [Modeling] (Step 1):** "I need to COMBINE [A] and [B]. [A] has [X], [B] has [Y]. [X] plus [Y] = [combined]."
- **Heavy [Modeling] (Step 2):** "Now I COMPARE [combined] with [C]. [C] has [Z]. [Combined] minus [Z] = [difference]."
- **Post-Modeling (RDR §7):** "That's how two-step problems work — combine first, then compare."
- **Validator tags:** [Validator: Misconception_#6]

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0111 |
| template_type | standard |
| skill_id | S4 |
| secondary_skill | S5 |
| skill | Two-step: combine two categories, then compare to a third |
| problem_type | Sequential: Step 1 = "How many A and B combined?" Step 2 = "How many more/fewer is that than C?" |
| workspace_description | Picture Graph or Bar Graph (Mode 1: Reading). Mixed orientation. 4 categories (3 named in problem + 1 distractor). Values: 3–8. Data Table NOT visible. Step 1: MC for the sum. Step 2: MC for the difference (after Step 1 total displays on screen). |
| action_description | Two sequential multiple choice submissions |
| mastery_tier | stretch |
| mastery_verb | apply |
| parameter_coverage | Values: 3, 4, 5, 6, 7, 8. Categories: 4. Orientation: mixed. Graph type: mixed. |
| correct_end_state | Student correctly answers both steps. |
| key_teaching_moment | Lesson 3.3b–3.4c: Two-step problem modeled by Guide. "Step 1: COMBINE Yellow and Red first." Shows total. "Step 2: Now compare that total to Green." Sequential submissions. |
| remediation_track | MC (per RDR §3) |
| validator_tag | [Validator: Misconception_#6] |
| problem_count | 3 |

---

#### Template 0112 — Cross-Graph-Type Reading (Stretch)

**🟢 SKILL:** S1 + S2 combined — Read from both graph types in same problem

**🔵 PROBLEM TYPE:** Same data shown as both a picture graph and a bar graph. Student answers a question that requires reading one value from each.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **tight** — each graph needs its own context, and the two contexts must be plausibly surveyed together (e.g., same class, same event). The cross-graph question must make sense.

| Context | Category Examples (PG / BG) | Notes |
|---------|------------------------------|-------|
| Favorite fruits / Favorite drinks | apples, bananas, grapes / milk, water, juice | Two related surveys in same class |
| Pets at home / Toys at home | dogs, cats, fish / dolls, cars, blocks | Two "things at home" surveys |
| Playground games / Indoor games | tag, swings, slides / puzzles, drawing, reading | Outdoor vs. indoor; same students |
| Favorite sports / Favorite foods | soccer, basketball, swimming / pizza, tacos, pasta | Two "favorites" from same group |

**🟠 PROMPT EXAMPLES:**
1. "The picture graph shows favorite fruits. The bar graph shows favorite drinks. How many MORE students chose apples than chose milk?"
2. "Look at both graphs. How many students chose bananas and water in all?"
3. "One graph shows pets. The other shows toys. How many FEWER fish are there than dolls?"
4. "How many MORE votes did soccer get on the picture graph than basketball on the bar graph?"
5. "Compare: How many students chose red on the picture graph and blue on the bar graph in all?"

**🟣 SUCCESS DIALOGUE:**
1. "3 more. Apples had 7 on the picture graph, milk had 4 on the bar graph."
2. "11 in all. You read both graphs."
3. "Right — 2 fewer."
4. "4 more votes for soccer."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold Type | Tier | Trigger | Reference |
|---|---|---|---|
| (none at stretch tier) | — | — | — |

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| wrong_graph_value | Reads the correct category but from the wrong graph (e.g., reads apple from bar graph instead of picture graph) | Key Beat: Cross-format reading (2.1) | "Check both graphs. The question asks about [A] in the picture graph and [B] in the bar graph. Read each carefully." |
| swapped_categories | Reads from the correct graph but swaps which category goes where | Key Beat: Category identification (1.1, 2.1) | "You're in the right graph but reading the wrong category. Look for [A], not [B]." |
| off_by_one | Reads both correctly but miscount the value | Key Beat: Precise reading (1.4, 2.2) | "Recount the symbols (or bar height) carefully. [A] has [X], [B] has [Y]." |
| visual_impression | Chooses based on which graph looks bigger or more filled, ignoring actual values (#16-adjacent) | #16-adjacent | "Don't judge by how the graph looks. Read the actual values carefully by comparing each bar or counting symbols." |

**🟤 REMEDIATION DESIGN:**

**RDR §3 (MC Track):**

- **Medium per-distractor (see table above)**
- **Heavy [Modeling]:** "I have two graphs. The question asks about [A] in the picture graph and [B] in the bar graph. In the picture graph, [A] has [X] symbols. In the bar graph, [B] has [Y]. Now I compare/add: [X] and [Y] gives [answer]."
- **Post-Modeling (RDR §7):** "That's how you read across graph types — find each value, then use them together."
- **Validator tags:** —

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0112 |
| template_type | standard |
| skill_id | S1 + S2 |
| skill | Read values from both a picture graph and a bar graph |
| problem_type | Answer a question requiring reading from two different graph types |
| workspace_description | Side-by-side display: Picture Graph (Mode 1) and Bar Graph (Mode 1). Different contexts or same data in both formats. 3 categories each. Values: 3–8. Data Table NOT visible. Student must read one value from each graph to answer. |
| action_description | Multiple choice (4 options) |
| mastery_tier | stretch |
| mastery_verb | identify |
| parameter_coverage | Values: 3, 4, 5, 6, 7, 8. Categories: 3 per graph. Orientation: mixed. Both graph types. |
| correct_end_state | Student selects the correct answer based on values read from both graphs. |
| key_teaching_moment | Lesson 2.1: "Same information, different format. Instead of counting symbols, we read where the bar ends." Cross-representation introduced when bar graphs appear alongside picture graphs. |
| remediation_track | MC (per RDR §3) |
| validator_tag | — |
| problem_count | 2 |

---

### Misconception Remediation Templates

---

#### Template 0120 — Remediation: Graph as Picture (#16)

**🟢 SKILL:** S2 — Read a specific value from a bar graph

**🔵 PROBLEM TYPE:** Bar graph where two bars look similar in height but differ by 3+. Student must read the actual value, not judge by appearance.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **misconception-sensitive** — use only high-familiarity themes so the student focuses on reading the scale, not parsing the context. Avoid themes where bar height differences might be interpreted qualitatively.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite fruits | oranges, bananas, grapes | Values must make visually misleading pairs (e.g., 3 and 7) |
| Pets at home | dogs, cats, birds | Simple, familiar; no emotional weight to "more/fewer" |
| Favorite sports | soccer, swimming, running | Universal; no category is "better" |
| Playground equipment | swings, slides, climbing bars | School familiar |

**🟠 PROMPT EXAMPLES:**
1. "How many students chose oranges? Read the number from the side."
2. "Look at where the bar for dogs ENDS. What number is that?"
3. "Find the bar for bikes. What value does it reach?"
4. "Read the number for spring. Look at the scale on the side."
5. "Where does the fish bar end? Read it from the scale."

**🟣 SUCCESS DIALOGUE:**
1. "3 students. The bar for oranges reaches 3 — not 7 like bananas, even though they look close."
2. "Right — 4 dogs. You read the scale, not just the shape."
3. "6 for bikes. You read the value from the axis markings."
4. "Correct. The scale tells you the exact number."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tier | When Deployed | Reference |
|----------|------|---------------|-----------|
| Helping line animation | confidence | System fires on student's first bar click | SP §1.5.2; Lesson 2.1 |
| Data Table visible (verification) | confidence | Always present — student can cross-check | SP §1.5.3 |

**Key Teaching Moment:** Lesson 2.1: Helping line technique. System draws line from bar top to axis. Guide: "The HEIGHT of the bar tells us the amount." This template re-invokes the helping line as both scaffold and remediation.

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| visually_similar_bar | Student picks value of the bar that LOOKS similar in height to the target bar | #16 | "Look at where each bar ENDS on the scale — not how they look side by side." |
| tallest_bar_value | Picks the visually tallest bar's value regardless of the question asked | #16 | "The question asks about [category]. Find that bar and read its value." |
| off_by_one | Reads axis position ±1 from actual endpoint | Key Beat: Axis reading (2.1) | "Look at exactly where the bar ends. Which number does it reach?" |
| between_values | Selects a number between two bars' values (visual averaging) | #16 | "Each bar has its own number on the scale. Read just the one for [category]." |

**🟤 REMEDIATION DESIGN:**

**RDR §3 (MC Track):**

- **Medium per-distractor (see table above)**
- **Heavy [Modeling]:** "Let me show you. Look at where [category]'s bar ENDS on the scale. [Modeling] I trace from the top of the bar straight across... it reaches [value]. The bar for [other category] reaches [other value]. They might look similar, but the numbers are different."
- **Post-Modeling (RDR §7):** "Now you've seen — always read the scale, not the shape."
- **Validator tags:** [Validator: Misconception_#16]

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0120 |
| template_type | misconception_remediation |
| skill_id | S2 |
| skill | Read a specific value from a bar graph (1:1 scale) |
| problem_type | Read bar value where visual appearance is misleading |
| workspace_description | Bar Graph (Mode 1: Reading). Vertical orientation. 3 categories. Axis 0–10 by 1s. Values chosen so two bars look similar in height but differ by 3+ (e.g., 3 and 7 in a graph scaled 0–10 — on screen, the 3 bar is ~30% height and the 7 bar is ~70%, which can appear similar to a young student). Data Table visible (scaffold — student can verify). |
| action_description | Multiple choice (4 options: correct value, visually-similar bar's value, off-by-one, between-values) |
| mastery_tier | confidence |
| mastery_verb | identify |
| parameter_coverage | Values: 3, 7 (or 4, 8 or 3, 6). Categories: 3. Orientation: vertical. |
| correct_end_state | Student selects the correct value by reading the axis, not estimating by visual height. |
| key_teaching_moment | Lesson 2.1: Helping line technique. System draws line from bar top to axis. Guide: "The HEIGHT of the bar tells us the amount." This template re-invokes the helping line as both scaffold and remediation. |
| remediation_track | MC (per RDR §3) |
| validator_tag | [Validator: Misconception_#16] |
| problem_count | 3 |

---

#### Template 0121 — Remediation: All Data Must Be Used (#17)

**🟢 SKILL:** S4 — Solve "how many more/fewer" comparison problems

**🔵 PROBLEM TYPE:** "How many more A than B?" from a graph with 5 categories. Error answer = operation on all 5 categories. Correct answer involves only 2.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **misconception-sensitive** — needs 5 categories to create the "use all data" trap, but context must be dead simple so cognitive load is on the math, not the story.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite pets | cats, dogs, fish, birds, lizards | 5 categories; familiar animals |
| Favorite colors | red, blue, yellow, green, purple | 5 simple categories; universal |
| Sports day events | soccer, basketball, tennis, swimming, running | Active; 5 events |
| Books read by students | Ava, Dan, Mia, Sam, Leo | Name-based; use diverse names |

**🟠 PROMPT EXAMPLES:**
1. "How many MORE students chose cats than fish?"
2. "How many FEWER votes did yellow get than blue?"
3. "How many MORE people picked soccer than tennis?"
4. "How many FEWER books did Dan read than Ava?"
5. "How many MORE students like dogs than lizards?"

**🟣 SUCCESS DIALOGUE:**
1. "5 more. Cats got 8, fish got 3. You only needed those two."
2. "Right — 4 fewer. You used just yellow and blue."
3. "3 more. Only soccer and tennis matter for this question."
4. "Correct — 5 fewer."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tier | When Deployed | Reference |
|----------|------|---------------|-----------|
| Two-category highlight | support | Question loads — system highlights the two named categories | Lesson 3.4a |
| Data Table visible | support | Always present at support tier | SP §1.5.3 |

**Key Teaching Moment:** Lesson 3.4a: "Which categories do you need?" (selective data use). Guide models question analysis: read the question, identify the two named categories, ignore the rest.

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| total_all_categories | Adds or operates on all 5 categories | #17 | "This question only asks about [A] and [B]. The other categories don't matter here." |
| partial_all | Uses 3–4 categories instead of just 2 | #17 variant | "Still too many categories. Only [A] and [B] — that's all you need." |
| sum_of_pair | Adds the two named categories instead of subtracting | #6 | "'How many more' means compare — subtract, not add." |
| single_value | Picks one of the two named category values only | Key Beat: Two-value comparison (3.1) | "You need both [A] and [B] to compare them." |
| random_category | Picks a value from a non-named category | Key Beat: Question reading (3.4a) | "That value is for [wrong category]. Find [A] and [B]." |

**🟤 REMEDIATION DESIGN:**

**RDR §3 (MC Track):**

- **Medium per-distractor (see table above)**
- **Heavy [Modeling]:** "Let me show you. The question asks about [A] and [B] — just those two. [Modeling] I dim the other categories — they don't matter. [A] has [X], [B] has [Y]. Now I compare: [X] minus [Y] = [difference]."
- **Post-Modeling (RDR §7):** "Now you've seen — only the two named categories matter. The rest is extra information."
- **Validator tags:** [Validator: Misconception_#17]

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0121 |
| template_type | misconception_remediation |
| skill_id | S4 |
| skill | Solve "how many more/fewer" comparison problems (subtract) |
| problem_type | "How many more/fewer A than B?" from a 5-category graph |
| workspace_description | Picture Graph or Bar Graph (Mode 1: Reading). Mixed orientation. 5 categories. Values: 3–8. The two named categories have a clear, easy difference (e.g., 8 and 3 → difference of 5). The total of all 5 categories produces a very different number (e.g., 30), making the "all data" error obviously wrong. Data Table visible (scaffold). MC distractors: correct difference, total of all categories (#17), sum of the two named values (#6), one random category value. |
| action_description | Multiple choice (4 options) |
| mastery_tier | support |
| mastery_verb | compare |
| parameter_coverage | Values: 3, 4, 5, 6, 7, 8. Categories: 5. |
| correct_end_state | Student selects the correct difference using only the two named categories. |
| key_teaching_moment | Lesson 3.4a: "Which categories do you need?" (selective data use). Guide models question analysis: read the question, identify the two named categories, ignore the rest. |
| remediation_track | MC (per RDR §3) |
| validator_tag | [Validator: Misconception_#17] |
| problem_count | 3 |

---

#### Template 0122 — Remediation: "More Than" Means Add (#6)

**🟢 SKILL:** S4 — Solve "how many more/fewer" comparison problems

**🔵 PROBLEM TYPE:** "How many more A than B?" with values chosen so the sum and difference are obviously different. Student sees that adding produces an implausibly large answer.

**⚪ RECOMMENDED CONTEXTS:**

Coupling: **misconception-sensitive** — values must produce an implausibly large sum to make the #6 error self-evident. Use only simple, familiar contexts so the student focuses on the operation, not the story.

| Context | Category Examples | Notes |
|---------|------------------|-------|
| Favorite pets | dogs, cats, birds | Values chosen so sum exceeds max shown (e.g., 8+2=10 on 0–10 axis) |
| Favorite colors | red, green, blue | Simple categories; wide value pairs |
| Books read | Sam, Mia, Leo | Name-based; diverse |
| Ways to school | walk, bus, car | Universal; 3 categories |

**🟠 PROMPT EXAMPLES:**
1. "How many MORE students chose dogs than birds?"
2. "How many FEWER votes did green get than red?"
3. "How many MORE people picked summer than winter?"
4. "How many FEWER books did Sam read than Mia?"
5. "How many MORE students walk than ride the bus?"

**🟣 SUCCESS DIALOGUE:**
1. "6 more. Dogs got 8, birds got 2. 8 minus 2 is 6."
2. "Right — 5 fewer. Compare means subtract."
3. "7 more. You found the difference."
4. "4 fewer. You subtracted to compare."

**🟡 PROACTIVE SCAFFOLD SUGGESTIONS:**

| Scaffold | Tier | When Deployed | Reference |
|----------|------|---------------|-----------|
| Two-category highlight | confidence | Question loads — system highlights the two named categories | Lesson 3.1 |
| Data Table visible | confidence | Always present at confidence tier | SP §1.5.3 |

**Key Teaching Moment:** Lesson 3.1: "This is a COMPARISON question. We find the DIFFERENCE by subtracting." System highlights both bars. Guide: "Blue has 8. Yellow has 6. Since more students like Blue, subtract."

**🔴 DISTRACTOR TYPES:**

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| sum_of_pair | Adds instead of subtracts | #6 | "You added. But 'how many MORE' means compare — find the DIFFERENCE. Subtract." |
| larger_value_only | Selects the larger value as answer | Key Beat: Two-value comparison (3.1) | "That's how many [A] has total. The question asks how many MORE than [B]." |
| smaller_value_only | Selects smaller value | Key Beat: Two-value comparison (3.1) | "That's [B]'s value. To find how many more, you need both values." |
| total_all | Includes all categories | #17 | "Only [A] and [B] matter for this question." |
| off_by_one | Correct operation but miscounts (±1) | Key Beat: Subtraction accuracy (3.1–3.2) | "Almost — check your subtraction one more time." |

**🟤 REMEDIATION DESIGN:**

**RDR §3 (MC Track):**

- **Medium per-distractor (see table above)**
- **Heavy [Modeling]:** "Let me show you. [A] has [X], [B] has [Y]. [Modeling] If we ADD, we get [sum] — but look, [A] only has [X], so [sum] can't be right. COMPARE means find the DIFFERENCE: [X] minus [Y] = [diff]."
- **Post-Modeling (RDR §7):** "That's how comparing works — find the difference by subtracting."
- **Validator tags:** [Validator: Misconception_#6]

**Technical Details:**

| Field | Value |
|-------|-------|
| template_id | 0122 |
| template_type | misconception_remediation |
| skill_id | S4 |
| skill | Solve "how many more/fewer" comparison problems (subtract) |
| problem_type | "How many more/fewer A than B?" with parameters that make the addition error visibly wrong |
| workspace_description | Bar Graph (Mode 1: Reading). Vertical orientation. 3 categories. Axis 0–10 by 1s. Values chosen so the two compared categories have a large gap and the sum is implausible: e.g., A=8, B=2 (diff=6, sum=10 exceeds max shown). Data Table visible (scaffold). MC distractors: correct difference (6), sum of the two values (10, #6 detection), the larger value alone (8), off-by-one (5). |
| action_description | Multiple choice (4 options) |
| mastery_tier | confidence |
| mastery_verb | compare |
| parameter_coverage | Value pairs: (8, 2), (9, 3), (7, 2), (10, 4). Categories: 3. Orientation: vertical. |
| correct_end_state | Student selects the correct difference. |
| key_teaching_moment | Lesson 3.1: "This is a COMPARISON question. We find the DIFFERENCE by subtracting." System highlights both bars. Guide: "Blue has 8. Yellow has 6. Since more students like Blue, subtract." |
| remediation_track | MC (per RDR §3) |
| validator_tag | [Validator: Misconception_#6] |
| problem_count | 3 |

---

## §PT.4 Template Summary

### Standard Templates (count toward Pool Target)

| # | ID | Problem Type | Verb | Tier | Skill | Misc. Detected | Problems |
|---|------|--------------------------------------|----------|------------|-------|----------------|----------|
| 1 | 0101 | Read picture graph value | identify | confidence | S1 | — | 6 |
| 2 | 0102 | Read picture graph value | identify | baseline | S1 | #16 | 6 |
| 3 | 0103 | Read bar graph value | identify | confidence | S2 | — | 6 |
| 4 | 0104 | Read bar graph value | identify | baseline | S2 | #16 | 6 |
| 5 | 0105 | Most/least — picture graph | compare | support | S3 | — | 4 |
| 6 | 0106 | Most/least — bar graph | compare | baseline | S3 | #16 | 5 |
| 7 | 0107 | How many more/fewer — PG | compare | support | S4 | #6 | 4 |
| 8 | 0108 | How many more/fewer — BG | compare | baseline | S4 | #6, #17 | 7 |
| 9 | 0109 | How many more/fewer — 4-5 cats | compare | stretch | S4 | #6, #17 | 4 |
| 10 | 0110 | In all / total | apply | baseline | S5 | #6 inv., #17 | 5 |
| 11 | 0111 | Two-step: combine then compare | apply | stretch | S4 (+ S5) | #6 | 3 |
| 12 | 0112 | Cross-graph-type reading | identify | stretch | S1+S2 | — | 2 |
| | | | | | | **STANDARD POOL TOTAL** | **58** |
| | | | | | | **POOL TARGET** | **55–65** |

### Misconception Remediation Templates (separate sub-pool)

| # | ID | Problem Type | Targets | Tier | Problems |
|---|------|----------------------------------------|---------|------------|----------|
| 1 | 0120 | Read bar value — visual mismatch | #16 | confidence | 3 |
| 2 | 0121 | How many more/fewer — 5 categories | #17 | support | 3 |
| 3 | 0122 | How many more/fewer — sum vs difference | #6 | confidence | 3 |
| | | | | **REMEDIATION SUB-POOL TOTAL** | **9** |

---

## §PT.5 Coverage Validation

### Tier Distribution (standard templates only)

| Tier | Target | Actual | Count | Status |
|------|--------|--------|-------|--------|
| confidence | 8–12% | 21% | 12 | ℹ️ Pool coverage adequate. Algorithm tunes session-level draw rate. |
| support | 15–20% | 14% | 8 | ℹ️ Pool coverage adequate. Future S5 support template would broaden. |
| baseline | 40–50% | 50% | 29 | ✅ |
| stretch | 15–20% | 16% | 9 | ✅ |
| challenge | 5–8% | 0% | 0 | ℹ️ Intentional for M1 review module. Algorithm won't draw what doesn't exist. |

### Skill Coverage

| Skill | Description | Templates | Tiers Covered | Target % | Actual % | Status |
|-------|-------------|-----------|---------------|----------|----------|--------|
| S1 | Read picture graph value | 0101, 0102, 0112 | conf, base, stretch | 20% | 24% (14) | ✅ |
| S2 | Read bar graph value | 0103, 0104, 0112 | conf, base, stretch | 20% | 24% (14) | ✅ |
| S3 | Most/least | 0105, 0106 | support, base | 15% | 16% (9) | ✅ |
| S4 | How many more/fewer | 0107, 0108, 0109, 0111 | sup, base, stretch | 28% | 31% (18) | ✅ |
| S5 | In all / total | 0110, 0111 | baseline, stretch | 8% | 14% (8) | ✅ (includes two-step overlap) |

### Verb Distribution

| Verb | Target | Actual | Count | Status |
|------|--------|--------|-------|--------|
| identify | ~40% | 45% | 26 | ✅ |
| compare | ~46% | 40% | 23 | ✅ (S3 9 + S4 14 = 23; S5's 5 problems moved to apply) |
| apply | ~10% | 14% | 8 | ✅ (S5 baseline 5 + two-step stretch 3) |

### Misconception Detection Coverage (standard templates)

| ID | Priority | Detected In | Detection Strategy | Status |
|----|----------|-------------|-------------------|--------|
| 16 | PRIMARY | 0102, 0104, 0106 | MC distractor = visually prominent category value | ✅ (3 templates) |
| 17 | SECONDARY | 0108, 0109, 0110 | MC distractor = total of all categories | ✅ (3 templates) |
| 6 | ADDRESSED | 0107, 0108, 0109, 0110, 0111 | MC distractor = sum instead of difference (S4) or difference instead of sum (S5) | ✅ (5 templates) |

### Misconception Remediation Coverage (dedicated templates)

| ID | Priority | Remed. Template | Remediation Approach | Status |
|----|----------|-----------------|---------------------|--------|
| 16 | PRIMARY | 0120 | Visual mismatch bars + helping line animation + Data Table verification | ✅ (≥1) |
| 17 | SECONDARY | 0121 | 5-category graph + category dimming + selective data prompt | ✅ (≥1) |
| 6 | ADDRESSED | 0122 | Large-gap values where sum is implausibly large + explicit "compare = subtract" | ✅ (≥1) |

### Practice Phase Guidance Compliance

| Requirement | Met? | How |
|-------------|------|-----|
| S4 weighted most heavily | ✅ | S4 has 18 problems (31%) — highest share |
| Both orientations | ✅ | Horizontal: 0101, 0105, 0107. Vertical: 0103. Mixed: 0102, 0104, 0106, 0108, 0109, 0110, 0111, 0112. |
| Both graph types in same problem | ✅ | 0112 (cross-graph-type reading, 2 problems) |
| "How many more/fewer" language | ✅ | 0107, 0108, 0109, 0111 all use exact phrasing |
| MC interaction type | ✅ | All templates use MC. 0105, 0106 use click-to-select. |
| Data Table visibility scaffolding | ✅ | Visible in confidence/support (0101, 0103, 0105, 0107). Hidden in baseline+ (0102, 0104, 0106, 0108–0112). |
| No creation in Practice | ✅ | All templates are reading/interpreting. |
| "All data" distractors | ✅ | 0108, 0109, 0110, 0121 include all-categories distractor. |

### Action Variety

| Action Type | Templates | Status |
|-------------|-----------|--------|
| Multiple choice | 0101–0104, 0107–0112, 0120–0122 | ✅ |
| Click to select category | 0105, 0106 | ✅ |
| Sequential MC (two-step) | 0111 | ✅ |

### Dimension Coverage

- All valid parameter values used across template set? **Yes** — values 3–10 covered across tiers.
- Novel values (not in Early Lesson) present in baseline+? **Yes** — values 7–10 appear in stretch templates.
- Early-phase values reserved for confidence/support? **Yes** — confidence uses 3–6 only.

### Context Coverage

| Check | Status | Notes |
|-------|--------|-------|
| All templates have ⚪ RECOMMENDED CONTEXTS? | ✅ All | All 15 templates have context sections |
| Context coupling appropriate per template? | ✅ All | Loose: 0101–0109. Tight: 0110–0112. Misconception-sensitive: 0120–0122. |
| Context variety across template set? | ✅ | 40+ unique context themes across all templates; minimal reuse (pets/fruits appear in multiple templates with different category examples) |
| Category examples plausible for parameter range? | ✅ All | All category sets produce plausible count data within 3–10 range |

### Remediation Design Compliance (per RDR v3)

| Check | Status | Notes |
|-------|--------|-------|
| MC templates with per-distractor Medium? | ✅ All | 0102, 0104, 0107–0112, 0120–0122 — all have distractor types with Medium directions |
| MC templates with shared Heavy + [Modeling]? | ✅ All | All MC templates above include Heavy [Modeling] block |
| Non-MC templates with full L-M-H? | ✅ All | 0105, 0106 — click-to-select, full L-M-H provided |
| Confidence templates with Light only? | ✅ All | 0101, 0103 — Light only, no Medium/Heavy |
| Post-modeling language checked (RDR §7)? | ✅ | All Heavy blocks use assistance-acknowledging language, no independent success claims |
| Validator tags assigned? | ✅ All | Templates detecting misconceptions have validators; others have — |
| Distractor type pools ≥ 4 types? | ✅ All | All MC templates have 4–5 distractor types |

### Gaps / Flags

- ℹ️ **Confidence tier at 21%.** Playbook target is 8–12%. The pool defines coverage breadth — the adaptive algorithm controls session-level tier balance at runtime. Two confidence templates (S1, S2) ensure low-entry coverage for review skills. No action needed at pool level.
- ℹ️ **Support tier at 14%.** Playbook target is 15–20%. Same principle — pool coverage is adequate; algorithm tunes draw rates. A future support-tier S5 template would strengthen coverage breadth.
- ℹ️ **No challenge tier.** M1 is a review module — challenge would push beyond taught scope. Acceptable for M1; flag if pattern repeats in M2+.
- ⚠️ **S3 has no stretch tier.** Most/least only appears at support and baseline. A stretch variant (most/least with 5 categories and close values) would improve coverage breadth for this skill.
- All PRIMARY/HIGH misconceptions have dedicated remediation templates. ✅
- All remediation templates have concrete source references (RDR + SP). ✅
- All MC templates have per-distractor Medium remediation directions. ✅

### SP Delta

*Differences between Toy Flow and SP that affected template design:*

- Toy Flow lacked Data Constraints, Toy Requirements, Vocabulary, and Scaffolding tables. SP §1.5 provided all values and configurations used in templates.
- Toy Flow listed misconceptions without priority. SP §1.4 classified #16 as PRIMARY and #17 as SECONDARY, which determined remediation template allocation.
- SP §1.8.5 Distribution Targets (S1 30%, S2 30%, S3 30%, S4 10%) were adjusted: S3 broken out as separate skill, S4 elevated to 28% per SP's own "highest-demand" note.
- SP §1.8.5 4-skill decomposition expanded to 5 skills (S3 most/least separated from S1/S2) based on decomposition framework analysis.
