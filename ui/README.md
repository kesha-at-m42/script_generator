# Pipeline UI

Web-based interface for managing and running pipelines.

## Quick Start

```bash
# From project root
streamlit run ui/app.py

# Or with auto-reload
python ui/run_dev.py
```

## Files

- `app.py` - Main Streamlit application
- `run_dev.py` - Development server with auto-reload
- `nodemon.json` - Config for nodemon (if using)
- `config/saved_pipelines.json` - User-saved pipelines

## Features

1. **Build Pipelines** - Add AI and formatting steps
2. **Edit Prompts** - Edit prompt files directly
3. **Save/Load** - Save custom pipelines for reuse
4. **Run** - Execute pipelines with configuration
