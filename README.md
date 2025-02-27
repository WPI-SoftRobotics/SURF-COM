# SURF-COM
SURF-COM (Simple Underwater Robotic Framework for Communication), an open-source acoustic controller for underwater robots.


# GENERAL CASE CODE
## Receiver
This code is designed to run on the Raspberry Pi Zero, though may be able to run on other Raspberry Pi computers with little to no modification.


### Libraries
First, install all relavent libraries for your application (see Startup Guide, then Library Guide).


### Adapting the Code
Line 12 (target_freqs): rename or add target tones (changes must be reflected in target_freqs file where targets are initialized, line 17 (direction_map), line 43 (TARGET_FREQS), and lines 100-109

Line 42 (THRESHOLD): maximum frequency difference from target (in Hz) that will be recognized as the target, decreasing this number allows you to use target frequencies that are closer together at the potential cost of accuracy

Line 54 (heard): how many times the receiver needs to hear a tone in a row to trigger, decreasing this number will make the receiver more sensitive

Line 55 (reset_timeout): how many seconds before the same action can be triggered twice in a row

Line 100-109: This is where you put the actions your receiver will perform when it hears a target frequency.

Change your copy of the code however you see fit, these are only suggestions!


### Use
Upload this code to your Raspberry Pi Zero. If you are running in headless mode and/or controlling actuators directly from the Pi, see Setup Guide.

Plug in a USB microphone to the Pi and power on your system. Running this script will cause the Pi to wait until it hears a target tone, then perform the specified action associated with that tone. There is a delay after each action in which the same action cannot be performed again.

The system may take up to five minutes to boot up upon powering on, so an indicator LED is recommended.


## Transmitter
Instead of using the transmitter code described in the conference paper (which can be found in the Dragon Example), we recommend plugging a phone or computer into a waterproof speaker with an amplifier and running a waveform generator application to generate the desired target tone.



# DRAGON EXAMPLE
## Current Receiver
A slightly modified version of the general code which drives a BLDC motor and a Servo, and has an LED indicator light.

## Current Transmitter
Can be run on a Raspberry Pi 3 or comparable, takes a simple USB video game controller as input, and outputs a constant tone through any speaker hooked up to the audio jack. Additional instructions for replication are included in this folder.
