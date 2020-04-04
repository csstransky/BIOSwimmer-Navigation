#!/usr/bin/python3

import time
import socket
import src.send_data as send
import src.bioswimmer as bswim
import simulation.src.midbrain as mbrain
import simulation.src.simulation as simu

bioswimmer = bswim.BIOSwimmer("simulation/data/gps_data.csv", "simulation/data/camera_target.csv")
midbrain = mbrain.MidBrain("simulation/data/animation_points.csv", 
	"simulation/data/animation_compass.csv")
try: 
	while ( not bioswimmer.is_mission_complete() ):
		midbrain.set_next_point()

		print( '<< receiving data' )
		simu.update_bioswimmer_data_from_client(bioswimmer, midbrain)
		bioswimmer.print()
		print('')

		print( '>> sending data' )
		move_byte_stream = simu.send_velocity_data_to_bioswimmer(bioswimmer, midbrain)
		print("Send Bytestream: ", move_byte_stream, "\n")

		print( '<< moving camera' )
		servo_angle = simu.move_servo(bioswimmer)
		print("Servo Angle: ", servo_angle, "\n")

		if send.is_current_gps_coordinate_complete(bioswimmer):
			print("************************************************************")
			print("Completed current coordinate: ", bioswimmer.path_coordinate_tuples[0])
			print("************************************************************")
			del bioswimmer.path_coordinate_tuples[0]
		else:
			print("\n\n")
		print("\n")

		time.sleep(1)

	print("************************************************************")
	print("Mission Complete!")
	print("************************************************************")
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

except KeyboardInterrupt:
	print('interrupted!')
