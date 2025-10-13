"""
Standalone Module Editor
Run this directly: streamlit run dashboard/run_module_editor.py
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dashboard.module_editor import render_module_editor

if __name__ == "__main__":
    render_module_editor()
