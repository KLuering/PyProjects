import tkinter as tk
import random

class DiceApp:

    def __init__(self, master):
        self.master = master
        master.title("Digital Dice")
        master.geometry("1400x1400")  # increase window size
        master.resizable(False, False)

        # create label for dice image
        self.dice_label = tk.Label(master, image=None)
        self.dice_label.pack(pady=20)

        # create roll button
        self.roll_button = tk.Button(master, text="Roll", command=self.roll_dice)
        self.roll_button.pack()

    def roll_dice(self):
        # generate random number between 1 and 6
        dice_value = random.randint(1, 6)

        # create filename for dice image
        filename = "dice-{}.png".format(dice_value)

        # update dice image
        self.photo = tk.PhotoImage(file=filename)
        self.dice_label.configure(image=self.photo)
        self.dice_label.image = self.photo


root = tk.Tk()
app = DiceApp(root)
root.mainloop()
