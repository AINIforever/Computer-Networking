from socket import *


s = socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8080
s.connect(('localhost', port))

print("Say hello to server!")
hello = "Hello, Server."
s.send(hello.encode())

msg = s.recv(1024)
print (msg.decode())

s.close()
