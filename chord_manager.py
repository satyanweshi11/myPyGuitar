import pygame


pygame.mixer.init()


chord_sounds = {
    "C": pygame.mixer.Sound("assets/sounds/C.wav"),
    "D": pygame.mixer.Sound("assets/sounds/D.wav"),
    "E": pygame.mixer.Sound("assets/sounds/E.wav"),
    "F": pygame.mixer.Sound("assets/sounds/F.wav"),
    "G": pygame.mixer.Sound("assets/sounds/G.wav"),
    "A": pygame.mixer.Sound("assets/sounds/A.wav"),
    "B": pygame.mixer.Sound("assets/sounds/B.wav"),
}


CHORD_MAP = {
    1: "C",  
    2: "D",  
    3: "E",  
    4: "F",  
    5: "G",  
    0: "A",  
    -1: "B"  
}

def update_chord(finger_count):
    
    current_chord = CHORD_MAP.get(finger_count, None)

    if current_chord:
        chord_sounds[current_chord].play()  

    return current_chord
