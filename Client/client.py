import socket

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect(('localhost', 9992))

client.send('addservice gcd&localhost&9993')
# client.send('removeservice gcd')
# client.send('lookupservice gcd')
# client.send('gcd 12&18')

# Get response
response = client.recv(4096)
client.close()
print response


