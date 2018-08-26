import socket

# Create a service directory
SERVICE_DIRECTORY = {}

# Add new service
def add_service(service_name, hostname, port):
	if (service_name in SERVICE_DIRECTORY):
		return "Service is already exists"

	SERVICE_DIRECTORY[service_name] = (hostname, port)
	return "Service '{}' is added successfully".format(service_name)


# Remove a service
def remove_service(service_name):
	if (service_name not in SERVICE_DIRECTORY):
		return "Service not found"
	del SERVICE_DIRECTORY[service_name]
	return "Service '{}' is deleted successfully".format(service_name)

# Lookup for a service
def lookup_service(service_name):
	if (service_name in SERVICE_DIRECTORY):
		(hostname, port) = SERVICE_DIRECTORY[service_name]
		return "Service '{}' is available at {}:{}".format(service_name, hostname, port)
	else:
		return "Service is not available"

# Check whether a service is in the service directory
def contains(service_name):
	return service_name in SERVICE_DIRECTORY

# Connect to service and get result
def request_service(service_name, params):
	# Get service info
	(hostname, port) = SERVICE_DIRECTORY[service_name]

	# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((hostname, int(port)))
	sock.send(' '.join(params))

	# receive the response data (4096 is recommended buffer size)
	response = sock.recv(4096)
	return response

