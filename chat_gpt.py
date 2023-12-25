from WebChatGPT import ChatGPT
import tkinter as tk
from flask import Flask, request, render_template_string
import threading
import webbrowser
import time
import requests
from urllib.parse import quote_plus
from tkinter import filedialog
from tkinter import Entry
from tkinter import messagebox

def call_chat_gpt(json_path, propmt):
    bot = ChatGPT(json_path)
    print(bot.chat(propmt))


def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        file_path_label.config(text=file_path, fg='blue')

def submit():
    file_path = file_path_label.cget("text")
    input_text = text_entry.get()
    submit_button.config(fg='blue')

    # Get the response from the ChatGPT function
    response = call_chat_gpt(json_path=file_path, propmt=input_text)
    print(response)

    # # Show the response in the browser
    # show_text_in_browser(response)

def start():
    start_button.config(fg='green')
    submit()  # Call the submit function to process text and file path


def confirm_exit():
    if messagebox.askokcancel("Quit", "Do you want to exit?"):
        root.destroy()

def clear_placeholder(event):
    if text_entry.get() == 'Please add text here and click submit button':
        text_entry.delete(0, tk.END)

root = tk.Tk()
root.title('Basic UI with Background Image')
root.geometry('800x600')  # Increase the size of the UI

# Set the background image
background_image = tk.PhotoImage(file=image_path)  # Replace with your image file
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# File path label
file_path_label = tk.Label(root, text='No file selected', bg='white')
file_path_label.pack(pady=25)

# File select button
file_button = tk.Button(root, text='Load File', command=load_file)
file_button.pack(pady=25)

# Text entry with a placeholder
text_label = tk.Label(root, text='Enter Text:', bg='white')
text_label.pack(pady=(15, 0))
text_entry = Entry(root, width=50)
text_entry.insert(0, 'Please add text here and click submit button')
text_entry.bind("<FocusIn>", clear_placeholder)
text_entry.pack(pady=25)

# Submit button
submit_button = tk.Button(root, text='Submit', command=submit)
submit_button.pack(pady=25)

# Start button
start_button = tk.Button(root, text='Start', command=start)
start_button.pack(pady=25)

# Exit button
exit_button = tk.Button(root, text='Exit', command=confirm_exit)
exit_button.pack(pady=25)

root.mainloop()


