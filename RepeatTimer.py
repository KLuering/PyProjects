import tkinter as tk
import tkinter.ttk as ttk
import time

class CountdownGUI:
    def __init__(self, master):
        self.master = master
        self.minutes = tk.StringVar(value="5")
        self.time_label = ttk.Label(master, font=("Helvetica", 48), foreground="#FFFFFF", background="#0077CC")
        self.time_label.pack(pady=50)
        self.entry_label = ttk.Label(master, text="Minutes:", font=("Helvetica", 16), foreground="#333333")
        self.entry_label.pack()
        self.entry = ttk.Entry(master, textvariable=self.minutes, font=("Helvetica", 16))
        self.entry.pack()
        self.start_button = ttk.Button(master, text="Start", command=self.start_countdown, style="Accent.TButton")
        self.start_button.pack(pady=50)

        style = ttk.Style()
        style.configure("Accent.TButton", background="#0077CC", foreground="#FFFFFF", font=("Helvetica", 16))

    def start_countdown(self):
        minutes = int(self.minutes.get())
        while True:
            for i in range(minutes, 0, -1):
                self.time_label.config(text=f"{i} minutes left")
                self.master.update()
                time.sleep(60)
            self.time_label.config(text="Time's up!")
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Countdown")
    root.geometry("400x400")
    root.configure(background="#FFFFFF")
    gui = CountdownGUI(root)
    root.mainloop()
