import tkinter as tk
import pyttsx3
from tkinter import ttk
from tkinter import messagebox
from gtts import gTTS
import os


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak_text():
    text = text_input.get("1.0", "end-1c")
    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Warning", "Please enter some text to speak.")

# Function to adjust the speech rate
def set_rate(val):
    rate = int(val)
    engine.setProperty('rate', rate)

# Function to adjust the volume
def set_volume(val):
    volume = float(val)
    engine.setProperty('volume', volume)

# Function to change voice (male/female)
def change_voice(val):
    voices = engine.getProperty('voices')
    if val == "Male":
        engine.setProperty('voice', voices[0].id)  # Male voice
    else:
        engine.setProperty('voice', voices[1].id)  # Female voice
        
        
        

# Function to save as MP3 using gTTS
def save_as_mp3():
    text = text_input.get("1.0", tk.END).strip()
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

# Create the main window
root = tk.Tk()
root.title("Text-to-Speech")
root.config(bg='silver')

# Text input area
text_input = tk.Text(root, height=8, width=50)
text_input.pack(padx=10, pady=10)

# Speak Button
speak_button = tk.Button(root, text="Speak", command=speak_text, bg="#2196F3", fg="white")
speak_button.pack(pady=5)

# Save Buttons
save_button = tk.Button(root, text="Save as MP3", command=save_as_mp3,bg="#4CAF50", fg="white")
save_button.pack(pady=5)

# Volume Control
volume_label = tk.Label(root, text="Volume",bg='yellow')
volume_label.pack(pady=5)
volume_slider = tk.Scale(root, from_=0, to_=1, resolution=0.1, orient=tk.HORIZONTAL, command=set_volume)
volume_slider.set(1)
volume_slider.config(bg='white')
volume_slider.pack()

# Rate Control
rate_label = tk.Label(root, text="Speech Speed (words per minute)",bg='yellow')
rate_label.pack(pady=5)
rate_slider = tk.Scale(root, from_=50, to_=200, orient=tk.HORIZONTAL, command=set_rate,)
rate_slider.set(150)
rate_slider.config(bg='white')
rate_slider.pack()

# Voice Selection (Male or Female)
voice_label = tk.Label(root, text="Voice Selection",bg='yellow')
voice_label.pack(pady=5)
voice_options = ttk.Combobox(root, values=["Male", "Female"], state="readonly", width=15)
voice_options.set("Male")
voice_options.pack(pady=5)
voice_options.bind("<<ComboboxSelected>>", lambda event: change_voice(voice_options.get()))


# Start the GUI event loop
root.mainloop()
