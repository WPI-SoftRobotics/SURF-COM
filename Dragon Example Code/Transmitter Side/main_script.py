import audio_device_monitor
import pygame
from get_direction import handle_direction

def main():
    card_1_found = audio_device_monitor.monitor_card_1()
    
    pygame.init()
    pygame.joystick.init()
    
    joystick_count = pygame.joystick.get_count()
    
    if joystick_count == 0:
        print("No controller connected")
        return
    
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    
    if card_1_found:
        print ("Card 1 has been found.")
        
        while True:
            direction = handle_direction(joystick)
            if direction == "stop":
                return
            elif direction == "start":
                break
    else:
        print("Card 1 was not found.")

if __name__ == '__main__':
    main()