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

        # Create playback buttons
        self.rewind_button = tk.Button(master, text="Rewind", command=self.rewind_sound)
        self.rewind_button.grid(row=2, column=0)
        self.slowdown_button = tk.Button(master, text="Slow Down", command=self.slowdown_sound)
        self.slowdown_button.grid(row=2, column=1)

    def load_sound(self):
        # Get the filepath from the file explorer
        filepath = tk.filedialog.askopenfilename(initialdir="/", title="Select MP3 file", filetypes=(("MP3 files", "*.mp3"), ("all files", "*.*")))
        
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

    def rewind_sound(self):
        # Stop any currently playing sounds
        pygame.mixer.stop()

        # Get the current playback position
        current_pos = pygame.mixer.music.get_pos()

        # Rewind the sound by 5 seconds (5000 milliseconds)
        new_pos = current_pos - 5000
        if new_pos < 0:
            new_pos = 0

        # Set the new playback position
        pygame.mixer.music.set_pos(new_pos)

        # Resume playback
        pygame.mixer.music.unpause()

    def slowdown_sound(self):
        # Stop any currently playing sounds
        pygame.mixer.stop()

        # Get the current playback rate
        current_rate = pygame.mixer.music.get_rate()

        # Slow down the playback rate by 50%
        new_rate = int(current_rate * 0.5)

        # Set the new playback rate
        pygame.mixer.music.set_rate(new_rate)

        # Resume playback
        pygame.mixer.music.unpause()


# Create the root window
root = tk.Tk()

# Create the sound board
sound_board = SoundBoard(root)

# Start the main event loop
root.mainloop()

# Quit Pygame when the program is finished
pygame.quit()
