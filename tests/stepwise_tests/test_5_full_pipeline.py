"""
Full Pipeline Test - Process questions through all stages with parallel execution
Tests: Question → Interaction Designer → Remediation Generator → Godot Formatter
"""

import asyncio
import json
import os
import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from core.claude_client import ClaudeClient
from core.prompt_builder import PromptBuilder


class FullPipelineTest:
    def __init__(self, max_concurrent=3, rate_limit_delay=1.0):
        """
        Args:
            max_concurrent: Maximum number of parallel API calls
            rate_limit_delay: Delay in seconds between API calls (rate limiting)
        """
        self.max_concurrent = max_concurrent
        self.rate_limit_delay = rate_limit_delay
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.api_client = APIClient()
        self.interaction_designer = InteractionDesigner(self.api_client)
        self.remediation_generator = RemediationGenerator(self.api_client)
        self.godot_formatter = GodotFormatter(self.api_client)
        
    async def process_single_question(self, question, question_num, total_questions):
        """Process one question through all three stages"""
        async with self.semaphore:  # Limit concurrent API calls
            question_id = question.get('id', question_num)
            
            try:
                print(f"\n{'='*70}")
                print(f"[{question_num}/{total_questions}] Processing Question {question_id}")
                print(f"{'='*70}")
                
                # Stage 1: Interaction Designer
                print(f"  Stage 1/3: Interaction Designer...")
                await asyncio.sleep(self.rate_limit_delay)  # Rate limiting
                
                interaction_result = await self.interaction_designer.process_single(question)
                
                if not interaction_result or 'sequences' not in interaction_result:
                    raise Exception("Interaction designer failed")
                
                sequence = interaction_result['sequences'][0]
                print(f"    ✓ Generated {len(sequence.get('steps', []))} steps")
                
                # Stage 2: Remediation Generator
                print(f"  Stage 2/3: Remediation Generator...")
                await asyncio.sleep(self.rate_limit_delay)  # Rate limiting
                
                remediation_result = await self.remediation_generator.process_single(sequence)
                
                if not remediation_result:
                    raise Exception("Remediation generator failed")
                
                error_paths = [k for k in remediation_result.get('student_attempts', {}).keys() 
                             if k.startswith('error_path')]
                print(f"    ✓ Generated {len(error_paths)} error path(s)")
                
                # Stage 3: Godot Formatter
                print(f"  Stage 3/3: Godot Formatter...")
                await asyncio.sleep(self.rate_limit_delay)  # Rate limiting
                
                godot_result = await self.godot_formatter.process_single(remediation_result)
                
                if not godot_result or '@type' not in godot_result:
                    raise Exception("Godot formatter failed")
                
                print(f"    ✓ Godot formatted")
                print(f"  ✅ Question {question_id} completed successfully")
                
                return {
                    'question_id': question_id,
                    'status': 'success',
                    'interaction': sequence,
                    'remediation': remediation_result,
                    'godot': godot_result
                }
                
            except Exception as e:
                print(f"  ❌ Question {question_id} failed: {str(e)}")
                return {
                    'question_id': question_id,
                    'status': 'failed',
                    'error': str(e)
                }
    
    async def process_batch(self, questions):
        """Process multiple questions in parallel"""
        total = len(questions)
        
        print(f"\n{'='*70}")
        print(f"FULL PIPELINE TEST")
        print(f"{'='*70}")
        print(f"Questions to process: {total}")
        print(f"Max concurrent API calls: {self.max_concurrent}")
        print(f"Rate limit delay: {self.rate_limit_delay}s between calls")
        print(f"Estimated time: ~{total * 3 * self.rate_limit_delay / self.max_concurrent:.0f}s")
        print(f"{'='*70}")
        
        # Process all questions in parallel (controlled by semaphore)
        tasks = [
            self.process_single_question(q, i+1, total) 
            for i, q in enumerate(questions)
        ]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        return results


def load_questions(file_path):
    """Load questions from JSON file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['questions']


def save_results(results, output_dir):
    """Save results to output directory"""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Separate successful and failed results
    successful = [r for r in results if isinstance(r, dict) and r.get('status') == 'success']
    failed = [r for r in results if isinstance(r, dict) and r.get('status') == 'failed']
    
    # Save successful results by stage
    if successful:
        # Interaction sequences
        interactions = {
            "sequences": [r['interaction'] for r in successful]
        }
        with open(output_dir / 'interactions.json', 'w', encoding='utf-8') as f:
            json.dump(interactions, f, indent=2, ensure_ascii=False)
        
        # Remediations
        remediations = {
            "sequences": [r['remediation'] for r in successful]
        }
        with open(output_dir / 'remediations.json', 'w', encoding='utf-8') as f:
            json.dump(remediations, f, indent=2, ensure_ascii=False)
        
        # Godot formatted
        godot = {
            "@type": "SequencePool",
            "sequences": [r['godot'] for r in successful]
        }
        with open(output_dir / 'godot_sequences.json', 'w', encoding='utf-8') as f:
            json.dump(godot, f, indent=2, ensure_ascii=False)
    
    # Save summary
    summary = {
        "total_questions": len(results),
        "successful": len(successful),
        "failed": len(failed),
        "success_rate": f"{len(successful)/len(results)*100:.1f}%",
        "failed_questions": [
            {
                "question_id": r['question_id'],
                "error": r.get('error', 'Unknown error')
            }
            for r in failed
        ] if failed else []
    }
    
    with open(output_dir / 'summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    return summary


async def main():
    # Get input file from command line or use default
    if len(sys.argv) > 1:
        input_file = Path(sys.argv[1])
    else:
        input_file = Path('outputs/test_questions_20251021_104426/questions.json')
    
    # Get batch size from command line or use default
    batch_size = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    
    # Get max concurrent from command line or use default
    max_concurrent = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    
    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)
    
    # Load questions
    print(f"Loading questions from: {input_file}")
    all_questions = load_questions(input_file)
    print(f"Loaded {len(all_questions)} questions")
    
    # Interactive mode: ask how many to process
    print(f"\nHow many questions to process? (1-{len(all_questions)}) or enter number:")
    try:
        user_input = input().strip()
        if user_input.lower() == 'all':
            num_questions = len(all_questions)
        else:
            num_questions = min(int(user_input), len(all_questions))
    except (ValueError, EOFError):
        num_questions = batch_size
        print(f"Using default batch size: {num_questions}")
    
    questions = all_questions[:num_questions]
    
    # Create output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(f'outputs/test_full_pipeline_{timestamp}')
    
    # Process questions
    tester = FullPipelineTest(max_concurrent=max_concurrent, rate_limit_delay=1.0)
    results = await tester.process_batch(questions)
    
    # Save results
    print(f"\n{'='*70}")
    print(f"SAVING RESULTS")
    print(f"{'='*70}")
    summary = save_results(results, output_dir)
    
    # Print summary
    print(f"\n{'='*70}")
    print(f"TEST SUMMARY")
    print(f"{'='*70}")
    print(f"Total questions: {summary['total_questions']}")
    print(f"✓ Successful: {summary['successful']}")
    print(f"✗ Failed: {summary['failed']}")
    print(f"Success rate: {summary['success_rate']}")
    
    if summary['failed_questions']:
        print(f"\nFailed questions:")
        for failed in summary['failed_questions']:
            print(f"  - Question {failed['question_id']}: {failed['error']}")
    
    print(f"\nOutput files:")
    print(f"  - {output_dir / 'interactions.json'}")
    print(f"  - {output_dir / 'remediations.json'}")
    print(f"  - {output_dir / 'godot_sequences.json'}")
    print(f"  - {output_dir / 'summary.json'}")
    print(f"{'='*70}")


if __name__ == '__main__':
    asyncio.run(main())
