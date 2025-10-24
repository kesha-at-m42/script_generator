"""Deterministic step to split questions by difficulty level"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.pipeline import Step


class DifficultySplitter(Step):
    """Splits questions/sequences by difficulty level into separate files (no AI)"""
    
    def __init__(self):
        super().__init__(name="Difficulty Splitter", prompt_id=None)
    
    def execute(self, input_data, **kwargs):
        """Execute step - split by difficulty and save separate files"""
        
        # Determine if input is questions or sequences
        if "questions" in input_data:
            data_type = "questions"
            items = input_data.get("questions", [])
        elif "sequences" in input_data:
            data_type = "sequences"
            items = input_data.get("sequences", [])
        else:
            print("  ⚠️  No questions or sequences found in input data")
            return input_data
        
        print(f"  📊 Splitting {len(items)} {data_type} by difficulty level...")
        
        # Group by difficulty
        difficulty_groups = {
            0: [],  # Support
            1: [],  # Confidence
            2: [],  # Baseline
            3: [],  # Stretch
            4: []   # Challenge
        }
        
        difficulty_names = {
            0: "support",
            1: "confidence",
            2: "baseline",
            3: "stretch",
            4: "challenge"
        }
        
        # Group items by difficulty
        for item in items:
            difficulty = item.get("difficulty_level" if data_type == "questions" else "difficulty")
            if difficulty in difficulty_groups:
                difficulty_groups[difficulty].append(item)
            else:
                print(f"  ⚠️  Unknown difficulty level: {difficulty}")
        
        # Print summary
        print(f"\n  Difficulty distribution:")
        for level, items_list in difficulty_groups.items():
            if items_list:
                name = difficulty_names[level].capitalize()
                print(f"    Level {level} ({name}): {len(items_list)} {data_type}")
        
        # Get the run folder from kwargs if available (passed from pipeline)
        run_folder = kwargs.get("run_folder")
        
        if run_folder:
            self._save_difficulty_files(difficulty_groups, difficulty_names, data_type, run_folder)
        
        # Return original data unchanged (this step only saves additional files)
        return input_data
    
    def _save_difficulty_files(self, difficulty_groups, difficulty_names, data_type, run_folder):
        """Save separate JSON files for each difficulty level"""
        from datetime import datetime
        
        timestamp = datetime.now().strftime("%H%M%S")
        saved_files = []
        
        for level, items in difficulty_groups.items():
            if not items:
                continue
            
            name = difficulty_names[level]
            filename = f"{data_type}_{name}_{timestamp}.json"
            filepath = Path(run_folder) / filename
            
            # Create output structure
            output = {data_type: items}
            
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(output, f, indent=2)
            
            saved_files.append(filepath)
            print(f"  💾 Saved {len(items)} {data_type} to {filename}")
        
        return saved_files


# Test it
if __name__ == "__main__":
    import json
    
    print("Testing DifficultySplitter...\n")
    
    # Sample questions data
    sample_questions = {
        "questions": [
            {"id": 1, "difficulty_level": 0, "question_text": "Easy question"},
            {"id": 2, "difficulty_level": 0, "question_text": "Another easy one"},
            {"id": 3, "difficulty_level": 1, "question_text": "Medium question"},
            {"id": 4, "difficulty_level": 2, "question_text": "Baseline question"},
            {"id": 5, "difficulty_level": 2, "question_text": "Another baseline"},
            {"id": 6, "difficulty_level": 3, "question_text": "Stretch question"},
            {"id": 7, "difficulty_level": 4, "question_text": "Challenge question"},
        ]
    }
    
    print("Input: 7 sample questions with various difficulty levels")
    
    splitter = DifficultySplitter()
    
    # Test with mock run_folder
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        result = splitter.execute(sample_questions, run_folder=tmpdir)
        
        print(f"\n✓ Split complete")
        print(f"  Output directory: {tmpdir}")
        
        # List created files
        output_files = list(Path(tmpdir).glob("questions_*.json"))
        print(f"\n  Created {len(output_files)} files:")
        for f in output_files:
            with open(f, 'r') as file:
                data = json.load(file)
                count = len(data.get('questions', []))
                print(f"    - {f.name}: {count} questions")
