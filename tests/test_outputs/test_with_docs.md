# Prompt: test_doc_prompt
# Generated: 2026-04-03T10:54:13.574152
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

### Block 2: Instructions
Purpose: Step-by-step task instructions
Cacheable: Yes

# TASK INSTRUCTIONS

Process the input data.

----------------------------------------------------------------------

### Block 3: Examples
Purpose: Demonstration of expected output format
Cacheable: Yes

# EXAMPLES

<examples>
Example 1:
Example 1: Simple test

Test output
</examples>

----------------------------------------------------------------------

### Block 4: Output Schema
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

======================================================================

