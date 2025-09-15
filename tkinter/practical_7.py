import tkinter as tk

root = tk.Tk()
root.title("Label widget")
root.geometry("360x200")

label = tk.Label(root, text="Jay Chamar", font="Poppins", fg="Blue")

label.pack(pady=50)
root.mainloop()