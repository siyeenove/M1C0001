# Imports go at the top
from microbit import *
import radio

# Display image
display.show(Image.HAPPY)
sleep(400)

# Configure the radio
radio.config(group=1, power=3)
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    x_strength = accelerometer.get_x()/10
    radio.send('x' + str(x_strength))
    sleep(50)
    y_strength = accelerometer.get_y()/10
    radio.send('y' + str(y_strength))
    sleep(50)

