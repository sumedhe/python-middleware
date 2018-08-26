import time
import service_handler
from utils.message_parser import *
from models.queue import Queue



SLEEP_TIME = 1


# Consume messages
def handle_request_queue(REQUEST_QUEUE, RESPONSE_QUEUE):
	print 'Request queue handler started'

	while True:
		if (REQUEST_QUEUE.isEmpty()):
			time.sleep(SLEEP_TIME)
		else:
			# Consume
			(client_socket, message) = REQUEST_QUEUE.dequeue()

			handle_request(client_socket, message, RESPONSE_QUEUE)

# Send responses to client
def handle_response_queue(RESPONSE_QUEUE):
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
def handle_request(client_socket, message, RESPONSE_QUEUE):
	# Parse message
	try:
		(action, params) = get_params(message)
		print "Action: " + action

		# Handle request
		if (action.lower() == "addservice"):
			response = service_handler.add_service(params[0], params[1], params[2])
		elif (action.lower() == "removeservice"):
			response = service_handler.remove_service(params[0])
		elif (action.lower() == "lookupservice"):
			response = service_handler.lookup_service(params[0])
		elif (service_handler.contains(action.lower())):
			response = service_handler.request_service(action, params)
		else:
			response = "Service not found"
	except Exception as e:
		print e
		response = "Invalid request format"


	RESPONSE_QUEUE.enqueue((client_socket, str(response)))




	# if (not len(params) == 2):
	# 	response = "Parameters does not match"
	# else:
	# 	# try:
	# 	response = gcd(int(params[0]), int(params[1]))
	# 	# except:
	# 		# response = "Invalid parameters"

