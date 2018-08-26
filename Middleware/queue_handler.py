import time
import service_handler
from utils.message_parser import *
from models.queue import Queue


# Create message queues for requests and responds
REQUEST_QUEUE  = Queue()
RESPONSE_QUEUE = Queue()


SLEEP_TIME = 0.5


# Consume messages
def handle_request_queue():
	print 'Request queue handler started'

	while True:
		if (REQUEST_QUEUE.isEmpty()):
			time.sleep(SLEEP_TIME)
		else:
			# Consume
			(client_socket, message) = REQUEST_QUEUE.dequeue()

			handle_request(client_socket, message)

# Send responses to client
def handle_response_queue():
	print 'Request queue handler started'

	while True:
		if (RESPONSE_QUEUE.isEmpty()):
			time.sleep(SLEEP_TIME)
		else:
			# Send response to the client
		 	(client_socket, message) = RESPONSE_QUEUE.dequeue()
		 	client_socket.send(message)
		 	client_socket.close()

# Handle the request
def handle_request(client_socket, message):
	# Parse message
	try:
		(action, params) = get_params(message)
		print "Action: " + action

		# Handle request
		if (action.lower() == "addservice"): # Add new service
			response = service_handler.add_service(params[0], params[1], params[2])
		elif (action.lower() == "removeservice"): # Remove a service
			response = service_handler.remove_service(params[0])
		elif (action.lower() == "lookupservice"): # Lookup for a service
			response = service_handler.lookup_service(params[0])
		elif (service_handler.contains(action.lower())): # Caheck in service directory
			response = service_handler.request_service(action, params)
		else:
			response = "Service not found"
	except Exception as e:
		print e
		response = "Invalid request format"

	RESPONSE_QUEUE.enqueue((client_socket, str(response)))

