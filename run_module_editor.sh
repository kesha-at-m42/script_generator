#!/bin/bash
# Launch Module Editor (Mac/Linux/Git Bash)

echo ""
echo "========================================"
echo "  Module Editor Launcher"
echo "========================================"
echo ""
echo "Starting module editor..."
echo ""

cd "$(dirname "$0")"
source venv/Scripts/activate
streamlit run dashboard/run_module_editor.py
