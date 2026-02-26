# Prompt: test_doc_prompt
# Generated: 2026-01-21T16:09:35.941611
======================================================================

## API Parameters

======================================================================

## System Prompt

### Block 1: Role
Purpose: Establishes AI role and task context
Cacheable: Yes

# ROLE & CONTEXT

You are a test assistant.

----------------------------------------------------------------------

### Block 2: Reference Doc (visuals.md)
Purpose: Reference documentation
Cacheable: Yes

# REFERENCE DOCUMENTATION: visuals.md

<visuals>
# Visual Constraints - Module 1 Path B

## Tangible Types
- Rectangle bars

## Description
Rectangle bars are the primary visual for this module. Bars can be partly shaded or unshaded, partitioned into equal or unequal parts.

## Constraints
- All fractions are shown using rectangle bars divided into parts
- Parts can be shaded or unshaded
- A maximum of 4 bars can be shown for comparison
- Bars can show 2, 3, 4, 5, 6, or 8 parts based on the denominator

</visuals>

----------------------------------------------------------------------

### Block 3: Reference Doc (visual_guide.md)
Purpose: Reference documentation
Cacheable: Yes

# REFERENCE DOCUMENTATION: visual_guide.md

<visual_guide>
# Visual Guide for Module 1 Path B

## Tangible Types
- Rectangle Bars
---

## Task 1: Divide/Partition into X Equal Parts
- **Tangible**: Rectangle Bars
- **Tool**: cut

## Task 2: Shade 1 Part
- **Tangible**: Rectangle Bars
- **Tool**: shade

## Task 3: Identify Shape with Equal/Unequal Parts
- **Tangible**: Rectangle Bars
- **Tool**: select

## Task 4: Identify Shape with X Equal Parts
- **Tangible**: Rectangle Bars
- **Tool**: select
</visual_guide>

----------------------------------------------------------------------

### Block 4: Examples
Purpose: Demonstration of expected output format
Cacheable: Yes

# EXAMPLES

<examples>
Example 1:
Example 1: Simple test

Test output
</examples>

----------------------------------------------------------------------

### Block 5: Output Schema
Purpose: Defines expected output structure
Cacheable: Yes
*[CACHED: {'type': 'ephemeral'}]*

# OUTPUT STRUCTURE

<output_structure>
Expected output format:
{
    "result": "value"
}
</output_structure>

----------------------------------------------------------------------

## User Message

<input>
Test input content here.
</input>

Process the input data.

======================================================================

