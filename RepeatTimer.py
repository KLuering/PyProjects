import tkinter as tk
import tkinter.ttk as ttk
import time
import os

class CountdownGUI:
    def __init__(self, master):
        self.master = master
        self.minutes = tk.StringVar(value="5")
        self.seconds = tk.StringVar(value="00")
        self.time_label = ttk.Label(master, font=("Helvetica", 48), foreground="#FFFFFF", background="#0077CC")
        self.time_label.pack(pady=50)
        self.entry_label = ttk.Label(master, text="Minutes:", font=("Helvetica", 16), foreground="#333333")
        self.entry_label.pack()
        self.entry = ttk.Entry(master, textvariable=self.minutes, font=("Helvetica", 16))
        self.entry.pack()
        self.seconds_label = ttk.Label(master, text="Seconds:", font=("Helvetica", 16), foreground="#333333")
        self.seconds_label.pack()
        self.seconds_entry = ttk.Entry(master, textvariable=self.seconds, font=("Helvetica", 16))
        self.seconds_entry.pack()
        self.start_button = ttk.Button(master, text="Start", command=self.start_countdown, style="Accent.TButton")
        self.start_button.pack(pady=50)
        self.count_label = ttk.Label(master, text="Countdowns completed: 0", font=("Helvetica", 16), foreground="#333333")
        self.count_label.pack(pady=20)
        self.pin_button = ttk.Button(master, text="Pin", command=self.pin_window, style="Accent.TButton")
        self.pin_button.pack(pady=10)

        style = ttk.Style()
        style.configure("Accent.TButton", background="#0077CC", foreground="#FFFFFF", font=("Helvetica", 16))

        self.countdowns_completed = 0

    def start_countdown(self):
        minutes = int(self.minutes.get())
        seconds = int(self.seconds.get())
        total_seconds = minutes * 60 + seconds
        while True:
            for i in range(total_seconds, -1, -1):
                minutes = i // 60
                seconds = i % 60
                self.time_label.config(text=f"{minutes:02}:{seconds:02}")
                self.master.update()
                time.sleep(1)
                if i == 0:
                    self.countdowns_completed += 1
                    self.count_label.config(text=f"Countdowns completed: {self.countdowns_completed}")
                    break
            self.time_label.config(text="Time's up!")

    def pin_window(self):
        if os.name == 'nt':
            self.master.wm_attributes('-topmost', True)
            self.master.after_idle(self.master.wm_attributes, '-topmost', False)
        elif os.name == 'posix':
            self.master.attributes('-topmost', True)
            self.master.attributes('-topmost', False)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Countdown")
    root.geometry("400x550")
    root.configure(background="#FFFFFF")
    gui = CountdownGUI(root)
    root.mainloop()
