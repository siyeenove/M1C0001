# Imports go at the top
from microbit import *
import utime
import random

# Car I2C address
i2cAddr = 0x2a

# For wheels
leftwheel  = 0
rightwheel = 1
backward = 0
forward  = 1
i2cBuf = bytearray([0x00, 0x00])

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

# Set the wheel speed function
# wheel: 0 = left wheel, 1 = right wheel
# direction: 0 = backward, 1 = forward
# speed: 0--100
def setWheelSpeed(wheel, direction, speed):
    # Important! The speed is between 0 and 100.
    if speed > 100:      
        speed = 100
    elif speed < 0:
        speed = 0

    if wheel == leftwheel:          
        i2cBuf[0] = 0x05  # left wheel register 
        if direction == forward:
            # speed value, 101 is the default required data.
            i2cBuf[1] = speed + 101     
        elif direction == backward:
            i2cBuf[1] = speed
        i2c.write(i2cAddr, i2cBuf)

    if wheel == rightwheel:         
        i2cBuf[0] = 0x06  # right wheel register
        if direction == forward:
            i2cBuf[1] = speed     
        elif direction == backward:
            # speed value, 101 is the default required data.
            i2cBuf[1] = speed + 101
        i2c.write(i2cAddr, i2cBuf)

setup_ultrasonic()
display.show(Image.HAPPY)
sleep(400)

# Code in a 'while True:' loop repeats forever
while True:
    # measuring distance
    dist = measure_distance()  
    sleep(200) # Necessary delay

    if dist < 15:
        # Stop
        setWheelSpeed(leftwheel, forward, 0)
        setWheelSpeed(rightwheel, forward, 0)
        
        if random.randint(0, 1) == 0:
            # Turn left
            setWheelSpeed(leftwheel, backward, 50)
            setWheelSpeed(rightwheel, forward, 50)
        else:
            # Turn right
            setWheelSpeed(leftwheel, forward, 50)
            setWheelSpeed(rightwheel, backward, 50)
        sleep(200)
        
    else:
        # Forward
        setWheelSpeed(leftwheel, forward, 70)
        setWheelSpeed(rightwheel, forward, 70)      
     

