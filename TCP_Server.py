import socket, threading, time

#After the connection established, server will send welcome to client and add hello to the message send from client
def tcplink(sock, addr):
	print('Acceppt new connection from %s:%s...' % addr)
	sock.send(bytes('Welcome!', 'utf-8'))
	while True:
		data = str(sock.recv(1024), 'utf-8')
		print(data)
		time.sleep(1)
		if data == 'exit' or not data:
			break
		sock.send(bytes('Hello, %s!' % data, 'utf-8'))
	sock.close()
	print('Connection from %s:%s closed.' % addr)

#Create a socket with IPv4 address
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind socket to local IP and 9999 port
s.bind(('127.0.0.1', 9999))
#Make the socket start listening, and set the max number of connection
s.listen(5)
print('Waiting for connection...')

#Use a perminent loop to accept the connection
while True:
	sock, addr = s.accept()
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()

