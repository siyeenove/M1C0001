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
    if button_a.was_pressed():
        radio.send('1')
        
    if button_b.was_pressed():
        radio.send('2')
     
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send('3')

