"""Input parsers for extracting data from structured JSON files"""
import json
from pathlib import Path
from typing import Dict, List, Any

class ModuleInputParser:
    """Parser for module JSON files to extract learning goals and metadata"""
    
    def __init__(self, json_file_path: str):
        self.file_path = Path(json_file_path)
        self.data = self._load_json()
        
    def _load_json(self) -> Dict:
        """Load JSON file"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def get_learning_goals(self) -> str:
        """Extract learning goals as formatted string"""
        goals = self.data.get('moduleMetadata', {}).get('verbatimLearningGoals', [])
        return '\n'.join(f"- {goal}" for goal in goals)
    
    def get_deconstructed_goals(self) -> List[Dict]:
        """Get detailed deconstructed learning goals"""
        return self.data.get('deconstructedLearningGoals', [])
    
    def get_goals_by_id(self, goal_id: int) -> Dict:
        """Get specific goal by ID"""
        for goal in self.get_deconstructed_goals():
            if goal.get('goalId') == goal_id:
                return goal
        return None
    
    def get_all_goal_descriptions(self) -> List[str]:
        """Get all goal descriptions"""
        return [goal['goal'] for goal in self.get_deconstructed_goals()]
    
    def get_example_questions(self, goal_id: int = None) -> List[str]:
        """Get example questions for a specific goal or all goals"""
        if goal_id:
            goal = self.get_goals_by_id(goal_id)
            return goal.get('example_questions', []) if goal else []
        
        # Return all example questions
        all_questions = []
        for goal in self.get_deconstructed_goals():
            all_questions.extend(goal.get('example_questions', []))
        return all_questions
    
    def get_module_info(self) -> Dict:
        """Get basic module information"""
        return {
            "name": self.data.get('moduleName'),
            "number": self.data.get('moduleNumber'),
            "grade": self.data.get('gradeLevel'),
            "variant": self.data.get('pathVariant')
        }
    
    def get_vocabulary(self) -> List[str]:
        """Get key vocabulary"""
        return self.data.get('moduleMetadata', {}).get('keyVocabulary', [])
    
    def get_misconceptions(self) -> List[Dict]:
        """Get common misconceptions"""
        return self.data.get('moduleMetadata', {}).get('misconceptions', [])
    
    def get_standards(self) -> Dict:
        """Get curriculum standards"""
        return self.data.get('moduleMetadata', {}).get('standards', {})
    
    def format_for_pipeline(self) -> Dict:
        """Format data for pipeline input"""
        return {
            "module_info": self.get_module_info(),
            "learning_goals": self.get_learning_goals(),
            "detailed_goals": self.get_all_goal_descriptions(),
            "vocabulary": self.get_vocabulary(),
            "misconceptions": self.get_misconceptions(),
            "standards": self.get_standards()
        }
    
    def format_for_question_generation(self, goal_ids: List[int] = None) -> Dict:
        """Format specifically for question generation step"""
        if goal_ids:
            # Get specific goals
            goals = [self.get_goals_by_id(gid) for gid in goal_ids]
            goals = [g for g in goals if g]  # Filter None
        else:
            # Get all goals
            goals = self.get_deconstructed_goals()
        
        # Format learning goals
        learning_goals_text = '\n'.join(f"- {goal['goal']}" for goal in goals)
        
        # Include content categories for context
        categories_info = []
        for goal in goals:
            if 'contentCategories' in goal:
                for cat in goal['contentCategories']:
                    categories_info.append(
                        f"  {cat['categoryName']}: {', '.join(str(v) for v in cat['values'])}"
                    )
        
        context = f"""Module: {self.get_module_info()['name']} (Grade {self.get_module_info()['grade']})

Learning Goals:
{learning_goals_text}

Content Categories:
{chr(10).join(categories_info) if categories_info else 'N/A'}

Key Vocabulary: {', '.join(self.get_vocabulary())}
"""
        
        return {
            "learning_goals": learning_goals_text,
            "full_context": context,
            "module_name": self.get_module_info()['name'],
            "grade_level": self.get_module_info()['grade']
        }


# Example usage and testing
if __name__ == "__main__":
    print("ModuleInputParser loaded successfully!")
    print("\nExample usage:")
    print("  parser = ModuleInputParser('path/to/module.json')")
    print("  goals = parser.get_learning_goals()")
    print("  formatted = parser.format_for_question_generation()")
