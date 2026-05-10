# import tkinter as tk
# from tkinter import messagebox


# # Function to show a message box when a button is clicked
# root = tk.Tk()
# root.title("Front Page")
# root.geometry("400x300")

# # Create three buttons
# button1 = tk.Button(root, text="text to voice")
# button1.config(command=lambda: messagebox.showinfo("Button 1", "You clicked Button 1!"))
# button2 = tk.Button(root, text="voice to text")
# button2.config(command=lambda: messagebox.showinfo("Button 2", "You clicked Button 2!"))


# # Pack the buttons vertically
# button1.pack(pady=10)
# button2.pack(pady=10)


# root.mainloop()



import tkinter as tk
import subprocess  # or use subprocess.system



def run_first_program():
    subprocess.run(["python", "E:/VS Code/Voice or text project/text_to_voice2.py"])  # this runs the second file
def run_second_program():
    subprocess.run(["python", "E:/VS Code/Voice or text project/voice_to_text1.py"])  # this runs the second file

window = tk.Tk()
window.title("Front page ")
window.configure(bg="#f0f0f0")
window.geometry("500x400")
window.config(bg='silver')



title_label = tk.Label(window, text="TextSpeak & VoiceWeaver", font=("Comic Sans MS", 20 , "bold"), bg="silver", fg="black")
title_label.pack(pady=10)


run_button = tk.Button(window, text="Text To Voice", command=run_first_program,font=("Arial", 20))
run_button.pack(pady=(50,30))
run_button.config(bg='yellow')
    
run_button = tk.Button(window, text="Voice To Text ", command=run_second_program,font=("Arial", 20))
run_button.pack(pady=20)
run_button.config(bg='yellow')


window.mainloop()
