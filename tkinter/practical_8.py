import tkinter as tk
from tkinter import messagebox

def show_message_info():
    messagebox.showinfo("button_message", "Kyu click kiya")

root = tk.Tk()
root.title("Button widget")
root.geometry("360x260")

btn = tk.Button(root, text="Click Me", command=show_message_info, fg="orange")

btn.pack(pady=40)
root.mainloop()