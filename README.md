# 🎙️ JARVIS - Autonomous AI Voice Assistant

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![SpeechRecognition](https://img.shields.io/badge/Audio-SpeechRecognition-orange.svg)](https://pypi.org/project/SpeechRecognition/)
[![Groq](https://img.shields.io/badge/AI-Groq%20LPU%20(Llama%203)-red.svg)](https://groq.com/)

> **JARVIS** is an autonomous desktop voice assistant built in Python. Powered by **Groq's ultra-low latency LPU engine (Llama 3)**, it delivers near-instantaneous spoken answers, ambient listening, dual-engine speech synthesis (Google Cloud TTS with offline `pyttsx3` fallback), web navigation, news streaming, and curated music playback.

---

## ⚡ Why Groq?

Traditional cloud LLMs often introduce 2–4 seconds of latency, which interrupts natural voice conversation flow. By powering Jarvis with **Groq LPU (Language Processing Unit)**:
- **Instant Response Times:** Groq delivers inference speeds over 500–800 tokens/sec.
- **State-of-the-Art Intelligence:** Defaulted to `llama-3.3-70b-versatile` (or `llama-3.1-8b-instant`).
- **Free API Tier:** Generous free access for developers via [Groq Console](https://console.groq.com/keys).

---

## 🚀 Key Features

- **Groq LPU Conversational Brain:** Sub-second conversational responses using Llama 3 with zero conversational lag.
- **Dual-Engine Speech Synthesis (TTS):** Uses Google Cloud TTS (`gTTS`) via `pygame` for smooth, natural speech, with automatic zero-delay fallback to offline `pyttsx3` if offline or on network error.
- **Ambient Noise Calibration:** Automatically adjusts microphone sensitivity to room background noise on startup.
- **Natural Wake-Word Detection:** Listens for `"Jarvis"` with support for single-breath commands (e.g., *"Jarvis open YouTube"* or *"Jarvis what's the time"*).
- **Curated & Global Music Player:** Plays from a curated YouTube playlist or dynamically searches and plays any track on YouTube if not in the local library.
- **Top News Briefing:** Fetches live top headlines in real-time via NewsAPI.
- **System & Utility Tools:** Tells real-time date, current time, programming jokes, and handles graceful voice shutdowns.

---

## 📁 Project Architecture

```
Mega Project1-JARVIS/
├── main.py              # Main voice assistant loop, STT, TTS, Groq integration, & command router
├── client.py            # Interactive dual-mode testing console (voice & text)
├── musicLibrary.py      # Curated playlist and case-insensitive song matcher
├── requirements.txt     # Python dependencies (groq, speechrecognition, pyttsx3, etc.)
├── .env.example         # Template for environment variables (GROQ_API_KEY, NEWS_API_KEY)
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
# Get your free API key at: https://console.groq.com/keys
GROQ_API_KEY=gsk_your_groq_api_key_here

# Optional: Groq Model (default: llama-3.3-70b-versatile or llama-3.1-8b-instant)
GROQ_MODEL=llama-3.3-70b-versatile

# Get your free key at: https://newsapi.org
NEWS_API_KEY=your_news_api_key_here
```
*(Note: Jarvis will still function for navigation, time, music, and jokes even without API keys!)*

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
| **Groq AI Q&A** | *"Explain black holes in two sentences"*, *"How does recursion work?"* | Fast response via Groq Llama 3 |
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
