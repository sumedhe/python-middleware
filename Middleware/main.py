#!/usr/bin/python

import time, threading
import server_sock
from models.queue import Queue
from queue_handler import *

RECV_SIZE = 1024

# Create message queues for requests and responds
REQUEST_QUEUE  = Queue()
RESPONSE_QUEUE = Queue()


# Start queue handlers
try:
	# Request queue thread
	threading.Thread(
		target = handle_request_queue,
		args = (REQUEST_QUEUE, RESPONSE_QUEUE,)
	).start()

	# Response queue thread
	threading.Thread(
		target = handle_response_queue,
		args = (RESPONSE_QUEUE,)
	).start()

except Exception as e:
	print(e)


# Start server
server = server_sock.start()


# Accept connections
while True:
    client_socket, client_address = server.accept()
    print("Accepted connection from {}:{}".format(client_address[0], client_address[1]))

    # Add to message queue
    message = client_socket.recv(RECV_SIZE)
    REQUEST_QUEUE.enqueue((client_socket, message))
