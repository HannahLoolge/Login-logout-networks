import csv
import socket
import sys

f = open('attendance.csv','r')
reader = csv.reader(f)

att = {}

for row in reader:
	i=0
	#print row[1]
	if row[2]=="Done":
		i+=1
	if row[3]=="Done":
		i+=1
	if row[4]=="Done":
		i+=1
	if row[5]=="Done":
		i+=1
	if row[6]=="Done":
		i+=1
	if row[7]=="Done":
		i+=1
	if row[8]=="Done":
		i+=1
	if row[9]=="Done":
		i+=1				
	att[row[1]] = i

f.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket 4D successfully created"

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
	print "Server 4D received username:\n", un

	attun = str(att[un])
	c.send(attun)
	
	c.close()	

