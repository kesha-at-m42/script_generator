"""
Module Data - All Modules

This file re-exports from starter_packs/ for backwards compatibility.
For new code, import directly from:
    from inputs.modules.starter_packs import MODULES
"""

from .starter_packs import (
    MODULES,
    module_1,
    module_2,
    module_3,
    module_4,
    module_5
)

# Export for easy import
__all__ = ['MODULES', 'module_1', 'module_2', 'module_3', 'module_4', 'module_5']
