import tkinter as tk
from tkinter import messagebox

timer_running = False
timer_seconds = 25 * 60

def setup_window():
    root = tk.Tk()
    root.title("Pomodoro Timer")
    root.geometry("300x250")
    return root

def create_timer_display(root):
    timer_label = tk.Label(root, text="Timer", font=("Helvetica", 24))
    timer_label.pack(pady=20)

    time_display = tk.Label(root, text="25:00", font=("Helvetica", 48))
    time_display.pack(pady=20)
    return timer_label, time_display

def create_buttons(root, start_timer, reset_timer):
    start_button = tk.Button(root, text="Start", command=start_timer)
    start_button.pack(side=tk.LEFT, padx=20, pady=20)

    reset_button = tk.Button(root, text="Reset", command=reset_timer)
    reset_button.pack(side=tk.RIGHT, padx=20, pady=20)

    return start_button, reset_button

def start_timer(time_display):
    global timer_running
    if not timer_running:
        timer_running = True
        countdown(time_display)

def reset_timer(time_display):
    global timer_running, timer_seconds
    timer_running = False
    timer_seconds = 25 * 60
    time_display.config(text="25:00")

def countdown(time_display):
    global timer_running, timer_seconds
    if timer_running and timer_seconds > 0:
        minutes = timer_seconds // 60
        seconds = timer_seconds % 60
        time_display.config(text=f"{minutes:02d}:{seconds:02d}")
        timer_seconds -= 1
        time_display.after(1000, countdown, time_display)
    elif timer_seconds == 0:
        messagebox.showinfo("Pomodoro Timer", "Time's up!")
        reset_timer(time_display)

def main():
    root = setup_window()
    
    timer_label, time_display = create_timer_display(root)
    start_button, reset_button = create_buttons(root, lambda: start_timer(time_display), lambda: reset_timer(time_display))
    
    root.mainloop()

if __name__ == "__main__":
    main()
