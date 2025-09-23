import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")
root.configure(bg='black')

clock_label = tk.Label(root, font=('Helvetica', 48), fg='green', bg='black')
clock_label.pack()

date_label = tk.Label(root, font=('Helvetica', 20), fg='white', bg='black')
date_label.pack()

def update_time():
    current_time = strftime('%H:%M:%S')
    current_date = strftime('%A, %d %B %Y')
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    clock_label.after(1000, update_time)

update_time()

root.mainloop()