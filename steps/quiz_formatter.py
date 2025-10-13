"""Step 3: Quiz Formatter - Formats questions and answers into various output formats"""
import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from core.json_utils import parse_json
from core.pipeline import Step

class QuizFormatter(Step):
    """Formats quiz content into different output formats"""
    
    def __init__(self, claude_client: ClaudeClient = None, format_type: str = "html"):
        super().__init__(name="Quiz Formatter", prompt_id="quiz_formatter")
        self.claude = claude_client
        self.format_type = format_type
    
    def execute(self, input_data, **kwargs):
        """Format quiz data"""
        print(f"  📄 Formatting as {self.format_type}...")
        
        format_type = kwargs.get('format_type', self.format_type)
        
        if format_type == "html":
            return self._format_html(input_data)
        elif format_type == "markdown":
            return self._format_markdown(input_data)
        elif format_type == "json":
            return input_data  # Already JSON
        else:
            raise ValueError(f"Unknown format: {format_type}")
    
    def _format_html(self, data):
        """Format as HTML"""
        html = ["<!DOCTYPE html>", "<html>", "<head>"]
        html.append("  <title>Educational Quiz</title>")
        html.append("  <style>")
        html.append("    body { font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; }")
        html.append("    .question { margin: 30px 0; padding: 20px; background: #f5f5f5; border-radius: 8px; }")
        html.append("    .answer { margin-top: 10px; color: #2e7d32; font-weight: bold; }")
        html.append("    .explanation { margin-top: 10px; color: #555; }")
        html.append("    .hints { margin-top: 10px; }")
        html.append("    .hint { color: #1976d2; margin-left: 20px; }")
        html.append("  </style>")
        html.append("</head>")
        html.append("<body>")
        html.append("  <h1>📚 Educational Quiz</h1>")
        
        for i, item in enumerate(data, 1):
            html.append(f'  <div class="question">')
            html.append(f'    <h3>Question {i}</h3>')
            html.append(f'    <p><strong>{item.get("question", "")}</strong></p>')
            
            if "answer" in item:
                html.append(f'    <div class="answer">Answer: {item["answer"]}</div>')
            
            if "explanation" in item:
                html.append(f'    <div class="explanation">Explanation: {item["explanation"]}</div>')
            
            if "hints" in item and item["hints"]:
                html.append(f'    <div class="hints">')
                html.append(f'      <strong>Hints:</strong>')
                for hint in item["hints"]:
                    html.append(f'      <div class="hint">💡 {hint}</div>')
                html.append(f'    </div>')
            
            html.append(f'  </div>')
        
        html.append("</body>")
        html.append("</html>")
        
        print(f"  ✓ Generated HTML ({len(html)} lines)")
        return "\n".join(html)
    
    def _format_markdown(self, data):
        """Format as Markdown"""
        md = ["# 📚 Educational Quiz\n"]
        
        for i, item in enumerate(data, 1):
            md.append(f"## Question {i}\n")
            md.append(f"**{item.get('question', '')}**\n")
            
            if "answer" in item:
                md.append(f"### ✓ Answer\n")
                md.append(f"{item['answer']}\n")
            
            if "explanation" in item:
                md.append(f"### 📖 Explanation\n")
                md.append(f"{item['explanation']}\n")
            
            if "hints" in item and item["hints"]:
                md.append(f"### 💡 Hints\n")
                for hint in item["hints"]:
                    md.append(f"- {hint}")
                md.append("")
            
            md.append("---\n")
        
        print(f"  ✓ Generated Markdown")
        return "\n".join(md)


# Test
if __name__ == "__main__":
    print("Testing QuizFormatter...\n")
    
    formatter = QuizFormatter(format_type="html")
    
    test_data = [
        {
            "question": "What is 1/2 + 1/4?",
            "answer": "3/4",
            "explanation": "Convert to common denominator and add",
            "hints": ["Find common denominator", "Convert fractions"]
        }
    ]
    
    html_output = formatter.execute(test_data)
    print("\nHTML Output:")
    print(html_output[:200] + "...")
