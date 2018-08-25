import time
from services.gcd_service import *
from utils.message_parser import *
from models.queue import Queue



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

			# Call GCD Service
			params = get_params(message)
			if (not len(params) == 2):
				response = "Parameters does not match"
			else:
				# try:
				response = gcd(int(params[0]), int(params[1]))
				# except:
					# response = "Invalid parameters"

			response_queue.enqueue((client_socket, str(response)))


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
