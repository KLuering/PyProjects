import tkinter as tk
import pygame

# Initialize Pygame
pygame.init()

class SoundBoard:
    def __init__(self, master):
        self.master = master
        master.title("Sound Board")

        # Create a dictionary to store sound objects
        self.sounds = {}

        # Create a label and entry for file path
        self.label = tk.Label(master, text="Enter MP3 file path:")
        self.label.grid(row=0, column=0)
        self.filepath_entry = tk.Entry(master)
        self.filepath_entry.grid(row=0, column=1)

        # Create a button to load the file
        self.load_button = tk.Button(master, text="Load Sound", command=self.load_sound)
        self.load_button.grid(row=0, column=2)

        # Create a grid of buttons to play the sounds
        self.button_grid = tk.Frame(master)
        self.button_grid.grid(row=1, column=0, columnspan=3)

    def load_sound(self):
        # Get the filepath from the entry
        filepath = self.filepath_entry.get()

        # Load the sound file with Pygame
        sound = pygame.mixer.Sound(filepath)

        # Add the sound object to the dictionary
        self.sounds[filepath] = sound

        # Create a new button with the filename as text
        filename = filepath.split("/")[-1]
        button = tk.Button(self.button_grid, text=filename, command=lambda: self.play_sound(filepath))
        button.pack()

    def play_sound(self, filepath):
        # Get the sound object from the dictionary
        sound = self.sounds[filepath]

        # Play the sound
        sound.play()

# Create the root window
root = tk.Tk()

# Create the sound board
sound_board = SoundBoard(root)

# Start the main event loop
root.mainloop()

# Quit Pygame when the program is finished
pygame.quit()
