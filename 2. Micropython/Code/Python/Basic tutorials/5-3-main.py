# micro:bit V2 only
# Imports go at the top
from microbit import *
import neopixel

np = neopixel.NeoPixel(pin8, 2)  # Using pin8, 2 neopixel.

# Code in a 'while True:' loop repeats forever
while True:
    np.fill((255, 0, 0))  # Light all NeoPixels red
    np.show()
    sleep(1000)
    np.fill((0, 255, 0))  # Light all NeoPixels green
    np.show()
    sleep(1000)
    np.fill((0, 0, 255))  # Light all NeoPixels blue
    np.show()
    sleep(1000)
    np.clear()            # Clear NeoPixels

    np[0] = (255, 0, 0)   # A NeoPixel bright red
    np[1] = (0, 255, 0)   # The other NeoPixel is bright green
    np.show()
    sleep(1000)
    np.clear()            # Clear NeoPixels
    
    