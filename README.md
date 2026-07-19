# Gitship 🐳

**Turn any GitHub repository into a production-ready Docker container with AI-powered Dockerfile generation.**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-00a393.svg)](https://fastapi.tiangolo.com/)

Gitship is an AI-powered web application that automatically generates production-ready Dockerfiles by analyzing GitHub repositories. Paste in a GitHub URL and get a tailored Dockerfile back, complete with intelligent base image selection, dependency management, and Docker best practices.

> 🏆 Built for **[OpenAI Build Week](https://openai.devpost.com/)** — Developer Tools track.

## 🤖 How Codex & GPT-5.6 Were Used

- **Codex** — [describe here: e.g. which parts of Gitship's codebase Codex generated or accelerated, such as the FastAPI backend scaffolding, the WebSocket streaming logic, or the Dockerfile-generation prompt engineering]
- **GPT-5.6** — [describe here: e.g. how GPT-5.6 is used at runtime to analyze repository structure and generate the Dockerfile itself]
- **Key decisions made with Codex's help** — [describe here: e.g. choosing the multi-stage build strategy, structuring the `tools/` module, or debugging the gitingest integration]
- **/feedback Codex Session ID:** `[paste your session ID here]`

## ✨ Features

- **🤖 AI-Powered Analysis** — Uses Groq's Llama models to analyze repository structure and generate intelligent Dockerfiles
- **⚡ Real-time Streaming** — Watch the AI generate your Dockerfile live via WebSocket streaming
- **🎯 Smart Detection** — Automatically detects technology stacks (Python, Node.js, Java, Go, etc.)
- **🔧 Production-Ready Output** — Generates Dockerfiles following best practices: proper security, multi-stage builds, and optimization
- **📋 Custom Instructions** — Add your own requirements for specialized environments
- **📄 Docker Compose Support** — Automatically suggests a `docker-compose.yml` for multi-service applications
- **🎨 Modern UI** — Clean, responsive interface with Monaco editor for syntax highlighting
- **📱 Mobile Friendly** — Works seamlessly on desktop and mobile

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Git
- A Groq API key ([console.groq.com](https://console.groq.com/))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hasnainaliasghar/Gitship.git
   cd Gitship
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   # Create .env file
   echo "GROQ_API_KEY=your_groq_api_key_here" > .env
   echo "GROQ_MODEL=llama-3.1-70b-versatile" >> .env
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your browser:**
   Navigate to `http://localhost:8000`

## 🛠️ How It Works

1. **Repository Cloning** — Gitship clones the target GitHub repository locally using Git
2. **Code Analysis** — Uses [gitingest](https://github.com/cyclotruc/gitingest) to analyze repository structure and extract relevant context
3. **AI Generation** — Sends the analysis to Groq's API with specialized prompts for Dockerfile generation
4. **Smart Optimization** — The AI considers:
   - Technology stack detection
   - Dependency management
   - Security best practices
   - Multi-stage builds where beneficial
   - Port configuration
   - Environment variables
   - Health checks

## 📁 Project Structure

```
Gitship/
├── app.py                 # Main FastAPI application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── static/                # Static assets (icons, CSS)
├── templates/
│   └── index.jinja        # Main HTML template
└── tools/                 # Core functionality modules
    ├── __init__.py
    ├── create_container.py  # AI Dockerfile generation
    ├── git_operations.py    # GitHub repository cloning
    └── gitingest.py          # Repository analysis
```

## 🔧 Configuration

### Environment Variables

| Variable      | Description                          | Required |
|----------------|---------------------------------------|----------|
| `GROQ_API_KEY` | Your Groq API key                    | Yes      |
| `GROQ_MODEL`   | Groq model to use (e.g. `llama-3.1-70b-versatile`) | No |
| `PORT`         | Server port (default: `8000`)        | No       |
| `HOST`         | Server host (default: `0.0.0.0`)     | No       |

### Advanced Usage

You can also use the tools programmatically:

```python
from tools import clone_repo_tool, gitingest_tool, create_container_tool
import asyncio

async def generate_dockerfile(github_url):
    # Clone repository
    clone_result = await clone_repo_tool(github_url)

    # Analyze with gitingest
    analysis = await gitingest_tool(clone_result['local_path'])

    # Generate Dockerfile
    dockerfile = await create_container_tool(
        gitingest_summary=analysis['summary'],
        gitingest_tree=analysis['tree'],
        gitingest_content=analysis['content']
    )

    return dockerfile

# Usage
result = asyncio.run(generate_dockerfile("https://github.com/user/repo"))
print(result['dockerfile'])
```

## 🎨 Customization

Use the "Additional instructions" field to customize generation, for example:

- `"Use Alpine Linux for smaller image size"`
- `"Include Redis and PostgreSQL"`
- `"Optimize for production deployment"`
- `"Add development tools for debugging"`

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Groq](https://groq.com/)** for fast LLM inference
- **[gitingest](https://github.com/cyclotruc/gitingest)** for repository analysis capabilities
- **[FastAPI](https://fastapi.tiangolo.com/)** for the web framework
- **[Monaco Editor](https://microsoft.github.io/monaco-editor/)** for code syntax highlighting

## 🔗 Links

- **GitHub Repository:** [github.com/hasnainaliasghar/Gitship](https://github.com/hasnainaliasghar/Gitship)
- **Issues:** [Report bugs or request features](https://github.com/hasnainaliasghar/Gitship/issues)

---

*Turn any repository into a container in seconds.*
