import socket
import sys
import time

# Assumes Python3 environment

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
fbrain = "10.221.22.2"
buffsz = 2048

client.connect((fbrain, 55557))

while ( True ):
	print( '<< receiving data' )
	response = client.recv(buffsz).decode('utf-8')
	print( response )

	print( '>> send test message' )
	client.send("{vNorth: 0.43, vEast: 1.56, depth: 0.56}".encode())
	# client.send("{vNorth: 0.43, vEast: 1.56, depth: 0.56, TailAngleEnable:True, TailAngle: 3, SpeedOverrideEnable:True, SpeedOver: 0.1}".encode())

	