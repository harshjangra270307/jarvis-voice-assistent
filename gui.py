import tkinter as tk
from main import on_intent, stt, tts, ie

def listen_and_respond():
    user_input = stt.listen_for_wakeword(block=True)
    if user_input:
        lang = 'hi' if user_input.startswith('Namaste') else 'en'
        parsed = ie.parse(user_input, lang)
        if parsed:
            intent, args = parsed
            response = on_intent(intent, args)
            text_out.insert(tk.END, f"User: {user_input}\nJarvis: {response}\n")
        else:
            text_out.insert(tk.END, f"User: {user_input}\nJarvis: Sorry, I didn't get that.\n")

window = tk.Tk()
window.title("Jarvis Voice Assistant")

listen_btn = tk.Button(window, text="Talk to Jarvis", command=listen_and_respond)
listen_btn.pack()

text_out = tk.Text(window)
text_out.pack(fill=tk.BOTH, expand=True)

window.mainloop()
