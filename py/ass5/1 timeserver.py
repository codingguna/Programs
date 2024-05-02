import socket
from datetime import datetime


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind(('localhost', 12345))
ss.listen(1)

print('Server is listening...')

while True:
    cs, ca = ss.accept()
    print(f'Connected with {ca}')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cs.send(current_time.encode('utf-8'))

    cs.close()
