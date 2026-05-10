import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound

def text_to_mp3(text, filename="output.mp3"):
    try:
        # Convert the text to speech using gTTS
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        messagebox.showinfo("Success", f"Audio saved as {filename}")
        
        # Play the audio file
        playsound(filename)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_convert_button_click():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Required", "Please enter some text.")
    else:
        text_to_mp3(text)

# Create main window
root = tk.Tk()
root.title("Text to Speech Converter")
root.geometry("400x300")

# Create a label
label = tk.Label(root, text="Enter Text to Convert to Speech:", font=("Arial", 14))
label.pack(pady=10)

# Create a text box for user input
text_input = tk.Text(root, height=6, width=35, font=("Arial", 12))
text_input.pack(pady=10)

# Create a button to convert text to speech
convert_button = tk.Button(root, text="Convert to Speech", font=("Arial", 14), command=on_convert_button_click)
convert_button.pack(pady=10)

# Run the application
root.mainloop()
