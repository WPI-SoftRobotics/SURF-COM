# Updated by Soft Robotics Lab
# 2/26/2025

# IMPORTS
# Libraries
import pygame

# Reference other files
import audio_device_monitor

# FUNCTIONS    
# Function: main() initializes the joystick and reads controller inputs
# Inputs: none
# Outputs: none
def main():
    # Initialize
    card_1_found = audio_device_monitor.monitor_card_1()

    pygame.init()
    pygame.joystick.init()
    
    joystick_count = pygame.joystick.get_count()
    
    if joystick_count == 0:
        print("No controller connected")
        return
    
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    
    # Main loop of program
    if card_1_found:
        print ("Card 1 has been found.")
        
        while True:
            direction = handle_direction(joystick)
            if direction == "quit":
                return
            
    # Errors out if initialization failed
    else:
        print("Card 1 was not found.")


# Function: handle_direction() reads controller input and plays the corresponding tone
# Inputs: pygame.joystick.Joystick
# Outputs: none
def handle_direction(joystick):
    n_sound_file = 'direction_sound_files/north.wav'
    s_sound_file = 'direction_sound_files/south.wav'
    e_sound_file = 'direction_sound_files/east.wav'
    w_sound_file = 'direction_sound_files/west.wav'
    b_sound_file = 'direction_sound_files/button.wav'
    
    running = True
    while running:
        direction = read_input(joystick)
        if direction == "n":
            print(f'You entered "North"')
            sound_player(n_sound_file)
        elif direction == "s":
            print(f'You entered "South"')
            sound_player(s_sound_file)
        elif direction == "e":
            print(f'You entered "East"')
            sound_player(e_sound_file)
        elif direction == "w":
            print(f'You entered "West"')
            sound_player(w_sound_file)
        elif direction == "b":
            print(f'You entered "Button"')
            sound_player(b_sound_file)
        elif direction == "quit":
            print("Quit")
            running = False
        else:
            continue
  

# Function: read_input() reads the input from a controller
# Inputs: pygame.joystick.Joystick
# Outputs: string containing the input command
def read_input(joystick):
    direction = ""
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 1:
                direction = "b"
            if event.button == 8:
                direction = "quit"
        if event.type == pygame.JOYAXISMOTION:
            x_axis = joystick.get_axis(0)
            y_axis = joystick.get_axis(1)
                           
            if x_axis < -0.5:
                direction = "w"
            elif x_axis > 0.5:
                direction = "e"
            if y_axis < -0.5:
                direction = "n"
            elif y_axis > 0.5:
                direction = "s"
            
        if event.type == pygame.QUIT:
            return "quit"
    return direction


# Function: sound_player() plays a .wav file at a specified file path
# Inputs: string file path
# Outputs: none
def sound_player(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


# START 
if __name__ == '__main__':
    main()