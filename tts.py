import pyttsx3
import coqui_tts
import os

class VoiceSynthesizer:
    def __init__(self, config):
        self.provider = config["tts"].get("provider", "pyttsx3")
        if self.provider == "pyttsx3":
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 160)
        else:
            # For demo simplicity; See Coqui docs for full setup
            self.coqui_en = coqui_tts.TTS(config["tts"]["coqui_voice_en"])
            self.coqui_hi = coqui_tts.TTS(config["tts"]["coqui_voice_hi"])
        
    def say(self, text, lang='en'):
        if self.provider == "pyttsx3":
            self.engine.say(text)
            self.engine.runAndWait()
        else:
            if lang == 'hi':
                self.coqui_hi.tts_to_file(text, "tmp_hi.wav")
                os.system("mpv tmp_hi.wav")
            else:
                self.coqui_en.tts_to_file(text, "tmp_en.wav")
                os.system("mpv tmp_en.wav")
