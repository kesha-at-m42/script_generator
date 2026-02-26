# Problem Template Schema Guide

Each template represents a **type** of problem that can generate multiple specific problem instances.

---

## Field-by-Field Explanation

### **template_id** (string)
- **Purpose**: Unique identifier for this template
- **Format**: `"XXXX"` where X is a digit (e.g., `"4001"`, `"5002"`)
- **Convention**: First digit(s) = module number; last digits = sequential template number within module
- **Example**: `"4001"` = Module 4, Template 1

---

### **problem_type** (string)
- **Purpose**: Human-readable description of what the problem asks students to do
- **Format**: One clear sentence describing the task
- **Example**: `"Student places tick marks to divide a 0-1 number line into the specified number of equal intervals"`

---

### **goal_decomposition** (object)
Breaks down the learning objective this template assesses.

#### **mastery_tier** (array of strings)
- **Purpose**: Difficulty level(s) this template can generate problems for
- **Options**: `"confidence"`, `"support"`, `"baseline"`, `"stretch"`, `"challenge"`
- **Example**: `["baseline", "stretch"]`

#### **mastery_verb** (string)
- **Purpose**: The cognitive action being assessed
- **Options**: `"create"`, `"identify"`, `"compare"`, `"apply"`, `"analyze"`, `"evaluate"`
- **Example**: `"create"`

#### **mastery_component** (string)
- **Purpose**: Type of mathematical knowledge being assessed
- **Options**:`"procedural"`, `"conceptual"`, `"transfer"`
- **Example**: `"procedural"`

#### **mastery_skill_id** (string)
- **Purpose**: Unique identifier linking to curriculum standards
- **Format**: MX-0Y (where X and Y are digits)
- **Convention**:X = module number; Y = sequential skill number within module
- **Example**: `"M5-03"`

#### **mastery_skill** (string)
- **Purpose**: Complete sentence describing the skill
- **Example**: `"Student can partition a number line into equal intervals"`

#### **non_curriculum_skills** (array of strings)
- **Purpose**: Technical or interface skills required but not being assessed
- **Common values**: `"click_accuracy"`, `"drag_precision"`, `"fine_motor_control"`
- **Example**: `["click_accuracy"]`

---

### **parameter_coverage** (object)
Defines the mathematical parameters that will vary across problem instances. Can contain different parameter types depending on the problem template needs.

#### **Common parameter types:**

**fractions** (array)
- **Purpose**: List of all fractions this template can generate problems for
- **Example**: `["1/2", "1/3", "2/3", "3/4", "5/6"]`

**denominators** (array)
- **Purpose**: List of denominators to use (when problems vary denominator but not specific fractions)
- **Example**: `["2", "3", "4", "6", "8"]` or `[2, 3, 4, 6, 8]`

**other_parameters** (flexible)
- Add any problem-specific parameters needed (e.g., `"ranges"`, `"benchmark_values"`, `"comparison_types"`)

---

### For each tier:

**whatever parameters** (optional,varies based on parameter_coverage)
- **Purpose**: Which parameter values are used at this difficulty level
- **Format**: Should match the parameter types defined in `parameter_coverage`
- **Examples**:
- If `parameter_coverage` has `fractions`: use `"fractions": ["1/2", "1/3", "2/3"]`
- If `parameter_coverage` has `denominators`: use `"denominators": [2, 3, 4]`
- If `parameter_coverage` has multiple types: include all relevant types

**target_count** (number)
- **Purpose**: How many problem instances to generate for this tier
- **Example**: `10`

**workspace_requirements** (string)
- **Purpose**: Specific constraints for how the workspace should be set up
- **Examples**:
- `"Intervals pre-numbered 1, 2, 3 for scaffolding"`
- `"No scaffold - student works independently"`
- `"Extended number line 0 to 2 for fractions > 1"`

**additional_notes** (string, optional)
- **Purpose**: Any other relevant information for this tier

---

## **prompt_examples** (array of strings)
  - **Purpose**: Multiple concrete example phrasings of the problem prompt
 **Example for a partitioning problem:**
  ```json
  [
    "Divide this number line into 3 equal parts.",
    "Place ticks to make fourths.",
    "Split the line into 6 equal spaces."
  ]
  ```
---

### **workspace_description** (string)
- **Purpose**: Plain-language description of the visual workspace which includes interactables as well as options for multiple choice questions
- **Example**: `"Number line from 0 to 1 with only endpoints labeled. No tick marks between 0 and 1."`

---

### **workspace_detailed** (array of objects)
Technical specification of the workspace elements. Each object represents one visual component.

**Structure**: Array of workspace element objects

#### **For each element:**

**toy** (string, required)
- The visualization tool or component type
- Examples: `"extended_number_line"`, `"fraction_bar"`, `"multiple_choice_options"`, `"ruler"`

**Additional fields** (as needed to fully describe the element)
- Use whatever fields necessary to specify the workspace element
- Common examples: `range`, `orientation`, `tick_marks`, `labeled_endpoints`, `scaffold`, `point_placed`

#### **For MCQ elements:**

When `toy` is `"multiple_choice_options"`:

**mcq_options** (object)
- `choice_count`: Number of options
- `display_format`: Layout style (e.g., `"vertical_list"`, `"horizontal_row"`, `"grid"`)
- `option_type`: Type of options (e.g., `"fractions"`, `"numbers"`, `"text"`)
- Any other fields needed for MCQ configuration

---

### **action_list** (array of strings)
- **Purpose**: List of interactions the student will perform
- **Example**: `["place_tick", "select_tick"]`

---

### **action_description** (string)
- **Purpose**: Narrative description of the actions student is expected to perform
- **Example**: `"Student taps on the line to place tick marks at positions they choose"`

---

### **correct_end_state** (string)
- **Purpose**: Description of what the workspace looks like when correct
- **Example**: `"Line shows 5 equal intervals with 4 evenly spaced tick marks between 0 and 1"`

---

### **success_dialogue** (object)
Feedback shown when student answers correctly.

#### **tone** (string, optional)
- **Purpose**: Guidance on the emotional/pedagogical tone
- **Example**: `"Brief confirmation acknowledging equal spacing"`

#### **examples** (array of strings)
- **Purpose**: Actual success messages to display
- **Should**: Be varied, brief (5-15 words), encouraging
- **Example**:
```json
[
  "That's {six equal parts.",
  "Equal spaces. Got it."
]
```

#### **feedback_visual** (string, optional)
- **Purpose**: Visual changes that accompany the success message
- **Example**: `"Correct ticks highlighted, equal spacing confirmed"`

---

### **misconceptions_targeted** (array of objects)
Lists common student errors this problem can detect.

#### For each misconception:

**misconception_id** (number)
- **Purpose**: Unique ID for tracking across templates
- **Example**: `5`

**misconception_tag** (string)
- **Purpose**: Short, readable identifier
- **Format**: lowercase_with_underscores
- **Example**: `"counting_ticks_not_spaces"`

**evidence** (string)
- **Purpose**: Observable behavior indicating this misconception
- **Example**: `"Student places {denominator} ticks instead of {denominator-1} ticks (creates {denominator+1} parts)"`

**detection_method** (string)
- **Purpose**: Technical identifier for how system detects this
- **Format**: snake_case description
- **Example**: `"tick_count_equals_denominator"`

---

### **remediation_approach** (object)
Describes how to help students when they make errors.

#### **light** (string)
- **Example**: `"Redirect to counting spaces, not ticks"`

#### **medium** (string)
- **Example**: `"Visual hint showing equal spacing with Helper guidance"`

#### **heavy** (string)
- **Example**: `"Step-by-step guided placement with modeling"`

---

### **design_notes** (object)
Implementation guidance for problem generation.

#### **vary_by** (array of strings)
- **Purpose**: Which parameters should change between problem instances
- **Example**: `["denominator", "prompt wording"]`

#### **hold_constant** (array of strings)
- **Purpose**: Which parameters should stay the same across all instances
- **Example**: `["0-1 range", "place_tick interaction", "horizontal orientation"]`

#### **difficulty_scaling** (string)
- **Purpose**: Explains how difficulty increases within this template
- **Example**: `"Larger denominators require more precise spacing"`

---

## Complete Example

```json
{
  "template_id": "4001",
  "problem_type": "Place unit or non-unit fraction on 0-1 number line by clicking the correct tick mark",

  "goal_decomposition": {
    "mastery_tier": ["baseline", "stretch"],
    "mastery_verb": "create",
    "mastery_component": "procedural",
    "mastery_skill_id": "M4-01",
    "mastery_skill": "Student can place fractions on a 0-1 number line by counting intervals from zero",
    "non_curriculum_skills": ["click_accuracy"]
  },

  "parameter_coverage": {
    "fractions": []
  },

  "tier_constraints": {
    "baseline": {
      "fractions": ["1/3", "2/3", "1/4", "2/4", "3/4", "1/6", "3/6", "5/6"],
      "target_count": 10,
      "workspace_requirements": "Pre-placed tick marks at all fraction positions. No scaffolding (no interval numbers or shading).",
      "additional_notes": "Core grade-level fractions with simpler denominators (thirds, fourths, sixths)"
    },
    "stretch": {
      "fractions": ["1/5", "2/5", "3/5", "4/5", "1/8", "3/8", "5/8", "7/8"],
      "target_count": 6,
      "workspace_requirements": "Pre-placed tick marks at all fraction positions. No scaffolding.",
      "additional_notes": "More challenging denominators (fifths and eighths) requiring more intervals to count"
    }
  },

  "prompt_examples": [
      "Place three fourths on the number line.",
      "Find one half on the number line.",
      "Click the tick mark that shows 2/3.",
      "Where is five sixths? Place a point there."
    ],

  "workspace_description": "Horizontal number line from 0 to 1 with tick marks pre-placed at all positions for the given denominator. Only 0 and 1 are labeled. No intermediate labels or scaffolding visible.",

  "workspace_detailed": [
      {
        "toy": "extended_number_line",
        "range": [0, 1],
        "orientation": "horizontal",
        "tick_marks": "pre-placed",
        "labeled_endpoints": true,
        "point_placed": true,
        "scaffold": "none"
      },
      {
        "toy": "multiple_choice_options",
        "mcq_options": {
          "choice_count": 3,
          "display_format": "vertical_list",
          "option_type": "fractions"
        }
      }
    ],

  "action_list": ["click_tick"],

  "action_description": "Student clicks a tick mark to place a point at that position on the number line",

  "correct_end_state": "Point placed at the correct tick mark position with label showing the fraction",

  "success_dialogue": {
      "tone": "Brief confirmation with interval count",
      "examples": [
        "That's three fourths. Three intervals from zero.",
        "Two spaces from zero—two thirds.",
        "You found five sixths.",
        "One half. Right at one interval."
      ],
      "feedback_visual": "Point highlighted at correct position, fraction label appears"
   },

  "misconceptions_targeted": [
    {
      "misconception_id": 5,
      "misconception_tag": "counting_ticks_not_spaces",
      "evidence": "Student clicks tick at position (numerator + 1) or (numerator - 1) instead of position numerator",
      "detection_method": "click_position_off_by_one"
    },
    {
      "misconception_id": 6,
      "misconception_tag": "numerator_denominator_reversal",
      "evidence": "Student clicks tick at denominator position instead of numerator position (e.g., clicks 4th tick for 3/4)",
      "detection_method": "click_position_equals_denominator"
    }
  ],

  "remediation_approach": {
    "light":"Redirect to counting spaces, not ticks",
    "medium": "Visual hint showing equal spacing with Helper guidance",
    "heavy": "Step-by-step guided placement with modeling"
  },

  "design_notes": {
    "vary_by": ["denominator", "numerator", "prompt_wording"],
    "hold_constant": ["0-1 range", "click_tick interaction", "horizontal orientation", "no intermediate labels"],
    "difficulty_scaling": "Stretch tier uses fifths and eighths, which have more intervals to count than the baseline thirds, fourths, and sixths"
  }
}
```
