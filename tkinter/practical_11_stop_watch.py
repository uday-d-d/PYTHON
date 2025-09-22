import tkinter as tk

counter = 0
running = False

def start_watch():
    global running, counter
    disable_others(start_btn)
    label.config(text="Starting...")
    counter = 0
    running = True
    run_timer()

def run_timer():
    global counter
    if running:
        counter += 1
        label.config(text=str(counter))
        root.after(1000, run_timer)

def stop_watch():
    global running
    disable_others(stop_btn)
    running = False

def reset_watch():
    global counter, running
    disable_others(reset_btn)
    counter = 0
    if running:
        label.config(text=str(counter))
    else:
        label.config(text="Welcome")

def disable_others(active_btn):
    start_btn.config(state="normal")
    stop_btn.config(state="normal")
    reset_btn.config(state="normal")
    active_btn.config(state="disabled")

root = tk.Tk()
root.title("Stopwatch")
root.geometry("400x200")

label = tk.Label(root, text="Welcome", font=("Arial", 30))
label.pack(pady=20)

start_btn = tk.Button(root, text="Start", command=start_watch, width=20)
start_btn.pack(padx=30)

stop_btn = tk.Button(root, text="Stop", command=stop_watch, width=20)
stop_btn.pack(padx=30)

reset_btn = tk.Button(root, text="Reset", command=reset_watch, width=20)
reset_btn.pack(padx=30)

root.mainloop()