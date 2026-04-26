# Imports go at the top
from microbit import *

# Car I2C address
i2cAddr = 0x2a

# Type of battery
aaBattery = bytearray([0x01])

# For wheel
leftwheel  = 0
rightwheel = 1
backward = 0
forward  = 1
i2cBuf = bytearray([0x00, 0x00])
speed = 0

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
    # Read the battery power level
    i2c.write(i2cAddr, aaBattery, True)
    batLevel = i2c.read(i2cAddr, 1)[0]

    # Set the wheel speed
    if 70 <= batLevel:
        speed =50
    elif 60 <= batLevel < 70:
        speed =65
    elif 50 <= batLevel < 60:
        speed =80
    else:
        speed =95

    # CW
    setWheelSpeed(leftwheel, backward, speed)
    setWheelSpeed(rightwheel, forward, speed)
    sleep(1000)
    # stop
    setWheelSpeed(leftwheel, backward, 0)
    setWheelSpeed(rightwheel, forward, 0)
    sleep(1000)
    # CCW
    setWheelSpeed(leftwheel, forward, speed)
    setWheelSpeed(rightwheel, backward, speed)
    sleep(1000)
    # stop
    setWheelSpeed(leftwheel, forward, 0)
    setWheelSpeed(rightwheel, backward, 0)
    sleep(1000)

    

    