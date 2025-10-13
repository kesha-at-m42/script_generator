"""Automated pipeline using module JSON - no user input required"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from core.pipeline import Pipeline
from core.input_parsers import ModuleInputParser
from core.file_utils import save_to_file, save_json
from steps.question_generator import QuestionGenerator
from steps.answer_generator import AnswerGenerator
from steps.quiz_formatter import QuizFormatter

def generate_module_quiz(
    module_json_path: str,
    num_questions: int = 5,
    goal_ids: list = None,
    output_format: str = "html"
):
    """
    Generate quiz from module JSON file
    
    Args:
        module_json_path: Path to module JSON file
        num_questions: Number of questions to generate
        goal_ids: List of goal IDs to target (None = all goals)
        output_format: Output format ("html" or "markdown")
    
    Returns:
        dict: Results including file paths and statistics
    """
    print(f"🚀 Starting automated quiz generation...")
    print(f"   Input: {module_json_path}")
    print(f"   Questions: {num_questions}")
    print(f"   Goal IDs: {goal_ids or 'All'}\n")
    
    # Parse module
    parser = ModuleInputParser(module_json_path)
    module_info = parser.get_module_info()
    
    # Format input
    pipeline_input = parser.format_for_question_generation(goal_ids)
    pipeline_input["num_questions"] = num_questions
    
    # Create pipeline
    client = ClaudeClient()
    pipeline = Pipeline(f"module_{module_info['number']}_automated")
    
    pipeline.add_step(QuestionGenerator(client))
    pipeline.add_step(AnswerGenerator(client))
    pipeline.add_step(QuizFormatter(format_type=output_format))
    
    # Execute
    results = pipeline.execute(pipeline_input)
    
    # Save pipeline results
    pipeline_file = pipeline.save_results()
    
    # Save final output
    module_name_clean = module_info['name'].replace(' ', '_').lower()
    extension = "html" if output_format == "html" else "md"
    output_file = save_to_file(
        pipeline.get_final_output(),
        f"{module_name_clean}_quiz.{extension}",
        "output"
    )
    
    # Save metadata
    metadata = {
        "module_info": module_info,
        "generation_params": {
            "num_questions": num_questions,
            "goal_ids": goal_ids,
            "output_format": output_format
        },
        "files": {
            "quiz": str(output_file),
            "pipeline_results": str(pipeline_file)
        },
        "statistics": client.get_stats()
    }
    
    metadata_file = save_json(
        metadata,
        f"{module_name_clean}_metadata.json",
        "output"
    )
    
    print(f"\n✅ Quiz generation complete!")
    print(f"   Quiz: {output_file}")
    print(f"   Metadata: {metadata_file}")
    print(f"   Pipeline: {pipeline_file}")
    
    return metadata


# Example usage
if __name__ == "__main__":
    # Example 1: Generate quiz with all goals
    result1 = generate_module_quiz(
        "inputs/module_1_fractions.json",
        num_questions=6,
        goal_ids=None,  # All goals
        output_format="html"
    )
    
    print("\n" + "="*60)
    print(f"📊 Statistics:")
    print(f"   Total Tokens: {result1['statistics']['total_tokens']}")
    print(f"   Questions Generated: {result1['generation_params']['num_questions']}")
    print("="*60)
