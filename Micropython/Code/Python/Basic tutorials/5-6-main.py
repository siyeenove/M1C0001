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
    # CW
    setWheelSpeed(leftwheel, backward, 100)
    setWheelSpeed(rightwheel, forward, 100)
    sleep(1000)
    # stop
    setWheelSpeed(leftwheel, backward, 0)
    setWheelSpeed(rightwheel, forward, 0)
    sleep(1000)
    # CCW
    setWheelSpeed(leftwheel, forward, 100)
    setWheelSpeed(rightwheel, backward, 100)
    sleep(1000)
    # stop
    setWheelSpeed(leftwheel, forward, 0)
    setWheelSpeed(rightwheel, backward, 0)
    sleep(1000)

    

    