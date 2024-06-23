import time

def traffic_light_simulator():
    states = ["Red", "Green", "Yellow"]
    current_state = 0

    while True:
        print(f"Traffic Light State: {states[current_state]}")
        if states[current_state] == "Red":
            time.sleep(5)  # Red light for 5 seconds
        elif states[current_state] == "Green":
            time.sleep(4)  # Green light for 4 seconds
        elif states[current_state] == "Yellow":
            time.sleep(2)  # Yellow light for 2 seconds
        
        current_state = (current_state + 1) % len(states)

if __name__ == "__main__":
    traffic_light_simulator()
