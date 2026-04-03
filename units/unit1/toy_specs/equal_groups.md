# Equal Groups with Pictures or Dots

Category: Unit 1
Created: February 3, 2026 5:28 PM
Status: UX in Process
Target Audience: Grade 3 Unit 1, Grade 3 Unit 4

---

> **WHAT:** Visual representations showing multiplication through equal groups—multiple clusters of items where each cluster contains the same quantity. Items can be pictures (apples, cookies, stars) or dots, grouped using containers (bags, boxes, circles) or spatial separation. Items within each group may be arranged in patterns (including mini-array arrangements like 2×2).

**WHY:** Equal groups provide the foundational visual model for understanding "3 × 4" as "3 groups of 4 items." This representation bridges concrete counting to abstract symbolic notation. The system must support multiple grouping methods (containers vs spacing), multiple item types (pictures vs dots), and various contexts (kitchen, garden, sports) to demonstrate multiplication's universal applicability. Interactive features (highlighting, counting animations, connection lines) transform static images into active learning tools where students explore structure rather than passively viewing. Research on CRA (Concrete-Representational-Abstract) approaches shows effect sizes of 0.67-0.85 for multiplication understanding, making flexible visual representation capabilities essential for effective digital instruction.
>

## Shape

![image.png](image.png)

### Group Structure

The fundamental unit: a cluster of items with clear boundaries.

![image.png](image%201.png)

**Grouping Methods:**

**Container-Based Grouping:**

- **Visual treatment:** Items enclosed in illustrated containers (bags, boxes, circles, ovals)
- **Group boundary:** Container edge defines the group
- **Purpose:** Clear visual separation; "container = group" metaphor
- **Examples:**
    - Bags with apples inside
    - Boxes with cookies inside
    - Circles with dots inside
    - Ovals with stars inside

**Spatial Grouping:**

- **Visual treatment:** Items clustered with spacing; no container boundaries
- **Group boundary:** Spacing between clusters defines groups
- **Purpose:** Shows structure without physical boundaries

![image.png](image%202.png)

---

### Item Types

What can appear inside each group.

![image.png](image%203.png)

<aside>
‼️

Final art for bag and stack containers incoming. Will need to support 3 different visualizations. Items inside of stacks and bags should be able to be customizable

</aside>

**Pictures (Illustrated Objects):**

- **Visual style:** Emoji-style, colorful, Grade 3-appropriate
- **Item variety:** Apples, oranges, cookies, stars, flowers, balls, books, pencils, etc
- **Context-specific:** Kitchen items for kitchen contexts, sports items for sports contexts
- **Size:** Large enough to distinguish clearly

**Dots (Abstract Shapes):**

- **Visual style:** Simple circles, uniform size
- **Color:** Single color or multi-color for variety
- **Purpose:** Generic representation; reduces visual complexity

**Internal Arrangement Within Groups:**

- Items within a group **can be arranged in patterns**
- Possible arrangements: linear, 2×2, 2×3, 2×4, 2×5, 3×2, 5x4 random clustering
- **Note:** Internal arrangement doesn't affect "equal groups" counting—we count GROUPS, not internal structure

---

## Properties

### Mode

- UX to provide visuals for each mode

| Mode | Description | Student Interaction | When Used |
| --- | --- | --- | --- |
| **Mode 1: Structural Recognition** | Students observe and analyze equal groups structure | Click to highlight, count groups/items; no equation building | M7 |
| **Mode 2: With Equation Building** | Students observe structure AND create expressions/equations | Same as Mode 1 + equation construction via Equation Builder | M8-M12 |
| Mode 3: Partitive Division (Unit 4) | Students observe items being dealt equally into a known number of groups, then identify how many items end up in each group | Observe dealing animation; count items per group; answer MC; build ÷ equation (when paired with Equation Builder) | Unit 4 Section A–B |
| Mode 4: Quotitive Division (Unit 4) | Students observe items being measured out into groups of a known size, then identify how many groups were formed | Observe measuring animation; count groups formed; answer MC; build ÷ equation (when paired with Equation Builder) | Unit 4 Section A–B |
| Mode 5: Multiplication-Division Dual Reading (Unit 4) | A completed equal groups display is read as BOTH a multiplication fact and a division fact. No animation — interpretive overlay on static image. | Observe both equations; build fact family via Equation Builder; match expressions to visual | Unit 4 Section A–B |

### Grouping Type

- UX to provide visual examples

| Type | Description | Boundary Indicator | Example Use Cases |
| --- | --- | --- | --- |
| **Container: Bags** | Items in illustrated bags | Bag edge | Concrete contexts, real-world connection |
| **Container: Boxes** | Items in illustrated boxes | Box edge | Concrete contexts, real-world connection |
| **Container: Circles** | Items in circles/ovals | Circle edge | Most common, reduces visual clutter |
| **Spatial** | Items clustered with spacing only | Spacing (40-50px between groups) | Abstract representation |

### Item Type

- UX to provide examples

| Type | Description | Visual Style | When Used |
| --- | --- | --- | --- |
| **Pictures** | Illustrated objects (apples, cookies, stars, etc.) | Emoji-style, colorful, 20-30px | Context variety, concrete scenarios |
| **Dots** | Simple circular shapes | Uniform circles, 8-12px | Generic representation, circles grouping |

### Item Arrangement Within Group

- UX to provide examples

| Arrangement | Description | Example |
| --- | --- | --- |
| **Linear** | Items in single row or column | ● ● ● ● |
| **2×2** | 2 rows of 2 items | ● ●● ● |
| **2×3** | 2 rows of 3 items | ● ● ●● ● ● |
| **2×4** | 2 rows of 4 items | ● ● ● ●● ● ● ● |
| **2×5** | 2 rows of 5 items | ● ● ● ● ●● ● ● ● ● |
| **Random clustering** | Items loosely arranged | ●  ● ● ●  ● |

**Note:** Internal arrangement is incidental to equal groups counting—students count GROUPS and ITEMS PER GROUP, not internal structure.

### Orientation

- UX to provide examples

| Orientation | Description | Visual |
| --- | --- | --- |
| **Horizontal** | Groups arranged left-to-right | `[Group] [Group] [Group]` |
| **Vertical** | Groups arranged top-to-bottom | `[Group][Group][Group]` |

### Quantity Ranges

| Property | Typical Range | Unit 4 Division Range | Notes |
| --- | --- | --- | --- |
| Number of groups | 2-6 groups | 2–10 groups | Extended for division within 100 (e.g., 40 ÷ 5 = 8 needs 8 groups). When groups > 6, keep items per group ≤ 5 for visual parsability. |
| Items per group | 2-10 items | 2–10 items | Must be countable at a glance |
| Total items (dividend) | N/A (derived from groups × items) | 4–100 | Must divide evenly by divisor. Products within multiplication table. |

## Division Properties (Unit 4)

Equal Groups is one of the primary visual models for introducing division in Unit 4. The same tool that builds groups for multiplication now operates in reverse — starting from a total and decomposing into equal groups to find an unknown.

### Pedagogical Shift from Unit 1

**Unit 1 direction (multiplication):** Known groups × known size → find total

- 3 bags with 5 apples each → "How many altogether?"
- Groups exist from the start; student combines to find product

**Unit 4 direction (division):** Known total → decompose into equal groups → find unknown

- 15 apples shared among 3 bags → "How many in each bag?" (partitive)
- 15 apples, 5 per bag → "How many bags?" (quotitive)
- Total exists from the start; student observes decomposition to find quotient

**Critical research connection:** The tool must visually distinguish partitive and quotitive division because they involve fundamentally different physical processes, even when the symbolic expression is identical (15 ÷ 3 = 5). Squire & Bryant (2002) found that the match between representation type and division type affects student performance. Fischbein et al. (1985) and Correa et al. (1998) establish partitive as children's intuitive entry point.

**Same end state, dual reading:** After either division animation completes, the resulting static image (3 groups of 5 = 15) is visually identical to Unit 1's multiplication display. This is the key instructional moment — the guide can surface that one image encodes both 3 × 5 = 15 AND 15 ÷ 3 = 5. This directly supports the inverse relationship (Misconception U4.3, Research Commitment #3).

### Mode 3: Partitive Division (Fair Sharing)

**Description:** Students observe items being distributed equally among a known number of groups, then identify how many items end up in each group.

**Setup state:**

- A collection of ungrouped items (the dividend) displayed on screen
- A known number of empty containers visible from the start (the divisor) — bags, boxes, or circles
- The total is established before dealing begins

**Animation — Dealing process:**

- Items move from the ungrouped collection into containers
- Distribution is fair/equal — each container receives items
- UX to determine dealing animation style. Considerations and options:
    - **Round-robin (one at a time to each container in turn):** Most concrete; shows "fairness" explicitly; slow for larger numbers. Best for introduction.
    - **Batch dealing (equal portions placed simultaneously):** Faster; still shows equal distribution; less explicit about the dealing process. Better for larger numbers or repeated practice.
    - **Speed control:** Allow system to accelerate after the dealing pattern is established (e.g., show first full round slowly, then fast-forward remaining rounds). Balances pedagogy with pacing.
- Purpose: The process of dealing IS the concept — students must see that equal distribution is what makes it division

**End state:** All items distributed; each container has the same number of items. Visually identical to a multiplication display.

**Student question:** "How many in each group?" → answer is items per group (quotient)

**Paired equation:** `15 ÷ 3 = ?` where 15 = total items, 3 = number of groups, ? = items per group

### Mode 4: Quotitive Division (Measurement / Grouping)

**Description:** Students observe items being measured out into groups of a known size, then identify how many groups were formed.

**Setup state:**

- A collection of ungrouped items (the dividend) displayed on screen
- Knowledge of required group size (the divisor) — displayed as a label or reference group
- No containers visible at start — groups form as items are measured out

**Animation — Measuring process:**

- Items are counted off from the collection in sets of the specified group size
- Each complete set forms a new visible group (container appears or spatial group forms)
- Groups accumulate as more sets are measured out
- UX to determine visual treatment for group formation. Considerations and options:
    - **Slide out:** Items move from the collection to form a new group at a new position. Shows "taking away" clearly.
    - **Circle formation:** A container boundary draws around counted items in place. Shows "grouping" clearly.
    - The key visual distinction from partitive: containers/groups don't exist at the start — they APPEAR as items are measured out
- Purpose: The process of measuring out IS the concept — students see "how many groups of 5 fit in 15?"

**End state:** All items grouped; each group has the specified number of items; groups are countable. Visually identical to a multiplication display and to the partitive end state.

**Student question:** "How many groups?" → answer is number of groups (quotient)

**Paired equation:** `15 ÷ 5 = ?` where 15 = total items, 5 = items per group, ? = number of groups

### Mode 5: Multiplication-Division Dual Reading (Static)

**Description:** A completed equal groups display (whether built via multiplication in Unit 1 or via division animation in Unit 4) is read as BOTH a multiplication fact and a division fact. No animation — this is an interpretive overlay on a static image.

**Display:** Same static equal groups visual as Modes 1–2, but paired with both a multiplication equation AND a division equation (or fact family set), typically via Equation Builder.

**Purpose:** Operationalize the inverse relationship. The student sees that one image = one set of related facts. Bridge from "division is a new thing" to "division is multiplication read differently."

**Scaffolding levels:**

- **Guided:** System displays both equations; guide narrates the connection
- **Prompted:** System displays multiplication equation; student builds division equation via Equation Builder
- **Independent:** System displays visual only; student produces both equations

**Paired equations:** Both `3 × 5 = 15` AND `15 ÷ 3 = 5` (and/or `15 ÷ 5 = 3`) displayed simultaneously

## Allowed Student Actions

### Observe Structure

- UX to provide interaction visual/video

**Description:** Student views equal groups visual to identify mathematical structure.

**Interaction:**

- View static image
- Visually identify: "How many groups?"
- Visually identify: "How many in each group?"

**Purpose:** Build pattern recognition; connect visual to symbolic.

### Click to Highlight Group

<aside>
‼️

- UX to provide interaction visual/video
</aside>

**Interaction:**

1. States
    1. Select Group: Default, Hover, Selected
    2. Select Item in Group: efault, Hover, Selected

**Visual Feedback:**

- Distinct highlight
- Display for  ("This group has 5 items")

**Purpose:** Active exploration of structure; focus attention on "equal" (each group has same amount); support counting.

### Count Groups (Structured Question)

- UX to provide interaction visual/video

**Description:** Student counts groups and indicates how many exist.

**Interaction:**

- **Manual count:** Student counts visually
- **Input answer:** Multiple choice ("How many groups? A) 3 B) 4 C) 5") OR number input OR click each group to count

**Feedback:**

- **Correct:** "Yes, there are 4 groups!"
- **Incorrect:** "Let's count together." [highlights each group sequentially]

**Purpose:** Identify first factor in multiplication (number of groups).

### Count Items Per Group (Structured Question)

- UX to provide interaction visual/video

**Description:** Student counts items in one group and indicates how many.

**Interaction:**

- **Click one group to focus** (optional)
- **Count items in that group**
- **Input answer:** Multiple choice ("How many items in each group?") OR number input

**Feedback:**

- **Correct:** "Right! Each group has 5 items!"
- **Incorrect:** "Let's count the items in this group." [highlights items sequentially within one group]

**Purpose:** Identify second factor in multiplication (items per group).

## Division Student Actions (Unit 4)

### Identify Total Before Division

- UX to provide interaction visual/video

**Description:** Before division animation begins, student confirms or identifies the total number of items.

**Interaction:**

- View ungrouped collection
- Input answer: Multiple choice ("How many items altogether? A) 12 B) 15 C) 18")
- OR: Count items via click-to-count (each item highlights with running count)

**Purpose:** Establish the dividend. Ensures student knows what's being divided before the action starts. Addresses Misconception A1 (confusing dividend and divisor) by making the total salient.

**Feedback:**

- **Correct:** Total displayed as label; division animation begins
- **Incorrect:** Sequential item highlighting with counting; retry

### Identify Items Per Group (After Partitive Division)

- UX to provide interaction visual/video

**Description:** After partitive dealing animation completes, student identifies how many items ended up in each group.

**Interaction:**

- View completed groups (items now distributed in containers)
- **Click one group to focus** (optional — zoom to count)
- Input answer: Multiple choice ("How many in each group?")

**Purpose:** Find the quotient in a partitive context. This is the "answer" to "share 15 among 3."

**Feedback:**

- **Correct:** "Each group has 5 items!" + highlight all groups briefly
- **Incorrect:** Zoom into one group + sequential item highlighting within that group; retry

### Identify Number of Groups (After Quotitive Division)

- UX to provide interaction visual/video

**Description:** After quotitive measuring animation completes, student identifies how many groups were formed.

**Interaction:**

- View completed groups (items now in measured sets)
- Count groups visually
- Input answer: Multiple choice ("How many groups of 5 did you make?")

**Purpose:** Find the quotient in a quotitive context. This is the "answer" to "how many 5s in 15?"

**Feedback:**

- **Correct:** Sequential group highlighting with count ("1, 2, 3 — 3 groups!")
- **Incorrect:** Sequential group highlighting to recount; retry

### Match Division Expression to Visual

- UX to provide interaction visual/video

**Description:** Given a completed equal groups visual (from either division type), student selects the matching division expression from options.

**Interaction:**

- View completed groups visual
- Select from MC options (e.g., "Which expression matches? A) 15 ÷ 3 = 5 B) 15 ÷ 5 = 3 C) 5 ÷ 3 = 15")
- Note: Both A and B may be valid depending on which reading is being assessed

**Purpose:** Bridge from visual to symbolic for division. Critical for Misconception A1 awareness — students must know which number is the dividend, divisor, and quotient.

**Feedback:**

- **Correct:** Connection lines animate from visual to equation parts
- **Incorrect:** Guide identifies which number in the expression maps to which visual element

### Identify Division Type

- UX to provide interaction visual/video

**Description:** Given a word problem or scenario, student identifies whether it's a "sharing" (partitive) or "grouping" (quotitive) situation.

**Interaction:**

- Read scenario (displayed as text or narrated by guide)
- Select from MC: "Is this about sharing equally into groups, or measuring out groups of the same size?"
- OR: Select which animation setup matches (empty containers shown vs. group size label shown)

**Purpose:** Build awareness that division has two distinct meanings. Addresses Misconception U4.2 directly.

**When used:** After both division types have been introduced; primarily in Practice phase

## Additional Teaching/Remediation Actions

### Highlight Single Group

- UX to provide visual/video

**Description:** Guide (system) draws attention to specific group during instruction.

**Example:** Guide says "Look at this bag" → That bag highlights

**Purpose:** Direct focus; model structure identification.

### Sequential Group Highlighting (Count Animation)

- UX to provide visual/video

**Description:** Groups highlight one at a time in sequence, often with skip-counting narration.

**Example - Skip-Counting by 5s:**

- Highlight group 1: Guide says "5"
- Highlight group 2: "10"
- Highlight group 3: "15"
- Highlight group 4: "20"

**Purpose:** Demonstrate counting groups; connect to skip-counting; bridge to product calculation.

### Sequential Item Highlighting (Within-Group Count)

- UX to provide visual/video

**Description:** Items within ONE group highlight one at a time in sequence.

**Example:**

- Focus on one circle with 5 dots
- Highlight each dot: "1, 2, 3, 4, 5"
- Guide: "Each group has 5 items"

**Purpose:** Model counting items in a group; support students who struggle with subitizing.

### Connection Lines to Equation

- UX to provide visual/video

**Description:** Visual lines connect groups/items to parts of equation.

**Example:**

- Visual: 3 bags with 4 apples each
- Equation: `3 × 4 = 12`
- **Connection lines:**
    - Number of bags (3) → First factor (3) [line from bags to "3"]
    - Apples per bag (4) → Second factor (4) [line from inside one bag to "4"]
    - Total apples (12) → Product (12) [line from all items to "12"]

**Purpose:** Make visual-symbolic connection explicit; show what each number represents.

### Zoom/Focus on Single Group

- UX to provide visual/video

**Description:** Temporarily enlarge one group for closer examination.

**Interaction:**

- **Click group** → Group enlarges (fills more screen space)
- **Items become more visible** (easier to count)
- **Exit zoom** → Return to full view

**Purpose:** Help students count items in group when visual is small or complex; reduce cognitive load temporarily.

## Division Teaching/Remediation Actions (Unit 4)

### Partitive Distribution Demonstration

- UX to provide visual/video

**Description:** System shows items being distributed equally among a known number of containers.

**Requirements:**

- Must convey equal/fair distribution — each group ends up with the same amount
- Must start from ungrouped items + visible empty containers
- Must end in a state visually identical to a multiplication equal groups display
- For introduction (first exposure), the process should be visible — not just start state → end state
- For practice/review, the system may show the end state directly (skip the process)

**Purpose:** Model the partitive division concept concretely. "Share 15 among 3" becomes visible.

### Quotitive Grouping Demonstration

- UX to provide visual/video

**Description:** System shows items being grouped into sets of a known size, with new groups forming as items are measured out.

**Requirements:**

- Must convey "measuring out" — taking sets of a known size from the total
- Must start from ungrouped items + group size reference (no containers visible)
- Groups must appear/form during the process (not pre-existing)
- Must end in a state visually identical to a multiplication equal groups display
- Same introduction vs. practice distinction as partitive: show process on first exposure, may skip for review

**Purpose:** Model the quotitive division concept concretely. "How many groups of 5 in 15?" becomes visible.

### Reverse Skip-Counting (Unit 4)

- UX to provide visual/video

**Description:** Groups highlight in sequence with DESCENDING count from the total, showing division as repeated subtraction.

**Example — 15 ÷ 5 (quotitive reading):**

- Highlight group 1: "15 → 10" (subtracted 5)
- Highlight group 2: "10 → 5" (subtracted 5)
- Highlight group 3: "5 → 0" (subtracted 5)

**Purpose:** Connect quotitive division to repeated subtraction; bridge to number line representation; prepare for partial quotients strategy in later modules.

### Division Connection Lines to Equation (Unit 4)

- UX to provide visual/video

**Description:** Visual lines connect elements of the equal groups display to parts of a division equation. Same mechanic as existing Connection Lines to Equation, but mapped to division notation.

**Partitive mapping:**

- Visual: 15 items in 3 bags, 5 in each
- Equation: `15 ÷ 3 = 5`
- Total items (15) → Dividend (15)
- Number of containers (3) → Divisor (3)
- Items per container (5) → Quotient (5)

**Quotitive mapping:**

- Visual: 15 items in groups of 5, making 3 groups
- Equation: `15 ÷ 5 = 3`
- Total items (15) → Dividend (15)
- Items per group (5) → Divisor (5)
- Number of groups (3) → Quotient (3)

**Purpose:** Make visual-symbolic connection explicit for division. Critical for Misconception A1 (confusing dividend and divisor).

### Dual-Reading Overlay (Unit 4)

- UX to provide visual/video

**Description:** System displays both a multiplication equation AND a division equation simultaneously alongside the same equal groups visual.

**Requirements:**

- Static equal groups display (no process — just the completed groups)
- Both `3 × 5 = 15` and `15 ÷ 3 = 5` visible at the same time
- Visual emphasis should distinguish the two equations (color, position, sequencing — UX to determine)

**Purpose:** Operationalize the inverse relationship (Misconception U4.3, Commitment #4). Visual proof that multiplication and division are two readings of the same structure.

### Reset to Ungrouped State (Unit 4)

- UX to provide visual/video

**Description:** System returns a completed equal groups display to its pre-division ungrouped state.

**Purpose:** Reset for retry; transition between demonstrating partitive and quotitive on the same total; reinforce that grouping/ungrouping doesn't change the total (conservation).

## Constraints

### Behavior Constraints

| Constraint | Description |
| --- | --- |
| Equal groups always equal | Every group contains exactly the same number of items (no unequal groups) |
| Abstraction progression sequential | Cannot skip stages: Concrete → Circles → Spatial (in that order) |
| Context consistency (M7-M8) | ONLY bags/boxes/circles in M7-M8; variety introduced mid-M9 (Activities 4-5) with explicit Guide announcement |
| Groups countable at glance | Maximum ~6 groups per visual to avoid overwhelming |
| Items countable at glance | Maximum ~10 items per group for subitizing/counting |

### Unit 4 Behavior Constraints

| Constraint | Description |
| --- | --- |
| Division always exact — no remainders (Unit 4) | All division problems produce whole-number quotients. Remainders are not addressed in this tool for Unit 4. |
| Division type tracked per problem (Unit 4) | System internally labels each division problem as partitive or quotitive. Label available for analytics and guide scripting to ensure balanced exposure per Burtscher & Gaidoschik (2023) finding. |
| Partitive setup shows empty containers (Unit 4) | For partitive division, the number of containers (divisor) is visible from the start. Items are ungrouped. |
| Quotitive setup shows group size reference (Unit 4) | For quotitive division, the required group size (divisor) is displayed as a label or reference. No containers exist at start — they form during the process. |
| End state identical to multiplication display (Unit 4) | After any division process completes, the resulting visual is indistinguishable from a multiplication Mode 1/2 display with the same groups × items. This is by design — supports inverse relationship. |
| Process skippable after introduction (Unit 4) | After initial exposure, division process can show end state directly (Practice phase efficiency). System tracks whether student has seen full process for each division type. |

### Interaction Constraints (What Students CAN Do)

| Action | Constraint | Notes |
| --- | --- | --- |
| Click groups to highlight | One group at a time | No multi-select |
| Count groups | Always available | Basic observation skill |
| Count items per group | Always available | Basic observation skill |
| Zoom on group | Optional feature | May not be implemented for all contexts |

### Unit 4: Interaction Constraints (What Students CAN Do)

| Action | Constraint | Notes |
| --- | --- | --- |
| Observe division process (Unit 4) | Always available during division introduction | Cannot skip on first exposure per type |
| Identify total / dividend (Unit 4) | Before division process begins | Establishes what's being divided |
| Identify items per group — partitive result (Unit 4) | After partitive distribution completes | Click group to count if needed |
| Identify number of groups — quotitive result (Unit 4) | After quotitive grouping completes | Count groups visually |
| Match division expression to visual (Unit 4) | After any division display | MC selection |
| Identify division type (Unit 4) | After both types introduced | MC: "sharing" vs. "grouping" |
| Build division equation via Equation Builder (Unit 4) | When paired with Equation Builder in division context | Same integration pattern as multiplication |

### Question Constraints (What We ASK Students to Do)

**By Module & Abstraction Level:**

| Module | Abstraction Level | Primary Visual | Questions Asked | Equation Building |
| --- | --- | --- | --- | --- |
| **M7 Early** | Concrete (bags/boxes) | Bags with apples, boxes with cookies | "How many groups?" "How many in each?" | NO - Guide shows notation only |
| **M7 Mid-Late** | Semi-Abstract (circles) | Circles with dots | Same questions | NO - Guide shows notation only |
| **M8 Early-Mid** | Semi-Abstract (circles) | Circles with dots | Same + match visual to expression | YES - Student builds expressions |
| **M8 Late** | Abstract (spatial grouping) | Dots with spacing | Same + build expressions independently | YES - Full construction |
| **M9 Early-Mid** | Semi-Abstract Circles | Circles with dots | Expression fluency (2s, 5s, 10s); graph connection | YES - All methods available |
| **M9 Late** | Context Variety Introduced | Rows, stacks, groups | Same + variety contexts | YES - All methods available |
| **M10** | Context Variety (full) | Kitchen, garden, sports, classroom | Complete equations with unknowns | YES - All methods + unknowns |

**Never Ask:**

- Identify or work with unequal groups (all groups are always equal by design)
- Use context variety before M9 (M7-M8 strict: bags/boxes/circles only)
- Build equations in M7 (observation only; guide shows notation)
- Count more than 10 items in a group (exceeds subitizing range; creates unnecessary difficulty)

### Unit 4 Division Question Constraints (By Section)

| Section / Phase | Division Type Available | Primary Questions | Equation Building | Abstraction Level |
| --- | --- | --- | --- | --- |
| **Section A Early** | Partitive only | "How many in each group?" | NO — guide shows equation | Concrete (bags/boxes with pictures) |
| **Section A Mid** | Both partitive and quotitive | "How many in each group?" / "How many groups?" | Guided — student selects from options | Concrete → Semi-abstract (circles with dots) |
| **Section A Late** | Both types, explicitly contrasted | Same + "Is this sharing or grouping?" + match expression | YES — student builds division equations | Semi-abstract (circles with dots) |
| **Section B** | Both types + dual reading | Same + "Write the fact family" + "What multiplication helps?" | YES — full construction including fact families | Semi-abstract → Abstract (spatial) |

**Unit 4 Division — Never Ask:**

- Division with remainders (all problems divide evenly in this tool)
- Division where dividend < divisor (e.g., 3 ÷ 5) — not in Unit 4 scope for equal groups
- Quotitive division before partitive has been introduced
- Both division types in the same problem (one problem = one type; comparison is across problems)
- "Which is bigger, the dividend or divisor?" — teaches a false rule (Misconception A1)

### Visual/Teaching Constraints (What Remediation Tools Support)

| Feature | Constraint | Notes |
| --- | --- | --- |
| Sequential highlighting | One group at a time | For counting animations |
| Within-group item highlighting | One group at a time | For counting items animations |
| Connection lines to equations | Only when equation is also displayed | Visual-symbolic bridge |
| Zoom on group | Optional; may not implement for all contexts | Resource-dependent |

### Unit 4: Visual/Teaching Constraints (What Remediation Tools Support)

| Feature | Constraint | Notes |
| --- | --- | --- |
| Partitive distribution demo (Unit 4) | Requires: ungrouped items + visible empty containers | Containers = divisor |
| Quotitive grouping demo (Unit 4) | Requires: ungrouped items + group size label visible | No containers at start |
| Division connection lines (Unit 4) | Only when division equation is also displayed | Maps to ÷ equation, not × |
| Dual-reading overlay (Unit 4) | Only after both × and ÷ introduced for that fact set | Shows both equations simultaneously |
| Reverse skip-counting (Unit 4) | Optional — supplements quotitive understanding | Descending count from total |
| Reset to ungrouped (Unit 4) | Available for retry and for transitioning between division type demos | Returns to pre-division state |

## Layout Constraints

- UX to determine positioning

| Constraint | Value | Notes |
| --- | --- | --- |
| Groups displayed | 2-6 groups typical | Avoid overwhelming visual complexity |
| Items per group | 2-10 items typical | Must be countable at glance |
| Can appear with | Equation Builder, word problems, picture graphs (M9 connection) | Common pairings |
| Cannot appear with | Multiple equal groups visuals simultaneously | Focus on one scenario at a time |
| Visual orientation | Both horizontal and vertical arrangements | Flexibility throughout |

**Unit 1 Common Layout Patterns:**

- **M7:** Equal groups visual (left or top) + Guide narration (right or bottom)
- **M8:** Equal groups visual (left) + Equation Builder (right)
- **M9:** Picture graph (top) + Equal groups visual (bottom) for "scales are multiplication" connection
- **M10:** Word problem (top) + Equal groups visual (center) + Equation Builder (bottom)

**Unit 4 Division Layout Patterns:**

- **Section A intro:** Ungrouped items + containers/reference → division process → completed groups + Guide narration
- **Section A with equation:** Completed division display (left) + Equation Builder showing ÷ equation (right)
- **Section A comparison:** Partitive result (left) + Quotitive result (right) — same numbers, different process, same end state
- **Section B dual reading:** Equal groups visual (center) + Multiplication equation (top-right) + Division equation (bottom-right)
- **Section B fact family:** Equal groups visual (left) + Fact Family display in Equation Builder (right) — all 4 equations visible

## Tool to Schema Vocab Translation

- Engineering to complete

| Curriculum Term | Schema Property | Notes |
| --- | --- | --- |
| "concrete context (bags)" | `context_type: "bags", abstraction_level: "concrete"` | M7 Early |
| "concrete context (boxes)" | `context_type: "boxes", abstraction_level: "concrete"` | M7 Early |
| "circles with dots" | `context_type: "circles", abstraction_level: "semi_abstract"` | M7 Mid-Late, M8, M9 |
| "spatial groups" | `context_type: "spatial", abstraction_level: "abstract"` | M8 Late |
| "context variety: kitchen" | `context_type: "kitchen", abstraction_level: "concrete_variety"` | M9-M10 |
| "context variety: garden" | `context_type: "garden", abstraction_level: "concrete_variety"` | M9-M10 |
| "number of groups" | `groups: 4` | Equal groups property |
| "items per group" | `items_per_group: 5` | Equal groups property |
| "highlight group" | `highlighted_group: 2` | Interaction state (0-indexed or 1-indexed?) |
| "horizontal orientation" | `orientation: "horizontal"` | Groups arranged left-to-right |
| "vertical orientation" | `orientation: "vertical"` | Groups arranged top-to-bottom |

## Curriculum Animators Techs

- Waiting on engineering implementation

*CAT team will document workflow once equal groups visual implementation is*

## Open Questions

- [ ]  **Zoom feature?:** Implement across all contexts or only certain types (bags/boxes)?
- [ ]  **Highlight persistence:** Stay highlighted until new click, or auto-deselect after delay?
- [ ]  **Sequential highlighting speed:** What pace for counting animations? (1 second per group? Adjustable?)
- [ ]  **Connection line style:** Solid, dashed, arrows, color-coded?
- [ ]  **Container variety:** How many different container types (bags, boxes, circles)? Standardize?
- [ ]  **Emoji style consistency:** Uniform style across all contexts or context-specific styles?
- [ ]  **Maximum items per group:** Hard cap at 10, or allow 12 for dozen contexts?
- [ ]  **Spatial grouping animation:** Items "gathering" into groups animation on initial display?
- [ ]  **Within-group item highlighting:** Individual items highlight during counting feedback?
- [ ]  **Hover preview:** Show count on hover without requiring click?
- [ ]  **Internal arrangement control:** Should curriculum/CAT specify internal arrangement, or auto-generated?

**Unit 4 Division Questions:**

- [ ]  **Ungrouped item display (Unit 4):** How should items appear before division? (pile, line, scattered, etc.) May vary by abstraction level.
- [ ]  **Quotitive "group size reference" display (Unit 4):** How should the group size (divisor) be communicated? (example group, numeric label, both?)
- [ ]  **10-group display arrangement (Unit 4):** How to handle 8–10 groups without overwhelming the visual? (2 rows of 5? Smaller items? Grid?)
- [ ]  **Division type indicator (Unit 4):** Should there be an on-screen label identifying "Sharing" vs. "Grouping," or is this guide-script territory only?
- [ ]  **Process skip threshold (Unit 4):** After how many exposures can the division process be skipped to show end state directly? Per division type or global?
- [ ]  **Transition from process to static end state (Unit 4):** How should the division process resolve into the final static display?

## JSON Schema Formatting

[20260209-0025-10.3827252.mp4](20260209-0025-10.3827252.mp4)

[20260209-0022-28.8451105.mp4](20260209-0022-28.8451105.mp4)

![image.png](image%204.png)

![image.png](image%205.png)

![image.png](image%206.png)

![image.png](image%207.png)

![image.png](image%208.png)

![image.png](image%209.png)

![image.png](image%2010.png)

![image.png](image%2011.png)

[20260209-0015-03.6547269.mp4](20260209-0015-03.6547269.mp4)
---

