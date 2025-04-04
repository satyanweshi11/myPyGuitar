import pygame
import os


pygame.mixer.init()

BASE_DIR = "assets/sounds/"

def play_chord_sound(chord_name):
    
    sound_file = os.path.join(BASE_DIR, f"{chord_name}.wav")

    if os.path.exists(sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        print(f"Playing: {chord_name}")
    else:
        print(f"Sound file not found: {chord_name}")
