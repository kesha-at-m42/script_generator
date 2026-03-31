# MODULE 2: Tiling Rectangles — No Gaps, No Overlaps

**Version:** 03.12.26 (v1 — Task 1 Draft)

```
---
module_id: M02
unit: 2
domain: measurement_area
primary_toys:
  - name: "Grid Rectangles"
    notion_url: "https://www.notion.so/ocpgg/Grid-Rectangles-2fb5917eac528035a19dc2b5b49aeeca"
  - name: "Unit Square Tiles"
    notion_url: "https://www.notion.so/ocpgg/Unit-Square-Tiles-2fb5917eac52801185a0f9e4e942bf83"
secondary_toys: []
interaction_tools:
  - MC
  - Drag-to-Place
---
```

---

# BACKBONE

---

## **1.0 THE ONE THING**

**[REQUIRED]**

Students must understand that unit squares must fit together with no gaps and no overlaps to accurately measure area — gaps mean uncounted space (area too low), and overlaps mean double-counted space (area too high).

**Critical Misconception:** #1.0 — Gaps/Overlaps Acceptable. Students believe tiling with gaps or overlaps still produces a valid area measurement. They count tiles without evaluating coverage quality, leading to incorrect counts.

**Success Indicator:** Given a rectangle and unit square tiles, the student tiles the shape with no gaps and no overlaps, counts the tiles, and states the area in square units. Given a pre-made tiling with an error, the student identifies whether the error is a gap or an overlap and explains why it produces a wrong count.

**Biggest Risk:** Students learn the PROCEDURE of tiling neatly without understanding WHY gaps and overlaps are problems. If the connection between coverage quality and count accuracy isn't made explicit (gaps → too few, overlaps → too many), students may tile correctly through mechanical compliance rather than conceptual understanding. The sequential error presentation (gaps first, then overlaps) is designed to make each error type's numerical consequence visible before combining them into a single rule.

---

## **1.1 LEARNING GOALS**

**[REQUIRED]**

*Verbatim from OUR Curriculum — Script Must Achieve These*

**L1:** "Explain that rectangles that can be covered by the same number of unit squares without gaps or overlaps have the same area."

**L2:** "Find the area of rectangles (within 24 square units) by counting unit squares."

**Module Goal (Student-Facing):** "Today you'll find out what happens when tiles don't fit right — and learn the rules for measuring area perfectly."

**Exit Check Tests:**
- Can student tile a rectangle completely with no gaps and no overlaps using drag-to-place?
- Can student correctly count the tiles and state the area in square units?
- Can student identify whether a pre-made tiling has a gap or an overlap?

**Question/Test Language Stems (from Module Mapping):**
- "Is this tiled correctly? Why or why not?" → Maps to EC Problem 2 (error identification) and Lesson Section 1 (error presentation)
- "These rectangles have the same area — how do you know?" → Maps to L1 goal (same area = same number of squares). Target for Lesson Section 2 or Synthesis.

### **1.1.1 Standards Cascade**

| Building On | 3.MD.C.5.a (unit square definition — from M1) |
| :---- | :---- |
| **Addressing** | 3.MD.C.5.b (area as n unit squares, no gaps/overlaps); 3.MD.C.6 (counting unit squares — intro) |
| **Building Toward** | 3.MD.C.6 (systematic counting — M3+) |

**Standards Note:** M2 begins addressing 3.MD.C.6 (counting unit squares) but defers the full standard's vocabulary (rows, columns) and advanced strategies (systematic counting, skip-counting) to M3+. Standard units (sq cm, sq in, etc.) required by 3.MD.C.6 are deferred to M5-M6. M2's contribution to 3.MD.C.6 is establishing that accurate counting requires accurate tiling.

### **1.1.2 Module Bridges**

**From M1 (What is Area? Measuring with Unit Squares):** Students know that area is the space a shape covers, measured by counting unit squares. They've tiled rectangles and rectilinear shapes using drag-to-place, counted tiles one by one, and stated area in square units. M1 Synthesis previewed a "bad" tiling with gaps and overlaps: "But look at this one. Something's off. See those gaps? And that overlap? Next time, we'll figure out why that matters." Overlap detection (mechanical feedback) was always active in M1, but the conceptual rules for WHY gaps/overlaps are errors were not taught.

**This Module:** Students discover that gaps cause undercounting and overlaps cause overcounting, establishing the rules for accurate area measurement. They formalize "no gaps, no overlaps" as the standard for valid tiling. Rectangle focus begins — students work exclusively with rectangles in M2 (rectangles defined as polygons with 4 sides and 4 right angles, per Grade 2 prior knowledge). Students tile rectangles with increasing independence, applying self-check routines.

**To M3 (Structured Counting — Rows and Columns):** Students leave M2 able to tile rectangles accurately and count tiles one by one. M2 Synthesis bridge: display a correctly tiled 3×4 rectangle, highlight one row — "You can tile perfectly now! But counting every square takes time. Is there a FASTER way?" This creates motivation for M3's row-by-column structuring.

### **1.1.3 OUR Lesson Sources**

| OUR Lesson | Content Used | Adaptation Notes |
| :---- | :---- | :---- |
| L3 | No gaps/overlaps rule; finding area by counting unit squares; same area = same number of squares | Adapted from physical tile manipulation to digital drag-to-place with Grid Rectangles. OUR's "Card Sort by area" replaced with sequential error presentation (SME decision — sequential better for building distinct mental models of gap vs. overlap errors). OUR's "create rectangles with specific areas on grids" deferred to Practice. |

---

## **1.2 SCOPE BOUNDARIES**

**[REQUIRED]**

### **✅ Must Teach**

- Why gaps produce wrong area counts (too few — uncounted space)
- Why overlaps produce wrong area counts (too many — double-counted space)
- "No gaps, no overlaps" as the rule for accurate area measurement
- Same area = same number of unit squares (with proper tiling)
- Tiling rectangles with unit squares using drag-to-place (with gap/overlap awareness)
- Identifying gaps and overlaps in pre-made tilings
- Self-check routine: "Before you submit, check: Any gaps? Any overlaps?"
- Vocabulary: gap, overlap, tiling, rectangle (activation)
- Rectangle as the focus shape (4 sides, 4 right angles — activated from Grade 2 knowledge)

### **❌ Must Not Include**

- Structured counting, skip-counting, or row/column organization — M3
- Rows and columns as counting strategies — M3
- Area as multiplication (rows × columns) — M5
- Standard units (square centimeters, square inches, etc.) — M5-M6
- Perimeter — NOT in Unit 2 (Decision #5)
- Decomposition strategies for non-rectangular shapes — M11
- Formula language ("length times width") — M7+
- Non-rectangular shapes in tiling activities — M2 focuses exclusively on rectangles (L/T shapes were M1-Late; M2 narrows to rectangles per TVP)
- Grid fading — M2 uses full grids throughout (Decision #3: M1-M4 full grids)

> ⚠️ **GAP/OVERLAP DISTINCTION:** The Lesson must build SEPARATE mental models for gaps (too few) and overlaps (too many) before combining them into a single rule. Sequential error presentation (gaps first, then overlaps, then correct) is the TVP's resolved approach.

> ⚠️ **CRA STAGE — CONCRETE:** M2 remains in the Concrete phase of CRA — heavy manipulation with explicit rule-building. Students tile and count, now with attention to coverage quality. No structured counting, no multiplication connection. One-by-one counting is still appropriate and expected.

### **Scope Confirmation Checklist**

*Resolve these questions before drafting:*

- [x] What concepts are IN scope vs. deferred? — Gap/overlap rules + rectangle tiling IN; structured counting, multiplication connection, non-rectangular shapes OUT
- [x] What vocabulary is introduced vs. just used vs. forbidden? — See §1.3. Gap, overlap, tiling are NEW. Rectangle is ACTIVATED. Area, unit square, square unit continue from M1.
- [x] What specific values/parameters are required? — Dimensions: 2-6 per side. Areas: 6-25 square units. Rectangles only. Both orientations.
- [x] What value constraints apply? — All shapes tile cleanly with unit squares. No partial tiles. No curves or diagonals. Full grids visible on all target rectangles.
- [x] Are there any "both X and Y" situations? — Yes: M2 teaches BOTH tiling (CREATE) and error identification (IDENTIFY). EC tests both skills.
- [x] What OUR lessons does this module cover? — L3 only
- [x] What are the scope boundaries with adjacent modules? — M1 owns initial tiling experience + area concept; M2 owns gap/overlap rules; M3 owns structured counting.

---

## **1.3 VOCABULARY ARCHITECTURE**

**[REQUIRED]**

**Assessment Vocabulary (appears on state test):** area, unit square, square unit (continuing from M1) + gaps, overlaps, tiling (new for 3.MD.C.5.b)

### **Vocabulary Staging by Phase**

| Phase | Terms | Introduction Approach |
| :---- | :---- | :---- |
| **Warm-Up** | area, unit square, square unit, tile/tiles | Continue from M1 — use naturally. "Look at how the tiles fit this rectangle." No new formal vocabulary in Warmup. |
| **Lesson Section 1 (Error Presentation)** | gap, overlap | Introduced DURING concrete observation of errors: "See these empty spaces? Those are GAPS." / "See these stacked tiles? That's an OVERLAP." Terms introduced as students observe the visual evidence — vocabulary grounded in experience per Lesson Playbook. |
| **Lesson Section 1 (Rule Formation)** | tiling | Formalized after students have seen all three cases (gap, overlap, correct): "When you cover a shape with tiles and there are NO gaps and NO overlaps — that's called TILING." |
| **Lesson Section 2 (Guided Practice)** | (all terms) | Used in context during guided tiling. Guide uses terms in instructions: "Tile this rectangle — remember, no gaps, no overlaps." |
| **Lesson Section 3 (Independent)** | (all terms) | Used in self-check prompts: "Any gaps? Any overlaps?" Student applies vocabulary independently. |
| **Exit Check** | gap, overlap, area, square unit | Used in prompts. "Is there a gap or an overlap?" / "What is the area in square units?" |
| **Synthesis** | (all terms) + rectangle (activation) | Rule consolidation. Rectangle vocabulary activated from Grade 2 knowledge. All terms used naturally. |

### **Vocabulary Note: "Rectangle"**

"Rectangle" appears in Module Mapping's Vocabulary to Teach list. Per TVP, rectangle vocabulary is "reinforced (prior knowledge from Grade 2): 4 sides, 4 right angles, opposite sides equal and parallel. Not new teaching — activation of existing knowledge." In §1.3, "rectangle" is treated as ACTIVATION (students know this word from Grade 2) rather than new introduction. The Synthesis phase explicitly reinforces rectangle properties as prior knowledge.

### **Terms to Avoid (Save for Later Modules)**

- rows / columns (M3)
- skip-count / skip-counting (M3)
- multiply / multiplication (M5)
- formula (M7+)
- length / width (M7+)
- perimeter (NOT in Unit 2 — Decision #5)
- square centimeters / square inches / square feet / square meters (M5-M6)
- decompose / partition (M11)
- array (M3+ in this unit's context — Decision #4)

### **Vocabulary Teaching Notes**

- "Gap" = space left uncovered between tiles. Gaps mean some space isn't counted → area measurement is TOO LOW.
- "Overlap" = tiles stacked on top of each other. Overlaps mean some space is counted twice → area measurement is TOO HIGH.
- "Tiling" = covering a shape with tiles so there are no gaps and no overlaps. Valid tiling = accurate measurement.
- "Rectangle" = polygon with 4 sides and 4 right angles. Opposite sides are equal and parallel. Activated from Grade 2 — not new teaching in M2.
- Continue from M1: "Area" = how much space a shape covers. "Unit square" = the tile itself. "Square unit" = the measurement unit.

---

## **1.4 MISCONCEPTIONS**

**[REQUIRED]**

### **1.4.1 #1.0: Gaps/Overlaps Acceptable (PRIMARY)**

**Trigger Behavior:** When asked to find area, student counts tiles even when they overlap or leave gaps. Student may place tiles carelessly and report the tile count without checking coverage quality. When shown a pre-made tiling with errors, student says the area measurement is correct.

**Why It Happens:** In M1, overlap detection was mechanically active (visual + audio feedback prevented overlaps), and gap feedback was not active. Students may have learned "just place tiles and count" without developing the concept that coverage quality affects count accuracy. The mechanical feedback did the quality checking — the student didn't.

**Visual Cue:** Grid Rectangles display showing (a) a rectangle with gaps — visible empty grid squares between tiles, with a count showing "10 tiles" when the real area is 12; (b) the same rectangle with overlaps — stacked tiles visible, with a count showing "14 tiles" when the real area is 12. The numerical consequences (10 vs. 12 vs. 14) make the error concrete.

**Prevention Strategy:** Sequential error presentation (Lesson Section 1) surfaces each error type independently with explicit numerical consequences before students tile. Students DISCOVER the errors and their effects before being told the rules. The self-check routine ("Any gaps? Any overlaps?") is modeled and practiced through Sections 2-3.

### **1.4.2 #9.0: Array Structure Not Seen (PREVIEW)**

**Trigger Behavior:** Student sees a rectangle of tiles but doesn't recognize the row/column structure — counts randomly instead of by rows. With a 3×4 rectangle, student counts 1, 2, 3... 12 instead of recognizing "3 rows of 4."

**Why It Happens:** Students are still in the one-by-one counting phase (appropriate for M1-M2). Array/row-column structuring is an explicit instructional target in M3-M4 (Decision #2: Explicit Spatial Structuring). Including as PREVIEW because M2 students tile rectangles that inherently have row/column structure — some students may begin noticing it organically.

**Visual Cue:** Not actively addressed in M2. Students tile and count one-by-one. If a student spontaneously counts by rows, the Guide can acknowledge it ("You found a pattern!") without formally teaching structured counting.

**Prevention Strategy:** Not a prevention target in M2 — this is a PREVIEW. M2 establishes accurate tiling; M3 builds structure on top of it. The Synthesis bridge (highlighting one row of a completed tiling) is the only intentional connection to M3's structuring.

> **Design Note:** TVP also notes "Rectangle properties unclear (MODERATE)" as a pedagogical concern. Per author decision, this does not warrant a formal Misconception ID — it is addressed through Synthesis vocabulary activation (rectangle defined as 4 sides, 4 right angles, from Grade 2 knowledge). Not tracked in the Misconceptions database.

---

## **1.5 TOY SPECIFICATIONS**

**[REQUIRED]**

### **1.5.1 Grid Rectangles**

**Notion Spec:** [Grid Rectangles](https://www.notion.so/ocpgg/Grid-Rectangles-2fb5917eac528035a19dc2b5b49aeeca) | **Changes from M1:** First appearance. Replaces Plane Figures (M1's display-only comparison toy). Grid Rectangles displays rectangles on a full grid — consistent with Decision #3 (M1-M4: Full grids).

**Purpose:** Display rectangles with visible grid. In M2, Grid Rectangles serves two roles: (1) Display mode — showing pre-tiled rectangles (correct, with gaps, or with overlaps) for observation and error identification. (2) Target mode — providing the target surface for student tiling with Unit Square Tiles.

**Spec Verification (completed):** Grid Rectangles is a display object (NOT draggable). Student actions supported: Shade (individual squares), Select Row, Select Column. Grid state is system-controlled — students cannot toggle grid visibility. For M2, only the Shade action is potentially relevant (shaded squares = "tiled" squares in pre-made displays; unshaded within boundary = gaps). Row/Column selection is M3+ only.

**Spec-Confirmed Capabilities for M2:**
- Full Grid state supported (`grid_state: "full"`) — confirmed for M1-M6
- Generic unit type ("square units") — confirmed for M1-M4
- Can appear with Unit Square Tiles (M1-M2 tiling) — confirmed
- Can appear with Counter (M1-M2) — Counter auto-increments as tiles are placed (see Counter note in §1.5.2)
- Maximum 2 instances on screen simultaneously
- Dimension range: whole numbers 1-10; typical M1-M2 up to 24 square units

**Spec-Identified Constraint:** The Notion spec says "Typical M1-M2: Up to 24 square units" which matches OUR's learning goal. The TVP says "6-25 square units." This 1-unit difference (24 vs. 25) means a 5×5=25 rectangle is technically within TVP range but at the edge of the spec's M1-M2 typical range. Recommendation: keep dimensions at 2-5 for most interactions (max 25 sq units from 5×5), allowing 6 as a dimension only when paired with a small other dimension (e.g., 2×6=12, 3×6=18). This keeps all areas within 24 except 5×5=25, which is within spec maximum but at the boundary.

#### Module Configuration (M2)

| Aspect | This Module |
| :---- | :---- |
| **Mode** | Display (Warmup, Lesson Section 1) + Target (Lesson Sections 2-3, EC, Practice) |
| **Grid State** | Full grid (`grid_state: "full"`) — always visible. System-controlled. (Decision #3: M1-M4 full grids) |
| **Unit Type** | Generic ("square units") — no standard units until M5 |
| **Shape Types** | Rectangles only (dimensions 2-6 per side; areas 6-24 typical, 25 max) |
| **Orientations** | Both horizontal and vertical (+ square when dimensions equal) |
| **Pre-Tiled States (Display)** | Correct tiling: all grid squares shaded. Gap tiling: some squares unshaded within boundary. Overlap tiling: stacked tiles visible via Unit Square Tiles overlap detection (color change + audio). |
| **Error Visualization** | Gaps: visible unshaded grid cells within the rectangle boundary. Overlaps: Unit Square Tiles' always-on overlap detection (visual color change per TVP). |
| **Interaction (Display)** | No student interaction with Grid Rectangles itself — student observes and responds via MC |
| **Interaction (Target)** | Receives tiles from Unit Square Tiles via drag-to-place. Counter auto-increments as tiles are placed. |
| **Dimension Labels** | Available on rectangle edges. System-controlled display. |

#### M2 Guardrails

| DO | DO NOT |
| :---- | :---- |
| Show full grid on all target rectangles | Hide or fade the grid (full grids through M4 per Decision #3) |
| Use display mode for error examples (gaps/overlaps) | Let students interact with error displays (these are observation-only) |
| Support both horizontal and vertical rectangle orientations | Use only one orientation (varied orientations build flexibility) |
| Keep dimensions within 2-6 per side constraint | Use dimensions outside 2-6 range |

#### Progression Within M2

| Phase | Configuration |
| :---- | :---- |
| **Warmup** | Display only. Correctly tiled rectangle shown. Student observes. |
| **Lesson Section 1** | Display (sequential error presentation: gap → overlap → correct) + MC student action (error identification — student classifies new example as gap/overlap/correct). Teaches error identification as an explicit skill before EC tests it. |
| **Lesson Section 2** | Target mode. Student tiles rectangles (3×4, 2×5, 4×4). Full grid visible. |
| **Lesson Section 3** | Target mode. Student tiles 4-5 rectangles independently. Varied orientations. |
| **Exit Check** | Target mode (Problems 1, 3) + Display mode (Problem 2 — pre-made tiling for error identification). |
| **Synthesis** | Display only. Correctly tiled 3×4 for rule consolidation + M3 bridge. |

---

### **1.5.2 Unit Square Tiles**

**Notion Spec:** [Unit Square Tiles](https://www.notion.so/ocpgg/Unit-Square-Tiles-2fb5917eac52801185a0f9e4e942bf83) | **Changes from M1:** Now paired with Grid Rectangles (instead of self-rendered target surface). Overlap detection behavior unchanged. Gap feedback behavior elevated — gap/overlap conceptual rules are now taught (were deferred in M1).

**Purpose:** The measurement tool students use to tile rectangles. Students drag unit square tiles onto Grid Rectangle targets, aiming for complete coverage with no gaps and no overlaps. Counting remains manual (one-by-one) — structured counting deferred to M3.

#### Module Configuration (M2)

| Aspect | This Module |
| :---- | :---- |
| **Unit Type** | Generic — "square unit" (not sq cm, sq in, etc.) |
| **Target Surface** | Grid Rectangles (see §1.5.1) — NOT self-rendered shape outlines as in M1 |
| **Snap Mode** | Quarter-tile snap (half linear measure). Semi-freeform placement per SME decision. Students must apply gap/overlap rules with genuine precision, but motor demands stay age-appropriate. |
| **Overlap Feedback** | Active — immediate visual color change + audio cue on overlap, with opportunity to correct. Always on. Same behavior as M1. |
| **Gap Feedback** | Conceptual gap awareness is NOW TAUGHT (unlike M1 where gap feedback was inactive). Visual: empty grid cells visible within the rectangle. The grid itself makes gaps visible. No separate gap-detection system needed — the full grid serves this purpose. |
| **Tile Supply (Guided)** | Exact match — bank contains exactly the tiles needed. Consistent with M1 Section 2 approach. |
| **Tile Supply (Independent / EC)** | Modest surplus — bank contains more tiles than needed. Student judges completeness. Consistent with M1 Section 3 approach. |
| **Interaction** | Drag-to-place (not tap) per Decision #6 |
| **Side Length Labels** | Available via tap/click but not proactively shown. Consistent with M1. |

#### M2 Guardrails

| DO | DO NOT |
| :---- | :---- |
| Use drag-to-place for all tiling interactions (Decision #6) | Use tap-to-place for tiling |
| Start with exact tile supply, progress to surplus | Provide unlimited/infinite tiles |
| Let students count tiles one-by-one | Expect or prompt structured counting (M3) |
| Keep overlap detection always active (mechanical correction) | Turn off overlap detection |
| Teach gap/overlap rules conceptually in Lesson Section 1 | Assume students will discover rules from feedback alone |
| Model self-check routine ("Any gaps? Any overlaps?") before expecting independent use | Skip self-check modeling |

#### Scaffolded Feedback Progression (from TVP)

Overlap detection is always active (immediate visual + audio, opportunity to correct). The scaffolding that fades is the COMPLETION feedback (area count accuracy):

| Phase | Overlap Feedback | Completion Feedback | Self-Check |
| :---- | :---- | :---- | :---- |
| **Lesson Section 2 (Guided)** | Always active | Immediate — system confirms/corrects area count | Guide models self-check routine |
| **Lesson Section 2→3 (Transition)** | Always active | Submit-only — feedback after student submits | Guide prompts self-check |
| **Lesson Section 3 (Independent)** | Always active | Self-check before submit — no system feedback until EC | Student self-checks independently |
| **Exit Check** | Always active | No feedback until results | N/A |

> **Design Note (Scaffolding):** The TVP specifies a three-stage feedback fading for completion (area count accuracy): immediate → submit-only → self-check before submit. Overlap detection does NOT fade — it stays active across all tiling modules. This creates an asymmetric scaffolding design: the quality feedback is permanent, but the accuracy feedback fades to build student independence.

#### Counter (Remediation Only)

Per M1 design decision (KDD #2): Counter is NOT part of standard path. Counter remains available as guide-activated remediation for persistent miscounting (correct tiling, wrong area count on 2+ consecutive problems). Not available during EC.

#### Data Constraints

| Constraint | Value |
| :---- | :---- |
| Rectangle dimensions (per side) | 2–6 units |
| Area range (all M2 activities) | 6–25 square units |
| Tiling targets | Rectangles ONLY (no L/T shapes — narrowed from M1) |
| Orientations | Both horizontal and vertical |
| No partial tiles | All rectangles tile cleanly with unit squares |
| No non-rectilinear targets | No curves, no diagonals |
| Tile supply (guided) | Exact match |
| Tile supply (independent/EC) | Modest surplus (never infinite) |
| Specific dimensions called out by TVP | 3×4, 2×5, 4×4 (Lesson Mid) |

---

### **Interaction Constraints (All Toys)**

- NO verbal/spoken student responses — Guide speaks, student acts
- NO keyboard/text input — all responses via click/tap/drag
- NO open-ended questions requiring typed answers — use selection or action tasks
- Questions in Guide speech must be either rhetorical (Guide answers) or answered through on-screen action
