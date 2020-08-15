import sys
import socket
import csv

with open('login_credentials.csv', 'r') as file:
	reader = csv.reader(file)
	pwd = {}
	for row in reader:
		pwd[row[0]] = row[1]

TCP_IP = '0.0.0.0'
print "Enter the port number\n"
TCP_PORT = int(sys.stdin.readline())

BUFFER_SIZE = 20

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket successfully created\n"

#tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
tcpServer.bind((TCP_IP, TCP_PORT))

tcpServer.listen(3)
print "Socket is listening\n"

while True:
	conn, addr = tcpServer.accept()
	print "Server connected"
	
	un = conn.recv(2048)
	#print "Server received username:",un
	if pwd.get(un)!=None:
		#print "Verify username"
		M = ("Verified username")
		conn.send(M)
		pw = conn.recv(2048)
		#print "Server received password: ", pw
		if pwd[un]==pw:
			M2 = ("Verified username and password")
			conn.send(M2)
			#while True:
			#	M3 = conn.recv(2048)
				#if M3 == "exit":
					#print "Client "+str(addr) + " " + "is exiting"
				#else:
					#print M3
	else:
		M = ("Username does not exists")
		conn.send(M)
	
#	conn.close()	

	
