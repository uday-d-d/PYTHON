import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("User Registration Form")
root.geometry("450x500")
root.configure(bg="#f0f0f0")

# Tkinter variables
name_var = tk.StringVar()
email_var = tk.StringVar()
password_var = tk.StringVar()
gender_var = tk.StringVar(value="Male")  # default
country_var = tk.StringVar(value="Select Country")
age_var = tk.StringVar()

# Function to clear form
def clear_form():
    name_var.set("")
    email_var.set("")
    password_var.set("")
    gender_var.set("Male")
    country_var.set("Select Country")
    age_var.set("")

# Function to submit form
def submit_form():
    name = name_var.get()
    email = email_var.get()
    password = password_var.get()
    gender = gender_var.get()
    country = country_var.get()
    age = age_var.get()
    
    if name and email and password and gender and country != "Select Country" and age:
        messagebox.showinfo("Registration Successful", f"Welcome {name}!\nGender: {gender}\nCountry: {country}")
        clear_form()
    else:
        messagebox.showwarning("Error", "All fields are required!")

# Labels and Entries
tk.Label(root, text="User Registration Form", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)

tk.Label(root, text="Name", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=name_var, width=30).pack(pady=5)

tk.Label(root, text="Email", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=email_var, width=30).pack(pady=5)

tk.Label(root, text="Password", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=password_var, width=30, show="\u2022").pack(pady=5)

tk.Label(root, text="Gender", bg="#f0f0f0").pack()
gender_frame = tk.Frame(root, bg="#f0f0f0")
gender_frame.pack(pady=5)
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="#f0f0f0").pack(side="left", padx=10)
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="#f0f0f0").pack(side="left", padx=10)
tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other", bg="#f0f0f0").pack(side="left", padx=10)

tk.Label(root, text="Country", bg="#f0f0f0").pack()
countries = ["Select Country", "India", "USA", "UK", "Canada", "Australia", "Other"]
tk.OptionMenu(root, country_var, *countries).pack(pady=5)

tk.Label(root, text="Age", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=age_var, width=30).pack(pady=5)

# Submit Button
tk.Button(root, text="Register", command=submit_form, width=20, bg="green", fg="white").pack(pady=20)

root.mainloop()

