# Imports go at the top
from microbit import *

# Car I2C address
i2cAddr = 0x2a

# For head RGB LED
leftLed  = 0
rightLed = 1
i2cBuf = bytearray([0x00, 0x00])

# Set the head RGB LED function
# led: 0 is the left led and 1 is the right LED.
# r: red brightness value
# g: green brightness value
# b: blue brightness value
def setHeadRgbLed(led, r, g, b):
    if led == leftLed:          
        i2cBuf[0] = 0x07  # red register 
        i2cBuf[1] = r     # red brightness value
        i2c.write(i2cAddr, i2cBuf)
        i2cBuf[0] = 0x08  # green register
        i2cBuf[1] = g     # green brightness value
        i2c.write(i2cAddr, i2cBuf)
        i2cBuf[0] = 0x09  # blue register
        i2cBuf[1] = b     # blue brightness value
        i2c.write(i2cAddr, i2cBuf)
    if led == rightLed:         
        i2cBuf[0] = 0x0a  # red register
        i2cBuf[1] = r     # red brightness value
        i2c.write(i2cAddr, i2cBuf)
        i2cBuf[0] = 0x0b  # green register
        i2cBuf[1] = g     # green brightness value
        i2c.write(i2cAddr, i2cBuf)
        i2cBuf[0] = 0x0c  # blue register
        i2cBuf[1] = b     # blue brightness value
        i2c.write(i2cAddr, i2cBuf)

# Code in a 'while True:' loop repeats forever
while True:
    setHeadRgbLed(leftLed, 255, 0, 0)    # red
    setHeadRgbLed(rightLed, 255, 0, 0)   
    sleep(1000)
    setHeadRgbLed(leftLed, 0, 255, 0)    # green    
    setHeadRgbLed(rightLed, 0, 255, 0)   
    sleep(1000)
    setHeadRgbLed(leftLed, 0, 0, 255)    # blue
    setHeadRgbLed(rightLed, 0, 0, 255)    
    sleep(1000)