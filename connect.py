import socket
import sys
import time

# Assumes Python3 environment

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
fbrain = "10.221.22.2"
buffsz = 2048

client.connect((fbrain, 55557))
client.setblocking(0)

while ( True ):
	print( '<< receiving data' )
	try:
		response = client.recv(buffsz).decode('utf-8')
		print( response )

		print( '>> send test message' )
		client.send("{vNorth: 0.43, vEast: 1.56, depth: 0.56}".encode())
	except BlockingIOError:
		pass


	