import pygame

def sound_player(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
 
def main():
    sound_file = '/home/nat/modem_speaker/direction_sound_files/miracle.wav'
    sound_player(sound_file)
    
if __name__ == "__main__":
    main()