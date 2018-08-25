import socket

# Socket config
HOSTNAME = 'localhost'
PORT = 9999
MAX_BACKLOG = 10

def start():
	# Initialize socket
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((HOSTNAME, PORT))
	server.listen(MAX_BACKLOG)
	print("Listening on {}:{}".format(HOSTNAME, PORT))

	return server

