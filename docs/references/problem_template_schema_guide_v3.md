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
- **Example**: `"Student identifies which fraction is closer to 0"`

---

### **workspace_description** (string)
- **Purpose**: Plain-language description of the visual workspace which includes interactables as well as options for multiple choice questions
- **Example**: `"Number line from 0 to 1 with only endpoints labeled. No tick marks between 0 and 1."`
- Can be empty string `""` if not yet specified

---

### **prompt_examples** (array of strings)
- **Purpose**: Multiple concrete example phrasings of the problem prompt
- **Example**:
  ```json
  [
    "Divide this number line into 3 equal parts.",
    "Place ticks to make fourths.",
    "Split the line into 6 equal spaces."
  ]
  ```
- Can be `[""]` if not yet specified

---

### **action_description** (string)
- **Purpose**: Narrative description of the actions student is expected to perform
- **Example**: `"Student taps on the line to place tick marks at positions they choose"`
- **Example**: `"Student selects the correct option"`

---

### **no_of_steps** (number)
- **Purpose**: The number of steps required to complete the problem
- **Format**: Integer value (e.g., `1`, `2`, `3`)
- **Example**: `2` for a two-step problem

---

### **target_count** (number)
- **Purpose**: The target number of problem instances to generate from this template
- **Format**: Integer value (e.g., `5`, `10`, `20`)
- **Example**: `10` means we want to generate 10 different problem instances from this template

---

### **mastery_tier** (array of strings)
- **Purpose**: Difficulty level(s) this template can generate problems for
- **Options**: `"confidence"`, `"support"`, `"baseline"`, `"stretch"`, `"challenge"`
- **Example**: `["baseline", "stretch"]`

---

### **mastery_verb** (string)
- **Purpose**: The cognitive action being assessed
- **Options**: `"create"`, `"identify"`, `"compare"`, `"apply"`, `"analyze"`, `"evaluate"`
- **Example**: `"apply"`

---

### **parameter_coverage** (object)
Defines the mathematical parameters that will vary across problem instances.

#### **Common parameter types:**

**fractions** (array)
- **Purpose**: List of all fractions this template can generate problems for
- **Example**: `["1/2", "1/3", "2/3", "3/4", "5/6"]`
- **Example**: `["5/4", "6/4", "7/4"]`

**denominators** (array)
- **Purpose**: List of denominators to use (when problems vary denominator but not specific fractions)
- **Example**: `["2", "3", "4", "6", "8"]` or `[2, 3, 4, 6, 8]`

**other_parameters** (flexible)
- Add any problem-specific parameters needed (e.g., `"ranges"`, `"benchmark_values"`, `"comparison_types"`)

---

### **correct_end_state** (string)
- **Purpose**: Description of what the workspace looks like when correct
- **Example**: `"Line shows 5 equal intervals with 4 evenly spaced tick marks between 0 and 1"`
- **Example**: `"Selected answer highlighted"`

---

### **success_dialogue** (array of strings)
- **Purpose**: Feedback messages shown when student answers correctly
- **Should**: Be varied, brief (5-15 words), encouraging
- **Example**:
  ```json
  [
    "Five spaces from zero—five-fourths.",
    "Right! Six intervals means 6/4.",
    "Seven-fourths. Past one whole."
  ]
  ```

---

## Complete Example

```json
{
  "template_id": "4015",
  "problem_type": "Student identifies which fraction is closer to 0",
  "workspace_description": "Number line from 0 to 2 with tick marks at quarter intervals. Multiple choice options showing fractions.",
  "prompt_examples": [
    "Which fraction is closer to zero?",
    "Select the fraction nearest to 0.",
    "Which of these fractions is closest to zero?"
  ],
  "action_description": "Student selects the correct option",
  "no_of_steps": 1,
  "target_count": 10,
  "mastery_tier": ["baseline", "stretch"],
  "mastery_verb": "apply",
  "parameter_coverage": {
    "fractions": ["5/4", "6/4", "7/4"]
  },
  "correct_end_state": "Selected answer highlighted",
  "success_dialogue": [
    "Five spaces from zero—five-fourths.",
    "Right! Six intervals means 6/4.",
    "Seven-fourths. Past one whole."
  ]
}
```
