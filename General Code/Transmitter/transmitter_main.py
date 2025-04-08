# Updated by Soft Robotics Lab
# 4/8/2025

# IMPORTS
# Libraries
import numpy as np
import pygame
import time

# Initialise the pygame library
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)

# Connect to controller
controller = pygame.joystick.Joystick(0)
controller.init()
print("Initialized Controller : " + controller.get_name())
time.sleep(2)

### UPDATE FILE PATHS FOR WAV FILES HERE ###
# Initialize Tones
first_tone = pygame.mixer.Sound('C:/Users/.../first.wav')
second_tone = pygame.mixer.Sound('C:/Users/.../second.wav')
third_tone = pygame.mixer.Sound('C:/Users/.../third.wav')
fourth_tone = pygame.mixer.Sound('C:/Users/.../fourth.wav')
fifth_tone = pygame.mixer.Sound('C:/Users/.../fifth.wav')
sixth_tone = pygame.mixer.Sound('C:/Users/.../sixth.wav')
seventh_tone = pygame.mixer.Sound('C:/Users/.../seventh.wav')

# Initialize Constants
playing = [False,False,False,False,False,False,False]

# FUNCTIONS
# Function: main() is the main loop of the program, reads inputs from a USB controller and plays sounds corresponding to button presses
# Inputs: none
# Outputs: none
def main():
    global playing
    # Main Loop
    try:
        while True:
            pygame.event.get()

            # Button presses
            # Circle button on PS2
            if controller.get_button(1) and not playing[0]:
                first_tone.play(loops=-1)
                playing[0] = True
            elif playing[0] and not controller.get_button(1):
                first_tone.stop()
                playing[0] = False
            # Triangle Button on PS2
            if controller.get_button(3) and not playing[5]:
                sixth_tone.play(loops=-1)
                playing[5] = True
            elif playing[5] and not controller.get_button(3):
                sixth_tone.stop()
                playing[5] = False
            # Star button on PS2
            if controller.get_button(0) and not playing[6]:
                seventh_tone.play(loops=-1)
                playing[6] = True
            elif playing[6] and not controller.get_button(0):
                seventh_tone.stop()
                playing[6] = False

            # D-pad presses
            d_pad_pos = controller.get_hat(0)
            # Right on D-pad
            if d_pad_pos[0] == 1 and not playing[1]:
                second_tone.play(loops=-1)
                playing[1] = True
            elif playing[1] and d_pad_pos[0] != 1:
                second_tone.stop()
                playing[1] = False
            # Left on D-pad
            if d_pad_pos[0] == -1 and not playing[2]:
                third_tone.play(loops=-1)
                playing[2] = True
            elif playing[2] and d_pad_pos[0] != -1:
                third_tone.stop()
                playing[2] = False
            # Up on D-pad
            if d_pad_pos[1] == 1 and not playing[3]:
                fourth_tone.play(loops=-1)
                playing[3] = True
            elif playing[3] and d_pad_pos[1] != 1:
                fourth_tone.stop()
                playing[3] = False
            # Down on D-pad
            if d_pad_pos[1] == -1 and not playing[4]:
                fifth_tone.play(loops=-1)
                playing[4] = True
            elif playing[4] and d_pad_pos[1] != -1:
                fifth_tone.stop()
                playing[4] = False



    # Handles exits and crashes        
    except KeyboardInterrupt:
        controller.quit()


if __name__ == '__main__':
    main()