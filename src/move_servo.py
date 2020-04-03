#!/usr/bin/python
# importing csv module 
import math
#import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
servoPIN = 11
GPIO.setup(servoPIN, GPIO.OUT)
pwm=GPIO.PWM(servoPIN, 50)
pwm.start(0)

def move_raspberry_servo(current_x, current_y, compass_angle, target_x, target_y):

    print("start") 

    dx = current_x-target_x
    dy = current_y-target_y

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
    #GPIO.output(servoPIN,True)
    pwm.ChangeDutyCycle(12.5)
    sleep(0.865*(duty))

    pwm.stop()
    #GPIO.cleanup()
    return angle

def move_servo(bioswimmer):
    cam_target_longitude, cam_target_latitude = bioswimmer.camera_target_tuple
    return move_raspberry_servo(bioswimmer.gps_longitude, bioswimmer.gps_latitude, 
        bioswimmer.compass_direction, cam_target_longitude, cam_target_latitude)
    