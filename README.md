# 🧠 Natural Language Terminal Agent

This project is an AI-powered terminal assistant that converts plain English instructions into system commands using a local LLM via [Ollama](https://ollama.com). It supports multiple operating systems like Windows, Linux, and macOS.

---

## ✨ Features

- 🧠 Powered by `gemma3:1b` model via Ollama
- 🗣 Converts natural language to terminal commands
- ⚠️ Asks for confirmation before executing any command
- 💻 Works with Windows CMD, Linux shell, or macOS terminal
- 🔒 Runs completely offline

---

## 🧰 Tech Stack

- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.com)
- Python 3.10+

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Pull the Model (if not already)

```bash
ollama pull gemma3:1b
```

### 3. Start Ollama
Keep Ollama running in the background:
```bash
ollama run gemma3:1b
```
### 4. Run the Assistant

```bash
python main.py
```

### 🖥️ Demo
```bash
Choose your Operating System:
1. Windows
2. Linux
3. macOS
Enter option number: 1

📝 Enter instruction (or 'exit' to quit): create a folder called "sample" in desktop

💡 Suggested Command:
mkdir %USERPROFILE%\Desktop\sample

⚠️ Execute this command? (y/n): y
⏳ Running...
```

### 🛡️ Safety
- Commands are shown before execution.
- You must confirm each command (y) before it's run.

### 📁 Folder Structure
```bash
tui-agent/
│
├── main.py            # Main script
├── README.md          # Project documentation
└── requirements.txt   # Optional (for pip freeze)
```