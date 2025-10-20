# Imports go at the top
from microbit import *

channel1 = 0   # left   = P14
channel2 = 0   # centre = P15
channel3 = 0   # right  = P16

pin14.set_pull(pin14.PULL_UP)
pin15.set_pull(pin15.PULL_UP)
pin16.set_pull(pin16.PULL_UP)

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
    
    if value == 0b111:
        display.show(Image.NO)
    if value == 0b000:
        display.show(Image.YES)
    sleep(250)

    
    

