import queue
import sounddevice as sd
import vosk
import json

class SpeechRecognizer:
    def __init__(self, config):
        self.model_en = vosk.Model(config["stt"]["vosk_model_path_en"])
        self.model_hi = vosk.Model(config["stt"]["vosk_model_path_hi"])
        self.samplerate = 16000
        self.q = queue.Queue()

    def listen_for_wakeword(self):
        # Continually listen, return phrase after wakeword detected
        print("Listening for the wake word ('Jarvis')...")
        # For demo: simulate, actual code should implement continuous detection
        return input("You (say 'Jarvis' ...): ")
