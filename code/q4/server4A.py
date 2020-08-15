import csv
import socket
import sys

f = open('login_credentials.csv', 'r')
reader = csv.reader(f)

n = 24
i=0
pwd={}
for row in reader:
	if i<=n:
		pwd[row[0]]=row[1]
	i+=1
	
f.close()
		

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket successfully created"

ip = '0.0.0.0'
print "Enter port number"
port = int(sys.stdin.readline())

s.bind((ip, port))
print "socket binded to %s" %(port)

s.listen(2)
print "socket is listening"

while True:
	c, addr = s.accept()
	un = c.recv(2048)
	print "Server received username:\n", un

	if pwd.get(un)!=None:
		print "Verify username\n"
		M=("Verified username\n")
		c.send(M)
		pw = c.recv(2048)
		print "Server received password: \n", pw
		if pwd[un]==pw:
			M2 = "p\n"
			c.send(M2)
		else:
			M2 = "Incorrect Password\n"
			c.send(M2)
		
	c.close()
		
