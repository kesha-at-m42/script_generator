# Formatting Steps

Deterministic post-processing functions that don't call AI.

## Available Formatters

### script_formatter.py
- `format_interactions_to_markdown()` - Converts interaction JSON to readable markdown

## How to Add a New Formatter

1. Create a new `.py` file in this directory
2. Define your formatting function:
   ```python
   def my_formatter(input_data, module_number=None, path_letter=None, **kwargs):
       """
       Your formatting logic here

       Args:
           input_data: The data to format (from previous step)
           module_number: Auto-passed by pipeline
           path_letter: Auto-passed by pipeline
           **kwargs: Custom arguments from function_args

       Returns:
           Formatted output (string, dict, or list)
       """
       # Your code here
       return formatted_output
   ```

3. The function will automatically appear in the UI dropdown!

## Convention

- Function names should be descriptive: `format_X_to_Y`
- Always accept `input_data` as first parameter
- Optional: `module_number`, `path_letter` (auto-passed)
- Use `**kwargs` for custom arguments
