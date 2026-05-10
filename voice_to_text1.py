import tkinter as tk
from tkinter import messagebox, filedialog
import speech_recognition as sr

# Language codes for Google Speech Recognition
language_options = {
    "English (US)": "en-US",
    "Hindi (India)": "hi-IN",
    "Spanish (Spain)": "es-ES",
    "French (France)": "fr-FR",
    "German (Germany)": "de-DE"
}

def recognize_speech():
    recognizer = sr.Recognizer()
    selected_language = language_options[language_var.get()]
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            status_label.config(text="Recognizing...")
            text = recognizer.recognize_google(audio, language=selected_language)
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, text)
            status_label.config(text="Done")
        except sr.UnknownValueError:
            status_label.config(text="Could not understand audio")
        except sr.RequestError:
            status_label.config(text="API unavailable")
        except sr.WaitTimeoutError:
            status_label.config(text="Listening timed out")

def save_text():
    text_content = text_box.get("1.0", tk.END).strip()
    if not text_content:
        messagebox.showwarning("Warning", "There's no text to save!")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_content)
        messagebox.showinfo("Success", f"Text saved to {file_path}")

# GUI setup
window = tk.Tk()
window.title("Speech to Text Converter")
window.geometry("500x400")
window.configure(bg="#f0f0f0")
window.config(bg='silver')

title_label = tk.Label(window, text="🎤 Speech to Text with Language Support", font=("Arial", 16,'bold'), bg='silver')
title_label.pack(pady=10)

language_frame = tk.Frame(window, bg="#f0f0f0")
language_frame.pack(pady=5)

tk.Label(language_frame, text="Select Language:", font=("Arial", 12)).pack(side=tk.LEFT)

language_var = tk.StringVar(value="English (US)")
language_menu = tk.OptionMenu(language_frame, language_var, *language_options.keys())
language_menu.config(font=("Arial", 11),bg='yellow')
language_menu.pack(side=tk.LEFT, padx=10)

text_box = tk.Text(window, height=8, width=55, font=("Arial", 12),bg="white")
text_box.pack(pady=10)

record_button = tk.Button(window, text="Start Recording", command=recognize_speech, bg="#4CAF50", fg="white", font=("Arial", 12))
record_button.pack(pady=5)

save_button = tk.Button(window, text="Save to File", command=save_text, bg="#2196F3", fg="white", font=("Arial", 12))
save_button.pack(pady=5)

status_label = tk.Label(window, text="", font=("Arial", 10))
status_label.pack(pady=5)

window.mainloop()
