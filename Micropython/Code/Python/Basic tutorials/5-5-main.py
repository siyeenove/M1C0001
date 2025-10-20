# Imports go at the top
from microbit import *
import utime

# Define the pins of the ultrasonic module.
TRIG_PIN = pin13
ECHO_PIN = pin12

# Initialize the ultrasonic module
def setup_ultrasonic():
    TRIG_PIN.write_digital(0)
    ECHO_PIN.set_pull(ECHO_PIN.NO_PULL)

# Measuring distance (cm)
def measure_distance():
    # A trigger signal of 10μs was sent
    TRIG_PIN.write_digital(1)
    utime.sleep_us(10)
    TRIG_PIN.write_digital(0)
    
    # Wait for the echo pin to get high
    timeout = 50000   # 50ms timeout
    start_time = utime.ticks_us()
    while ECHO_PIN.read_digital() == 0:
        if utime.ticks_diff(utime.ticks_us(), start_time) > timeout:
            return -1  # timeout
    
    # The echo onset time was recorded
    pulse_start = utime.ticks_us()
    
    # Wait for the echo pin to get low
    while ECHO_PIN.read_digital() == 1:
        if utime.ticks_diff(utime.ticks_us(), pulse_start) > timeout:
            return -1  # timeout
    
    # The echo end time was recorded
    pulse_end = utime.ticks_us()
    
    # Calculate the pulse duration
    pulse_duration = utime.ticks_diff(pulse_end, pulse_start)
    
    # Calculating distance（The Speed of Sound 
    # 340m/s = 0.034cm/μs，Round trip, so divided by 2）
    distance = (pulse_duration * 0.034) / 2
    
    return distance

setup_ultrasonic()

# Code in a 'while True:' loop repeats forever
while True:  
    # measuring distance
    dist = measure_distance()
    
    if dist == -1:    # Measurement timeout
        display.show(Image.NO)
    elif dist > 200:  # Greater than the maximum measurement range
        display.show(Image.ASLEEP)
    else:
        display.scroll(str(int(dist)))   # Displaying distance values
            
    sleep(1000)

    