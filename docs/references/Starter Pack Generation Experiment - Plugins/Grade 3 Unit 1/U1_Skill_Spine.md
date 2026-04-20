═══════════════════════════════════════════════════════════════
UNIT 1: Data and Scaled Graphs — SKILL SPINE v1
═══════════════════════════════════════════════════════════════

UNIT CONTEXT
─────────────────────────────────────────────────────────────
Grade: 3
Module Count: 12
Concept Thread Count (from Conceptual Spine): 12 (excluding optional L21 Integrated Application)
Skill Thread Count (this spine): 15 parent + 3 sub-skills = 18 knowledge graph nodes
Ratio (skill:concept): 1.25x (parent skills only; 1.5x including sub-skills)
§1.8.5 Calibration Data: None available (no G3U1 Starter Packs exist)

Note on ratio: 1.25x (parent only) is below the suggested 1.5x minimum,
but including sub-skills brings it to 1.5x. The multiplication domain
(M7-M12) features a sequential chain of concept introductions, each
building one new capability per module. Artificially splitting these would
create skills without independent assessable presence across multiple
modules. The data domain's CompareData sub-skills provide the additional
granularity needed for the knowledge graph without over-decomposing the
multiplication domain. See Scoping Decisions Log for detailed rationale.

CONCEPT-TO-SKILL ALIGNMENT
─────────────────────────────────────────────────────────────

Concept: Single-Unit Data Representation (M1)
  └── ReadPicGraph — Read values from picture graphs
  └── ReadBarGraph — Read values from bar graphs
  └── CompareData — Compare data across graph categories
      ├── CompareData:ordinal — most/least/fewest
      ├── CompareData:difference — how many more/fewer
      └── CompareData:combination — how many in all

Concept: Scaled Picture Graphs (M2-M3)
  └── ReadPicGraph — Read values from picture graphs
  └── CreatePicGraph — Create scaled picture graphs
  └── InterpretHalfScale — Represent non-round values (half-symbols/interpolation)
  └── CompareData — Compare data (picture graph context)

Concept: Scaled Bar Graphs (M4-M5)
  └── ReadBarGraph — Read values from bar graphs
  └── CreateBarGraph — Create scaled bar graphs
  └── InterpretHalfScale — Represent non-round values (half-symbols/interpolation)
  └── SelectScale — Select an appropriate graph scale
  └── CompareData — Compare data (bar graph context)

Concept: Data-Based Problem Solving (M6)
  └── CompareData — Compare data across graph categories
  └── SolveMultiStepData — Solve multi-step data problems

Concept: Equal Groups as Multiplication (M7)
  └── IdentifyEqualGroups — Identify equal groups structure

Concept: Multiplication Expressions (M8)
  └── WriteMultExpression — Write multiplication expressions from visual groups
  └── InterpretMultExpression — Interpret multiplication expressions as visual groups

Concept: Multiplication Equations (M10)
  └── SolveMultEquation — Write multiplication equations with unknowns

Concept: Factor-Specific Fluency (M9)
  └── LearnFactorProducts — Achieve factor fluency with 2s, 5s, 10s

Concept: Arrays as Physical Objects (M11 early)
  └── BuildArray — Describe and build arrays

Concept: Arrays as Drawings/Diagrams (M11 mid-late)
  └── BuildArray — Describe and build arrays

Concept: Array Problem Solving (M12 early-mid)
  └── BuildArray — Describe and build arrays
  └── ApplyCommutative — Apply commutative property (turn-around facts)

Concept: Commutative Property (M12 mid-late)
  └── ApplyCommutative — Apply commutative property (turn-around facts)

Note: InterpretHalfScale (half-symbols/interpolation) bridges two concept threads
(Scaled Picture Graphs and Scaled Bar Graphs). This is intentional:
the "half of the scale value" concept is introduced with scale 2 (M2)
and applied to scale 10 (M4), connecting the two representation domains.

SKILL THREADS
─────────────────────────────────────────────────────────────

ReadPicGraph — Read values from scaled picture graphs
  Description:    Read a specific data value from a picture graph by using the key/scale to determine the count represented by symbols (including scaled symbols).
  Component:      conceptual
  Primary Verb:   identify
  Representations: picture graph (1:1 in M1, 1:2 in M2, 1:5 in M3)
  Thread Type:    progressive → terminal (picture graph focus ends after M3)
  Introduced:     M1 — Read 1:1 picture graphs (each symbol = 1 item); identify most, least, total, difference
  Practiced:      M2 — Read scaled (1:2) picture graphs; interpret whole and half symbols
                  M3 — Read scaled (1:5) picture graphs; connect to skip-counting by 5s
  Extended:       (none — reading skill transfers to bar graphs after M3)
  Transforms:     M4 → ReadBarGraph (reading skill continues in bar graph format)
  Misconceptions: 1 (Counting Symbols Instead of Scaling), 2 (Scale Means Addition), 16 (Graph as Picture)
  Standards:      2.MD.D.10, 3.MD.B, 3.MD.B.3
  EC Appearances: M1 (bar graph reading tested, not picture — see ReadBarGraph), M2 (implicit in creation check), M3 (implicit in creation)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  likely LC alignment exists (graph reading is a fundamental skill track)

ReadBarGraph — Read values from scaled bar graphs
  Description:    Read a specific data value from a bar graph by interpreting the scaled axis, including values at tick marks and halfway points.
  Component:      conceptual
  Primary Verb:   identify
  Representations: bar graph (1:1 in M1, 1:10 in M4, various scales M5-M6; both orientations)
  Thread Type:    progressive
  Introduced:     M1 — Read 1:1 bar graphs (scale of 1, both orientations)
  Practiced:      M4 — Read 1:10 bar graphs including halfway-point interpolation (multiples of 5)
                  M5 — Read bar graphs at various scales as part of scale selection evaluation
                  M6 — Read pre-made bar graphs (various scales, both orientations) to extract data for problem solving
  Extended:       M6 — Full independence reading unfamiliar graphs (no data table provided); multiple scales and orientations mixed
  Misconceptions: 1 (Counting Symbols Instead of Scaling), 5 (Can't Interpolate Bar Heights), 16 (Graph as Picture)
  Standards:      2.MD.D.10, 3.MD.B, 3.MD.B.3
  EC Appearances: M1 (bar graph reading), M4 (bar graph with mix of multiples), M6 (read pre-made graphs for problem solving)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  likely LC alignment exists

CreatePicGraph — Create scaled picture graphs
  Description:    Construct a picture graph by calculating and placing the correct number of symbols (whole and half) to represent data values at the given scale.
  Component:      procedural
  Primary Verb:   create
  Representations: picture graph (1:1 in M1, 1:2 in M2, 1:5 in M3)
  Thread Type:    progressive → terminal (transitions to bar graph creation after M3)
  Introduced:     M1 — Create 1:1 picture graph with collected data (warm-up; limited scaffolding)
                  M2 — Create scaled (1:2) picture graphs: even numbers (whole symbols) then odd numbers (half-symbols); pre-fill decreases 3→2→0
  Practiced:      M3 — Create scaled (1:5) picture graphs (multiples of 5 only; no half-symbols); pre-fill 2→1→0
  Extended:       (none — picture graph creation terminates; bar graphs take over in M4)
  Transforms:     M3 late → CreateBarGraph (students create bar graphs starting mid-M3)
  Misconceptions: 1 (Counting Symbols Instead of Scaling), 2 (Scale Means Addition), 3 (Can't Create Fractional Symbols)
  Standards:      2.MD.D.10, 2.NBT.B.5, 3.MD.B, 3.MD.B.3
  EC Appearances: M2 (create picture graph with half-symbols), M3 (create picture graph, multiples of 5)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  likely LC alignment exists

CreateBarGraph — Create scaled bar graphs
  Description:    Construct a bar graph by setting bar heights to accurately represent data values on a scaled axis, including at tick marks and halfway points.
  Component:      procedural
  Primary Verb:   create
  Representations: bar graph (1:5 in M3, 1:10 in M4, various scales in M6)
  Thread Type:    progressive → terminal (graph creation ends after M6)
  Introduced:     M3 late — Create bar graphs with scale 5 (introduced alongside picture graph comparison; multiples of 5 only)
  Practiced:      M4 — Create bar graphs with scale 10: multiples of 10 first (snap-to-10), then halfway points (multiples of 5); gridline scaffolding fades; pre-set decreases 3→0 bars
  Extended:       M6 — Create bar graphs as prerequisite to problem solving (Activities 1-3, 7-9); scale pre-set; full independence
  Misconceptions: 1 (Counting Symbols), 5 (Can't Interpolate Bar Heights)
  Standards:      3.MD.B, 3.MD.B.3
  EC Appearances: M4 (create bar graph, mix of multiples and halfway points)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  likely LC alignment exists

InterpretHalfScale — Represent non-round values using half-symbols or interpolation
  Description:    Apply the "half of the scale value" concept to represent data values that are not exact multiples of the scale — using half-symbols in picture graphs (half of 2 = 1) and halfway-point bar placement in bar graphs (half of 10 = 5).
  Component:      conceptual
  Primary Verb:   apply
  Representations: picture graph (half-symbols, M2) → bar graph (interpolation, M4). Same concept across representations.
  Thread Type:    progressive (two teaching moments linked by "half of scale" concept)
  Introduced:     M2 mid — Half-symbols with scale of 2 (half of 2 = 1); explicit teaching with animation; even/odd connection
  Practiced:      M2 late, M2 EC — Independent half-symbol placement with odd numbers
  Extended:       M4 — Interpolation at halfway points with scale of 10 (half of 10 = 5); guide: "Remember half-symbols from scale of 2? Same idea here."
  Misconceptions: 3 (Can't Create Fractional Symbols), 5 (Can't Interpolate Bar Heights)
  Standards:      3.MD.B, 3.MD.B.3
  EC Appearances: M2 (half-symbols required for odd values), M4 (mix of multiples and non-multiples)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  likely LC alignment exists (half-symbol/interpolation is a distinct subskill)

CompareData — Compare data across graph categories [PARENT SKILL]
  Description:    Use graph data to answer comparison questions ("how many more/fewer," "how many in all") by reading values and performing one-step addition or subtraction. PARENT SKILL — decomposes into three sub-skills at the template level by operation type.
  Component:      conceptual (parent-level; sub-skills vary — see below)
  Primary Verb:   compare (parent-level; sub-skills vary — see below)
  Representations: picture graph (M1-M3) → bar graph (M1, M4-M6). Comparison operations apply across both representations; difficulty increases with scale complexity and graph type.
  Thread Type:    progressive
  Introduced:     M1 — Simple comparison on 1:1 graphs (most, least, total, difference); guide models comparison language
  Practiced:      M2 — Comparison after creation ("How many fewer chose X than Y?"; "How many in all?")
                  M3 — Comparison across scales (same data, 1:2 vs 1:5 — which needs fewer symbols?)
                  M4 — Comparison with scale 10 including halfway-point values
                  M5 — Comparison as part of scale selection evaluation
  Extended:       M6 — One-step comparison and total problems using pre-made graphs (Activities 4-6, 10-12); reading from graph only (no data table)
  Misconceptions: 6 ("More Than" Means Add), 16 (Graph as Picture), 17 (All Data Must Be Used)
  Standards:      2.OA.C.3, 3.MD.B.3
  EC Appearances: M1 (simple reading/comparison), M6 (one-step problems within mixed EC)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  LC likely splits by operation type AND representation — ordinal/difference may align to comparison standards, combination may align to addition/problem-solving standards. Representation context (picture vs bar graph) may map to separate LC components.
  Sub-skills:     CompareData:ordinal, CompareData:difference, CompareData:combination

  ┌─ CompareData:ordinal — Compare data: ordinal (most/least/fewest)
  │  Description:    Identify the category with the most, least, or fewest items by comparing bar heights or symbol counts across a graph.
  │  Component:      conceptual
  │  Primary Verb:   compare
  │  Representations: picture graph (M1-M3) + bar graph (M1, M4-M6)
  │  Misconceptions: 16 (Graph as Picture — reads graph as illustration rather than data)
  │  Template Design: Workspace shows a graph; student selects the category that answers "which has the most/fewest." Different template variants for picture graph vs bar graph contexts.
  │  EC Appearances: M1 (ordinal comparison is part of "answer data questions")
  │  Notes:         Simplest comparison operation — no arithmetic required. Serves as the confidence-tier entry point for CompareData.

  ├─ CompareData:difference — Compare data: difference (how many more/fewer)
  │  Description:    Determine "how many more" or "how many fewer" between two categories by reading values from a graph and computing the difference.
  │  Component:      conceptual
  │  Primary Verb:   compare
  │  Representations: picture graph (M1-M3) + bar graph (M1, M4-M6)
  │  Misconceptions: 6 ("More Than" Means Add — adds values instead of subtracting), 17 (All Data Must Be Used — includes irrelevant categories)
  │  Template Design: Workspace shows a graph; prompt asks "how many more/fewer X than Y." Requires reading two values and subtracting. Picture graph variants use symbol counting; bar graph variants use axis reading.
  │  EC Appearances: M1 (difference questions in data EC), M6 (one-step comparison problems)
  │  Notes:         Core comparison operation. Language direction ("more" vs "fewer") is a known difficulty factor — templates should vary this.

  └─ CompareData:combination — Compare data: combination (in all / total)
     Description:    Determine "how many in all" or a total across categories by reading values from a graph and computing the sum.
     Component:      transfer
     Primary Verb:   apply
     Representations: picture graph (M1-M3) + bar graph (M1, M4-M6)
     Misconceptions: 6 ("More Than" Means Add — inverse: confuses "in all" with comparison), 17 (All Data Must Be Used — includes all categories when only some are specified)
     Template Design: Workspace shows a graph; prompt asks "how many in all" for specified categories. Requires reading multiple values and adding. Bar graph variants with interpolation (M4+) are harder than picture graph variants.
     EC Appearances: M6 (combination problems in mixed EC)
     Notes:         Classified as transfer (not conceptual) because it requires applying addition in a data context, not just comparing. This is the bridge to SolveMultiStepData, which extends combination into multi-step territory.

SelectScale — Select an appropriate graph scale
  Description:    Evaluate a data set's range and characteristics to choose the most appropriate scale (2, 5, or 10) for a bar graph, using preview/comparison tools and providing justification.
  Component:      transfer
  Primary Verb:   apply
  Representations: bar graph only (M5)
  Thread Type:    emergent → terminal (M5 only)
  Introduced:     M5 early — Binary choice (scale 5 or 10) with preview system; guide scaffolds: "Look at your highest number"
  Practiced:      M5 mid — Three scale options (2, 5, 10); guide demonstrates poor choice first (bar goes off graph); student evaluates with preview
  Extended:       M5 late — Full evaluation of tradeoffs; compare student's choice to alternatives; pattern discovery (small → scale 2, medium → scale 5, large → scale 10)
  Misconceptions: 4 (Wrong Scale Selection)
  Standards:      3.MD.B.3
  EC Appearances: M5 (given dataset → choose scale → justify)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  likely LC alignment exists (meta-cognitive skill may be a distinct LC target)

SolveMultiStepData — Solve multi-step data problems
  Description:    Solve two-step "how many more/fewer" and combination problems using data from scaled bar graphs, identifying the required operations and executing them in sequence.
  Component:      transfer
  Primary Verb:   apply
  Representations: bar graph only (M6; various scales, both orientations)
  Thread Type:    emergent → terminal (M6 only; extends CompareData comparison into multi-operation territory)
  Introduced:     M6 Activities 7-9 — Two-step problems with scaffolded step decomposition ("What should you find first?"); guide breaks problem into steps
  Practiced:      M6 Activities 8-9 — Reduced then removed step prompting
  Extended:       M6 Activities 10-12 — Mixed one-step and two-step problems; student must identify structure independently; no scaffolding within problems
  Misconceptions: 7 (Combining Before Comparing), 6 ("More Than" Means Add), 17 (All Data Must Be Used)
  Standards:      3.MD.B.3
  EC Appearances: M6 (2 two-step problems in EC, mixed with 1 one-step)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  likely LC alignment exists (multi-step problem solving is typically an LC progression point)

IdentifyEqualGroups — Identify equal groups structure
  Description:    Recognize equal groups in various contexts (bags, boxes, rows, stacks, circles with dots) and accurately count the number of groups and items per group.
  Component:      conceptual
  Primary Verb:   identify
  Thread Type:    progressive
  Introduced:     M7 — Recognize equal groups in bags/boxes; count groups and items per group; guide models "X groups of Y" language; graph-to-multiplication bridge in warm-up
  Practiced:      M8 — Identify group structure as precursor to writing expressions; bags/boxes contexts; recognition becomes prerequisite for notation
  Extended:       M10 — Identify equal groups in varied contexts (rows, stacks, groups, animals); guide explicitly announces variety; structure language maintained ("___ groups/rows/stacks of ___")
  Misconceptions: 9 (Array Dimensions as Addition), 10 (Groups vs. Size Confusion), 11 (Multiplication Only Adds)
  Standards:      2.NBT.B.5, 3.OA.A.1
  EC Appearances: M7 ("How many groups? Items per group?"), M8 (implicit in expression EC), M10 (implicit in equation EC)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  likely LC alignment exists

WriteMultExpression — Write multiplication expressions from visual groups
  Description:    Translate a visual equal-groups scenario into a multiplication expression (e.g., see 3 groups of 4 → write "3 × 4"), with first number representing groups and second representing items per group.
  Component:      procedural
  Primary Verb:   create
  Thread Type:    progressive
  Introduced:     M8 early — Select matching expression from multiple choice (recognition before construction)
  Practiced:      M8 mid — Build expressions using equation builder (drag-drop tiles into ___ × ___ template)
                  M8 late — Full independence with all methods; bidirectional practice
  Extended:       M10 — Write expressions as part of complete equations; varied contexts (not just bags/boxes)
  Misconceptions: 10 (Groups vs. Size Confusion — factor reversal: 3×4 for 4 groups of 3), 11 (Multiplication Only Adds), 12 (Times Means Plus)
  Standards:      3.OA.A.1, 3.OA.A.3
  EC Appearances: M8 (visual → build expression), M10 (expression as part of equation)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  likely LC alignment exists

InterpretMultExpression — Interpret multiplication expressions as visual groups
  Description:    Given a multiplication expression (e.g., "2 × 6"), identify or create the corresponding visual representation (2 groups of 6 items), demonstrating understanding of what the expression means.
  Component:      transfer
  Primary Verb:   connect
  Thread Type:    emergent → progressive (emerges in M8, continues into M10)
  Introduced:     M8 mid — Given expression → select matching visual from options; guide: "2 × 6 means 2 groups with 6 in each group. Which picture shows that?"
  Practiced:      M8 late — Given expression → select or create matching visual; full bidirectional fluency
  Extended:       M10 — Expression → construction (given "5 × ☐ = 15," specify groups to match); applied as part of equation interpretation
  Misconceptions: 10 (Groups vs. Size Confusion), 12 (Times Means Plus)
  Standards:      3.OA.A.1 (specifically: "describe a context in which a total number of objects can be expressed as 5 × 7")
  EC Appearances: M8 (expression → select matching visual)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  likely LC alignment exists (bidirectional understanding is often an LC target)

LearnFactorProducts — Achieve factor fluency with 2s, 5s, 10s
  Description:    Recall products of 2, 5, and 10 with increasing automaticity through pattern discovery (2s are even, 5s end in 0 or 5, 10s end in 0) and repeated practice, connecting to skip-counting and graph scale callbacks.
  Component:      conceptual
  Primary Verb:   identify
  Thread Type:    emergent → terminal (M9 only, but fluency supports downstream skills)
  Introduced:     M9 Activities 1-3 — Pattern discovery: highlight multiples, discover rules (2s even, 5s end 0/5, 10s end 0); graph callback: "These were our SCALES!"
  Practiced:      M9 Activities 4-6 — Product selection (given 7 × 2 = ?, select product); mix of 2s, 5s, 10s
  Extended:       M9 Activities 7-9 — Rapid recall; turn-around facts previewed (7×2 AND 2×7); all three factors mixed; building automaticity
  Misconceptions: 18 (Skip Counting Without Meaning), 20 (Memorization Without Relationships)
  Standards:      3.OA.A.1, 3.OA.A.3, 3.OA.D.9
  EC Appearances: M9 (mix of 2s, 5s, 10s; product selection or equation building)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  likely LC alignment exists (factor fluency is a tracked progression)

SolveMultEquation — Write multiplication equations with unknowns
  Description:    Construct complete multiplication equations (expression = product) and solve for unknown values in any position (unknown product: 3 × 4 = ☐; unknown first factor: ☐ × 4 = 12; unknown second factor: 3 × ☐ = 12), understanding that = means "same value as."
  Component:      procedural
  Primary Verb:   create
  Thread Type:    emergent → terminal (M10 only, but capstone of multiplication expression/equation progression)
  Introduced:     M10 Activities 1-3 — All values given; arrange tiles into equation; = sign flexibility (3 × 4 = 12 AND 12 = 3 × 4)
  Practiced:      M10 Activities 4-5 — Unknown product with variety of contexts (rows, stacks, groups); guide announces context variety explicitly
  Extended:       M10 Activities 6-8 — Unknown as first or second factor; language prompts alongside symbolic equations; multiple activity types (visual → equation, specification → equation, expression → construction)
  Misconceptions: 14 (Unknown Must Be Last), 19 (Equal Sign as "Put Answer Here"), 15 (Can't Use Inverse Operations)
  Standards:      3.OA.A.1, 3.OA.A.3, 3.OA.A.4, 3.OA.C.7, 3.OA.D.9
  EC Appearances: M10 (variety of contexts; unknown in middle or beginning position)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  likely LC alignment exists

BuildArray — Describe and build arrays
  Description:    Construct or specify array structure (rows × items per row OR columns × items per column), describe arrays using precise language ("___ rows of ___" or "___ columns of ___"), and write the multiplication expression that matches the chosen description.
  Component:      procedural
  Primary Verb:   create
  Thread Type:    progressive
  Introduced:     M11 Activities 1-3 — Concrete arrays (egg cartons, 2×3, 2×6); teach convention (rows first: 2 × 3); then teach flexibility (can also describe as columns: 3 × 2); critical emphasis: "Your WORDS must match your EXPRESSION"
  Practiced:      M11 Activities 4-5 — Mix of concrete (muffin tins) and abstract (dot arrays); moderate factors (3-7); specify structure then write expression; guide: "Did you use rows or columns? Your expression must match."
                  M11 Activities 6-9 — Primarily dot arrays; larger factors (up to 9); full independence
  Extended:       M12 Activities 1-2 — Write BOTH expressions for same array (highlighting review); toggle row/column highlighting
                  M12 Activities 3-5 — Create multiple arrays from same total; discover turn-around pairs
  Misconceptions: 8 (Rows/Columns Confusion), 9 (Array Dimensions as Addition), 10 (Groups vs. Size Confusion)
  Standards:      2.OA.C.4, 3.OA.A.1
  EC Appearances: M11 (identify array structure, match expression), M12 (both expressions for same array)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  likely LC alignment exists

ApplyCommutative — Apply commutative property (turn-around facts)
  Description:    Recognize that changing the order of factors does not change the product (3 × 4 = 4 × 3), demonstrated through both highlighting (same array, two descriptions) and rotation (physical 90° turn), and apply this property strategically to solve problems using known facts.
  Component:      transfer
  Primary Verb:   connect
  Thread Type:    emergent → terminal (M12 only, but capstone of unit)
  Introduced:     M12 warm-up — Rotation animation preview; question: "Did the total change?"
                  M12 Activities 1-2 — Highlighting review: toggle row/column views, write both expressions
  Practiced:      M12 Activities 3-5 — Discovery: create arrays from same total; rotation animation proves property; guide: "Two ways to understand why 5×4 = 4×5"
  Extended:       M12 Activities 6-8 — Property application: given 6×7=42, what's 7×6?; distinguish equivalent (rotated) from different (different shape) arrays; strategic use: "Which way is easier to count?"
  Misconceptions: 13 (Order Changes Answer)
  Standards:      3.OA.A.1, 3.OA.A.3, 3.OA.B.5, 3.OA.C.7, 3.OA.D.9
  EC Appearances: M12 (both expressions for array, predict after rotation, recognize equivalent vs different arrays)
  §1.8.5 Calibration: No §1.8.5 available
  LC Breadcrumb:  likely LC alignment exists (commutative property is a milestone)

CROSS-MODULE MATRIX
─────────────────────────────────────────────────────────────

Skill ID                │ Skill (short)              │ M1  │ M2  │ M3  │ M4  │ M5  │ M6  │ M7  │ M8  │ M9  │ M10 │ M11 │ M12
────────────────────────┼────────────────────────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────
ReadPicGraph            │ Read picture graphs        │ INT │ PRC │ PRC │     │     │     │     │     │     │     │     │
ReadBarGraph            │ Read bar graphs            │ INT │     │     │ PRC │ PRC │ EXT │     │     │     │     │     │
CreatePicGraph          │ Create picture graphs      │ INT │ INT │ PRC │     │     │     │     │     │     │     │     │
CreateBarGraph          │ Create bar graphs          │     │     │ INT │ PRC │     │ EXT │     │     │     │     │     │
InterpretHalfScale      │ Half-symbols/interpolation │     │ INT │     │ EXT │     │     │     │     │     │     │     │
CompareData             │ Compare data [PARENT]      │ INT │ PRC │ PRC │ PRC │ PRC │ EXT │     │     │     │     │     │
  :ordinal              │   └ most/least/fewest      │ INT │ PRC │ PRC │ PRC │     │     │     │     │     │     │     │
  :difference           │   └ how many more/fewer    │ INT │ PRC │ PRC │ PRC │ PRC │ EXT │     │     │     │     │     │
  :combination          │   └ in all / total         │ INT │ PRC │ PRC │ PRC │     │ EXT │     │     │     │     │     │
SelectScale             │ Select scale               │     │     │     │     │ INT │     │     │     │     │     │     │
SolveMultiStepData      │ Multi-step problems        │     │     │     │     │     │ INT │     │     │     │     │     │
IdentifyEqualGroups     │ Identify equal groups      │     │     │     │     │     │     │ INT │ PRC │     │ EXT │     │
WriteMultExpression     │ Write expressions          │     │     │     │     │     │     │     │ INT │     │ PRC │     │
InterpretMultExpression │ Interpret expressions      │     │     │     │     │     │     │     │ INT │     │ EXT │     │
LearnFactorProducts     │ Factor fluency (2,5,10)    │     │     │     │     │     │     │     │     │ INT │     │     │
SolveMultEquation       │ Equations with unknowns    │     │     │     │     │     │     │     │     │     │ INT │     │
BuildArray              │ Describe/build arrays      │     │     │     │     │     │     │     │     │     │     │ INT │ PRC
ApplyCommutative        │ Commutative property       │     │     │     │     │     │     │     │     │     │     │     │ INT

Key: INT = Introduced, PRC = Practiced, EXT = Extended, TRN = Transforms into another skill
     (blank) = skill not active in this module
     Indented :qualifier rows are sub-skills of the parent above them. Sub-skills inherit
     the parent's module range but may have narrower presence (e.g., :ordinal absent from M5-M6).

Observations:
- Clear two-domain structure: M1-M6 data domain, M7-M12 multiplication domain
- No skill thread crosses the M6→M7 MAJOR TRANSITION boundary
- CreatePicGraph → CreateBarGraph transformation at M3 (picture → bar graph creation)
- ReadPicGraph → ReadBarGraph transformation at M4 (picture → bar graph reading)
- M7 is the thinnest module (only IdentifyEqualGroups introduced) — appropriate since it's the conceptual bridge module focused on structural recognition
- M9 and M12 each contain a single-module skill (LearnFactorProducts, ApplyCommutative) — justified because both have full lesson + EC + practice coverage

COMPONENT DISTRIBUTION
─────────────────────────────────────────────────────────────

Parent skills only (15):
Component    │ Count │ % of Total │ Target    │ Status
─────────────┼───────┼────────────┼───────────┼────────
Procedural   │ 5     │ 33%        │ 30-40%    │ ✅
Conceptual   │ 6     │ 40%        │ 30-40%    │ ✅ (at boundary)
Transfer     │ 4     │ 27%        │ 20-30%    │ ✅

Including sub-skills (18 knowledge graph nodes):
Component    │ Count │ % of Total │ Target    │ Status
─────────────┼───────┼────────────┼───────────┼────────
Procedural   │ 5     │ 28%        │ 30-40%    │ ⚠️ (below; no sub-skills are procedural)
Conceptual   │ 8     │ 44%        │ 30-40%    │ ⚠️ (above; +ordinal, +difference)
Transfer     │ 5     │ 28%        │ 20-30%    │ ✅ (+combination)

Procedural skills: CreatePicGraph, CreateBarGraph, WriteMultExpression, SolveMultEquation, BuildArray
Conceptual skills: ReadPicGraph, ReadBarGraph, InterpretHalfScale, CompareData (parent), CompareData:ordinal, CompareData:difference, IdentifyEqualGroups, LearnFactorProducts
Transfer skills: CompareData:combination, SelectScale, SolveMultiStepData, InterpretMultExpression, ApplyCommutative

VERB DISTRIBUTION
─────────────────────────────────────────────────────────────

Parent skills only (15):
Verb         │ Count │ % of Total │ Notes
─────────────┼───────┼────────────┼────────────────────────
create       │ 5     │ 33%        │ CreatePicGraph, CreateBarGraph, WriteMultExpression, SolveMultEquation, BuildArray
identify     │ 4     │ 27%        │ ReadPicGraph, ReadBarGraph, IdentifyEqualGroups, LearnFactorProducts
compare      │ 1     │ 7%         │ CompareData (parent)
apply        │ 3     │ 20%        │ InterpretHalfScale, SelectScale, SolveMultiStepData
connect      │ 2     │ 13%        │ InterpretMultExpression, ApplyCommutative

Including sub-skills (18 knowledge graph nodes):
Verb         │ Count │ % of Total │ Notes
─────────────┼───────┼────────────┼────────────────────────
create       │ 5     │ 28%        │ (unchanged)
identify     │ 4     │ 22%        │ (unchanged)
compare      │ 3     │ 17%        │ CompareData (parent), :ordinal, :difference — comparison is now well-represented
apply        │ 4     │ 22%        │ InterpretHalfScale, SelectScale, SolveMultiStepData, CompareData:combination
connect      │ 2     │ 11%        │ (unchanged)

Note: The sub-skill decomposition resolves the previous concern about low "compare" count.
CompareData:combination uses "apply" (not "compare") because totaling across categories
requires applying addition in a data context — it's closer to problem-solving than comparison.

COVERAGE CHECKS
─────────────────────────────────────────────────────────────

Standards Coverage:
  All standards from Standards Mapping covered? Yes

  Standard     │ Where Addressed │ Covered By
  ─────────────┼─────────────────┼──────────────────────
  2.MD.D.10    │ M1              │ ReadPicGraph, ReadBarGraph, CreatePicGraph
  2.NBT.B.5   │ M2, M7          │ CreatePicGraph, IdentifyEqualGroups
  2.OA.C.3    │ M1, M6          │ ReadPicGraph, CompareData, SolveMultiStepData
  2.OA.C.4    │ M11             │ BuildArray
  3.MD.B      │ M1-M4           │ ReadPicGraph, ReadBarGraph, CreatePicGraph, CreateBarGraph, InterpretHalfScale
  3.MD.B.3    │ M3-M6           │ CreatePicGraph, CreateBarGraph, InterpretHalfScale, CompareData, SelectScale, SolveMultiStepData
  3.OA.A.1    │ M7-M12          │ IdentifyEqualGroups, WriteMultExpression, InterpretMultExpression, LearnFactorProducts, SolveMultEquation, BuildArray, ApplyCommutative
  3.OA.A.3    │ M8-M10, M12     │ WriteMultExpression, LearnFactorProducts, SolveMultEquation, ApplyCommutative
  3.OA.A.4    │ M10             │ SolveMultEquation
  3.OA.B.5    │ M12             │ ApplyCommutative
  3.OA.C.7    │ M12             │ SolveMultEquation, ApplyCommutative
  3.OA.D.9    │ M9, M10, M12    │ LearnFactorProducts, SolveMultEquation, ApplyCommutative
  3.NBT.A.2   │ M12 (building toward) │ Not yet assessed — building toward only

Misconception Coverage:
  All misconceptions from Misconceptions tab addressable? Yes

  ID    │ Misconception (short)                │ Detectable via Skill     │ Status
  ──────┼──────────────────────────────────────┼──────────────────────────┼────────
  1     │ Counting Symbols Instead of Scaling   │ ReadPicGraph, CreatePicGraph, InterpretHalfScale            │ ✅
  2     │ Scale Means Addition                  │ ReadPicGraph, CreatePicGraph                 │ ✅
  3     │ Can't Create Fractional Symbols       │ InterpretHalfScale                      │ ✅
  4     │ Wrong Scale Selection                 │ SelectScale                      │ ✅
  5     │ Can't Interpolate Bar Heights         │ ReadBarGraph, InterpretHalfScale                 │ ✅
  6     │ "More Than" Means Add                 │ CompareData:difference, CompareData:combination, SolveMultiStepData │ ✅
  7     │ Combining Before Comparing            │ SolveMultiStepData                      │ ✅
  8     │ Rows/Columns Confusion                │ BuildArray                     │ ✅
  9     │ Array Dimensions as Addition                    │ BuildArray, IdentifyEqualGroups                │ ✅
  10    │ Groups vs. Size Confusion             │ IdentifyEqualGroups, WriteMultExpression, BuildArray          │ ✅
  11    │ Multiplication Only Adds              │ IdentifyEqualGroups, WriteMultExpression                │ ✅
  12    │ Times Means Plus                      │ WriteMultExpression, InterpretMultExpression               │ ✅
  13    │ Order Changes Answer                  │ ApplyCommutative                     │ ✅
  14    │ Unknown Must Be Last                  │ SolveMultEquation                     │ ✅
  15    │ Can't Use Inverse Operations          │ SolveMultEquation                     │ ✅
  16    │ Graph as Picture                      │ ReadPicGraph, ReadBarGraph, CompareData:ordinal │ ✅
  17    │ All Data Must Be Used                 │ CompareData:difference, CompareData:combination, SolveMultiStepData │ ✅
  18    │ Skip Counting Without Meaning         │ LearnFactorProducts                     │ ✅
  19    │ Equal Sign as "Put Answer Here"       │ SolveMultEquation                     │ ✅
  20    │ Memorization Without Relationships    │ LearnFactorProducts                     │ ✅

Module Coverage:
  Every module has ≥1 active skill thread? Yes

  Module │ Active Skills                        │ Count
  ───────┼──────────────────────────────────────┼──────
  M1     │ ReadPicGraph, ReadBarGraph, CreatePicGraph, CompareData                   │ 4
  M2     │ ReadPicGraph, CreatePicGraph, InterpretHalfScale, CompareData                   │ 4
  M3     │ ReadPicGraph, CreatePicGraph, CreateBarGraph, CompareData                   │ 4
  M4     │ ReadBarGraph, CreateBarGraph, InterpretHalfScale, CompareData                   │ 4
  M5     │ ReadBarGraph, CompareData, SelectScale                        │ 3
  M6     │ ReadBarGraph, CreateBarGraph, CompareData, SolveMultiStepData                   │ 4
  M7     │ IdentifyEqualGroups                                  │ 1
  M8     │ IdentifyEqualGroups, WriteMultExpression, InterpretMultExpression                      │ 3
  M9     │ LearnFactorProducts                                 │ 1
  M10    │ IdentifyEqualGroups, WriteMultExpression, InterpretMultExpression, SolveMultEquation                │ 4
  M11    │ BuildArray                                 │ 1
  M12    │ BuildArray, ApplyCommutative                           │ 2

  Note: M7, M9, M11 each have low skill counts (1). This is expected:
  - M7 is the conceptual bridge module focused on structural recognition (one primary skill)
  - M9 is a fluency-building module (one primary skill with extensive practice)
  - M11 introduces arrays (one primary skill with rich activity sequence)
  All three have full lesson arcs with EC and Practice — the skill count reflects focus, not thinness.

EC Coverage:
  Every EC-tested action maps to a skill thread? Yes

  Module │ What EC Tests                                    │ Mapped to
  ───────┼──────────────────────────────────────────────────┼──────────
  M1     │ Bar graph → answer data questions                │ ReadBarGraph, CompareData
  M2     │ Data table → create picture graph (half-symbols) │ CreatePicGraph, InterpretHalfScale
  M3     │ Data table → create picture graph (multiples 5)  │ CreatePicGraph
  M4     │ Data table → create bar graph (mix of values)    │ CreateBarGraph, InterpretHalfScale
  M5     │ Given dataset → choose scale → justify           │ SelectScale
  M6     │ 3 problems (1 one-step, 2 two-step)             │ CompareData, SolveMultiStepData
  M7     │ Context → "How many groups? Items per group?"    │ IdentifyEqualGroups
  M8     │ Visual→expression + expression→visual            │ WriteMultExpression, InterpretMultExpression
  M9     │ Mix of 2s, 5s, 10s products                     │ LearnFactorProducts
  M10    │ Context → equation; unknown in various positions │ SolveMultEquation
  M11    │ Pre-made array → identify + expression           │ BuildArray
  M12    │ Both expressions + rotation prediction + equiv.  │ BuildArray, ApplyCommutative

SCOPING DECISIONS LOG
─────────────────────────────────────────────────────────────

DECISION 1: Split "Read graph values" into picture (ReadPicGraph) and bar (ReadBarGraph)
  Action: Split into ReadPicGraph (picture graphs) and ReadBarGraph (bar graphs)
  Rationale: The Conceptual Spine separates "Scaled Picture Graphs" from
  "Scaled Bar Graphs" as distinct concept threads. Skill threads should
  nest within concept threads. Additionally, the two skills follow
  different module trajectories: picture graph reading peaks at M3,
  while bar graph reading extends through M6. The cognitive mechanics
  differ (counting discrete symbols × scale vs. reading continuous axis).
  Evidence: Conceptual Spine rows 3-4 separate picture from bar graphs.
  M1 introduces both, M2-M3 focus on picture, M4-M6 focus on bar.

DECISION 2: Folded "Create 1:1 picture graph" (M1 warm-up) into CreatePicGraph
  Action: Folded
  Rationale: M1 warm-up has students create a 1:1 picture graph with
  collected data. This is the only instance of 1:1 graph creation, and
  it occurs in warm-up (not Lesson/EC/Practice). It's a one-off
  engagement that introduces the creation workflow. No EC tests 1:1
  creation. Treated as the introductory tier of CreatePicGraph.
  Evidence: M1 Toy Flow warm-up only. EC tests bar graph reading.

DECISION 3: Folded "Connect graph scales to multiplication" into IdentifyEqualGroups and LearnFactorProducts
  Action: Folded (not a separate skill)
  Rationale: The graph-to-multiplication conceptual bridge (M7 warm-up:
  "These scales were multiplication all along!") is the pedagogical glue
  between the data domain and multiplication domain. However, it is not
  independently assessed. Students never take an assessment where the sole
  task is "recognize that scaled graphs represent multiplication." The
  connection is tested through equal groups identification (IdentifyEqualGroups — M7 EC)
  and factor fluency (LearnFactorProducts — M9 graph callbacks).
  Evidence: M7 warm-up is guide-narrated with animation. M9 Activities
  4-6 have "Picture Graph Callbacks" that are occasional connections,
  not independent assessment targets.

DECISION 4: Split "Write expressions" (WriteMultExpression) from "Interpret expressions" (InterpretMultExpression)
  Action: Split into WriteMultExpression (visual → expression) and InterpretMultExpression (expression → visual)
  Rationale: Standard 3.OA.A.1 explicitly requires bidirectional understanding:
  both "interpret products" (expression → context) AND "describe contexts as
  products" (context → expression). These are distinct cognitive actions with
  different verbs (CREATE vs CONNECT). M8 EC independently tests both
  directions. The Toy Flow explicitly notes bidirectional practice as a
  design element from M8 mid-activities forward.
  Evidence: M8 EC tests both directions separately. M8 late activities
  emphasize: "Can you go both ways? Picture to expression AND expression
  to picture?" 3.OA.A.1 text: "describe a context in which a total
  number of objects can be expressed as 5 × 7."

DECISION 5: Kept SelectScale (Select scale) as independent despite single-module appearance
  Action: Kept as one thread
  Rationale: Scale selection appears only in M5, but it represents a
  qualitatively new cognitive action (meta-cognitive strategy) that doesn't
  exist before or after. M5 has a full lesson arc (early/mid/late), EC
  tests scale selection + justification, and practice builds fluency.
  The skill has >1 teaching interaction and is EC-tested. Additionally,
  it maps to a unique misconception (ID 4: Wrong Scale Selection) that
  no other skill addresses.
  Evidence: M5 Toy Flow shows 8+ activities, EC with justification
  requirement. Conceptual Development tab labels this "Apply" cognitive
  demand. Module Mapping lists misconception 4 exclusively for M5.

DECISION 6: Kept SolveMultiStepData (Multi-step problems) as independent despite single-module appearance
  Action: Kept as one thread
  Rationale: Two-step data problems in M6 are qualitatively different from
  one-step comparison (CompareData). The cognitive verb shifts from COMPARE to APPLY.
  Students must decompose problems, identify operations, and execute in
  sequence — a meta-cognitive skill. M6 has extensive coverage (Activities
  7-12 for two-step, plus 2 of 3 EC items test two-step). Unique
  misconception coverage (ID 7: Combining Before Comparing).
  Evidence: M6 Toy Flow Activities 7-9 have scaffolded step decomposition.
  M6 EC: 2 two-step + 1 one-step. Cognitive Development tab: "Apply."

DECISION 7: Folded "Identify problem structure" into SolveMultiStepData
  Action: Folded
  Rationale: In M6 Activities 10-12, students must identify whether a
  problem is one-step or two-step before solving. However, this
  identification is implicit in correct problem solving — it is not
  independently assessed (EC doesn't ask "Is this one-step or
  two-step?"). The meta-cognitive categorization is part of the
  problem-solving skill, not a separate assessable action.
  Evidence: M6 EC tests problem SOLVING, not problem CATEGORIZATION.

DECISION 8: Kept InterpretHalfScale (half-symbols/interpolation) as independent despite two-module gap
  Action: Kept as one thread
  Rationale: Half-symbol/interpolation appears in M2 (scale 2: half of 2 = 1)
  and M4 (scale 10: half of 10 = 5) with a gap at M3. Despite the gap,
  M4 explicitly callbacks to M2: "Remember half-symbols from scale of 2?
  Same idea here." The concept is the same cognitive action (represent
  "half of the scale value") applied across different scales. Both
  instances are EC-tested. M3's gap is by design: "NO half-symbols in M3"
  to focus on skip-counting.
  Evidence: M2 EC requires half-symbols. M4 EC has "mix of multiples
  and non-multiples." M4 Scaffolding Notes: "Reinforcement not
  introduction" for half-symbols.

DECISION 9: Ratio of 1.25x below suggested 1.5x minimum
  Action: Accepted with documentation
  Rationale: The 1.25x ratio reflects the unit's pedagogical design rather
  than under-decomposition. Three factors contribute:
  (a) The multiplication domain (M7-M12) introduces one new concept per
  module in a strict sequential chain. Each concept maps to 1-2 skills.
  Splitting further would create skills without independent assessable
  presence.
  (b) Single-module skills (SelectScale, SolveMultiStepData, LearnFactorProducts, SolveMultEquation, ApplyCommutative) are all
  EC-tested with full lesson arcs — they're genuinely contained within
  their modules, not under-decomposed.
  (c) The data domain (M1-M6) shows appropriate decomposition with
  skills spanning 2-6 modules and clear format/action splits.
  To reach 1.5x (18 threads), I would need to add 3 more skills. Candidates
  considered and rejected: separate "read at halfway points" (tier variant
  of ReadBarGraph), separate "comparison using subtraction vs addition" (tier variants
  of CompareData), separate "solve for unknown product vs unknown factor" (tier
  variants of SolveMultEquation). All rejected per the "don't create separate skills for
  every tier variant" anti-pattern.

DECISION 10: Classified LearnFactorProducts (factor fluency) as conceptual, not procedural
  Action: Classified as conceptual
  Rationale: While the end-state of factor fluency is automatic recall
  (procedural), the Toy Flow's approach and assessment focus on pattern
  DISCOVERY and IDENTIFICATION. The teaching arc emphasizes "2s are
  always even," "5s end in 0 or 5" — conceptual understanding that
  supports recall. The Cognitive Focus labels this IDENTIFY (Conceptual).
  The EC tests product selection (recognition), not timed recall.
  If the unit included timed fluency assessments, this would be procedural.
  Evidence: M9 Cognitive Focus: "IDENTIFY (Conceptual) - recognizing
  patterns." M9 Activities 1-3 are pattern discovery, not drill.

RESOLVED QUESTIONS (Author Review — 2026-04-15)
─────────────────────────────────────────────────────────────

R1. WriteMultExpression vs InterpretMultExpression (bidirectional expression skills) — KEEP SPLIT
   Author decision: Keep separate. Beyond the standard's language and
   cognitive verb differences, these produce fundamentally different
   practice template designs. WriteMultExpression templates show a picture → ask for
   expression. InterpretMultExpression templates show an expression → ask for matching
   visual. Different workspace_description, interaction type, and
   distractor strategy. Folding would force "bidirectional" templates
   that are harder to design, harder for teachers to review, and harder
   for the adaptive engine to diagnose.

R2. Graph-to-multiplication bridge — DO NOT ADD A SKILL
   Author decision: The bridge is a teaching moment, not an assessable
   skill. You can't write a practice template that tests "do you
   understand that scaled graphs are multiplication?" in isolation.
   Adequately tested through IdentifyEqualGroups (M7 EC) and LearnFactorProducts (M9 graph callbacks).
   If the adaptive engine needs to track this connection, it should look
   at the transition from CompareData/SelectScale performance to IdentifyEqualGroups performance, not at
   a separate skill. Adding one here would violate the folding rule
   (≤1 teaching interaction, not independently assessed).

R3. InterpretHalfScale cross-concept bridging — KEEP UNIFIED
   Author decision: Keep as one skill. Splitting into SK5a/SK5b would
   create two skills that the curriculum deliberately designed as one
   concept applied in two contexts. The template tier logic handles this
   naturally: confidence tier uses M2 parameters (scale 2, half-symbols),
   stretch tier uses M4 parameters (scale 10, interpolation). One skill,
   two parameter ranges, clean progression. The structural anomaly in the
   spine is less costly than the pedagogical misrepresentation of splitting.

OPEN QUESTIONS
─────────────────────────────────────────────────────────────

1. M7 has only one active skill (IdentifyEqualGroups). The module is intentionally
   focused on structural recognition without notation. If adaptive
   routing needs more granular data from M7, consider whether
   "count systematically" should be a separate skill from "identify
   groups." Currently folded because counting IS the mechanism for
   identification.

2. Factor order convention: M9 uses __ × 2/5/10 structure (second
   factor is always the scale/skip-counting unit), while M10 uses
   varied contexts. M11-M12 uses rows-first convention. Should the
   spine track "factor order understanding" as a skill, or is it
   adequately captured within WriteMultExpression, SolveMultEquation, and BuildArray?

═══════════════════════════════════════════════════════════════
