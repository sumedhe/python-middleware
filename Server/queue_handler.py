from models.queue import Queue
import consumer
import time

SLEEP_TIME = 1


# Consume messages
def handle_request_queue(request_queue, response_queue):
	print 'Request queue handler started'

	while True:
		if (request_queue.isEmpty()):
			time.sleep(SLEEP_TIME)
		else:
			# Consume
			(client_socket, message) = request_queue.dequeue()
			response = consumer.execute(message)
			response_queue.enqueue((client_socket, response))

# Send responses to client
def handle_response_queue(response_queue):
	print 'Request queue handler started'

	while True:
		if (response_queue.isEmpty()):
			time.sleep(SLEEP_TIME)
		else:
			# Send response to the client
		 	(client_socket, message) = response_queue.dequeue()
		 	client_socket.send(message)
		 	client_socket.close()
