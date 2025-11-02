# Perplexity MCP Server

A lightweight MCP (Model Context Protocol) server that integrates Perplexity AI with your development environment. Ask real-time questions and get AI-powered answers with live web search and citations.

## Features

- 🌐 **Real-time Web Search** - Get up-to-date information with citations
- 🤖 **Multiple Models** - Choose from 5 different Perplexity models
- 💬 **Easy Integration** - Works with Claude Code and other MCP clients
- ⚡ **Fast & Lightweight** - Minimal dependencies, quick setup
- 🔒 **Secure** - Your API key stays local

## Available Models

| Model | Use Case |
|-------|----------|
| **sonar** | Lightweight real-time search (default) |
| **sonar-pro** | Enhanced search with richer context |
| **sonar-reasoning** | Real-time reasoning with step-by-step analysis |
| **sonar-reasoning-pro** | Advanced reasoning with DeepSeek-R1 |
| **sonar-deep-research** | Long-form research and synthesis |

## Quick Start (One-Line Installation)

### Prerequisites
- Linux or macOS
- Python 3.8+
- `curl` (usually pre-installed)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/perplexity-mcp-server.git
cd perplexity-mcp-server
```

2. **Run the installation script**
```bash
chmod +x install.sh
./install.sh
```

3. **Enter your Perplexity API key when prompted**
   - Get your free API key at https://www.perplexity.ai/

That's it! ✅

## Manual Setup (If needed)

If the script doesn't work for you:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env and add your API key
nano .env
```

## Usage

### Start the Server

```bash
source venv/bin/activate
python server.py
```

### With Claude Code

Add to your Claude settings (typically `~/.claude/settings.json`):

```json
{
  "mcpServers": {
    "perplexity": {
      "command": "path/to/perplexity-mcp-server/venv/bin/python",
      "args": ["path/to/perplexity-mcp-server/server.py"],
      "env": {
        "PERPLEXITY_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

Then restart Claude and you'll have access to:
- `perplexity_ask` - Ask questions with configurable models and parameters
- `list_models` - See all available models

## Example Queries

### Basic Question
```
Ask Perplexity: "What are the latest developments in AI (2024)?"
```

### Advanced Reasoning
```
Ask with sonar-reasoning model: "Explain how transformers work in machine learning"
```

### Research
```
Ask with sonar-deep-research model: "Write a comprehensive summary of renewable energy trends"
```

## API Key Setup

1. Go to https://www.perplexity.ai/
2. Sign up or log in
3. Get your API key from the API settings
4. Run `./install.sh` or add it to `.env`:
   ```
   PERPLEXITY_API_KEY=your_key_here
   ```

## Troubleshooting

### "PERPLEXITY_API_KEY environment variable required"
- Make sure `.env` file exists and contains your API key
- Run: `cat .env | grep PERPLEXITY_API_KEY`

### "Curl failed" or "HTTP 401"
- Your API key is invalid or expired
- Get a new one from https://www.perplexity.ai/

### Python version issues
- Make sure you're using Python 3.8+
- Check with: `python3 --version`

### venv activation issues
On some Linux systems:
```bash
source venv/bin/activate
# or
. venv/bin/activate
```

## How It Works

The server uses:
- **FastMCP** - For the MCP protocol implementation
- **curl** - For direct HTTP requests to Perplexity API
- **python-dotenv** - For secure environment variable management

No heavy dependencies - just what you need!

## Contributing

Found a bug? Have a suggestion? Please open an issue on GitHub!

## License

MIT License - feel free to use and modify

## Questions?

Check the [Perplexity API docs](https://docs.perplexity.ai/) for more details on models and parameters.

---

**Made for developers. By developers.**
