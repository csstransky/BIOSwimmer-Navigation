#!/usr/bin/python3

import socket
import src.move_servo as servo
import src.bioswimmer as bswim
import simulation.src.midbrain as mbrain
import simulation.src.network_data as data

bioswimmer = bswim.BIOSwimmer("simulation/data/gps_data.csv", "simulation/data/camera_target.csv")
midbrain = mbrain.MidBrain("simulation/data/animation_points.csv", 
	"simulation/data/animation_compass.csv")
print("START")
try: 
	while ( not bioswimmer.is_mission_complete() ):
		midbrain.set_next_point()
		print(vars(midbrain))

		print( '<< receiving data' )
		data.update_bioswimmer_data_from_client(bioswimmer, midbrain)
		print(vars(bioswimmer), "\n")

		print( '>> sending data' )
		move_byte_stream = data.send_velocity_data_to_bioswimmer(bioswimmer, midbrain)
		print(move_byte_stream, "\n")

		print( '<< moving camera' )
		servo_angle = servo.move_servo(bioswimmer)
		print(servo_angle, "\n")

except KeyboardInterrupt:
	print('interrupted!')