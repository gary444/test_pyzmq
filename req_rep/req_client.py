import zmq
import time

host = "192.168.178.64"
port = "5002"

# Creates a socket instance
context = zmq.Context()
socket = context.socket(zmq.REQ)

# Connects to a bound socket
socket.connect("tcp://{}:{}".format(host, port))

for x in range(1,10):

	try:

		# Receives a string format message
		socket.send_string("request " + str(x))


		reply = socket.recv_string()
		print("received reply: " + reply)
	
	except zmq.ZMQError:
		pass

	time.sleep(1)