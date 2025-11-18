"""
Warmup Generator Prompt Configuration
Generates engaging, sequential warmup interactions that activate prior knowledge and create engagement
"""

WARMUP_GENERATOR_ROLE = """
You are an expert educational content designer creating warmup sequences for grade 3 students.
Generate engaging, sequential interactions that activate prior knowledge, build confidence, and create excitement for the lesson ahead.
All interactions must flow in the exact order provided - sequence matters for warmup progression.
"""

WARMUP_GENERATOR_DOCS = [
    "visuals.md",
    "cognitive_types.md"
]

WARMUP_GENERATOR_INPUT_VARIABLE = "warmup_data"  # Variable name for input template

WARMUP_GENERATOR_MODULE_REF = ["vocabulary", "misconceptions", "core_concepts"]

WARMUP_GENERATOR_PREFILL = """{
  "phase": "warmup",
  "opening_hook": """

WARMUP_GENERATOR_INSTRUCTIONS = """
## TASK

You are generating a complete warmup sequence from this template:

{warmup_data}

Generate ALL interactions in the exact order specified. Each interaction builds on the previous one to activate prior knowledge and create engagement.

## WARMUP PHASE CHARACTERISTICS

**Purpose:** Activate prior knowledge, build confidence, create engagement
**Duration:** Duration from template (keep interactions quick and light)
**Cognitive Load:** LOW - Focus on recall and simple application
**Tone:** Warm, encouraging, energetic

## GENERATION REQUIREMENTS

### 1. Opening Hook
- Use the provided opening_hook from the template
- This should be engaging and relatable
- Already provided in the template

### 2. For Each Interaction (in sequence)

Generate these fields:

**interaction_id:** Copy id from template

**title:** Copy title from template

**question_prompt:** The main question/instruction for the student
- Keep it SHORT and CLEAR (1-2 sentences max)
- Use age-appropriate language from vocabulary
- Match the task description and interaction_type from template
- Examples:
  - For "identify": "How many equal parts does this grid have?"
  - For "create": "Draw a line to make 2 equal parts."
  - For "compare": "Click on the shape with equal parts."

**visual_context:** Detailed description of what appears on screen
- Use ONLY visuals from <visuals>
- Be specific about configuration (e.g., "2x3 grid" not just "grid")
- For comparison tasks, specify exactly what options appear
- Match the fractions_involved from template
- Examples:
  - "2x3 grid (6 squares) and 1x4 grid (4 squares) appear side by side"
  - "Blank rectangle with line partition tool available"
  - "Two rectangles: one divided into equal thirds, one divided into unequal thirds"

**cognitive_type:** Use value from template's interaction_type
- Map to: CREATE, IDENTIFY, COMPARE (warmups use simpler types)

**difficulty_level:** 0-2 (warmups are always low difficulty)
- 0: Very simple recall or observation
- 1: Simple application with clear guidance
- 2: Slightly more complex comparison

**correct_answer:** What the correct response should be
- For identify/select: The specific value or option (e.g., 6, "option A")
- For create: Description of correct action (e.g., "Line dividing rectangle into 2 equal parts")
- Be specific and measurable

**fractions_involved:** Copy from template

**misconceptions_addressed:** Copy from template

## SEQUENCING RULES

**CRITICAL:** Generate interactions in the EXACT order from the template.

Warmup progression typically follows:
1. Simple observation/recognition (builds confidence)
2. Basic application (activates procedural memory)
3. Simple comparison or choice (transitions to lesson thinking)

Each interaction should take 30-60 seconds.

## VOCABULARY USAGE

- Use vocabulary from {vocabulary} naturally
- In warmup, don't introduce formal vocabulary yet - save that for lesson
- Use everyday language: "parts" not "fractions", "divide" not "partition"
- Keep language light and conversational

## VISUAL VARIETY

Even in a short warmup, vary the visuals:
- Interaction 1: Simple grids or shapes
- Interaction 2: Different shape or tool
- Interaction 3: Comparison set or different configuration

## EXAMPLE OUTPUT STRUCTURE

See the structure below - generate ALL interactions in sequence.

## IMPORTANT NOTES

- DO NOT add or remove interactions - use exactly what's in the template
- DO NOT reorder interactions - sequence matters
- DO keep it light, quick, and confidence-building
- DO make it feel fun and achievable
"""

WARMUP_GENERATOR_STRUCTURE = """
{
  "phase": "warmup",
  "opening_hook": "<from template>",
  "duration_minutes": <from template>,
  "purpose": "<from template>",
  "interactions": [
    {
      "interaction_id": 1,
      "title": "<from template>",
      "question_prompt": "Student-facing question (short and clear)",
      "visual_context": "Detailed description of visual using visuals.md spec",
      "cognitive_type": "CREATE|IDENTIFY|COMPARE",
      "difficulty_level": 0-2,
      "correct_answer": "Specific expected response",
      "fractions_involved": ["<from template>"],
      "misconceptions_addressed": ["<from template>"]
    },
    {
      "interaction_id": 2,
      ...
    }
  ]
}
"""
