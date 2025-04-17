"""
Created by Ihor Chernyshev
Created on March 2025
This program controls servo through a distance sensor
"""

import time
import board
import adafruit_hcsr04
import pwmio
from adafruit_motor import servo

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP5, echo_pin=board.GP6)
pwm = pwmio.PWMOut(board.A0, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo
my_servo = servo.Servo(pwm)

while True:
    try:
        sonar_dist = sonar.distance
    except RuntimeError:
        print("Retrying!")
    else:
        if sonar_dist >= 50:
            my_servo.angle = 180
            time.sleep(1)
        else:
             my_servo.angle = 0
             time.sleep(1)
    time.sleep(0.1)
