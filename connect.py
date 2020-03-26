import socket
import sys
import time
import read_data as read
import send_data as send
import bioswimmer as bioswimmer

# Assumes Python3 environment

bioswimmer = bioswimmer.BIOSwimmer()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
fbrain = "10.221.22.2"
buffsz = 2048

client.connect((fbrain, 55557))

# 1. Connect the Raspberry Pi to the fish across WM-003
# 2. Connect the laptop to the fish across WM-003
# 3. Open the OCU (C:/program_files(x86)/AUV/BIOSwimmerOCU.exe) on the laptop
# 4. In the OCU, zero out the fins and tails
# 5. Click on the "Manual Mode" tab, then press the "Manual Mode Enable" once
# 6. In the top right, it should switch from "Setup" to "Operate (PDO)"
# 7. Now run the Python script to move and read the fish

try: 
	while ( True ):
		print( '<< receiving data' )
		read.update_bioswimmer_data_from_client(bioswimmer, client)
		print(vars(bioswimmer), "\n")

		print( '>> sending data' )
		move_byte_stream = send.get_bioswimmer_velocity_byte_stream(bioswimmer)
		print(move_byte_stream, "\n")
		client.send(move_byte_stream)

		print( '>> moving camera' )
		# TODO: add move servo here
except KeyboardInterrupt:
	client.close()
	print('interrupted!')
	
