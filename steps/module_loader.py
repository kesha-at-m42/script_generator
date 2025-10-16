import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.pipeline import Step
from inputs.modules import MODULES


class ModuleLoader(Step):
    """Loads learning goals and module data from a module number"""
    
    def __init__(self):
        super().__init__(name="Module Loader", prompt_id="module_loader")
    
    def execute(self, input_data, **kwargs):
        """Execute step - loads module data by module number"""
        # Handle both dict and direct number inputs
        if isinstance(input_data, dict):
            module_number = input_data.get("module_number")
        else:
            module_number = input_data
        
        # Allow override from kwargs
        if "module_number" in kwargs:
            module_number = kwargs["module_number"]
        
        if module_number is None:
            raise ValueError("module_number is required")
        
        # Fetch module data
        if module_number not in MODULES:
            available = ", ".join(str(k) for k in MODULES.keys())
            raise ValueError(f"Module {module_number} not found. Available modules: {available}")
        
        module_data = MODULES[module_number]
        
        # Extract and format learning goals (from detailed goals array)
        learning_goals = module_data["learning_goals"]  # Original simple goals
        goals = module_data.get("goals", [])  # Detailed goals with IDs
        
        # Format detailed goals for AI
        goals_text = ""
        for goal in goals:
            goals_text += f"\nGoal ID {goal['id']}: {goal['text']}\n"
            goals_text += f"  Vocabulary: {', '.join(goal.get('vocabulary_used', []))}\n"
            if goal.get('example_questions'):
                goals_text += f"  Example: {goal['example_questions'][0]}\n"
        
        print(f"  📚 Loaded Module {module_number}: {module_data['module_name']}")
        print(f"  🎯 Grade Level: {module_data['grade_level']}")
        print(f"  📖 Learning Goals: {len(goals)} detailed goals")
        
        # Return data in format expected by QuestionGenerator
        return {
            "module_number": module_number,
            "module_name": module_data["module_name"],
            "grade_level": module_data["grade_level"],
            "learning_goals": goals_text,
            "learning_goals_list": learning_goals,
            "goals": goals,  # Detailed goals with IDs
            "full_module_data": module_data
        }


# Test it
if __name__ == "__main__":
    from core.pipeline import Pipeline
    
    print("Testing ModuleLoader...\n")
    
    loader = ModuleLoader()
    
    # Test with pipeline
    pipeline = Pipeline("test_module_loader", save_intermediate=True)
    pipeline.add_step(loader)
    
    # Test module 1
    print("=" * 70)
    results = pipeline.execute({"module_number": 1})
    print("=" * 70)
    
    # Display results
    result = pipeline.get_final_output()
    
    print(f"\n✨ Module Data Loaded:\n")
    print(f"Module: {result['module_name']}")
    print(f"Grade: {result['grade_level']}")
    print(f"\nLearning Goals:")
    print(result['learning_goals'])
    
    print(f"\n✅ Ready to pass to QuestionGenerator!")
