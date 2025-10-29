"""
Module Data - All Modules
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
        "description": "rectangle bars are the primary visual for this module. Bars can be partly shaded or unshaded, partitioned into equal or unequal parts.",
        "constraints": [
            "All fractions are shown using rectangle bars divided into parts",
            "Parts can be shaded or unshaded",
            "A maximum of 4 bars can be shown for comparison",
            "Bars can show 2, 3, 4, 5, 6, or 8 parts based on the denominator"
        ]
    },
    "misconceptions": [
        {
            "misconception": "Unequal Parts",
            "description": "Believing parts can be different sizes and still count as equal fractions"
        },
        {
            "misconception": "Misidentifying the Whole",
            "description": "Losing track of what the '1' is; comparing parts of different wholes"
        }
    ]
}

module_2 = {
    "module_name": "Comparing Fractions",
    "module_number": 2,
    "grade_level": 3,
    "learning_goals": [
        "Understand a fraction a/b as the quantity formed by a parts of size 1/b."
    ],
    "vocabulary": [
        "unit fraction",
        "unit fractions",
        "one-half",
        "one-third",
        "less than",
        "equal to",
        "numerator",
        "denominator"
    ],
    "standards": {
        "building_on": [
            "3.NF.A.1"
        ],
        "addressing": [
            "3.NF.A.3",
            "3.NF.A.3d"
        ],
        "building_toward": [
            "4.NF.A.1",
            "4.NF.A.2"
        ]
    },
    "core_concepts": [
        "Unit fraction language",
        "Labeling parts"
    ],
    "misconceptions": [
        {
            "misconception": "Numerator/denominator as Independent",
            "description": "Progressive composition shows numerator growing as unit fractions accumulate"
        },
        {
            "misconception": "Reversing Numerator and Denominator",
            "description": "Consistent vertical stacking reinforces 'count on top, total parts below'"
        }
    ]
}

# Dictionary of all modules for easy lookup
MODULES = {
    1: module_1,
    2: module_2,
}

# Export for easy import
__all__ = ['module_1', 'module_2', 'MODULES']
