import tkinter as tk
from tkinter import messagebox

def login():
    username = "admin"
    password = "1234"

    if username == username_entry.get() and password == password_entry.get() :
        messagebox.showinfo("Login successful", "Welcome Admin")
    else:
        messagebox.showinfo("Login Failed", "Invalid Credentials")


root = tk.Tk()
root.title("Login Page")
root.geometry("360x260")

label = tk.Label(root, text="Login page")

label = tk.Label(root, text="username : ")
label.pack(pady=5)
username_entry = tk.Entry(root, width=40)
username_entry.pack(pady=5)

label = tk.Label(root, text="password : ")
label.pack(pady=5)
password_entry =   tk.Entry(root, width=40)
password_entry.pack(pady=5)

btn = tk.Button(root, text="Log In", command=login, bg="yellow", fg="red")
btn.pack(pady=5)

root.mainloop()