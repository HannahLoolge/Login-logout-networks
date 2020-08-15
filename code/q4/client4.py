import socket
import sys

#host = socket.gethostname()
print "Enter host name"
host = str(sys.stdin.readline())
#port = 6040
print "Enter port number"
port = int(sys.stdin.readline())

BUFFER_SIZE = 2000

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))

while True:
	M1 = raw_input("Client enter username:\n")
	tcpClient.send(M1)

	data = tcpClient.recv(BUFFER_SIZE)
	if data == "Verified username\n":
		print data
		M2 = raw_input("Client enter password:\n")
		tcpClient.send(M2)
		res = tcpClient.recv(BUFFER_SIZE)
		if res == "Verified username and password\n":	
			print res
			res2 = tcpClient.recv(BUFFER_SIZE)
			print res2
		else:
			print "Username and password didn't match\n"	
	else:
		print "Username does not exist\n"


tcpClient.close()
