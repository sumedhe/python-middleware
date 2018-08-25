import time, threading
import server_sock
from models.queue import Queue
from queue_handler import *

RECV_SIZE = 1024

# Create message queues for requests and responds
request_queue = Queue()
response_queue = Queue()

# Start queue handlers
try:
	# Request queue thread
	threading.Thread(
		target = handle_request_queue,
		args = (request_queue, response_queue,)
	).start()

	# Response queue thread
	threading.Thread(
		target = handle_response_queue,
		args = (response_queue,)
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
    request_queue.enqueue((client_socket, message))
