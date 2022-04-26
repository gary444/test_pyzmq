# simple_pub.py
import zmq
import time

host = "192.168.178.64"
port = "5002"

# Creates a socket instance
context = zmq.Context()
socket = context.socket(zmq.PUB)

# Binds the socket to a predefined port on localhost
socket.bind("tcp://{}:{}".format(host, port))


time.sleep(1) # new sleep statement


for x in range(1,100):
	
	# Sends a string message
	socket.send_string("hello" + str(x))

	time.sleep(1)
