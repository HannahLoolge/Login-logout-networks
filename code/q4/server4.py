import csv
import socket
import sys
from threading import Thread
from SocketServer import ThreadingMixIn

TCP_IP = '0.0.0.0'
#TCP_PORT = 6040
print "Enter port number"
TCP_PORT = int(sys.stdin.readline())
BUFFER_SIZE = 20

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket created successfully\n"

#tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
tcpServer.bind((TCP_IP, TCP_PORT))
tcpServer.listen(2)
print "socket is listening\n"

#while True:
conn, addr = tcpServer.accept() 
print "[+] New server socket thread started for " + str(addr) + "\n"

while True:
	un = conn.recv(2048)
	print "Server received username: \n", un
	i=0
	bl = 0
	l = {}
	fr = open('ask.rtl', 'r')
	read1 = csv.reader(fr)

	for row in read1:
	#x = row.strip().split(',')
		if i<3:
			print row[0] + " " + row[1] + " " + row[2] + " "
			tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			tcpClient.connect((row[1], int(row[2])))
			tcpClient.send(un)
			res = tcpClient.recv(BUFFER_SIZE)
			if res == "Verified username\n":
				print res
				conn.send(res)
				pw = conn.recv(2048)
				print "Server received password: \n", pw
				tcpClient.send(pw)
				res2 = tcpClient.recv(2048)
				if res2 == "p\n":
					M2 = "Verified username and password\n"
					conn.send(M2)
					bl = 1
				else:
					print res2
			tcpClient.close()
		
		else:
			l = row
		
		i+=1
	
	
	if(bl==1):
		tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcpClient.connect((l[1], int(l[2])))
		tcpClient.send(un)
		res = tcpClient.recv(BUFFER_SIZE)
		x = int(res)*100/8
		y = str(x)
		M3 = "You attended "+ res + " classes out of 8 " + y + "% " +"\n"
		conn.send(M3)
		tcpClient.close()
	else:	
		M3 = ("Username does not exist\n")
		conn.send(M3)
			
conn.close()
	
