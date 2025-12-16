"""
Module 1: Introduction to Fractions
"""

module_1 = {
    "module_name": "Introduction to Fractions",
    "module_number": 1,
    "grade_level": 3,
    "learning_goals": [
        "Partition shapes into equal areas (2,3,4,6,8) and name parts",
        "Express each equal part as a unit fraction of the whole"
    ],
    "vocabulary": [
        "partition",
        "whole",
        "equal parts",
        "halves",
        "thirds",
        "fourths",
        "sixths",
        "eighths"
    ],
    "variables": {
        "fraction_names": ["halves", "thirds", "fourths", "sixths", "eighths"],
        "fractions": ["1/2", "1/3", "1/4", "1/6", "1/8"],
    },
    "standards": {
        "building_on": [
            "2.G.A.3"
        ],
        "addressing": [
            "3.G.A.2",
            "3.NF.A.1"
        ],
        "building_toward": [
            "3.NF.A.2",
            "3.NF.A.2a"
        ]
    },
    "core_concepts": [
        "Equal Parts",
        "Defining the Whole"
    ],
    "available_visuals": {
        "tangibles": ["rectangle bar"],
        "description": "Rectangle bars are the primary visual for this module. Bars can be partly shaded or unshaded, partitioned into equal or unequal parts.",
        "constraints": [
            "All fractions are shown using rectangle bars divided into parts",
            "Parts can be shaded or unshaded",
            "A maximum of 4 bars can be shown for comparison",
            "Bars can show 2, 3, 4, 5, 6, or 8 parts based on the denominator"
        ]
    },
    "scope_fence":[
        "advanced_vocabulary": ["numerator", "denominator"],
        "advanced_concepts": ["comparing fraction sizes", "equivalent fractions", "number lines"]
    ],
    "misconceptions": [
        {
            "id": "1",
            "misconception": "Unequal Parts",
            "description": "Believing parts can be different sizes and still count as equal fractions"
        },
        {
            "id": "2",
            "misconception": "Misidentifying the Whole",
            "description": "Losing track of what the '1' is; comparing parts of different wholes"
        }
    ],
     "phases": [
    {
      "phase_name": "warm_up",
      "purpose": "Activate prior knowledge about equal-sized pieces and create engagement",
      "vocabulary_introduced_in_order": ["equal", "parts"],
      "variables": [
        {
          "fraction_names": [
            "halves",
            "fourths"
          ]
        }
      ],
      "interaction_count": "2-3"
    },
    {
      "phase_name": "lesson",
      "purpose": "Develop understanding that fractions require equal parts; learn to create equal partitions; name them with words, then with mathematical notation",
      "variables": [
        {
          "fraction_names": [
            "halves",
            "thirds",
            "fourths",
            "sixths",
            "eighths"
          ]
        }
      ],
      "vocabulary_introduced_in_order": [
        {
          "partition": "divide a shape into equal parts"
        },
        {
          "whole": "the entire shape together"
        },
        {
          "equal parts": "parts that are all the same size"
        }
      ],
      "interaction_count": "6-8"
    }
  ]
}
