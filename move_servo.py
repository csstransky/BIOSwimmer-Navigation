#!/usr/bin/python
# importing csv module 
import csv 
import math
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
servoPIN = 11
GPIO.setup(servoPIN, GPIO.OUT)
pwm=GPIO.PWM(servoPIN, 50)
pwm.start(0)

def read_files():
    # initializing the titles and rows list 
    fields = []  
    rows = []
    # reading csv file 
    with open('/home/pi/shared/bioswimmer_file.txt', "r") as csv_file: 
    # creating a csv reader object 
        csv_reader = csv.reader(csv_file) 
        
    # extracting field names through first row 
        fields = csv_reader.next() 
    
    # extracting each data row one by one 
        for row in csv_reader: 
            rows.append(row) 


        current_x = float (fields[0])
        current_y = float (fields[1])
        compass_angle = float (fields[2])
        destination_x = float (fields[3])
        destination_y = float (fields[4])

def move_servo(current_x, current_y, compass_angle, destination_x, destination_y):

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
