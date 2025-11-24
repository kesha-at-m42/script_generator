# File Reorganization Steps

## Changes Made:
✅ Created `ui/` directory
✅ Created `config/` directory
✅ Created `scripts/` directory
✅ Moved `pipeline_ui.py` → `ui/app.py`
✅ Moved `run_ui_dev.py` → `ui/run_dev.py`
✅ Moved `nodemon.json` → `ui/nodemon.json`
✅ Moved `pipeline_runner.py` → `scripts/run_pipeline.py`
✅ Created `config/pipelines.py` with predefined pipelines

## Manual Updates Needed:

### 1. Update `ui/app.py` (lines 13-28):

Replace:
```python
# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from core.pipeline import Step, run_pipeline
from core.prompt_builder import Prompt
import importlib

# Import predefined pipelines
try:
    from pipeline_runner import PIPELINES as PREDEFINED_PIPELINES
except ImportError:
    PREDEFINED_PIPELINES = {}

# Configuration
PROMPTS_DIR = Path("inputs/prompts")
OUTPUTS_DIR = Path("outputs")
SAVED_PIPELINES_FILE = Path("saved_pipelines.json")
```

With:
```python
# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from core.pipeline import Step, run_pipeline
from core.prompt_builder import Prompt
import importlib

# Import predefined pipelines
try:
    from config.pipelines import PIPELINES as PREDEFINED_PIPELINES
except ImportError:
    PREDEFINED_PIPELINES = {}

# Configuration
PROMPTS_DIR = project_root / "inputs" / "prompts"
OUTPUTS_DIR = project_root / "outputs"
SAVED_PIPELINES_FILE = project_root / "ui" / "config" / "saved_pipelines.json"
```

### 2. Update `ui/run_dev.py` (line 23):

Replace:
```python
[sys.executable, "-m", "streamlit", "run", "pipeline_ui.py"],
```

With:
```python
[sys.executable, "-m", "streamlit", "run", "ui/app.py"],
```

### 3. Update `ui/run_dev.py` (lines 34-38):

Replace:
```python
print("\nWatching for changes in:")
print("  - pipeline_ui.py")
print("  - core/*.py")
print("  - utils/*.py")
```

With:
```python
print("\nWatching for changes in:")
print("  - ui/app.py")
print("  - core/*.py")
print("  - utils/*.py")
print("  - config/*.py")
```

### 4. Update `ui/nodemon.json`:

Replace:
```json
{
  "watch": [
    "pipeline_ui.py",
    "core/*.py",
    "utils/*.py",
    "inputs/prompts/*.py"
  ],
  "ext": "py",
  "exec": "streamlit run pipeline_ui.py",
  "delay": 1000
}
```

With:
```json
{
  "watch": [
    "ui/app.py",
    "core/*.py",
    "utils/*.py",
    "config/*.py",
    "inputs/prompts/*.py"
  ],
  "ext": "py",
  "exec": "streamlit run ui/app.py",
  "delay": 1000
}
```

### 5. Update `scripts/run_pipeline.py` (lines 1-94):

Replace the top section with:
```python
"""
CLI Pipeline Runner - Run predefined pipelines from command line

Usage:
    python scripts/run_pipeline.py
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.pipeline import Step, run_pipeline
from config.pipelines import PIPELINES
```

(Keep the rest of the file - the main execution block starting at line 100)

## New Commands:

### Run UI:
```bash
# From project root
streamlit run ui/app.py

# With auto-reload
python ui/run_dev.py
```

### Run CLI Pipeline:
```bash
python scripts/run_pipeline.py
```

## New File Locations:

- UI App: `ui/app.py`
- Saved Pipelines: `ui/config/saved_pipelines.json`
- Predefined Pipelines: `config/pipelines.py`
- CLI Runner: `scripts/run_pipeline.py`
