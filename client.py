"""
JARVIS Interactive Testing Client
Allows testing Jarvis commands via both microphone voice input and keyboard text input.
"""

import sys
import main

def interactive_client():
    print("=" * 60)
    print("      JARVIS Interactive Console & Voice Test Client")
    print("=" * 60)
    print("Options:")
    print(" 1. Type commands directly (e.g. 'open youtube', 'time', 'play lofi')")
    print(" 2. Type 'voice' to speak a command through the microphone")
    print(" 3. Type 'exit' to quit")
    print("-" * 60)

    main.speak("Jarvis test console activated.")

    while True:
        try:
            user_input = input("\nEnter Command (or 'voice' / 'exit'): ").strip()
            
            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit", "q"]:
                main.speak("Exiting test client. Goodbye!")
                break

            if user_input.lower() == "voice":
                try:
                    with main.sr.Microphone() as source:
                        print("[Listening for voice input...]")
                        main.recognizer.adjust_for_ambient_noise(source, duration=0.8)
                        audio = main.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        cmd = main.recognizer.recognize_google(audio)
                        print(f"[Recognized]: {cmd}")
                        user_input = cmd
                except Exception as e:
                    print(f"[Voice Input Error]: {e}")
                    continue

            should_continue = main.processCommand(user_input)
            if not should_continue:
                break

        except KeyboardInterrupt:
            print("\nSession interrupted.")
            break
        except Exception as e:
            print(f"[Client Error]: {e}")

if __name__ == "__main__":
    interactive_client()
