import tkinter as tk
from tkinter import filedialog
import pygame
import os
import requests
from bs4 import BeautifulSoup
import random


class SoundBoard:
    def __init__(self, master):
        self.master = master
        master.title("Sound Board")

        # Create a dictionary to store sound objects
        self.sounds = {}

        # Create a label and entry for file path
        self.label = tk.Label(master, text="Enter file path:")
        self.label.grid(row=0, column=0)
        self.filepath_entry = tk.Entry(master)
        self.filepath_entry.grid(row=0, column=1)

        # Create a button to load the file
        self.load_button = tk.Button(master, text="Load Sound", command=self.load_sound)
        self.load_button.grid(row=0, column=2)

        # Create playback buttons
        self.play_button = tk.Button(master, text="Play", command=self.play)
        self.play_button.grid(row=2, column=0)
        self.pause_button = tk.Button(master, text="Pause", command=self.pause)
        self.pause_button.grid(row=2, column=1)
        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.grid(row=2, column=2)
        self.rewind_button = tk.Button(master, text="<<", command=self.rewind)
        self.rewind_button.grid(row=2, column=3)
        self.slowdown_button = tk.Button(master, text="Slower", command=self.slowdown)
        self.slowdown_button.grid(row=2, column=4)

        # Create a grid of buttons to play the sounds
        self.button_grid = tk.Frame(master)
        self.button_grid.grid(row=1, column=0, columnspan=5)

        # Load 10 Creative Commons sounds on start-up
        self.load_creative_commons_sounds()

    def load_sound(self):
        # Get the filepath from the file dialog
        filepath = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select sound file",
                                               filetypes=(("Sound files", "*.mp3 *.wav *.ogg"), ("all files", "*.*")))

        # Load the sound file with Pygame
        sound = pygame.mixer.Sound(filepath)

        # Add the sound object to the dictionary
        self.sounds[filepath] = sound

        # Create a new button with the filename as text
        filename = os.path.basename(filepath)
        button = tk.Button(self.button_grid, text=filename, command=lambda: self.play_sound(filepath))
        button.pack()

    def play_sound(self, filepath):
        # Stop any currently playing sound
        pygame.mixer.music.stop()

        # Get the sound object from the dictionary
        sound = self.sounds[filepath]

        # Play the sound
        sound.play()

    def load_creative_commons_sounds(self):
        # Get a list of Creative Commons sounds from freesound.org
        page = requests.get("https://freesound.org/search/?q=&f=license%3A%22Creative+Commons+0%22&advanced=0&g=1")
        soup = BeautifulSoup(page.content, 'html.parser')
        sound_links = soup.select('.title > a')

        # Load up to 10 random sounds from the list
        random.shuffle(sound_links)
        for link in sound_links[:10]:
            sound_url = "https://freesound.org" + link['href'] + "download"
            sound_name = link['href'].split("/")[-2] + ".wav"
           
