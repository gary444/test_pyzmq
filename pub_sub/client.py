# simple_sub.py
import zmq

# host = "*"
host = "192.168.178.64"
port = "5002"

# Creates a socket instance
context = zmq.Context()
socket = context.socket(zmq.SUB)

# Connects to a bound socket
socket.connect("tcp://{}:{}".format(host, port))

# Subscribes to all topics
socket.subscribe("")

while True:

	try:

		# Receives a string format message
		whole_message = socket.recv_string(flags=zmq.NOBLOCK)
		print(whole_message)            

		# message_frame = socket.recv(flags=zmq.NOBLOCK, copy=False)
		# print("Received message frame with " + str(len(message_frame)) + " bytes")

	
	except zmq.ZMQError:
		pass