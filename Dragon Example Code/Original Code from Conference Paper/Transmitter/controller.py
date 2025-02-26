import pygame

pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print("No joystick connected.")

else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    
    print(f"Joystick name: {joystick.get_name()}")
    print(f"Number of axes: {joystick.get_numaxes()}")
    print(f"Number of buttons: {joystick.get_numbuttons()}")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")
                
            if event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} released")
                
                
            x_axis = joystick.get_axis(0)
            y_axis = joystick.get_axis(1)
            
            if x_axis < -0.5:
                print("D-pad left")
            elif x_axis > 0.5:
                print("D-pad right")
                
            if y_axis < -0.5:
                print("D-pad up")
            elif y_axis > 0.5:
                print("D-pad down")
            
            if event.type == pygame.QUIT:
                running = False

pygame.quit()