import tkinter as tk
from tkinter import messagebox
import pyttsx3
from gtts import gTTS
import os
import speech_recognition as sr


# Function to speak text
def speak_text():
    text = text_box.get("1.0", tk.END).strip()
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Warning", "Please enter some text to speak.")

# Function to save as MP3 using gTTS
def save_as_mp3():
    text = text_box.get("1.0", tk.END).strip()
    if text:
        try:
            tts = gTTS(text=text, lang='en')
            filename = "output.mp3"
            tts.save(filename)
            messagebox.showinfo("Saved", f"Saved as {filename}")
            os.system(f"start {filename}")  # Use 'open' for macOS, 'xdg-open' for Linux
        except Exception as e:
            messagebox.showerror("Error", f"Error saving file: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text to save.")

        # Speech Recognition function

            
            

# Set up the GUI
root = tk.Tk()
root.title("Text to Speech Converter")
root.geometry("400x300")

# Label
label = tk.Label(root, text="Enter your text:")
label.pack(pady=5)

# Text box
text_box = tk.Text(root, height=10, width=40)
text_box.pack(pady=5)

# Buttons
speak_button = tk.Button(root, text="Speak", command=speak_text)
speak_button.pack(pady=5)

save_button = tk.Button(root, text="Save as MP3", command=save_as_mp3)
save_button.pack(pady=5)





# Run the GUI
root.mainloop()



# Function to recognize speech and convert it into text
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            status_label.config(text="Recognizing...")
            text = recognizer.recognize_google(audio)
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, text)
            status_label.config(text="Done")
        except sr.UnknownValueError:
            status_label.config(text="Could not understand audio")
        except sr.RequestError:
            status_label.config(text="API unavailable")
        except sr.WaitTimeoutError:
            status_label.config(text="Listening timed out")


# GUI setup
window = tk.Tk()
window.title("Speech to Text Converter")
window.geometry("400x300")
window.configure(bg="#f0f0f0")

title_label = tk.Label(window, text="🎤 Speech to Text", font=("Arial", 16), bg="#f0f0f0")
title_label.pack(pady=10)

text_box = tk.Text(window, height=8, width=40, font=("Arial", 12))
text_box.pack(pady=10)

record_button = tk.Button(window, text="Start Recording", command=recognize_speech, bg="#4CAF50", fg="white", font=("Arial", 12))
record_button.pack(pady=10)

status_label = tk.Label(window, text="", font=("Arial", 10), bg="#f0f0f0")
status_label.pack(pady=5)

window.mainloop()
