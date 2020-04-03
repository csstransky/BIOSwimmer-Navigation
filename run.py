#!/usr/bin/python3

import socket
import src.read_data as read
import src.send_data as send
import src.move_servo as servo
import src.bioswimmer as bswim

bioswimmer = bswim.BIOSwimmer("data/gps_data.csv", "data/camera_target.csv")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Static IP to the BIOSwimmer's wifi buoy
fbrain = "10.221.22.2"
# Special port to allow for BIOSwimmer data to be sent and received
port = 55557
client.connect((fbrain, port))
try: 
	while ( not bioswimmer.is_mission_complete ):
		print( '<< receiving data' )
		read.update_bioswimmer_data_from_client(bioswimmer, client)
		print(vars(bioswimmer), "\n")

		print( '>> sending data' )
		move_byte_stream = send.send_velocity_data_to_bioswimmer(bioswimmer, client)
		print(move_byte_stream, "\n")

		print( '<< moving camera' )
		servo_angle = servo.move_servo(bioswimmer)
		print(servo_angle, "\n")

except KeyboardInterrupt:
	client.close()
	print('interrupted!')