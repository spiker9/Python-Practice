import socket

#New a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Establish connection
s.connect(('127.0.0.1', 9999))
#Receive welcome message
print(s.recv(1024))

#Send message
for data in ['Michael', 'Tracy', 'Sarah']:
	s.send(bytes(data, 'utf-8'))
	print(s.recv(1024))
s.send(bytes('exit','utf-8'))

#Close Socket
s.close()