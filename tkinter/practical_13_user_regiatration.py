import tkinter as tk
from tkinter import messagebox
import re

root = tk.Tk()
root.title("User Registration Form")
root.geometry("450x600")
root.configure(bg="#f0f0f0")

name_var = tk.StringVar()
email_var = tk.StringVar()
password_var = tk.StringVar()
country_var = tk.StringVar(value="Select Country")
age_var = tk.StringVar()
gender_var = tk.StringVar(value="")
contact_var = tk.StringVar()

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def is_valid_contact(contact):
    pattern = r'^\d{10}$'
    return re.match(pattern, contact)

def clear_form():
    name_var.set("")
    email_var.set("")
    password_var.set("")
    gender_var.set("")
    country_var.set("Select Country")
    age_var.set("")
    contact_var.set("")

def submit_form():
    name = name_var.get()
    email = email_var.get()
    password = password_var.get()
    gender = gender_var.get()
    country = country_var.get()
    age = age_var.get()
    contact = contact_var.get()
    
    if not (name and email and password and gender and country != "Select Country" and age and contact):
        messagebox.showwarning("Error", "All fields are required!")
        return
    
    if not is_valid_email(email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address")
        return
    
    if not is_valid_contact(contact):
        messagebox.showerror("Invalid Contact", "Please enter a valid 10-digit contact number starting with 6-9")
        return
    
    messagebox.showinfo("Registration Successful", 
                        f"Welcome {name}!\nGender: {gender}\nCountry: {country}\nContact: {contact}")
    clear_form()

tk.Label(root, text="User Registration Form", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)

tk.Label(root, text="Name", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=name_var, width=30).pack(pady=5)

tk.Label(root, text="Email", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=email_var, width=30).pack(pady=5)

tk.Label(root, text="Password", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=password_var, width=30, show="*").pack(pady=5) #\u25CF -> •

tk.Label(root, text="Contact Number", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=contact_var, width=30).pack(pady=5)

tk.Label(root, text="Age", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=age_var, width=30).pack(pady=5)

tk.Label(root, text="Gender", bg="#f0f0f0").pack()
gender_frame = tk.Frame(root, bg="#f0f0f0")
gender_frame.pack(pady=5)
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="#f0f0f0").pack(side="left", padx=10)
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="#f0f0f0").pack(side="left", padx=10)
tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other", bg="#f0f0f0").pack(side="left", padx=10)

tk.Label(root, text="Country", bg="#f0f0f0").pack()
countries = ["Select Country", "India", "USA", "UK", "Canada", "Australia", "Other"]
tk.OptionMenu(root, country_var, *countries).pack(pady=5)

tk.Button(root, text="Register", command=submit_form, width=20, bg="green", fg="white").pack(pady=20)

root.mainloop()
