# simple_pub.py
import zmq
import time

host = "127.0.0.1"
port = "5002"

# Creates a socket instance
context = zmq.Context()

pub_socket = context.socket(zmq.PUB)
pub_socket.bind("inproc://test")

sub_socket = context.socket(zmq.SUB)
sub_socket.subscribe("")
sub_socket.connect("inproc://test")

for x in range(1,5):
	
	# Sends a string message
	pub_socket.send_string("hello" + str(x))

	time.sleep(1)

	try:
		whole_message = sub_socket.recv_string(flags=zmq.NOBLOCK)
		print(whole_message)            
	except zmq.ZMQError:
		pass