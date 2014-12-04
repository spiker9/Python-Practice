import socket

#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['Michael', 'Sarah']:
	s.sendto(bytes(data, 'utf-8'), ('127.0.0.1', 10000))
	print(s.recv(180))
s.close()