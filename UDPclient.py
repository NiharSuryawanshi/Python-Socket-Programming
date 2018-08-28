from socket import *
serverName = 'localhost'
serverPort = 12000
					#ADDRESS FAMILY          UDP PACKET
clientSocket = socket(AF_INET, SOCK_DGRAM)

print "Client getting ready.."
print "......................"

ch = 1
while ch!=0:

	#print "press 1 to enter string"
	print "press 0 to exit"

	message = raw_input('Please enter the string')

	clientSocket.sendto(message,(serverName,serverPort))

	modifiedMsg, serverAddress = clientSocket.recvfrom(2024)

	print modifiedMsg

clientSocket.close()
