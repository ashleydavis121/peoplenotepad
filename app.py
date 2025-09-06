import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My Simple Desktop App")
root.geometry("400x300")

def say_hello():
    messagebox.showinfo("Hello!", "Welcome to your desktop app!")

btn = tk.Button(root, text="Click Me", command=say_hello)
btn.pack(pady=50)

root.mainloop()
