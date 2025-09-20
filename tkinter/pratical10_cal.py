import tkinter as tk

def press(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

def equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "ERROR")

    
def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width = 25, borderwidth=5, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0),
]

for(text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=equal).grid(row=row, column=col)
    elif text == "C":
        tk.Button(root, text=text, padx=86, pady=20, font=("Arial",14), command=clear).grid(row=row, column=col, columnspan=4)
    else:
        tk.Button(root, text=text, padx=20, pady=20,font=("Arial",14),command=lambda t=text: press(t)).grid(row=row, column=col)

root.mainloop()