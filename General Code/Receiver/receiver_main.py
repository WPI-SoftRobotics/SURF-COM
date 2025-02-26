# Updated by Soft Robotics Lab
# 2/25/2025

# IMPORTS
# Libraries
import pyaudio
import numpy as np
import struct
import time

# Reference other files
from target_freqs import first, second, third, fourth, fifth


# SETUP
# Create map of frequencies to names
direction_map = {
    first: "First",
    second: "Second",
    third: "Third",
    fourth: "Fourth",
    fifth: "Fifth",
}

# Microphone settings (may change with different devices)
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000
CHUNK = 1024
DEVICE_INDEX = 1

# Setup Microphone
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=DEVICE_INDEX)

# Global variables
THRESHOLD = 400 # error threshold for recognizing a tone in Hz, accounts for doppler and distortions
TARGET_FREQS = [first, second, third, fourth, fifth]



# FUNCTIONS    
# Function: main() is the main loop of the program
# Inputs: none
# Outputs: none
def main():
    # Initialize constants
    # For noise filtering
    heard = 8 # How many time a tone needs to be heard in a row before action is taken
    reset_timeout = 3 # How often (in seconds) previous_action resets. Allows same input twice in a row, but should prevent triggering action twice from the same input
    previous_action = None # Stores most recent action
    detection_counts = {freq: 0 for freq in direction_map.keys()}
    start_time = time.time()
    
    print("Listening...")
    time.sleep(1)
    
    # Main Loop
    try:
        while True:
            # Periodic filter reset
            current_time = time.time()
            if previous_action and current_time >= reset_timeout + start_time:
                start_time = current_time
                previous_action = None

            # Read Microphone
            data = read_audio_chunk()
            
            # Check connection
            if not data:
                print("No microphone data received")

            # Signal detected
            if data:
                # Process signal
                frequency = get_frequency(data) # extract peak frequency
                print(f"Frequency detected: {frequency} Hz")
                detected = detect_frequencies(frequency) # list all targets within margin of error from peak frequency

                # Target frequency detected
                if detected:
                    # Clear all counts from other targets (filtering)
                    for target in detection_counts:
                        if target != detected:
                            detection_counts[target] = 0

                    detection_counts[detected] += 1 # Increase count on detected target

                    # Confidently heard target tone
                    if detection_counts[detected] >= heard:
                        # Ensures not triggering an action multiple times from one input
                        if detected != previous_action:
                            # Perform action
                            if detected == first:
                                print("Do something 1")
                            elif detected == second:
                                print("Do something 2")
                            elif detected == third:
                                print("Do something 3")
                            elif detected == fourth:
                                print("Do something 4")
                            elif detected == fifth:
                                print("Do something 5")
                                
                            # Post-action filter reset
                            previous_action = detected
                            detection_counts = {freq: 0 for freq in direction_map.keys()}

                
    # Handles turn off and clean up                                
    except KeyboardInterrupt:
        print("Stopped recording...")
    finally:
        close_stream()
        print("Stopped listening.")


# Function: read_audio_chunk() records a chunk of audio from a microphone
# Inputs: none
# Outputs: a list of sound bytes (if microphone is working)
def read_audio_chunk():
    #running
    data = stream.read(CHUNK, exception_on_overflow=False)
    if len(data) == CHUNK * CHANNELS *2:
        return data
    else:
        return None

# Function: get_frequency() extracts the peak frequency from an audio chunk using fast forier transforms
# Inputs: a list of sound bytes from read_audio_chunk()
# Outputs: a freqency in Hz
def get_frequency(data):
    fmt = f"{CHUNK * CHANNELS}h"
    data = struct.unpack(fmt, data)
    data = np.array(data, dtype='h')
    
    if CHANNELS == 2:
        data = np.mean(data.reshape(-1, 2), axis=1)
    
    fft_data = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(fft_data))
    peak_freq = np.argmax(np.abs(fft_data))
    
    return abs(freqs[peak_freq] * RATE)

# Function: detect_frequencies() compares a given frequency to all target frequencies with a margin of error to find the best match (if there is one)
# Input: float frequency, list of ints
# Output: int of matching target frequency within the margin of error
def detect_frequencies(frequency):
    closest_target = None
    closest_diff = None
    for target in TARGET_FREQS:
        diff = abs(frequency - target)
        if  diff < THRESHOLD:
            if (not closest_target) or closest_diff > diff:
                closest_target = target
                closest_diff = diff
    return closest_target

# Function: close_stream() shuts down the receiver and cleans up
# Inputs: none
# Outputs: none
def close_stream():
    print("close stream")
    stream.stop_stream()
    stream.close()
    p.terminate()


    

# START    
if __name__ == '__main__':
    main()