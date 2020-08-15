import sys
import socket

print "Enter host ip address"
host = str(sys.stdin.readline())
print "Enter the port number"
port = int(sys.stdin.readline())

BUFFER_SIZE = 2000

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))

M1 = raw_input("Client enter username: ")
tcpClient.send(M1)

data = tcpClient.recv(BUFFER_SIZE)
if data == "Verified username":
	print data
	M2 = raw_input("Client enter password:")
	tcpClient.send(M2)
	res = tcpClient.recv(BUFFER_SIZE)
	if res == "Verified username and password":	
		print res
			
	else:
		print "Username and password didn't match"
else:
	print "Username does not exist"

tcpClient.close()
