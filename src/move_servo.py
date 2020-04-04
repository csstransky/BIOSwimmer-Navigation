#!/usr/bin/python

import math
# TODO: Put this back later
# import RPi.GPIO as GPIO
# from time import sleep
# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
# servoPIN = 11
# GPIO.setup(servoPIN, GPIO.OUT)
# pwm=GPIO.PWM(servoPIN, 50)
# pwm.start(0)

def get_servo_angle(current_x, current_y, compass_angle, target_x, target_y):
    dx = current_x - target_x + 0.000001
    dy = current_y - target_y + 0.000001

    distance = math.sqrt((dx * dx) + (dy * dy))
    ang = math.atan(dx / dy) / math.pi * 180

    if dx == 0:
        ang = 0
    elif dx < 0 and dy < 0:
        ang = -180 + ang
    elif dx < 0 and dy >  0: 
        ang = 180 - ang
    else: 
        ang = ang

    moveAng = ang - compass_angle
    if moveAng < 0:
        moveAng = 360 + moveAng
    else:
        moveAng = moveAng

    return moveAng

def move_raspberry_servo(current_x, current_y, compass_angle, target_x, target_y):

    angle = get_servo_angle(current_x, current_y, compass_angle, target_x, target_y)
    # TODO: Put this back later
    # duty = float(angle/180)
    # GPIO.output(servoPIN,True)
    # pwm.ChangeDutyCycle(12.5)
    # sleep(0.865*(duty))

    # pwm.stop()
    # GPIO.cleanup()
    return angle

def move_servo(bioswimmer):
    cam_target_longitude, cam_target_latitude = bioswimmer.camera_target_tuple
    return move_raspberry_servo(bioswimmer.gps_longitude, bioswimmer.gps_latitude, 
        bioswimmer.compass_direction, cam_target_longitude, cam_target_latitude)
    