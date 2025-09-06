# 🧭 OpenAI Agents Trip Planner Bot

An intelligent, multi-agent conversational assistant for planning trips, built using OpenAI Agents SDK. This bot guides users through trip planning, recommends destinations, provides detailed travel info, and even generates location maps—all in a friendly, emoji-enhanced chat.

---

## 📋 Project Summary

| Feature                      | Description                                                                                 |
|------------------------------|---------------------------------------------------------------------------------------------|
| Multi-Agent Architecture     | Triage, Trip Planner, and Assistant agents coordinate to deliver expert travel planning.    |
| Tool Integration             | Uses custom tools for info gathering, location details, and map screenshot generation.      |
| Contextual Conversation      | Maintains and utilizes conversation history for coherent, context-aware responses.          |
| Asynchronous Processing      | Fast, non-blocking user interactions using Python's `asyncio`.                             |
| Emoji-Enhanced Responses     | Engaging, friendly replies with relevant emojis.                                            |
| Conversation Logging         | Automatically saves each bot response to a uniquely named text file for record-keeping.     |
| Easy Extensibility           | Modular agent and tool design for adding new features or agents.                           |

---

## 🚀 Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/yourusername/openai-agents-trip-planner.git
cd openai-agents-trip-planner
python -m venv .venv
.venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 2. Configure API Keys

Create a `.env` file in the root directory and add your keys:
```
OPENAI_API_KEY=your_openai_key
SERPER_API_KEY=your_serper_key
```

### 3. Run the Bot

```bash
python main.py
```

---

## 🗂️ Project Structure

```
openai-agents-trip-planner/
├── Agents/
│   └── Agents.py
├── History/
│   └── History.py
├── LLm_Setup/
│   └── llm.py
├── Tools/
│   └── Tools.py
├── conversation_logs/
├── main.py
├── .env
├── .gitignore
└── README.md
```

---

## 🤖 How It Works

- **Triage Agent:** First contact; routes queries to the right specialist agent.
- **Trip Planner Agent:** Gathers user preferences, suggests destinations, and calls tools for info and maps.
- **Assistant Agent:** Provides deep insights about the recommended destination.
- **Tools:** Custom Python functions for info gathering, location details, and map screenshots.
- **History:** Tracks conversation for context-aware responses.
- **Logging:** Each bot response is saved to a randomly named `.txt` file for easy review.

---

## 💬 Example Conversation

```
Trip Planner Bot: Hello! I can help you plan your trip. Type 'exit' to end or 'clear' to start fresh.

Enter Query: I want to visit Tokyo in spring.
[Bot suggests destinations, provides info, and saves a map screenshot]

Enter Query: What food should I try there?
[Assistant Agent lists local cuisine with emojis]

Enter Query: exit
Trip Planner Bot: Goodbye!
```

---

## 🛠️ Extending & Customizing

- Add new agents in `Agents/Agents.py`
- Create new tools in `Tools/Tools.py`
- Modify conversation logic in `main.py`
- Customize agent instructions for different domains

---

## 📝 License

MIT License

---

## 👤 Author

- **M. Younus**  
  [GitHub Profile](https://github.com/yourusername)

---

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/)
- [Agents SDK](https://github.com/openai/openai-agents)
- All contributors and users

---

## 📊 Feature Summary Table

| Agent/Tool         | Role/Functionality                                                                 |
|--------------------|------------------------------------------------------------------------------------|
| Triage Agent       | Routes queries, ensures quality, manages agent handoff                             |
| Trip Planner Agent | Gathers preferences, suggests destinations, calls info/map tools                   |
| Assistant Agent    | Provides detailed info about chosen destination                                    |
| get_info Tool      | Collects trip details from user                                                    |
| get_location_details Tool | Searches for destinations and gathers info                                  |
| take_map_screenshot Tool  | Generates and saves map screenshot for selected location                    |
| ConversationHistory| Tracks and manages conversation context                                            |
| Logging Function   | Saves each bot response to a uniquely named `.txt` file                            |

---

Happy trip planning! 🌏✈️🗺️
