import socket
import random
import time

# Sets variables to holdsocket info
localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
message = bytesAddressPair[0]
address = bytesAddressPair[1]
clientMsg = "Message from Client:{}".format(message)
clientIP  = "Client IP Address:{}".format(address)
	
print(clientMsg)
print(clientIP)

##Generate random red ID's for simulation
red1 = random.randint(1,5)
red2 = random.randint(1,5)
if (red1 == red2):
	while(red1 == red2):
		red2 = random.randint(1,5)
		
##Convert random ID's to strings
red1 = str(red1)
red2 = str(red2)
		
##Generate random green ID's for simulation
green1 = random.randint(6, 10)
green2 = random.randint(6, 10)
if (green1 == green2):
	while(green1 == green2):
		green2 = random.randint(6, 10)

##Convert random ID's to strings       
green1 = str(green1)
green2 = str(green2)

##Generate random number between 1 and 10 for number of events
counter = random.randint(1,10)
print(counter)
# Create datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# counter number of events, random player and order
i = 0
totalMessage = ""
redPoints = 0
greenPoints = 0

while i < int(counter):
	if random.randint(1,2) == 1:
		redplayer = red1
	else:
		redplayer = red2

	if random.randint(1,2) == 1:
		greenplayer = green1
	else: 
		greenplayer = green2	

	##Red team gets a hit and point
	if random.randint(1,2) == 1:
		message = "Red player " + redplayer + " shot Green player " + greenplayer
		redPoints += 1
	##Green team gets a hit and point
	else:
		message = "Green player " + greenplayer + " shot Red player " + redplayer
		greenPoints += 1
	
	##Concatinate events
	if i == 0:
	    totalMessage += message
	else:
	    totalMessage += " , " + message
	
	i += 1


UDPServerSocket.sendto(str.encode(str(totalMessage)), address)
UDPServerSocket.sendto(str.encode(str(redPoints)), address)
UDPServerSocket.sendto(str.encode(str(greenPoints)), address)
time.sleep(random.randint(1,3))
print("program complete")
