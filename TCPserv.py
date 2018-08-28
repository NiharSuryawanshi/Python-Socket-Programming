#here there are two socket connections,
# 1 for welcome and other for data transfer

from socket import *

print "Server getting ready..."
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))
#this is welcome socket which keeps the connection going
serverSocket.listen(1) #maximum no of Queue connection is 1.

print"server ready to receive"

while 1:

	connectionSocket, addr = serverSocket.accept()
	message  = connectionSocket.recv(2048)
	Modmsg = message.upper()
	connectionSocket.send(Modmsg)
	connectionSocket.close()

print"process Complete."