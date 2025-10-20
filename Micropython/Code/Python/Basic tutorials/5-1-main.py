# Imports go at the top
from microbit import *

# Car I2C address
i2cAddr = 0x2a

# Type of battery
aaBattery = bytearray([0x01])
lithiumBattery = bytearray([0x02])

# Initialize the I2C communication interface
i2c.init()


# Code in a 'while True:' loop repeats forever
while True:
    # Read the battery power level
    i2c.write(i2cAddr, aaBattery, True)
    batLevel = i2c.read(i2cAddr, 1)
    
    sleep(1000)                  # Delay: 1000 milliseconds
    display.scroll(batLevel[0])  # Scroll display of battery level
    sleep(3000)                  # Delay: 3000 milliseconds