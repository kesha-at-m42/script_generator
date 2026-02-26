"""
Module Data - All Modules

This file re-exports from starter_packs/ for backwards compatibility.
For new code, import directly from:
    from modules.starter_packs import MODULES
"""

import sys
from pathlib import Path

# Add project root to path if not already there
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from modules.starter_packs import (
    MODULES,
    module_1,
    module_2,
    module_3,
    module_4,
    module_5,
    module_6,
    module_7,
    module_8,
    module_9,
    module_10,
    module_11,
    module_12
)

# Export for easy import
__all__ = ['MODULES', 'module_1', 'module_2', 'module_3', 'module_4', 'module_5', 'module_6', 'module_7', 'module_8', 'module_9', 'module_10', 'module_11', 'module_12']
