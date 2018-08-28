#Here only one socket is used for communication

from socket import *
serverName = 'localhost'
serverPort = 12000
					#ADDRESS FAMILY          TCP PACKET
clientSocket = socket(AF_INET, SOCK_STREAM)
#connect the socket to welcoming socket
clientSocket.connect((serverName,serverPort))


print "Client getting ready.."
print "......................"

ch = 1
while ch!=0:

	#print "press 1 to enter string"
	print "press 0 to exit"

	message = raw_input('Please enter the string:')

	clientSocket.sendto(message,(serverName,serverPort))

	modifiedMsg, serverAddress = clientSocket.recvfrom(2024)

	print modifiedMsg

clientSocket.close()
