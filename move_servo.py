#!/usr/bin/python
# importing csv module 
import math
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
servoPIN = 11
GPIO.setup(servoPIN, GPIO.OUT)
pwm=GPIO.PWM(servoPIN, 50)
pwm.start(0)

def move_raspberry_servo(current_x, current_y, compass_angle, destination_x, destination_y):

    print("start") 

    dx = current_x-destination_x
    dy = current_y-destination_y

    distance = math.sqrt((dx*dx)+(dy*dy))
    print (dx)
    print (dy)
    print (distance)
    ang = math.atan(dx/dy)/(math.pi)*180
    print (ang)

    if dx == 0:
        ang = 0
    elif dx < 0 and dy< 0:
        ang =-180+ang
    elif dx < 0 and dy >  0: 
        ang = 180-ang
    else: 
        ang = ang
    print (ang)

    moveAng = ang - compass_angle
    print (moveAng)
    if moveAng <0:
        moveAng = 360 + moveAng
    else:
        moveAng = moveAng
    print (moveAng)
    angle = float (moveAng)
    duty = float(angle/180)
    print (duty)
    GPIO.output(servoPIN,True)
    pwm.ChangeDutyCycle(12.5)
    sleep(0.865*(duty))

    pwm.stop()
    GPIO.cleanup()

def move_servo(bioswimmer):
    destination_latitude, destination_longitude, _ = bioswimmer.destination_coordinates[0]
    move_raspberry_servo(bioswimmer.gps_longitude, 
        bioswimmer.gps_latitude, 
        bioswimmer.compass_direction, 
        destination_longitude, 
        destination_latitude)
    