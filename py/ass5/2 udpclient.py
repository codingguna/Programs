import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = 'Hello from the client!'
client_socket.sendto(message.encode(), ('localhost', 12345))

response, server_address = client_socket.recvfrom(1024)
print(f'Received response from {server_address}: {response.decode()}')
