import socket
import sys
import time

# Assumes Python3 environment

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
		response = client.recv(buffsz).decode('utf-8')
		print( response )

		print( '>> send test message' )
		# client.send("{vNorth: 0.43, vEast: 1.56, depth: 0.56}".encode())
		client.send("{vNorth: 0.43, vEast: 1.56, depth: 0.56, TailAngleEnable:True, TailAngle: 3, SpeedOverrideEnable:True, SpeedOver: 0.2}".encode())
except KeyboardInterrupt:
	client.close()
	print('interrupted!')
	
