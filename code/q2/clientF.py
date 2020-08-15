import socket
import sys

#host = socket.gethostname()
#port = 2018
print "Enter host ip address"
host = str(sys.stdin.readline())
print "Enter the port number"
port = int(sys.stdin.readline())
BUFFER_SIZE = 2000

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))

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
		while True:
			M3 = raw_input("Send server something\n")
			tcpClient.send(M3)
			if M3=="exit":
				break	
	else:
		print "Username and password didn't match\n"
else:
	print "Username does not exist\n"

tcpClient.close()
