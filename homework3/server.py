from socket import *

s = socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8080

s.bind(('localhost', port))

s.listen(5)

while True:
    clientsocket, addr = s.accept()
    msg = "Hello, client!"
    clientsocket.send(msg.encode())
    clientsocket.close()
