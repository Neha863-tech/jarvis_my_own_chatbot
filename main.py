"""
JARVIS - Advanced Python Voice Assistant
Powered by Groq ultra-low latency LLM inference (Llama 3), dual-engine Speech Synthesis
(gTTS + pyttsx3 fallback), intelligent wake-word detection, and robust error handling.
"""

import os
import sys
import time
import random
import urllib.parse
import webbrowser
from datetime import datetime
import tempfile

import speech_recognition as sr
import pyttsx3
import requests
import pygame

# Load environment variables if python-dotenv is installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Import Groq client (primary) with OpenAI fallback compatibility
GROQ_AVAILABLE = False
OPENAI_AVAILABLE = False

try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    pass

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    pass

# Import local music library
import musicLibrary


# ==============================================================================
# Configuration & Initialization
# ==============================================================================

# API Keys from environment or fallback
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

# Initialize Speech Recognizer
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8

# Initialize offline pyttsx3 engine
engine = pyttsx3.init()
try:
    # Set speech rate and volume for clear, natural offline voice
    engine.setProperty('rate', 175)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[0].id)
except Exception as e:
    print(f"[Warning] Failed to configure pyttsx3 voices: {e}")

# Initialize pygame audio mixer once
try:
    pygame.mixer.init()
except Exception as e:
    print(f"[Warning] Pygame mixer init warning: {e}")


# ==============================================================================
# Speech Synthesis (TTS)
# ==============================================================================

def speak(text: str):
    """
    Speaks the provided text using Google TTS (gTTS) with pygame.
    Automatically falls back to offline pyttsx3 on network error or file lock.
    """
    if not text:
        return

    print(f"\n[JARVIS]: {text}")
    temp_path = None

    try:
        from gtts import gTTS
        tts = gTTS(text=text, lang='en', slow=False)
        
        # Use tempfile to prevent file locking issues on Windows
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as fp:
            temp_path = fp.name

        tts.save(temp_path)

        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()

        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            clock.tick(15)

        pygame.mixer.music.unload()
        time.sleep(0.08)  # Brief pause to release Windows file handle

    except Exception as e:
        print(f"[TTS Fallback to pyttsx3]: {e}")
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as pyttsx_err:
            print(f"[Offline TTS Error]: {pyttsx_err}")

    finally:
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except OSError:
                pass


# ==============================================================================
# AI Integration (Groq LPU Inference)
# ==============================================================================

def aiProcess(command: str) -> str:
    """
    Queries Groq's ultra-fast LPU engine (Llama 3) for conversational intelligence.
    Supports native groq SDK with OpenAI base_url fallback.
    """
    api_key = GROQ_API_KEY
    if not api_key or api_key.startswith("<") or "YOUR_GROQ" in api_key:
        return "Groq API key is not configured. Please set your GROQ_API_KEY in the .env file."

    system_prompt = (
        "You are Jarvis, a brilliant, courteous, and highly capable AI assistant. "
        "Provide concise, clear, and natural spoken answers. Avoid markdown formatting."
    )

    try:
        # Native Groq Client
        if GROQ_AVAILABLE:
            client = Groq(api_key=api_key)
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": command}
                ],
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()

        # Fallback via OpenAI client targeting Groq API endpoint
        elif OPENAI_AVAILABLE:
            client = OpenAI(
                base_url="https://api.groq.com/openai/v1",
                api_key=api_key
            )
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": command}
                ],
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()

        else:
            return "Neither groq nor openai library is installed. Please run pip install groq."

    except Exception as e:
        print(f"[Groq AI Error]: {e}")
        return "I encountered an issue connecting to the Groq AI engine. Please verify your internet connection and API key."


# ==============================================================================
# Command Processor
# ==============================================================================

def processCommand(c: str) -> bool:
    """
    Parses and executes user commands.
    Returns False if user requested to exit/quit, otherwise returns True.
    """
    cmd = c.lower().strip()
    print(f"[Command Received]: {cmd}")

    # 1. Exit / Termination Commands
    if any(k in cmd for k in ["stop", "exit", "quit", "goodbye", "bye jarvis", "shutdown"]):
        speak("Goodbye Madam. Have a wonderful day!")
        return False

    # 2. Date & Time Queries
    elif "time" in cmd and ("what" in cmd or "tell" in cmd or "current" in cmd or cmd == "time"):
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")

    elif "date" in cmd and ("what" in cmd or "tell" in cmd or "today" in cmd or cmd == "date"):
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {current_date}.")

    # 3. Web Navigation Commands
    elif "open google" in cmd:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in cmd:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in cmd:
        speak("Opening Facebook.")
        webbrowser.open("https://www.facebook.com")

    elif "open linkedin" in cmd:
        speak("Opening LinkedIn.")
        webbrowser.open("https://www.linkedin.com")

    elif "open github" in cmd:
        speak("Opening GitHub.")
        webbrowser.open("https://www.github.com")

    elif "open instagram" in cmd:
        speak("Opening Instagram.")
        webbrowser.open("https://www.instagram.com")

    # 4. Search Query on Google
    elif cmd.startswith("search for ") or cmd.startswith("search ") or cmd.startswith("google "):
        query = cmd.replace("search for", "").replace("search", "").replace("google", "").strip()
        if query:
            speak(f"Searching Google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={urllib.parse.quote(query)}")
        else:
            speak("What would you like me to search for?")

    # 5. Music Player
    elif cmd.startswith("play"):
        song = cmd.replace("play", "", 1).strip()
        if not song:
            speak("Please tell me which song you want to play.")
            return True

        link = musicLibrary.get_music_url(song)
        if link:
            speak(f"Playing {song} from your library.")
            webbrowser.open(link)
        else:
            # Fallback to direct YouTube search so any song plays
            speak(f"Playing {song} on YouTube.")
            search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(song)}"
            webbrowser.open(search_url)

    # 6. News Headlines
    elif "news" in cmd or "headline" in cmd:
        api_key = NEWS_API_KEY
        if not api_key or api_key.startswith("<") or "YOUR_NEWS" in api_key:
            speak("News API key is not configured. Please add your NEWS_API_KEY to the .env file.")
            return True

        try:
            url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
            response = requests.get(url, timeout=6)
            if response.status_code == 200:
                data = response.json()
                articles = data.get('articles', [])
                if articles:
                    speak("Here are today's top headlines.")
                    for idx, article in enumerate(articles[:5], 1):
                        title = article.get('title', '')
                        if title:
                            clean_title = title.split(' - ')[0]
                            speak(f"Headline {idx}: {clean_title}")
                else:
                    speak("No headlines found at the moment.")
            else:
                speak("I could not retrieve the news right now. Please verify your NewsAPI key.")
        except Exception as e:
            print(f"[News Error]: {e}")
            speak("An error occurred while fetching news.")

    # 7. Humor & Jokes
    elif "joke" in cmd:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the developer go broke? Because he used up all his cache.",
            "There are only 10 types of people in the world: those who understand binary, and those who don't.",
            "Why was the JavaScript developer sad? Because they didn't Node how to Express themselves!",
            "An SQL query walks into a bar, walks up to two tables and asks: Can I join you?"
        ]
        speak(random.choice(jokes))

    # 8. Conversational Greetings
    elif any(greeting in cmd for greeting in ["how are you", "who are you", "what can you do"]):
        if "how are you" in cmd:
            speak("I am operating at peak performance with Groq AI, Madam! How may I assist you?")
        elif "who are you" in cmd:
            speak("I am Jarvis, your autonomous personal voice assistant, powered by Groq and Python.")
        elif "what can you do" in cmd:
            speak("I can play music, deliver top news headlines, open websites, search Google, tell jokes, and answer questions via Groq Llama 3.")

    # 9. Fallback to Groq AI Process
    else:
        output = aiProcess(cmd)
        speak(output)

    return True


# ==============================================================================
# Main Listener Loop
# ==============================================================================

def main():
    print("=" * 65)
    print("    JARVIS - Autonomous Voice Assistant (Powered by Groq)")
    print("=" * 65)

    speak("Hello Madam, Jarvis is online and powered by Groq. How can I assist you?")

    # Initial ambient calibration
    try:
        with sr.Microphone() as source:
            print("[Calibrating microphone for ambient room noise...]")
            recognizer.adjust_for_ambient_noise(source, duration=1.0)
            print("[Microphone calibrated successfully.]")
    except Exception as e:
        print(f"[Microphone calibration warning]: {e}")

    running = True

    while running:
        try:
            with sr.Microphone() as source:
                print("\n[Listening for wake word 'Jarvis'...]")
                audio = recognizer.listen(source, timeout=6, phrase_time_limit=6)

            try:
                spoken_text = recognizer.recognize_google(audio).lower()
                print(f"[Heard]: \"{spoken_text}\"")

                # Detect wake word
                if "jarvis" in spoken_text:
                    parts = spoken_text.split("jarvis", 1)
                    direct_command = parts[1].strip() if len(parts) > 1 else ""

                    if direct_command:
                        running = processCommand(direct_command)
                    else:
                        speak("Yes Madam?")
                        with sr.Microphone() as source:
                            print("[Listening for command...]")
                            audio_cmd = recognizer.listen(source, timeout=6, phrase_time_limit=7)
                            command = recognizer.recognize_google(audio_cmd)
                            running = processCommand(command)

            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"[Google STT Service Error]: {e}")

        except sr.WaitTimeoutError:
            continue
        except KeyboardInterrupt:
            print("\n[Terminating Jarvis on KeyboardInterrupt]")
            speak("Shutting down. Goodbye Madam!")
            break
        except Exception as e:
            print(f"[System Error]: {e}")
            time.sleep(0.5)


if __name__ == "__main__":
    main()