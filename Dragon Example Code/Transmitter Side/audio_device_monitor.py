import subprocess
import time

def get_card_1_details():
    try:
        result = subprocess.run(['aplay', '--list-devices'], capture_output=True, text=True, check=True)
        devices = result.stdout
        card_1_details = ""
        capture = False
        for line in devices.split('\n'):
            if "card 1:" in line:
                capture = True
            if capture:
                if line.strip() == "":
                    break
                card_1_details += line + "\n"
        return card_1_details if card_1_details else None
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while listening audio devices: {e}")
        return None

def check_card_1():
    card_1_details = get_card_1_details()
    card_1_found = False
    if card_1_details:
        card_1_found = True
    return card_1_found
    
def monitor_card_1():
    print("Monitoring for USB audio card...")
    card_1_found = False
    try:
        while True:
            card_1_found = check_card_1()
            current_card_1_details = get_card_1_details()
            if current_card_1_details:
                break
            else:
                print("No audio devices found.")
            time.sleep(10)
        return card_1_found
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == '__main__':
    card_1_details = get_card_1_details()
    if card_1_details:
        print("Found Card 1:")
        print(card_1_details)
        card_1_found = True
    else:
        card_1_found = monitor_card_1()
        print("Card 1 not found.")
        monitor_card_1()
