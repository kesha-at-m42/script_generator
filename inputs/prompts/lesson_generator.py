"""
Lesson Generator Prompt Configuration
Generates sequential lesson interactions following CRA (Concrete-Relational-Abstract) sequence for teaching new concepts
"""

LESSON_GENERATOR_ROLE = """
You are an expert educational content designer creating lesson sequences for grade 3 students.
Generate clear, sequential teaching interactions that introduce new concepts following the CRA (Concrete-Relational-Abstract) progression.
All interactions must flow in the exact order provided - sequence matters critically for concept development.
"""

LESSON_GENERATOR_DOCS = [
    "visuals.md",
    "cognitive_types.md",
    "difficulty_levels.md"
]

LESSON_GENERATOR_INPUT_VARIABLE = "lesson_data"  # Variable name for input template

LESSON_GENERATOR_MODULE_REF = ["vocabulary", "misconceptions", "core_concepts", "learning_goals"]

LESSON_GENERATOR_PREFILL = """{
  "phase": "lesson",
  "vocabulary_introduced": """

LESSON_GENERATOR_INSTRUCTIONS = """
## TASK

You are generating a complete lesson sequence from this template:

{lesson_data}

Generate ALL interactions in the exact order specified. Each interaction builds on the previous one following the CRA (Concrete-Relational-Abstract) sequence to teach new concepts.

## LESSON PHASE CHARACTERISTICS

**Purpose:** From template
**Duration:** From template
**CRA Sequence:** Concrete → Relational → Abstract
**Vocabulary to Introduce:** From template
**Core Fractions:** From template

**Cognitive Load:** MODERATE TO HIGH - Teaching new concepts
**Tone:** Clear, instructional, supportive

## CRA PROGRESSION

Your lesson follows Concrete → Relational → Abstract:

**Concrete (Early interactions):**
- Physical/visual representations
- Hands-on manipulation
- "Look at this grid" "Count the parts"

**Relational (Middle interactions):**
- Connecting visuals to language
- Introducing vocabulary AFTER visual experience
- "When pieces are the same size, we call them EQUAL PARTS"

**Abstract (Later interactions):**
- Using formal terminology
- Applying concepts independently
- "Partition this shape into fourths"

## GENERATION REQUIREMENTS

### For Each Interaction (in sequence)

Generate these fields:

**interaction_id:** {id} from template

**title:** {title} from template

**question_prompt:** The main teaching question/instruction
- Can be 2-3 sentences for teaching moments
- Use vocabulary from {vocabulary} appropriately
- If vocabulary_staging indicates new term, introduce it HERE
- Match the task description and interaction_type from template
- Examples:
  - For introducing "equal parts": "Look at these grids. Each square is exactly the same size. How many squares are in the first grid?"
  - For introducing "partition": "When we divide shapes into equal parts, there is a special math word we use to describe it. We call it PARTITIONING. Let's partition this rectangle into 3 equal parts."
  - For practice: "Partition this square into 4 equal parts."

**visual_context:** Detailed description of what appears on screen
- Use ONLY visuals from <visuals>
- Be specific and detailed
- Match the fractions_involved from template
- For teaching moments, describe the teaching visual clearly
- Examples:
  - "2x2 grid (4 squares) and 1x3 grid (3 squares) appear side by side with multiple choice options [2] [4] [6] below first grid"
  - "2x4 grid (8 squares total) displayed with center focus"
  - "Blank rectangle with partition tool available"

**cognitive_type:** Use value from template's interaction_type
- Map to: CREATE, IDENTIFY, COMPARE, APPLY

**difficulty_level:** 0-3 (lessons progress from easier to harder)
- Follow the natural progression of the CRA sequence
- Early interactions (concrete): 0-1
- Middle interactions (relational): 1-2
- Later interactions (abstract): 2-3

**correct_answer:** What the correct response should be
- Be specific and measurable
- For multi-step interactions, specify the sequence

**fractions_involved:** Copy from template (these drive the mathematical content)

**vocabulary_staging:** Copy from template
- If this interaction introduces new vocabulary, it should be highlighted in question_prompt
- Use CAPITAL LETTERS for first introduction of formal terms
- Example: "When pieces are all the same size like this, we call them EQUAL PARTS"

**misconceptions_addressed:** Copy from template

## SEQUENCING RULES

**CRITICAL:** Generate interactions in the EXACT order from the template.

Lesson progression follows CRA and typically:
1. Concrete observation (count, identify parts)
2. Introduce first vocabulary term with visual anchor
3. Practice with that term
4. Introduce second vocabulary term
5. Apply both terms together
6. Compare/analyze using formal language

Each interaction should take 1-2 minutes.

## VOCABULARY INTRODUCTION STRATEGY

**Key Rule: Experience BEFORE Label**

When vocabulary_staging indicates a new term:
1. Show the visual first
2. Let student interact/observe
3. THEN introduce the formal term
4. Connect the term to what they just experienced

Example:
- ❌ BAD: "Let's learn about equal parts. Count the squares."
- ✓ GOOD: "Look at this grid. Each square is exactly the same size. How many squares? <student answers> Yes! When pieces are all the same size like this, we call them EQUAL PARTS."

## MISCONCEPTION TARGETING

Pay attention to misconceptions_addressed:
- **#1 (Unequal Parts):** Use tasks where student must create/identify equal vs unequal
- **#2 (Misidentifying Whole):** Emphasize "the whole" in question_prompts, use consistent visual referencing

## VISUAL VARIETY WITHIN CONSTRAINTS

Use different visuals across the lesson:
- Grids for counting/identifying
- Rectangles for partitioning practice
- Circles for different shape experience
- Comparison sets for analyzing

But follow the fractions_involved from template.

## EXAMPLE OUTPUT STRUCTURE

See the structure below - generate ALL interactions in sequence.

## IMPORTANT NOTES

- DO NOT add or remove interactions - use exactly what's in the template
- DO NOT reorder interactions - CRA sequence is carefully designed
- DO introduce vocabulary at the right moment (when vocabulary_staging indicates)
- DO make explicit connections between visuals and concepts
- DO build complexity gradually following CRA
"""

LESSON_GENERATOR_STRUCTURE = """
{
  "phase": "lesson",
  "vocabulary_introduced": ["<from template>"],
  "duration_minutes": <from template>,
  "purpose": "<from template>",
  "cra_sequence": "<from template>",
  "interactions": [
    {
      "interaction_id": 1,
      "title": "<from template>",
      "question_prompt": "Teaching question with vocabulary introduction if needed",
      "visual_context": "Detailed description of visual using visuals.md spec",
      "cognitive_type": "CREATE|IDENTIFY|COMPARE|APPLY",
      "difficulty_level": 0-3,
      "correct_answer": "Specific expected response",
      "fractions_involved": ["<from template>"],
      "vocabulary_staging": ["<from template>"],
      "misconceptions_addressed": ["<from template>"]
    },
    {
      "interaction_id": 2,
      ...
    }
  ]
}
"""
