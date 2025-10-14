"""Pipeline system for chaining multiple steps together"""
import json
from pathlib import Path
from typing import Any, Dict, List, Callable
from datetime import datetime

class Step:
    """Base class for pipeline steps"""
    
    def __init__(self, name: str, prompt_id: str = None):
        self.name = name
        self.prompt_id = prompt_id
        self.input_data = None
        self.output_data = None
        
    def execute(self, input_data: Any, **kwargs) -> Any:
        """Execute the step - override in subclasses"""
        raise NotImplementedError("Subclasses must implement execute()")
    
    def get_result(self) -> Dict:
        """Get step execution result"""
        return {
            "name": self.name,
            "input": self.input_data,
            "output": self.output_data
        }


class Pipeline:
    """Orchestrates execution of multiple steps"""
    
    def __init__(self, name: str, save_intermediate=False, output_dir="outputs"):
        self.name = name
        self.steps: List[Step] = []
        self.results = []
        self.save_intermediate = save_intermediate
        self.output_dir = Path(output_dir)
        self.run_folder = None  # Will be set when pipeline starts
        
    def add_step(self, step: Step) -> 'Pipeline':
        """Add a step to the pipeline (chainable)"""
        self.steps.append(step)
        return self
    
    def execute(self, initial_input: Any, **global_kwargs) -> List[Dict]:
        """Execute all steps in sequence"""
        current_data = initial_input
        self.results = []
        
        # Override with kwargs if provided
        save_intermediate = global_kwargs.pop('save_intermediate', self.save_intermediate)
        output_dir = Path(global_kwargs.pop('output_dir', self.output_dir))
        
        # Create date-based folder for this run
        date_folder = datetime.now().strftime("%Y-%m-%d")
        self.run_folder = output_dir / date_folder
        self.run_folder.mkdir(parents=True, exist_ok=True)
        
        print(f"🔄 Starting pipeline: {self.name}")
        print(f"   Steps: {len(self.steps)}")
        print(f"   Output folder: {self.run_folder}\n")
        
        for i, step in enumerate(self.steps, 1):
            print(f"▶ Step {i}/{len(self.steps)}: {step.name}")
            
            try:
                # Execute step - pass run_folder in kwargs
                step.input_data = current_data
                step_kwargs = {**global_kwargs, 'run_folder': self.run_folder}
                current_data = step.execute(current_data, **step_kwargs)
                step.output_data = current_data
                
                # Store result
                self.results.append(step.get_result())
                
                # Save intermediate output if enabled
                if save_intermediate:
                    self._save_step_output(step, current_data, self.run_folder)
                
                print(f"  ✓ Completed\n")
                
            except Exception as e:
                print(f"  ✗ Error: {e}\n")
                raise
        
        print(f"✓ Pipeline '{self.name}' completed successfully!\n")
        return self.results
    
    def _save_step_output(self, step: Step, data: Any, output_dir: Path):
        """Save individual step output to JSON"""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%H%M%S")  # Just time, since date is in folder name
        # Convert step name to filename (e.g., "Question Generator" -> "question_generator")
        step_filename = step.name.lower().replace(' ', '_').replace('-', '_')
        filename = output_dir / f"{step_filename}_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"  💾 Saved: {filename}")
    
    def save_results(self, output_dir: str = "output/pipelines"):
        """Save pipeline results to file"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = output_path / f"{self.name}_{timestamp}.json"
        
        pipeline_output = {
            "pipeline_name": self.name,
            "timestamp": timestamp,
            "total_steps": len(self.steps),
            "results": self.results
        }
        
        with open(filename, 'w') as f:
            json.dump(pipeline_output, f, indent=2)
        
        print(f"💾 Results saved to: {filename}")
        return str(filename)
    
    def get_final_output(self) -> Any:
        """Get the output of the last step"""
        if self.results:
            return self.results[-1]['output']
        return None


# Example usage
if __name__ == "__main__":
    print("Pipeline system loaded successfully!")
