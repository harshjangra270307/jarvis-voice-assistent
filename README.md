# Jarvis Cross-Platform Voice Assistant

An extensible, privacy-first voice assistant for Laptops (Windows/macOS/Linux) and Android, supporting offline/hybrid voice, English/Hindi, local phonebook/profile, and easy plugins.

**Features**

- Wake-word ("Jarvis") activation with continuous listening
- Offline STT/TTS for Hindi & English (Vosk, pyttsx3/Coqui)
- Supports desktop + Android (with secure remote commands)
- Encrypted personal data/profile & local phonebook
- Local app launch, URL open, shell commands, YouTube/Spotify media control
- Weather/news/LLM chat (optional online with simple API config)
- Extensible intents & grammar files for voice
- Full CLI, optional lightweight Tkinter GUI

> See the Quickstart below to get running fast!

---

## Quickstart

1. **Clone the repo**
git clone https://github.com/harshjangra270307/jarvis-voice-assistent.git
cd jarvis-voice-assistent


2. **Setup Python venv**
python3 -m venv venv
source venv/bin/activate # on Windows:venv\Scripts\activate


3. **Install OS Prerequisites**
- Linux:  
  ```
  sudo apt-get install portaudio19-dev ffmpeg mpv vlc
  ```
- macOS:  
  ```
  brew install portaudio mpv ffmpeg
  ```
- Windows:  
  Download and install [Python 3.10+](https://www.python.org), [mpv](https://mpv.io/installation/), and [portaudio binaries](http://www.portaudio.com/).

4. **Install Python dependencies**
pip install -r requirements.txt


5. **Download Vosk STT models (English: 50MB, Hindi: 64MB)**
mkdir -p models
cd models
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
wget https://alphacephei.com/vosk/models/vosk-model-small-hi-0.22.zip
unzip vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-hi-0.22.zip
cd..


6. **Copy config files and set API keys/secrets**
cp config.example.json config.json
cp .env.example.env

- Edit `config.json` and `.env` to insert your OpenWeatherMap/Spotify/NewsAPI/OpenAI API keys.
- Strongly recommended: Generate a strong encryption key for profile data.

python -c "from cryptography.fernet import Fernet;
print(Fernet.genetate_key().decode())"


7. **Run the assistant (CLI mode)**
python main.py
 **7.1. Or, for optional GUI:**
   python gui.py


8. **Run tests**
pytest tests/


9. **Android companion setup**
- Open `android-companion` in Android Studio.
- Set emulator/device with Google Play services.
- Optional: configure WebSocket/HTTP bridge URL, API keys, permissions.
- Build & Run:
  ```
  ./gradlew assembleDebug
  # Or from Studio, Build > Run
  ```

**Tip:** For Spotify/Weather/News/OpenAI integration, see the API config notes below.

---

## Features & Platforms

| Feature                    | Desktop (Win/macOS/Linux) | Android                | Notes                                   |
|----------------------------|---------------------------|------------------------|-----------------------------------------|
| Wake Word                  | ✔️                        | ✔️                     | Always offline                          |
| Offline STT/TTS            | ✔️                        | ✔️                     | Vosk, pyttsx3/Coqui, Hindi/English      |
| Phone Calls (initiate)     | via companion app         | ✔️                     | See platform limitations                |
| App Launch / URLs          | ✔️                        | ✔️                     | Platform-agnostic methods               |
| Phonebook/Profile          | Encrypted JSON            | via companion, bridge  | Secure + easy CRUD                      |
| Weather/News/Chat/Spotify  | Optional (API needed)     | Optional               | Keys required                           |
| Remote Control             | via WebSocket/HTTP bridge | via bridge, push cmds  | Encrypted, opt-in                       |

---

# LICENSE

MIT License

Copyright (c) 2025 YourName

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
