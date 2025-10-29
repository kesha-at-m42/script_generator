import json
import re

def remove_event_tags(data):
    """
    Recursively removes all [event:...] tags from strings in the data structure.
    """
    if isinstance(data, dict):
        return {key: remove_event_tags(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [remove_event_tags(item) for item in data]
    elif isinstance(data, str):
        # Remove all [event:...] tags using regex
        return re.sub(r'\[event:[^\]]+\]', '', data)
    else:
        return data

import sys
import os

# Get input and output paths from command line arguments
if len(sys.argv) < 2:
    print("Usage: python script.py <input_file> [output_file]")
    print("Example: python script.py input.json")
    print("Example: python script.py input.json custom_output.json")
    sys.exit(1)

input_path = sys.argv[1]

# If output path is provided, use it; otherwise generate from input path
if len(sys.argv) > 2:
    output_path = sys.argv[2]
else:
    # Split the input path into directory, filename, and extension
    directory = os.path.dirname(input_path)
    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)
    
    # Create output filename with _untagged suffix
    output_filename = f"{name}_untagged{ext}"
    output_path = os.path.join(directory, output_filename) if directory else output_filename

# Read the input JSON file
try:
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: File '{input_path}' not found")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"Error: '{input_path}' is not a valid JSON file")
    sys.exit(1)

# Remove event tags
cleaned_data = remove_event_tags(data)

# Write the cleaned data to output file
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, indent=2, ensure_ascii=False)

print("Event tags removed successfully!")
print(f"Input file: {input_path}")
print(f"Output file: {output_path}")