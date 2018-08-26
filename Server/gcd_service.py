import socket
import threading

# Socket config
SERVICE_NAME = 'gcd'
HOSTNAME     = 'localhost'
PORT         = 9993

MIDDLEWARE_HOSTNAME = 'localhost'
MIDDLEWARE_PORT     = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOSTNAME, PORT))
server.listen(5)  # max backlog of connections

print 'Listening on {}:{}'.format(HOSTNAME, PORT)

def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    try:
        params   = request.split('&')
        response = gcd(int(params[0]), int(params[1]))
    except:
        response = "Invalid parameter count"
    
    client_socket.send(str(response))
    client_socket.close()


# Greatest Common Devisor
def gcd(num1, num2):
    while num2 != 0:
        (num1, num2) = (num2, num1 % num2)
    return num1


# Register the service
def register_service():
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the middleware
    sock.connect((MIDDLEWARE_HOSTNAME, MIDDLEWARE_PORT))
    sock.send("addservice {}&{}&{}".format(SERVICE_NAME, HOSTNAME, PORT))

    # Get response
    response = sock.recv(4096)
    sock.close()
    print response


# Register the service 
register_service()

# Accept requests
while True:
    client_sock, address = server.accept()
    print 'Accepted connection from {}:{}'.format(address[0], address[1])
    handle_client_connection(client_sock)
