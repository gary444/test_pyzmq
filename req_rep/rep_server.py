import zmq

host = "192.168.178.64"
port = "5002"

# Creates a socket instance
context = zmq.Context()
socket = context.socket(zmq.REP)

# Connects to a bound socket
socket.bind("tcp://{}:{}".format(host, port))

while True:

	try:

		# Receives a string format message
		whole_message = socket.recv_string(flags=zmq.NOBLOCK)
		print("received" + whole_message)            

		socket.send_string("reply to " + whole_message)

		# message_frame = socket.recv(flags=zmq.NOBLOCK, copy=False)
		# print("Received message frame with " + str(len(message_frame)) + " bytes")

	
	except zmq.ZMQError:
		pass