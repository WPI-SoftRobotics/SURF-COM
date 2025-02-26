# SURF-COM
SURF-COM (Simple Underwater Robotic Framework for Communication), an open-source acoustic controller for underwater robots.


**GENERAL CASE CODE**
**Receiver**
This code is designed to run on the Raspberry Pi Zero, though may be able to run on other Raspberry Pi computers with little to no modification.


_Libraries_
First, install all relavent libraries for your application (see Library Guide).


_Adapting the Code_
Line 12 (target_freqs): rename or add target tones (changes must be reflected in target_freqs file where targets are initialized, line 17 (direction_map), line 43 (TARGET_FREQS), and lines 100-109

Line 42 (THRESHOLD): maximum frequency difference from target (in Hz) that will be recognized as the target, decreasing this number allows you to use target frequencies that are closer together at the potential cost of accuracy

Line 54 (heard): how many times the receiver needs to hear a tone in a row to trigger, decreasing this number will make the receiver more sensitive

Line 55 (reset_timeout): how many seconds before the same action can be triggered twice in a row

Line 100-109: This is where you put the actions your receiver will perform when it hears a target frequency.

Change your copy of the code however you see fit, these are only suggestions!


_Use_
Upload this code to your Raspberry Pi Zero. If you are running in headless mode and/or controlling actuators directly from the Pi, see Setup Guide.

Plug in a USB microphone to the Pi and power on your system. Running this script will cause the Pi to wait until it hears a target tone, then perform the specified action associated with that tone. There is a delay after each action in which the same action cannot be performed again.


**Transmitter**
