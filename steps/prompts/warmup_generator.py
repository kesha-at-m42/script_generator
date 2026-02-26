"""
warmup_generator - AI Prompt
"""

import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

WARMUP_GENERATOR_PROMPT = Prompt(
    role="""You are converting a detailed lesson specification into structured JSON format. This is TRANSLATION work, not creative work. The pedagogical decisions have already been made—your job is faithful conversion.""",

    instructions="""


Convert each of the interactions listed in <warmup_specs> into the structured JSOn format.

For each interaction,
 #### Step 1: Understand Intent
 - What is the **educational purpose** of this interaction?
 - What **misconception** is it addressing or what **concept** is it activating?
 - What makes this interaction different from others?
 Using this, fill these fields of:
  "interaction_id": 1,
  "interaction_name": "Pithy name (3-6 words)"
 

 #### Step 2: Analyze Visual Description and refer to <visuals> to Set Up Workspace
 For each shape described:
 1. Determine **shape type** (rectangle or hexagon)
 2. Determine if **divided** or whole
 3. If divided, identify **cut type**:
    - Vertical cuts? How many columns?
    - Horizontal cuts? How many rows?
    - Radial cuts (hexagon)?
 4. Determine if parts are **equal or unequal**
 5. Express cuts as **part size fractions**:
    - Equal: all fractions identical (e.g., `[1/3, 1/3, 1/3]`)
    - Unequal: fractions differ (e.g., `[1/2, 1/4, 1/4]`)
 6. Determine **shading** (if any)

 Create workspace object:
 ```json
 {
   "toy_id": "descriptive_id",
   "toy_shape": "rectangle|hexagon",
   "toy_description": "Clear description from warmup_specs",
   "divided": true|false,
   "division_count": N,
   "is_divided_equal": true|false,
   "horizontal_cuts": [],
   "vertical_cuts": [],
   "radial_cuts": [],
   "shaded": []
 }
 ```

 #### Step 4: Determine Dialogue and Correct Answer
 Refer back to:
 - **Visual**: What student sees
 - **Purpose**: Why this interaction exists
 - **Content**: What warmup_specs says should happen

 Write:
 1. **dialogue**: Guide speaks (include [event:name] tags if demonstration)
    - Use only vocabulary from USE column
    - Match tone from specifications
    - Reference the visual purpose
 2. **prompt**: What student should do (clear action)
 3. **interaction_tool**: select, cut, shade, click_choice, or none
 4. **correct_answer**:
    - value: toy_id of correct choice OR expected input
    - context: Why this is correct (educational reasoning)

 ---

 ## CUT REPRESENTATION GUIDE:

 Cuts are **part sizes** (fractions that sum to 1).

 ### Simple divisions (1D array):
 ```
 ["1/2", "1/2"]           → 2 equal parts
 ["1/3", "1/3", "1/3"]      → 3 equal parts
 ["1/2", "1/4", "1/4"]      → 3 unequal parts
 ```

 ### Grids (both dimensions have 1D arrays):
 ```
 vertical_cuts: ["1/2", "1/2"]
 horizontal_cuts: ["1/2", "1/2"]
 → 2×2 grid = 4 equal parts
 ```

 ### Partial cuts (2D array for columns with different row divisions):
 ```
 vertical_cuts: ["1/2", "1/2"]           → 2 columns
 horizontal_cuts: [["1/2, "1/2"], ["1"]]  → column 1: 2 rows, column 2: whole
 → 3 total parts
 ```
 ---

  CRITICAL: Output ONLY valid JSON as described in <output_structure>. No explanations. No analysis. No verification.
  Your entire response must be ONLY the JSON object starting with { and ending with }.


""",

    doc_refs=['visuals.md'],  # Only static reference docs - warmup_specs is input data

    output_structure="""


{
  "sequences": [
    {
      "interaction_id": 1,
      "interaction_name": "Pithy name (3-6 words)",
      "fractions": [],
      "vocabulary_introduced": [],
      "steps": [
        {
          "dialogue": "Guide dialogue with [event:name] tags for demonstrations",
          "prompt": "Student action instruction",
          "interaction_tool": "cut|shade|select|multi_select|click_choice|none",
          "workspace": [
            {
            "toy_id": "rect_unequal_2",
            "toy_shape": "rectangle",
            "toy_description": "Rectangle divided into 2 unequal parts",
            "divided": true,
            "division_count": 2,
            "is_divided_equal": false,
            "horizontal_cuts": [],
            "vertical_cuts": ["1/3", "2/3"],
            "radial_cuts": [],
            "shaded": []
          }
          ],
          "correct_answer": {
            "value": "expected_answer",
            "context": "Why this is correct"
          },
          "student_attempts": {
            "success_path": {
              "dialogue": "Brief positive feedback"
            }
          }
        }
      ]
    }
  ]
}
  
""",

    prefill="""""",

    examples=[],

    module_ref={},

    template_ref={},

    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=18000,
    stop_sequences=[]
)
