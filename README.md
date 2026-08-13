# 🤖 AI Assistant

A Python-based desktop AI Assistant built with **CustomTkinter**. The project combines a modern graphical user interface with useful automation features such as website launching, calculations, password generation, jokes, motivational quotes, Google search, and chat-history management.

> 🚧 **Project Status:** Actively being developed. Voice input, text-to-speech, external APIs, and advanced AI capabilities are planned enhancements.

---

## 📸 Project Preview

*Add screenshots of your application here.*

```text
┌──────────────────────────────────────────────────────────────┐
│  AI Assistant                                                │
├──────────────┬───────────────────────────────────────────────┤
│              │                                               │
│ AI Assistant │        Chat / Conversation Area              │
│              │                                               │
│ 💾 Save Chat │                                               │
│              │                                               │
│ 🗑 Clear Chat│                                               │
│              │                                               │
│              ├───────────────────────────────────────────────┤
│              │ Type your message...              [ Send ]   │
└──────────────┴───────────────────────────────────────────────┘
```

---

## ✨ Features

### 💬 Chat Interface

* Interactive desktop chat interface
* User and AI messages displayed separately
* Press **Enter** to send messages
* Automatically scrolls to the latest message
* Dark-mode interface

### 🌐 Web Automation

The assistant can open commonly used websites directly from commands:

* YouTube
* Google
* GitHub
* LinkedIn
* Gmail

### 🔎 Google Search

Search the web directly from the assistant.

Example:

```text
search Python programming
```

The assistant opens Google with the requested search.

### 🧮 Calculator

Perform basic calculations directly through the assistant.

Example:

```text
calculate 25*4
```

Output:

```text
AI : Answer = 100
```

### 🔐 Password Generator

Generate random 12-character passwords containing:

* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Example:

```text
password
```

### 😂 Joke Generator

The assistant can randomly select a joke from its collection.

```text
joke
```

### 💡 Motivational Quotes

Ask for motivation or a quote:

```text
motivate
```

or:

```text
quote
```

### 💾 Chat History

The **Save Chat** button saves the current conversation to:

```text
history.txt
```

### 🗑 Clear Chat

The **Clear Chat** button removes the current conversation and starts a fresh session.

### 🆘 Help System

Use:

```text
help
```

to display the available commands.

---

## 🛠️ Technologies Used

| Technology    | Purpose                            |
| ------------- | ---------------------------------- |
| Python        | Core programming language          |
| CustomTkinter | Modern graphical interface         |
| Tkinter       | GUI utilities                      |
| datetime      | Date and time functionality        |
| webbrowser    | Opening websites and searches      |
| random        | Random jokes, quotes and passwords |
| string        | Password character generation      |
| File I/O      | Saving chat history                |

---

## 🧠 Python Concepts Used

This project demonstrates several important Python concepts:

* Functions
* Conditional statements
* `if / elif / else`
* Lists
* String manipulation
* Loops
* Exception handling
* File handling
* Randomization
* GUI programming
* Event handling
* Lambda functions
* Modules and imports
* Global constants
* Code organization

---

## 📂 Project Structure

```text
AI-Assistant/
│
├── AI_Assistance.py
├── history.txt
├── README.md
└── screenshots/
    └── assistant.png
```

> `history.txt` is generated automatically when chat history is saved.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Assistant.git
```

Move into the project:

```bash
cd AI-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows PowerShell

```powershell
.\venv\Scripts\activate
```

#### Windows Command Prompt

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install customtkinter
```

### 5. Run the application

```bash
python AI_Assistance.py
```

---

## 🎮 Available Commands

| Command          | Function            |
| ---------------- | ------------------- |
| `hello`          | Greeting            |
| `time`           | Current time        |
| `date`           | Current date        |
| `youtube`        | Open YouTube        |
| `google`         | Open Google         |
| `github`         | Open GitHub         |
| `linkedin`       | Open LinkedIn       |
| `gmail`          | Open Gmail          |
| `joke`           | Random joke         |
| `quote`          | Motivational quote  |
| `motivate`       | Motivational quote  |
| `password`       | Generate password   |
| `calculate 25*4` | Perform calculation |
| `search Python`  | Search Google       |
| `what is AI`     | Search Google       |
| `help`           | Display commands    |

---

## 🏗️ Current Architecture

The project is currently organized into several logical sections:

```text
AI Assistant
│
├── Settings
│
├── Data
│   ├── Jokes
│   ├── Quotes
│   └── Unknown Responses
│
├── Helper Functions
│   ├── add_message()
│   ├── save_history()
│   └── clear_chat()
│
├── Command Processing
│   └── send()
│
├── GUI
│   ├── Sidebar
│   ├── Chatbox
│   └── Input Area
│
└── Main Loop
```

---

## 🚀 Future Improvements

The project is being developed gradually. Planned features include:

### 🎤 Voice Assistant

* Speech recognition
* Microphone input
* Voice commands
* Indian English speech recognition

### 🔊 Text-to-Speech

The assistant will be able to speak its responses instead of only displaying text.

### 🤖 AI Integration

Connect the assistant to an actual AI/LLM so it can answer general questions instead of relying entirely on predefined commands.

Potential technologies:

* OpenAI API
* Ollama
* Local LLMs
* AI APIs

### 🌦️ Weather

Add live weather information using a weather API.

Example:

```text
weather in Jalandhar
```

### 📚 Wikipedia

Search Wikipedia and return short summaries directly in the application.

### 📰 News

Add a live news feature using a news API.

### 📝 Notes

Allow users to create, save, edit and delete notes.

### ✅ To-Do List

Add task management functionality:

```text
Add task
View tasks
Complete task
Delete task
```

### 💾 Improved Data Storage

Move from a simple text file to structured storage such as:

```text
JSON
SQLite
PostgreSQL
```

### 🎨 UI Improvements

Planned interface improvements:

* Better icons
* Theme switching
* Light/Dark mode
* Chat bubbles
* Loading animations
* Settings panel
* Responsive layout

---

## 🔒 Security Note

The current calculator uses Python's `eval()` for simple expressions.

This is acceptable for local experimentation, but it should **not be used with unrestricted user input in a production application**.

A future version will replace it with a safer mathematical expression parser.

---

## 📚 Learning Objectives

This project was created as a practical way to improve Python programming and software development skills.

Through this project, the following concepts are being practiced:

```text
Python
   ↓
Functions
   ↓
GUI Programming
   ↓
Event Handling
   ↓
File Handling
   ↓
APIs
   ↓
Automation
   ↓
Speech Recognition
   ↓
AI / Machine Learning
```

The long-term goal is to evolve the application from a rule-based Python assistant into an **AI-powered desktop assistant**.

---

## 📈 Development Roadmap

```text
[✓] Basic GUI
[✓] Chat Interface
[✓] Website Launcher
[✓] Calculator
[✓] Password Generator
[✓] Random Jokes
[✓] Motivational Quotes
[✓] Google Search
[✓] Save Chat History
[✓] Clear Chat

[ ] Voice Input
[ ] Text-to-Speech
[ ] Weather API
[ ] Wikipedia API
[ ] News API
[ ] Notes System
[ ] To-Do System
[ ] Database Integration
[ ] AI / LLM Integration
[ ] Final UI Polish
```

---

## 🎯 Future Vision

The final goal of this project is to create a desktop assistant capable of:

```text
             ┌───────────────────┐
             │   AI ASSISTANT    │
             └─────────┬─────────┘
                       │
       ┌───────────────┼────────────────┐
       │               │                │
       ▼               ▼                ▼
   Voice Input      AI / LLM         Automation
       │               │                │
       ▼               ▼                ▼
  Speech → Text     Answers          Websites
       │            Reasoning        Applications
       │            Summaries        Tasks
       └───────────────┼────────────────┘
                       │
                       ▼
                 Desktop GUI
```

---

## 👨‍💻 Author

**Krishna Sharma**

B.Tech CSE (AI/ML) Student

Interested in:

* Artificial Intelligence
* Machine Learning
* Data Structures & Algorithms
* Python
* C++
* Full-Stack Development
* Software Engineering

---

## ⭐ Contributing

This is primarily a learning project, but suggestions and improvements are welcome.

If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.

---

## 📄 License

This project is intended for educational and portfolio purposes.
