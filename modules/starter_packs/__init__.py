"""
Starter Packs - Module Definitions
Consolidates all module configurations for easy import
"""

from .module_1 import module_1
from .module_2 import module_2
from .module_3 import module_3
from .module_4 import module_4
from .module_5 import module_5
from .module_6 import module_6
from .module_7 import module_7
from .module_8 import module_8
from .module_9 import module_9
from .module_10 import module_10
from .module_11 import module_11
from .module_12 import module_12

# Dictionary of all modules for easy lookup
MODULES = {
    1: module_1,
    2: module_2,
    3: module_3,
    4: module_4,
    5: module_5,
    6: module_6,
    7: module_7,
    8: module_8,
    9: module_9,
    10: module_10,
    11: module_11,
    12: module_12
}

# Export for easy import
__all__ = ['MODULES', 'module_1', 'module_2', 'module_3', 'module_4', 'module_5', 'module_6', 'module_7', 'module_8', 'module_9', 'module_10', 'module_11', 'module_12']
