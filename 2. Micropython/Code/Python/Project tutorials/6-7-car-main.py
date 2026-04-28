# Imports go at the top
from microbit import *
import radio

# Car I2C address
i2cAddr = 0x2a

# For wheels
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

# Display image
display.show(Image.HAPPY)
sleep(400)

# Configure the radio
radio.config(group=1)
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    message = radio.receive()
    if message == '1':
        # Turn left at place
        setWheelSpeed(leftwheel, backward, 60)
        setWheelSpeed(rightwheel, forward, 60)  
    elif message == '2':
        # Turn right at place
        setWheelSpeed(leftwheel, forward, 60)
        setWheelSpeed(rightwheel, backward, 60) 
    elif message == '3':
        # Forward
        setWheelSpeed(leftwheel, forward, 70)
        setWheelSpeed(rightwheel, forward, 70) 
        sleep(200)
     

