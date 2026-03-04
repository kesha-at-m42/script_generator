"""
Starter Packs - Module Definitions
Loads all module configurations from JSON files.
"""

import json
from pathlib import Path

_DIR = Path(__file__).parent

MODULES: dict[int, dict] = {}
for _n in range(1, 13):
    _path = _DIR / f"module_{_n}.json"
    if _path.exists():
        MODULES[_n] = json.loads(_path.read_text(encoding="utf-8"))

# Individual module variables kept for backwards-compatibility
module_1 = MODULES.get(1, {})
module_2 = MODULES.get(2, {})
module_3 = MODULES.get(3, {})
module_4 = MODULES.get(4, {})
module_5 = MODULES.get(5, {})
module_6 = MODULES.get(6, {})
module_7 = MODULES.get(7, {})
module_8 = MODULES.get(8, {})
module_9 = MODULES.get(9, {})
module_10 = MODULES.get(10, {})
module_11 = MODULES.get(11, {})
module_12 = MODULES.get(12, {})

__all__ = [
    "MODULES",
    "module_1",
    "module_2",
    "module_3",
    "module_4",
    "module_5",
    "module_6",
    "module_7",
    "module_8",
    "module_9",
    "module_10",
    "module_11",
    "module_12",
]
