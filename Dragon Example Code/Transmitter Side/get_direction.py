from play_sound import sound_player
import pygame

pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()

def input_direction(joystick):
    direction = ""
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 1:
                direction = "f"
            if event.button == 8:
                direction = "stop"
            if event.button == 9:
                direction = "start"
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
        
def handle_direction(joystick):
    n_sound_file = '/home/nat/modem_speaker/direction_sound_files/north.wav'
    s_sound_file = '/home/nat/modem_speaker/direction_sound_files/south.wav'
    e_sound_file = '/home/nat/modem_speaker/direction_sound_files/east.wav'
    w_sound_file = '/home/nat/modem_speaker/direction_sound_files/west.wav'
    f_sound_file = '/home/nat/modem_speaker/direction_sound_files/straight.wav'
    
    running = True
    while running:
        direction = input_direction(joystick)
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
        elif direction == "f":
            print(f'You entered "Forward/Straight"')
            sound_player(f_sound_file)
        elif direction == "stop":
            print("Quit")
            running = False
        else:
            continue

def main():
    joystick_count = pygame.joystick.get_count()
    
    if joystick_count == 0:
        print("No controller detected.")
        return
    
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    
    handle_direction(joystick)
    
if __name__ == "__main__":
    main()