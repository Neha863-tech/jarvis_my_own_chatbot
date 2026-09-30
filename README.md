# 🎙️ JARVIS - Autonomous AI Voice Assistant

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![SpeechRecognition](https://img.shields.io/badge/Audio-SpeechRecognition-orange.svg)](https://pypi.org/project/SpeechRecognition/)
[![OpenAI](https://img.shields.io/badge/AI-OpenAI%20GPT-purple.svg)](https://platform.openai.com/)

> **JARVIS** is an autonomous desktop voice assistant built in Python. It features continuous ambient listening, dual-engine speech synthesis (Google TTS with offline `pyttsx3` fallback), web navigation, news streaming, curated music playback, and OpenAI GPT integration.

---

## 🚀 Key Features

- **Dual-Engine Speech Synthesis (TTS):** Uses Google Cloud TTS (`gTTS`) via `pygame` for smooth, natural speech, with automatic zero-delay fallback to offline `pyttsx3` if offline or on network error.
- **Ambient Noise Calibration:** Automatically adjusts microphone sensitivity to room background noise on startup.
- **Natural Wake-Word Detection:** Listens for `"Jarvis"` with support for single-breath commands (e.g., *"Jarvis open YouTube"* or *"Jarvis what's the time"*).
- **Curated & Global Music Player:** Plays from a curated YouTube playlist or dynamically searches and plays any track on YouTube if not in the local library.
- **Top News Briefing:** Fetches live top headlines in real-time via NewsAPI.
- **OpenAI GPT Conversational Brain:** Seamlessly answers open-ended questions using `gpt-3.5-turbo` with prompt engineering tuned for natural verbal responses.
- **System & Utility Tools:** Tells real-time date, current time, programming jokes, and handles graceful voice shutdowns.

---

## 📁 Project Architecture

```
Mega Project1-JARVIS/
├── main.py              # Main voice assistant loop, STT, TTS, & command router
├── client.py            # Interactive dual-mode testing console (voice & text)
├── musicLibrary.py      # Curated playlist and case-insensitive song matcher
├── requirements.txt     # Python dependencies
├── .env.example         # Template for environment variables
├── .gitignore           # Git ignore file for virtual envs, temp audio, & secrets
└── README.md            # Project documentation
```

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Neha863-tech/jarvis_my_own_chatbot.git
cd jarvis_my_own_chatbot
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

> **Note for PyAudio on Windows:** If `pip install pyaudio` fails, run `pip install pipwin` followed by `pipwin install pyaudio`.

### 4. Configure Environment Variables
Copy the example environment file:
```bash
cp .env.example .env
```
Open `.env` and insert your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
NEWS_API_KEY=your_news_api_key_here
```
*(Note: Jarvis will still function for all navigation, time, music, and jokes even without API keys!)*

---

## 🗣️ Supported Voice Commands

| Category | Example Command | Description |
| :--- | :--- | :--- |
| **Wake Word** | *"Jarvis"*, *"Hey Jarvis"* | Wakes assistant; responds with *"Yes Madam?"* |
| **Web Navigation** | *"Open Google"*, *"Open YouTube"*, *"Open GitHub"*, *"Open LinkedIn"* | Launches target site in default browser |
| **Google Search** | *"Search for quantum computing"*, *"Google python tutorials"* | Searches Google directly for query |
| **Music Playback** | *"Play lofi"*, *"Play skyfall"*, *"Play Believer"* | Plays curated link or searches YouTube |
| **News** | *"News"*, *"Tell me today's headlines"* | Reads the top 5 national headlines |
| **Date & Time** | *"What is the time?"*, *"What's the date today?"* | Announces current time and date |
| **Humor** | *"Tell me a joke"* | Delivers a clean tech/programming joke |
| **Conversational** | *"How are you?"*, *"Who are you?"*, *"What can you do?"* | Responds with identity & capabilities |
| **AI Q&A** | *"Explain black holes in two sentences"*, *"How does recursion work?"* | Answers via OpenAI GPT |
| **Exit** | *"Exit"*, *"Quit"*, *"Stop"*, *"Goodbye"* | Cleans up audio and shuts down cleanly |

---

## 🧪 Testing Console

You can also run the interactive test console to test commands without needing continuous microphone speech:

```bash
python client.py
```

---

## 🛡️ License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👩‍💻 Author

**Neha Kumari**  
- GitHub: [@Neha863-tech](https://github.com/Neha863-tech)
