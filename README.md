# Script Generator

An AI-powered prompt engineering and testing system for educational content generation using Claude API.

### 📝 Prompt Editor
- Create and manage reusable prompt templates
- Visual editing interface with variable detection
- Persistent storage of prompts

### 🧪 Test Prompt
- Test prompts with Claude API in real-time
- Preview prompts before execution
- View formatted JSON responses
- Track token usage
- Auto-save test results

### 📊 History
- View all past test runs
- See inputs and outputs side-by-side
- Manage saved results

### 🔧 Question Generator Workflow
- Programmatic question generation from learning goals
- JSON-based output
- Integration with dashboard prompts
- File I/O utilities included

### 🔗 Multi-Step Pipelines
- Chain multiple steps together (Question → Answer → Format)
- Reusable step components
- Built-in steps: QuestionGenerator, AnswerGenerator, QuizFormatter
- Create custom steps easily
- Dashboard-managed prompts for all steps
- See `docs/SCALING_GUIDE.md` for details

## Quick Start

### Prerequisites
- Python 3.8+
- Anthropic API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/script_generator.git
cd script_generator
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install anthropic python-dotenv streamlit
```

4. Create `.env` file with your API key:
```bash
ANTHROPIC_API_KEY=your-api-key-here
```

### Running the Dashboard

```bash
# Windows
run_dashboard.bat

# Linux/Mac/Git Bash
./run_dashboard.sh

# Or manually
streamlit run dashboard/app.py
```

The dashboard will open at `http://localhost:8501`

### Running Tests

```bash
# Test API connection
python test_api.py

# Run end-to-end workflow test
python tests/test_step1_e2e.py
```

## Project Structure

```
script_generator/
├── core/                      # Core utilities
│   ├── claude_client.py      # Claude API wrapper
│   ├── json_utils.py         # JSON parsing utilities
│   ├── file_utils.py         # File I/O utilities
│   └── prompts.py            # Prompt templates
├── dashboard/                 # Streamlit dashboard
│   ├── app.py                # Main dashboard app
│   └── README.md             # Dashboard documentation
├── steps/                     # Workflow steps
│   └── question_generator.py # Question generation logic
├── tests/                     # Test files
│   └── test_step1_e2e.py     # End-to-end test
├── prompts/                   # Saved prompts
│   └── saved_prompts.json    # Prompt storage
├── output/                    # Generated outputs (gitignored)
├── .env                       # API keys (gitignored)
├── .gitignore
└── README.md
```

## Usage

### 1. Edit Prompts in Dashboard
- Navigate to "Prompt Editor"
- Select or create a prompt
- Use `{variable_name}` syntax for dynamic values
- Save changes

### 2. Test Prompts
- Go to "Test Prompt"
- Select a prompt and fill in variables
- Click "Run Test with Claude"
- View results and token usage

### 3. Use in Code
```python
from core.claude_client import ClaudeClient
from steps.question_generator import QuestionGenerator

client = ClaudeClient()
generator = QuestionGenerator(client)

questions = generator.generate(
    learning_goals="Students can identify fractions",
    num_questions=5
)
```

The `QuestionGenerator` automatically loads prompts from the dashboard's `saved_prompts.json` file.

## Configuration

All prompts are stored in `prompts/saved_prompts.json` and can be edited either:
- Through the dashboard UI
- Directly in the JSON file

## API Key Security

⚠️ **Important**: Never commit your `.env` file or API keys to version control!

The `.gitignore` is configured to exclude:
- `.env` files
- Output files
- Virtual environment
- Cache files

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - feel free to use this project for your own purposes.

## Acknowledgments

- Built with [Anthropic Claude API](https://www.anthropic.com/)
- Dashboard powered by [Streamlit](https://streamlit.io/)

## Support

For issues or questions, please open an issue on GitHub.
