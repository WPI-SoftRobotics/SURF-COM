import prop_driver
import tail_driver
from gpiozero import LED
from find_freq import record_freqs, close_stream, read_audio_chunk, get_frequency, detect_frequencies
import collections
import time
from target_freqs import north, south, east, west, straight


# Initialize pins based on GPIO Tag
tail = tail_driver.Tail(12)
prop = prop_driver.Prop(13)
led = LED(27)

# Arm ESC
prop.stop()
led.blink()
time.sleep(10)
    
# Map directions
direction_map = {
    north: "North",
    south: "South",
    east: "East",
    west: "West",
    straight: "Straight",
}

    
# Main Function
def run(heard=8, reset_timeout=3):
    # Initialize constants
    tail_pos = 0 # -1 is left, 1 is right, 0 is straight
    
    # Start listening
    detected_freqs = []
    last_detected_times = {freq: 0 for freq in direction_map.keys()}
    detection_counts = {freq: 0 for freq in direction_map.keys()}
    detected_direction = None
    last_detection_time = None
    print("Listening...")
    
    # Main Loop
    try:
        while True:
            # Read Microphone
            data = read_audio_chunk()
            
            # Check connection
            if not data:
                print("No data received from audio chunk")
            else:
                #print(".")
                pass
            
            # Reset direction after a while
            current_time = time.time()
            if detected_direction and current_time - last_detection_time > reset_timeout:
                detected_direction = None
            
            # Target Frequencies Detected
            if data:
                frequency = get_frequency(data)
                print(f"Frequency detected: {frequency} Hz")
                detected = detect_frequencies(frequency, detected_freqs, last_detected_times)
                for target in detected:
                    detection_counts[target] += 1
                    if detection_counts[target] >= heard:
                        if detected_direction != direction_map[target]:
                            print(f"Direction: {direction_map[target]}")
                            detected_direction = direction_map[target]
                            last_detection_time = current_time
                            
                            # perform requested action
                            if detected_direction == direction_map[north]:
                                prop.forward()
                            elif detected_direction == direction_map[south]:
                                prop.backward()
                            elif detected_direction == direction_map[west]:
                                if tail_pos == 1:
                                    tail.straight()
                                    tail_pos = 0
                                else:
                                    tail.steerLeft()
                                    tail_pos = -1
                                time.sleep(0.5)
                            elif detected_direction == direction_map[east]:
                                if tail_pos == -1:
                                    tail.straight()
                                    tail_pos = 0
                                else:
                                    tail.steerRight()
                                    tail_pos = 1
                                time.sleep(0.5)
                            elif detected_direction == direction_map[straight]:
                                tail.straight()
                                prop.stop()
                                
                        detection_counts = {freq: 0 for freq in direction_map.keys()}
                        detected_freqs.clear()
                        break
                                    
                    
    except KeyboardInterrupt:
        print("Stopped recording...")
    finally:
        close_stream()
        print("Stopped listening.")
    
    
if __name__ == '__main__':
    run()