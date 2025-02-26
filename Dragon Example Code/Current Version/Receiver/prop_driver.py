import time
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

class Prop:
    
    def __init__(self, pin):
        pigpio_factory = PiGPIOFactory()
        self.motor = Servo(pin, pin_factory = pigpio_factory)
#         self.motor = Servo(pin)
        
    def forward(self):
        self.motor.max()
        
    def backward(self):
        self.motor.min()
        
    def stop(self):
        self.motor.mid()
        
    def disable(self):
        self.motor.detach()