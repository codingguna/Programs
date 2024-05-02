import socket


cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('localhost', 12345))

current_time = cs.recv(1024).decode('utf-8')
print(f'Current time from server: {current_time}')

cs.close()

