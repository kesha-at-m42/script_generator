"""Simple file utilities"""
import json
from pathlib import Path

def save_json(data, filename: str, output_dir: str = "output"):
    """Save data as JSON file"""
    # Create directory if needed
    Path(output_dir).mkdir(exist_ok=True)
    
    filepath = Path(output_dir) / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Saved to: {filepath}")
    return filepath

def load_json(filename: str, output_dir: str = "output"):
    """Load JSON file"""
    filepath = Path(output_dir) / filename
    
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

# Test it
if __name__ == "__main__":
    print("Testing file utilities...\n")
    
    # Test save
    test_data = {"test": "data", "number": 123}
    saved_path = save_json(test_data, "test.json")
    
    # Test load
    loaded = load_json("test.json")
    print(f"Loaded: {loaded}")
    
    print("\n✓ File utilities work!")