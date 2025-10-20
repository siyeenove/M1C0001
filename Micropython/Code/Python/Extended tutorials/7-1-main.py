# Imports go at the top
from microbit import *

# Car I2C address
i2cAddr = 0x2a
i2cBuf = bytearray([0x00, 0x00])

# Servo type
servo90  = 0
servo180 = 1
servo270 = 2
servo360 = 3
pinS1 = 0
pinS2 = 1
pinS3 = 2 
    
# Set the Angle function of 90, 180 and 270 servo.
# index: 0 = S1 pin, 1 = S2 pin, 2 = S3 pin
# servoType: 0 = 90 servo, 1 = 180 servo, 2 = 270 servo
# angle: 90 servo -> 0-90, 180 servo -> 0-180, 270 servo -> 0-270
def setServo(index, servoType, angle):
    angleMap = 0
    if servoType == servo90:
        # Map 0-90 to 50-200
        angleMap = scale(angle, from_=(0, 90), to=(50, 200))
    if servoType == servo180:
        # Map 0-180 to 50-200
        angleMap = scale(angle, from_=(0, 180), to=(50, 200))
    if servoType == servo270:
        # Map 0-270 to 50-200
        angleMap = scale(angle, from_=(0, 270), to=(50, 200))
        
    if index == pinS1:
        i2cBuf[0] = 0x0d  # S1 pin
    if index == pinS2:
        i2cBuf[0] = 0x0e  # S2 pin
    if index == pinS3:
        i2cBuf[0] = 0x0f  # S3 pin

    i2cBuf[1] = angleMap
    i2c.write(i2cAddr, i2cBuf)

# Set the speed of 360 servo
# index: 0 = S1 pin, 1 = S2 pin, 2 = S3 pin
# speed: -100 to +100
def setServo360(index, speed):
    # Map -100 - 100 to 0 - 180
    angle = scale(speed, from_=(-100, 100), to=(0, 180))
    setServo(index, servo180, angle)
    
# Code in a 'while True:' loop repeats forever
while True:
    # The 180 degree servo of the S1 pin turns to the 0 degree position
    setServo(pinS1, servo180, 0)  
    # The 360-degree servo of the S3 pin turns forward at the maximum speed
    setServo360(pinS3, 100)        
    sleep(1000)
    # The 180 degree servo of the S1 pin turns to the 180 degree position
    setServo(pinS1, servo180, 180) 
    # The 360-degree servo of the S3 pin turns backward at the maximum speed
    setServo360(pinS3, -100)       
    sleep(1000)





