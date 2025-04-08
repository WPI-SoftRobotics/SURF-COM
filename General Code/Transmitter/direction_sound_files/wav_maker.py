import numpy as np
import wave

def generate_tone(frequency, duration, sample_rate=44100, amplitude=32767):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    audio = amplitude * np.sin(2 * np.pi * frequency * t)
    return audio.astype(np.int16)

def generate_silence(duration, sample_rate=44100):
    return np.zeros(int(sample_rate * duration), dtype=np.int16)

def create_wav_file(filename, sample_rate=44100):
    # Generate tone for 1 second
    tone1 = generate_tone(10300, 1, sample_rate)


    # Concatenate the tones and silence
    audio_data = np.concatenate([tone1])

    # Write to .wav file
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

# Create the .wav file
create_wav_file('C:/Users/localmgr/Documents/GitHub/DRAGON/Acoustic Control/Code for General Case/Transmitter/direction_sound_files/seventh.wav')