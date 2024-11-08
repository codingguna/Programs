import socket
host = "localhost"
port = 5000
server = socket.socket()
server.bind((host,port))
server.listen()
conn, addr = server.accept()
print ("Connection from: " + str(addr))
while True:
   data = conn.recv(1024).decode()
   if not data:
      break
   data = str(data).upper()
   print (" from client: " + str(data))
   data = input("type message: ")
   conn.send(data.encode())
conn.close()
