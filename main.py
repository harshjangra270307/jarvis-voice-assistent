import os
import threading
import json
from dotenv import load_dotenv
from stt import SpeechRecognizer
from tts import VoiceSynthesizer
from intents import IntentEngine
from phonebook import PhoneBook
from profile1 import ProfileManager
from utils import detect_language, play_media, load_config

load_dotenv()
config = load_config()

def on_intent(intent, args):
    if intent == 'greet':
        tts.say("Hello! How can I help you?")
    elif intent == 'search':
        # Example: open Google search in browser
        import webbrowser
        if args:
            webbrowser.open(f'https://www.google.com/search?q={" ".join(args)}')
            tts.say("Here's what I found online.")
        else:
            tts.say("What should I search for?")
    elif intent == 'call':
        name = args[0] if args else None
        phone_info = phonebook.get_contact(name)
        if phone_info:
            tts.say(f"Initiating call to {name} at {phone_info['number']}")
            utils.initiate_call(phone_info["number"])
        else:
            tts.say(f"I couldn't find {name} in your phonebook.")
    elif intent == 'add_contact':
        name, number = args[0], args[1]
        phonebook.add_contact(name, number)
        tts.say(f"Contact {name} added.")
    elif intent == 'play_youtube':
        play_media('youtube', " ".join(args))
        tts.say("Opening YouTube for you.")
    elif intent == 'profile_set':
        profile.set_field(args[0], args[1])
        tts.say(f"Profile field {args[0]} updated.")
    elif intent == 'weather':
        weather = utils.get_weather()
        tts.say(weather)
    else:
        tts.say("Sorry, I didn't understand.")

if __name__ == '__main__':
    print("Jarvis initialized. Say the wake word to begin...")
    stt = SpeechRecognizer(config)
    tts = VoiceSynthesizer(config)
    phonebook = PhoneBook()
    profile = ProfileManager(config)
    ie = IntentEngine()
    while True:
        text = stt.listen_for_wakeword()
        if not text:
            continue
        lang = detect_language(text)
        print(f"[Detected {lang}] {text}")
        parsed = ie.parse(text, lang)
        if parsed:
            intent, args = parsed
            on_intent(intent, args)
        else:
            tts.say("Sorry, I could not understand that.")
