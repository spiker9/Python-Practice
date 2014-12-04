import socket

#Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind to local id and property
s.bind(('127.0.0.1', 10000))

print('Bind UDP on 10000')

while True:
	#recvfrom could get data and address at the same time
	data, addr = s.recvfrom(1024)
	print('Received from %s:%s' % addr)
	s.sendto(bytes('Hello, %s!' % data, 'utf-8'), addr)



