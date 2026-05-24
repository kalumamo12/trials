# Simple Login Page using Python Tkinter
#this is my first commit on it
import tkinter as tk
from tkinter import messagebox
import pandas as pd 
# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("350x250")
root.resizable(False, False)

# Heading
title = tk.Label(root, text="User Login", font=("Arial", 18, "bold"))
title.pack(pady=15)

# Username Label and Entry
username_label = tk.Label(root, text="Username")
username_label.pack()

username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

# Password Label and Entry
password_label = tk.Label(root, text="Password")
password_label.pack()

password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

# Login Function
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Example username and password
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

# Login Button
login_button = tk.Button(root, text="Login", width=15, command=login)
login_button.pack(pady=20)

# Run Application
root.mainloop()
