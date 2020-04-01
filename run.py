import socket
import sys
import time
import read_data as read
import send_data as send
import move_servo as servo
import bioswimmer as bswim

# Assumes Python3 environment

bioswimmer = bswim.BIOSwimmer("gps_data.csv", "camera_target.csv")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Static IP to the BIOSwimmer's wifi buoy
fbrain = "10.221.22.2"
# Special port to allow for data to be sent and received by the BIOSwimmer
port = 55557

client.connect((fbrain, port))

# 1. Connect the Raspberry Pi to the fish across WM-003
# 2. Connect the laptop to the fish across WM-003
# 3. Open the OCU (C:/program_files(x86)/AUV/BIOSwimmerOCU.exe) on the laptop
# 4. In the OCU, zero out the fins and tails
# 5. Click on the "Manual Mode" tab, then press the "Manual Mode Enable" once
# 6. In the top right, it should switch from "Setup" to "Operate (PDO)"
# 7. Now run the Python script to move and read the fish

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
	
