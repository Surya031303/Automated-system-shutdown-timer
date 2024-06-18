# MIT License
# 
# Copyright (c) 2024 Suryanarayana
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import pyttsx3
import os
import tkinter as tk
from tkinter import messagebox

# Set the time you want to lock the system
lock_time = "00:00:00"   # HH:MM:SS 24 hours format

while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == lock_time:
        # Create a popup window
        root = tk.Tk()
        root.title("System Shutdown")

        # Create a label to display the countdown
        countdown_label = tk.Label(root, font=('Helvetica', 24), fg='red')
        countdown_label.pack()

        # Display a message
        engine = pyttsx3.init()
        engine.say("Your Time is Up")  #Change this message what ever you want
        engine.runAndWait()
        engine.say(f"System shutting down in with the count of 10.")
        engine.runAndWait()

        # Show a popup window with the current time
        messagebox.showinfo("System Shutdown", f"System shutting down at {current_time}. Continue your work by tomorrow.")

        # Countdown and shutdown the system
        for i in range(10, 0, -1):
            countdown_label.config(text=f"System shutting down in {i} seconds...")
            root.update()  # Update the label
            engine.say(f"{i}")
            engine.runAndWait()
            time.sleep(1)

        # Shutdown the system
        os.system("shutdown /s /t 0")
