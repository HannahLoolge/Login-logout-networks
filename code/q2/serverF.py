import csv
import socket
import sys
from threading import Thread
from SocketServer import ThreadingMixIn

class ClientThread(Thread): 
 
    def __init__(self,conn,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "[+] New server socket thread started for " + ip + ":" + str(port) + "\n"
	self.conn = conn
 
    def run(self):
    	un = self.conn.recv(2048)
    	print "Server received username: \n", un
    	if pwd.get(un)!=None:
    		print "Verify username\n"
    		M = ("Verified username\n")
    		self.conn.send(M)
    		pw = self.conn.recv(2048)
    		print "Server received password: \n", pw
    		if pwd[un]==pw:
    			M2 = ("Verified username and password\n")
    			self.conn.send(M2)
    			while True:
    				M3 = self.conn.recv(2048)
    				if M3=="exit":
    					print "Client " + ip + " "+ str(port) + "is exiting\n"	
    					break			
    				else:
    					print M3	
    		else:
    			M2 = "Incorrect Password\n"
    			self.conn.send(M2)
    		
    	else:
    		#print "HHHH\n"
    		M = ("Username does not exist\n")
    		self.conn.send(M)
    	
    	#print "XXYZ\n"
    	 

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

tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

tcpServer.listen(1)
print "socket is listening\n"

while True:
	print "Multithreaded Python server : Waiting for connections from TCP clients...\n"
	(conn, (ip,port)) = tcpServer.accept() 
	newthread = ClientThread(conn,ip,port)
	newthread.start()
	threads.append(newthread)
    
    
