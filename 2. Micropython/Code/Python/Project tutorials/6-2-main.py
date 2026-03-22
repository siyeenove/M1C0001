# Imports go at the top
from microbit import *

# Car I2C address
i2cAddr = 0x2a

# For wheel
leftwheel  = 0
rightwheel = 1
backward = 0
forward  = 1
i2cBuf = bytearray([0x00, 0x00])

# For line Tracking Sensor
channel1 = 0   # left   = P14
channel2 = 0   # centre = P15
channel3 = 0   # right  = P16
pin14.set_pull(pin14.PULL_UP)
pin15.set_pull(pin15.PULL_UP)
pin16.set_pull(pin16.PULL_UP)

display.show(Image.HAPPY)
sleep(400)

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

# Code in a 'while True:' loop repeats forever
while True:
    # Read the values of three sensors, 0 or 1.
    # 0: Black is detected.
    # 1: White is detected.
    channel1 = pin14.read_digital()
    channel2 = pin15.read_digital()
    channel3 = pin16.read_digital()
    
    # Convert the values of the three sensors into one data.
    # Binary data notation:
    # 0b bit2 bit1 bit0
    # channel1 = bit2, chanel2 = bit1, chanel3 = bit0.
    value = (channel1 << 2) + (channel2 << 1) + channel3

    if value == 0b100:  # Slow right turn
        setWheelSpeed(leftwheel, forward, 25)
        setWheelSpeed(rightwheel, forward, 0)
    
    if value == 0b001:  # Slow left turn
        setWheelSpeed(leftwheel, forward, 0)
        setWheelSpeed(rightwheel, forward, 25)

    if value == 0b110:  # Quick right turn
        setWheelSpeed(leftwheel, forward, 40)
        setWheelSpeed(rightwheel, forward, 0)
    
    if value == 0b011:  # Quick left turn
        setWheelSpeed(leftwheel, forward, 0)
        setWheelSpeed(rightwheel, forward, 40)

    if value == 0b101 or value == 0b000:   # Forward
        setWheelSpeed(leftwheel, forward, 20)
        setWheelSpeed(rightwheel, forward, 20)

    if value == 0b111:  # Stop
        setWheelSpeed(leftwheel, forward, 0)
        setWheelSpeed(rightwheel, forward, 0)

