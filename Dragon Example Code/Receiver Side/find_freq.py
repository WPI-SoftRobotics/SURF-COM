import pyaudio
import numpy as np
import struct
import time
from target_freqs import north, south, east, west, straight

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000
CHUNK = 1024
DEVICE_INDEX = 1

THRESHOLD = 400
TARGET_FREQS = [north, south, east, west, straight]

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=DEVICE_INDEX)

def get_frequency(data):
    #running through
    fmt = f"{CHUNK * CHANNELS}h"
    data = struct.unpack(fmt, data)
    data = np.array(data, dtype='h')
    
    if CHANNELS == 2:
        data = np.mean(data.reshape(-1, 2), axis=1)
    
    fft_data = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(fft_data))
    peak_freq = np.argmax(np.abs(fft_data))
    
    power_spectrum = np.abs(fft_data)
    
    return abs(freqs[peak_freq] * RATE)

def read_audio_chunk():
    #running
    data = stream.read(CHUNK, exception_on_overflow=False)
    if len(data) == CHUNK * CHANNELS *2:
        return data
    else:
        return None

def close_stream():
    print("close stream")
    stream.stop_stream()
    stream.close()
    p.terminate()
    
def detect_frequencies(frequency, detected_freqs, last_detected_times):
    #running
    current_time = time.time()
    detected = []
    for target in TARGET_FREQS:
        if abs(frequency - target) < THRESHOLD:
            if target not in detected_freqs or (current_time - last_detected_times[target]) > 1.5:
                detected.append(target)
                last_detected_times[target] = current_time
    return detected
    
def record_freqs():
    print("Recording...")
    detected_freqs = []
    last_detected_times = {freq: 0 for freq in TARGET_FREQS}
    try:
        while True:
            data = read_audio_chunk()
            if data:
                frequency = get_frequency(data)
                print("Frequency: {:.2f} Hz".format(frequency))
                detected = detect_frequencies(frequency, detected_freqs, last_detected_times)
                if detected:
                    detected_freqs.extend(detected)
                    print(f"Target frequency detected")  
            else:
                print("Incomplete data chunk received")
                
    except KeyboardInterrupt:
        print(f"Stopped recording")
    return detected_freqs

if __name__ == "__main__":
    print("main started")
    try:
        print("in try loop")
        detected_freqs = record_freqs()
        
    except KeyboardInterrupt:
        print("Stopped recording")
    
    finally:
        close_stream()
        print("Recording finished")
