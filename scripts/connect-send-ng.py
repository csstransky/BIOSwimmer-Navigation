import socket
import sys
import time

# Assumes Python3 environment

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
heartb = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
fbrain = "10.221.22.2"
buffsz = 2048

# heartb.connect((fbrain, 55567))

# i = 0
# heartb_wait = 10
# while ( i < heartb_wait ):
# 	# send heartbeats for a time before recv'ing data
# 	print( '>> sending heartbeat' )
# 	heartb.send("{H}".encode())
# 	i+=1
# 	time.sleep(1)

client.connect((fbrain, 55557))

while ( True ):
	# print( '<< receiving data' )
	# response = client.recv(buffsz).decode('utf-8')
	# print( response )

	# print( '>> sending heartbeat' )
	# heartb.send("{H}".encode())

	print( '>> send test message' )
	client.send("{vNorth: 0.43, vEast: 1.56, depth: 0.56}".encode())
