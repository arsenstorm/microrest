import time
import random
import pygame

def play_beep():
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Initialize the mixer
pygame.mixer.init()

# Load the sound file
pygame.mixer.music.load('beep.mp3')

# Time between double beeps in minutes
double_beep_interval = 30
# Time to wait after double beeps in minutes
wait_after_double_beep = 5

start_time = time.time()
last_double_beep_time = start_time

while True:
    current_time = time.time()
    elapsed_minutes = (current_time - last_double_beep_time) / 60.0

    if elapsed_minutes >= double_beep_interval:
        print("Playing double beeps")
        play_beep()
        time.sleep(10)
        play_beep()

        # Wait for 5 minutes after the double beep
        print(f"Waiting for {wait_after_double_beep} minutes")
        time.sleep(wait_after_double_beep * 60)

        last_double_beep_time = time.time()

    else:
        time_to_wait = random.randint(110, 150)
        print(f"Waiting for {time_to_wait} seconds")
        time.sleep(time_to_wait)
        play_beep()
