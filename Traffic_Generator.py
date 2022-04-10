#Traffic Generator
import socket
import random
import time

bufferSize  = 1024
serverAddressPort   = ("127.0.0.1", 7501)


print('this program will generate some test traffic for 2 players on the red ')
print('team as well as 2 players on the green team')
print('')

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

# Create datagram socket
UDPClientSocketTransmit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# counter number of events, random player and order
i = 0
while i < int(counter):
	if random.randint(1,2) == 1:
		redplayer = red1
	else:
		redplayer = red2

	if random.randint(1,2) == 1:
		greenplayer = green1
	else: 
		greenplayer = green2	

	if random.randint(1,2) == 1:
		message = redplayer + ":" + greenplayer
	else:
		message = greenplayer + ":" + redplayer

	print(message)
	i+=1;
	UDPClientSocketTransmit.sendto(str.encode(str(message)), serverAddressPort)
	time.sleep(random.randint(1,3))
	
print("program complete")