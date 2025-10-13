# 📚 Documentation Structure

## Main Documentation
- **[docs/README.md](docs/README.md)** - Complete guide covering everything
- **[docs/QUICK_REFERENCE.py](docs/QUICK_REFERENCE.py)** - Quick visual reference (run with `python docs/QUICK_REFERENCE.py`)

## What's Covered

### Module Editor
- Visual form editor for module data
- How to add/edit/delete modules
- Dropdown selector usage
- Save functionality

### Pipeline System
- Creating multi-step workflows
- Using module data in pipelines
- Building custom steps
- Token usage tracking

### Dashboard
- 5 pages explained (Prompt Editor, Test, Chain, Module Editor, History)
- How to manage prompts
- Testing workflows

### Data Access
- Direct Python imports (no parser needed)
- Module data structure
- Working with `inputs/modules.py`

### Common Tasks
- Adding new modules
- Creating pipelines
- Managing prompts
- Troubleshooting

## Quick Start

```bash
# Module Editor
streamlit run dashboard/run_module_editor.py

# Full Dashboard
streamlit run dashboard/app.py

# Quick Reference
python docs/QUICK_REFERENCE.py
```

---

**Everything in one place: [docs/README.md](docs/README.md)** 🎯
