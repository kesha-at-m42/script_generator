# Problem 3: Connect

**Learning Goal:** Students can partition shapes into equal parts and identify unit fractions
**Difficulty Level:** 3
**Total Steps:** 5

---

## Step 1

**Tutor says:**
> Here's something to think about. Each shape is divided into equal parts.

**Visual elements shown:**
- [square] State: `divided_2_equal` - Square divided into 2 equal parts
- [horizontal_rectangle_bar] State: `divided_3_equal` - Rectangle divided into 3 equal parts
- [circle] State: `divided_4_equal` - Circle divided into 4 equal parts
- [hexagon] State: `divided_8_equal` - Hexagon divided into 8 equal parts
- [fraction_labels] State: `unmatched` - Fraction labels: 1/2, 1/3, 1/4, 1/8


## Step 2

**Tutor says:**
> Your job is to match each shape to the unit fraction that represents ONE of its equal parts.

**Visual elements shown:**
- [square] State: `divided_2_equal` - Square divided into 2 equal parts
- [horizontal_rectangle_bar] State: `divided_3_equal` - Rectangle divided into 3 equal parts
- [circle] State: `divided_4_equal` - Circle divided into 4 equal parts
- [hexagon] State: `divided_8_equal` - Hexagon divided into 8 equal parts
- [fraction_labels] State: `draggable` - Draggable fraction labels: 1/2, 1/3, 1/4, 1/8


## Step 3

**Tutor says:**
> Start with the square. Count its parts, then drag the matching fraction.

**Student action:**
- Drag fraction to match the square

**Visual elements shown:**
- [square] State: `divided_2_equal_highlighted` - Square divided into 2 equal parts, highlighted
- [horizontal_rectangle_bar] State: `divided_3_equal` - Rectangle divided into 3 equal parts
- [circle] State: `divided_4_equal` - Circle divided into 4 equal parts
- [hexagon] State: `divided_8_equal` - Hexagon divided into 8 equal parts
- [fraction_labels] State: `draggable` - Draggable fraction labels: 1/2, 1/3, 1/4, 1/8

**Expected student input:** drag_fraction


## Step 4

**Tutor says:**
> Now match the rectangle.

**Student action:**
- Drag fraction to match the rectangle

**Visual elements shown:**
- [square] State: `divided_2_equal_matched` - Square matched with 1/2
- [horizontal_rectangle_bar] State: `divided_3_equal_highlighted` - Rectangle divided into 3 equal parts, highlighted
- [circle] State: `divided_4_equal` - Circle divided into 4 equal parts
- [hexagon] State: `divided_8_equal` - Hexagon divided into 8 equal parts
- [fraction_labels] State: `remaining_draggable` - Remaining draggable fraction labels: 1/3, 1/4, 1/8

**Expected student input:** drag_fraction


## Step 5

**Tutor says:**
> Match the circle and hexagon.

**Student action:**
- Drag fractions to match remaining shapes

**Visual elements shown:**
- [square] State: `divided_2_equal_matched` - Square matched with 1/2
- [horizontal_rectangle_bar] State: `divided_3_equal_matched` - Rectangle matched with 1/3
- [circle] State: `divided_4_equal_highlighted` - Circle divided into 4 equal parts, highlighted
- [hexagon] State: `divided_8_equal_highlighted` - Hexagon divided into 8 equal parts, highlighted
- [fraction_labels] State: `remaining_draggable` - Remaining draggable fraction labels: 1/4, 1/8

**Expected student input:** drag_fractions


## Expected Final State

After completing all steps, the visual should show:

- **square:** `divided_2_equal_matched` - Square (2 parts) matched with 1/2
- **horizontal_rectangle_bar:** `divided_3_equal_matched` - Rectangle (3 parts) matched with 1/3
- **circle:** `divided_4_equal_matched` - Circle (4 parts) matched with 1/4
- **hexagon:** `divided_8_equal_matched` - Hexagon (8 parts) matched with 1/8

## Success Feedback

1. You matched the parts to the bottom number.
2. You're seeing the pattern - count the parts, that's your denominator.
3. You connected what you see to what the fraction means. That's solid math thinking.
