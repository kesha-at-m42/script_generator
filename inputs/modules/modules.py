"""
Module Data - All Modules
"""

module_1 = {
    "module_name": "Introduction to Fractions",
    "module_number": 1,
    "grade_level": 3,
    "path_variant": "B",
    "learning_goals": [
        "Partition shapes into equal areas (2,3,4,6,8) and name parts",
        "Express each equal part as a unit fraction of the whole"
    ],
    "vocabulary": [
        "partition",
        "whole",
        "equal parts",
        "unit fraction",
        "numerator",
        "denominator"
    ],
    "variables": {
        "parts": ["halves", "thirds", "fourths", "sixths", "eighths"],
        "unit_fraction": ["1/2", "1/3", "1/4", "1/6", "1/8"],
        "denominator": [2, 3, 4, 6, 8]
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
        "shapes": ["rectangle bar"],
        "description": "Rectangular bars are the primary visual for this module. Bars can be oriented horizontally or vertically, and can be partitioned into equal or unequal parts.",
        "constraints": [
            "All fractions are shown using rectangle bars divided into parts",
            "Parts can be shaded or unshaded",
            "Multiple bars can be shown for comparison",
            "Bars can show 2, 3, 4, 5, 6, or 8 parts based on the denominator"
        ]
    },
    "misconceptions": [
        {
            "misconception": "More pieces means bigger fractions",
            "correction": "More pieces means smaller unit fractions (1/8 < 1/4)"
        },
        {
            "misconception": "All pieces must be the same shape to be equal",
            "correction": "Pieces can be different shapes but same area/size"
        }
    ]
}

module_2 = {
    "module_name": "Comparing Fractions",
    "module_number": 2,
    "grade_level": 3,
    "path_variant": "B",
    "learning_goals": [
        "Compare fractions with the same numerator or denominator",
        "Understand that fractions with larger denominators represent smaller pieces"
    ],
    "vocabulary": [
        "compare",
        "greater than",
        "less than",
        "equal to",
        "numerator",
        "denominator",
        "equivalent"
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
        "Fraction Comparison",
        "Relative Size"
    ],
    "goals": [
        {
            "id": 1,
            "text": "Compare unit fractions and recognize that larger denominators mean smaller pieces",
            "content_categories": [
                "unit_fractions",
                "comparison"
            ],
            "examples": [
                "Which is larger: 1/3 or 1/6? Explain using a diagram",
                "Order these fractions from smallest to largest: 1/2, 1/4, 1/8"
            ]
        },
        {
            "id": 2,
            "text": "Compare fractions with the same denominator using numerators",
            "content_categories": [
                "comparison",
                "numerators"
            ],
            "examples": [
                "Which is larger: 2/5 or 4/5? How do you know?",
                "Use > or < to compare: 3/8 ___ 5/8"
            ]
        }
    ],
    "misconceptions": [
        {
            "misconception": "A fraction with a bigger denominator is always larger",
            "correction": "Larger denominators mean smaller unit fractions (1/8 is smaller than 1/4)"
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
