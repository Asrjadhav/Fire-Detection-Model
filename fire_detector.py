import time
import random

# Simulate sensor readings
def read_temperature():
    # Replace with actual sensor reading code
    return random.uniform(20.0, 40.0)  # Simulated temperature in Celsius

def read_smoke_level():
    # Replace with actual sensor reading code
    return random.uniform(0.0, 400.0)  # Simulated smoke level (ppm)

def check_fire(temperature, smoke_level):
    # Define thresholds for temperature and smoke level
    TEMPERATURE_THRESHOLD = 50.0  # Threshold temperature in Celsius
    SMOKE_THRESHOLD = 300.0       # Threshold smoke level (ppm)
    
    if temperature > TEMPERATURE_THRESHOLD or smoke_level > SMOKE_THRESHOLD:
        return True
    return False

def main():
    while True:
        temperature = read_temperature()
        smoke_level = read_smoke_level()
        
        print(f"Temperature: {temperature:.2f} °C")
        print(f"Smoke Level: {smoke_level:.2f} ppm")
        
        if check_fire(temperature, smoke_level):
            print("Fire detected! Activating alarm.")
        else:
            print("No fire detected.")
        
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()
