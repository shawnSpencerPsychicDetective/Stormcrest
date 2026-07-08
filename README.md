# Stormcrest

Stormcrest is a lightweight agentic command-line AI assistant that combines a language model with local tools, web search, filesystem access, and shell execution.

Built using LangGraph, Stormcrest allows an LLM to interact with your local environment through a simple tool-usage protocol without requiring native function-calling support.

---

## Features

### Local File Management

* View current working directory
* List files and folders
* Change directories
* Create directories
* Read files
* Write files

Supported file formats for reading:

* `.txt`
* `.md`
* `.pdf`
* `.docx`
* `.odt`

---

### Shell Access

Execute shell commands directly within the current working directory.

Examples:

```text
bash dir
bash git status
bash python main.py
```

---

### Web Capabilities

#### Search

Search the web using DuckDuckGo:

```text
Search for LangGraph tutorials
```

Returns the top 5 URLs.

#### Fetch

Fetch and read webpage contents:

```text
Read https://langchain-ai.github.io/langgraph/
```

Stormcrest uses Playwright to render pages and extract visible content before compressing it for LLM consumption.

---

### Context Compression

Large documents, webpages, and conversation histories are automatically compressed to fit within model context limits while preserving as much information as possible.

---

### Agentic Tool Usage

Unlike traditional function-calling systems, Stormcrest teaches the model how to invoke tools through prompting.

Example:

```text
Tool Name: read
Arguments: notes.txt
```

The system:

1. Detects the requested tool
2. Executes it
3. Returns the result
4. Continues the conversation

This allows Stormcrest to work with models that do not support native tool calling.

---

## Architecture

```text
User
 │
 ▼
Prompt Node
 │
 ▼
LLM Node
 │
 ▼
Tool Router
 │
 ├── Execute Tool
 │       │
 │       ▼
 │    Tool Output
 │       │
 └───────┘
 │
 ▼
LLM Node
 │
 ▼
User
```

The system is implemented as a LangGraph workflow:

```text
prompt
  ↓
llm
  ↓
smart_node
  ├─→ llm
  ├─→ prompt
  └─→ exit
```

---

## Available Tools

| Tool               | Description                        |
| ------------------ | ---------------------------------- |
| `get_cwd`          | Return current working directory   |
| `list`             | List files and folders             |
| `change_directory` | Move into a directory or to parent |
| `make_directory`   | Create a new directory             |
| `read`             | Read supported document formats    |
| `write`            | Write text files                   |
| `bash`             | Execute shell commands             |
| `web_search`       | Search the web                     |
| `fetch_url`        | Fetch webpage content              |
| `exit`             | End the session                    |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/shawnSpencerPsychicDetective/stormcrest.git
cd stormcrest
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -e .
```

Install Playwright browser:

```bash
playwright install chromium
```

---

## Environment Variables

Create a `.env` file:

```env
DEEPSEEK_API_KEY=your_api_key_here
```

Stormcrest currently uses:

* DeepSeek API
* Model: `deepseek-v4-flash`

---

## Running Stormcrest

After installation:

```bash
stormcrest
```

or:

```bash
python -m stormcrest
```

Stormcrest starts in the current directory and uses it as its working environment.

---

## Example Session

```text
>> What files are in this folder?

Tool Called: list

['README.md', 'notes.txt', 'src']

System: I found three items in the current directory:
- README.md
- notes.txt
- src
```

---

### Reading Files

```text
>> Read notes.txt
```

Stormcrest will automatically invoke:

```text
read notes.txt
```

and return the file contents.

---

### Searching the Web

```text
>> Search for LangGraph documentation
```

Stormcrest invokes:

```text
web_search LangGraph documentation
```

and returns the top URLs.

---

### Creating Directories

```text
>> Create a folder called experiments
```

Stormcrest invokes:

```text
make_directory experiments
```

---

## Project Structure

```text
stormcrest/
├── __main__.py
├── chat.py
├── generate.py
├── smart_route.py
├── tool_schemas.py
├── use_tool.py
├── bash.py
├── read.py
├── write.py
├── fetch.py
├── search.py
├── make_directory.py
├── change_directory.py
├── compress.py
└── forge_prompt.py
```

---

## Design Philosophy

Stormcrest follows a simple philosophy:

> Give an LLM a small set of useful tools, teach it how to use them through prompting, and let the agent reason about when to call them.

The project intentionally avoids:

* Complex agent frameworks
* Native function-calling dependencies
* Heavy orchestration layers

while still providing:

* Tool use
* Web access
* File access
* Shell access
* Long-context management

in a lightweight, understandable codebase.

---

## Future Improvements

Potential additions include:

* Memory system
* Vector database integration
* Multi-agent workflows
* Code execution sandboxing
* Streaming responses
* Tool permission controls
* Cross-platform path handling
* Native tool-calling support
* RAG integration

---

## License

MIT License
