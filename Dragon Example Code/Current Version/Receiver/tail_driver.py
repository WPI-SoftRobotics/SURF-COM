import time
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory


class Tail:
    
    def __init__(self, pin):
        pigpio_factory = PiGPIOFactory()
        self.servo = Servo(pin, pin_factory = pigpio_factory)
#         self.servo = Servo(pin)
        
    def steerRight(self):
        self.servo.min()
        
    def steerLeft(self):
        self.servo.max()
        
    def straight(self):
        self.servo.mid()
        
    def disable(self):
        self.servo.detach()
        
