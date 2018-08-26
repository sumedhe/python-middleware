import socket
import threading

# Socket config
HOSTNAME = 'localhost'
PORT = 9993

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOSTNAME, PORT))
server.listen(5)  # max backlog of connections

print 'Listening on {}:{}'.format(HOSTNAME, PORT)


def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    try:
        params = request.split('&')
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


while True:
    client_sock, address = server.accept()
    print 'Accepted connection from {}:{}'.format(address[0], address[1])
    handle_client_connection(client_sock)

