from ev3dev2.motor import *
from time import sleep

# Initialize the motor connected to port A
motor = Motor(OUTPUT_A)

# Turn on the motor at 50% speed for 2 seconds
motor.on(speed=50)
sleep(2)
motor.off()  # Turn off the motor
