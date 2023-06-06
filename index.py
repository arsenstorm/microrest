import time
import random
import pygame

def play_beep():
    pygame.mixer.music.play()

# Initialize the mixer
pygame.mixer.init()

# Load the sound file
pygame.mixer.music.load('beep.mp3')

while True:
    time_to_wait = random.randint(110, 150)  # Choose a random time
    print("Waiting for " + str(time_to_wait) + " seconds")
    time.sleep(time_to_wait)  # Wait for the chosen time
    play_beep()  # Play the beep
    while pygame.mixer.music.get_busy():  # Wait until the beep is finished
        pygame.time.Clock().tick(10)
    time.sleep(10)  # Wait for 10 seconds
    play_beep()  # Play the beep again
    while pygame.mixer.music.get_busy():  # Wait until the beep is finished
        pygame.time.Clock().tick(10)
