"""
Starter Packs - Module Definitions
Consolidates all module configurations for easy import
"""

from .module_1 import module_1
from .module_2 import module_2
from .module_3 import module_3
from .module_4 import module_4
from .module_5 import module_5

# Dictionary of all modules for easy lookup
MODULES = {
    1: module_1,
    2: module_2,
    3: module_3,
    4: module_4,
    5: module_5
}

# Export for easy import
__all__ = ['MODULES', 'module_1', 'module_2', 'module_3', 'module_4', 'module_5']
