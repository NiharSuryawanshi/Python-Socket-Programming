from socket import *

print "Server getting ready..."
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)

serverSocket.bind(('',serverPort))

print"server ready to receive"

while 1:
	message, clientAddr = serverSocket.recvfrom(2048)
	Modmsg = message.upper()
	serverSocket.sendto(Modmsg,clientAddr)

print"process Complete."