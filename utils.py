import langid
import json
import os
import requests

def detect_language(text):
    # Uses langid for language detection
    lang, _ = langid.classify(text)
    return lang

def play_media(service, query):
    if service == 'youtube':
        url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        import webbrowser
        webbrowser.open(url)

def load_config(path="config.json"):
    with open(path) as f:
        return json.load(f)

def get_weather(city=None):
    # Placeholder: actual API integration omitted for brevity
    return "It's sunny and 30°C."
def initiate_call(number):
    # For desktop OS: open a `tel:` URL
    import webbrowser
    webbrowser.open(f"tel:{number}")
