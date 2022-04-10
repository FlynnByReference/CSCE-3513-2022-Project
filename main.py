#  CSCE 3513 Back End Code
#
#  To-Do
#  
#  
#
# Start of Code

import socket
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask import json
from midhand import connectToHeroku 

##Variable for chosing front end path
app = Flask(__name__)

##Declares  class from midhand.py
mh = connectToHeroku()

# mh.addPlayer(4, 'Testing', 'Main.py', 'test')

serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


##Sets first path to splash screen
@app.route("/")
def home():
    return render_template('splash.html')

##Sets second path to player screen
@app.route("/game")
def game():
    return render_template('splitPlayers.html')

##When player enters info entry set path to get players in
@app.route('/submit', methods = ['POST'])
def addPlayerThroughMH():
    ##Array for players info
    playerInfo = []
    
    ##Checks for method POST from splitPlayers.html
    if request.method == 'POST':
        ##Add player info to array
        playerData = request.get_json(force=True)
        for i in playerData.keys():
            for j in playerData.values():
                playerInfo.append(i)
                playerInfo.append(j)
                
        ##Variables to pass into database for red player 1
        playerID = playerData["redplayerID1"]
        first_name = playerData["redfirstName1"]
        last_name = playerData["redlastName1"]
        codename = playerData["redcodeName1"]
                
        ##Call addPlayer method from midhand.py for red player 1
        mh.addPlayer(playerID, first_name, last_name, codename)
        
        ##Variables to pass into database for green player 1        
        playerID = playerData["greenplayerID1"]
        first_name = playerData["greenplayerfirstname1"]
        last_name = playerData["greenplayerlastname1"]
        codename = playerData["greenplayercodename1"]
        
        ##Call addPlayer method from midhand.py for green player 1
        mh.addPlayer(playerID, first_name, last_name, codename)
        
        ##Variables to pass into database for red player 1
        playerID = playerData["redplayerID2"]
        first_name = playerData["redfirstName2"]
        last_name = playerData["redlastName2"]
        codename = playerData["redcodeName2"]
        
        ##Call addPlayer method from midhand.py for red player 1
        mh.addPlayer(playerID, first_name, last_name, codename)
        
        ##Variables to pass into database for green player 1        
        playerID = playerData["greenplayerID2"]
        first_name = playerData["greenplayerfirstname2"]
        last_name = playerData["greenplayerlastname2"]
        codename = playerData["greenplayercodename2"]
        
        ##Call addPlayer method from midhand.py for green player 1
        mh.addPlayer(playerID, first_name, last_name, codename)
        
        ##Variables to pass into database for red player 1
        playerID = playerData["redplayerID3"]
        first_name = playerData["redfirstName3"]
        last_name = playerData["redlastName3"]
        codename = playerData["redcodeName3"]
        
        ##Call addPlayer method from midhand.py for red player 1
        mh.addPlayer(playerID, first_name, last_name, codename)
        
        ##Variables to pass into database for green player 1        
        playerID = playerData["greenplayerID3"]
        first_name = playerData["greenplayerfirstname3"]
        last_name = playerData["greenplayerlastname3"]
        codename = playerData["greenplayercodename3"]
        
        ##Call addPlayer method from midhand.py for green player 1
        mh.addPlayer(playerID, first_name, last_name, codename)
        
        ##Variables to pass into database for red player 1
        playerID = playerData["redplayerID4"]
        first_name = playerData["redfirstName4"]
        last_name = playerData["redlastName4"]
        codename = playerData["redcodeName4"]
        
        ##Call addPlayer method from midhand.py for red player 1
        mh.addPlayer(playerID, first_name, last_name, codename)
        
        ##Variables to pass into database for green player 1        
        playerID = playerData["greenplayerID4"]
        first_name = playerData["greenplayerfirstname4"]
        last_name = playerData["greenplayerlastname4"]
        codename = playerData["greenplayercodename4"]
        
        ##Call addPlayer method from midhand.py for green player 1
        mh.addPlayer(playerID, first_name, last_name, codename)
        
        ##Variables to pass into database for red player 1
        playerID = playerData["redplayerID5"]
        first_name = playerData["redfirstName5"]
        last_name = playerData["redlastName5"]
        codename = playerData["redcodeName5"]
        
        ##Call addPlayer method from midhand.py for red player 1
        mh.addPlayer(playerID, first_name, last_name, codename)
        
        ##Variables to pass into database for green player 1        
        playerID = playerData["greenplayerID5"]
        first_name = playerData["greenplayerfirstname5"]
        last_name = playerData["greenplayerlastname5"]
        codename = playerData["greenplayercodename5"]
        
        ##Call addPlayer method from midhand.py for green player 1
        mh.addPlayer(playerID, first_name, last_name, codename)
        
        
        # print(playerData)

        
    return jsonify(playerData)


##When path is /action change to the game screen
@app.route("/action")
def action():
    return render_template('playerAction.html')

##Get info from database to Action screen this should probably go in the action about ^^
@app.route('/getplayer', methods = ['GET'])
def retrievePlayer():
    ##Detect 'GET' method
    if request.method == 'GET':
        ##All players from database
        test = mh.getPlayer()
        
        ##Red player 1 info
        IDri1 = test[0][0]
        firstrf1 = test[0][1]
        lastrl1 = test[0][2]
        codeNamerc1 = test[0][3]
        
        ##Red player 2 info
        IDri2 = test[2][0]
        firstrf2 = test[2][1]
        lastrl2 = test[2][2]
        codeNamerc2 = test[2][3]
        
        ##Red player 3 info
        IDri3 = test[4][0]
        firstrf3 = test[4][1]
        lastrl3 = test[4][2]
        codeNamerc3 = test[4][3]
        
        ##Red player 4 info
        IDri4 = test[6][0]
        firstrf4 = test[6][1]
        lastrl4 = test[6][2]
        codeNamerc4 = test[6][3]
        
        ##Red player 5 info
        IDri5 = test[8][0]
        firstrf5 = test[8][1]
        lastrl5 = test[8][2]
        codeNamerc5 = test[8][3]
        
        ##Green player 1 info
        IDgi1 = test[1][0]
        firstgf1 = test[1][1]
        lastgl1 = test[1][2]
        codeNamegc1 = test[1][3]
        
        ##Green player 2 info
        IDgi2 = test[3][0]
        firstgf2 = test[3][1]
        lastgl2 = test[3][2]
        codeNamegc2 = test[3][3]
        
        ##Green player 3 info
        IDgi3 = test[5][0]
        firstgf3 = test[5][1]
        lastgl3 = test[5][2]
        codeNamegc3 = test[5][3]
        
        ##Green player 4 info
        IDgi4 = test[7][0]
        firstgf4 = test[7][1]
        lastgl4 = test[7][2]
        codeNamegc4 = test[7][3]
        
        ##Green player 5 info
        IDgi5 = test[9][0]
        firstgf5 = test[9][1]
        lastgl5 = test[9][2]
        codeNamegc5 = test[9][3]
        
        ##Dictionary for all players to be sent to playerAction.html
        playerDict = {
            "redplayer1ID" : IDri1,  ##Red player 1 info
            "redplayer1Name" : firstrf1,
            "redplayer1Last" : lastrl1,
            "redplayer1Code" : codeNamerc1,
            "greenplayer1ID" : IDgi1,  ##Green player 1 info
            "greenplayer1Name" : firstgf1,
            "greenplayer1Last" : lastgl1,
            "greenplayer1Code" : codeNamegc1,
            "redplayer2ID" : IDri2,  ##Red player 2 info
            "redplayer2Name" : firstrf2,
            "redplayer2Last" : lastrl2,
            "redplayer2Code" : codeNamerc2,
            "greenplayer2ID" : IDgi2,  ##Green player 2 info
            "greenplayer2Name" : firstgf2,
            "greenplayer2Last" : lastgl2,
            "greenplayer2Code" : codeNamegc2,
            "redplayer3ID" : IDri3,  ##Red player 3 info
            "redplayer3Name" : firstrf3,
            "redplayer3Last" : lastrl3,
            "redplayer3Code" : codeNamerc3,
            "greenplayer3ID" : IDgi3,  ##Green player 3 info
            "greenplayer3Name" : firstgf3,
            "greenplayer3Last" : lastgl3,
            "greenplayer3Code" : codeNamegc3,
            "redplayer4ID" : IDri4,  ##Red player 4 info
            "redplayer4Name" : firstrf4,
            "redplayer4Last" : lastrl4,
            "redplayer4Code" : codeNamerc4,
            "greenplayer4ID" : IDgi4,  ##Green player 4 info
            "greenplayer4Name" : firstgf4, 
            "greenplayer4Last" : lastgl4,
            "greenplayer4Code" : codeNamegc4,
            "redplayer5ID" : IDri5,  ##Red player 5 info
            "redplayer5Name" : firstrf5,
            "redplayer5Last" : lastrl5,
            "redplayer5Code" : codeNamerc5,
            "greenplayer5ID" : IDgi5,  ##Green player 4 info
            "greenplayer5Name" : firstgf5,
            "greenplayer5Last" : lastgl5,
            "greenplayer5Code" : codeNamegc5,
        }
        
        msgFromClient = str(playerDict)
        print(msgFromClient)
        bytesToSend = str.encode(msgFromClient)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = "Message from Server {}".format(msgFromServer[0])
        print(msg)
        
        totalDict = {
            "redplayer1ID" : IDri1,  ##Red player 1 info
            "redplayer1Name" : firstrf1,
            "redplayer1Last" : lastrl1,
            "redplayer1Code" : codeNamerc1,
            "greenplayer1ID" : IDgi1,  ##Green player 1 info
            "greenplayer1Name" : firstgf1,
            "greenplayer1Last" : lastgl1,
            "greenplayer1Code" : codeNamegc1,
            "redplayer2ID" : IDri2,  ##Red player 2 info
            "redplayer2Name" : firstrf2,
            "redplayer2Last" : lastrl2,
            "redplayer2Code" : codeNamerc2,
            "greenplayer2ID" : IDgi2,  ##Green player 2 info
            "greenplayer2Name" : firstgf2,
            "greenplayer2Last" : lastgl2,
            "greenplayer2Code" : codeNamegc2,
            "redplayer3ID" : IDri3,  ##Red player 3 info
            "redplayer3Name" : firstrf3,
            "redplayer3Last" : lastrl3,
            "redplayer3Code" : codeNamerc3,
            "greenplayer3ID" : IDgi3,  ##Green player 3 info
            "greenplayer3Name" : firstgf3,
            "greenplayer3Last" : lastgl3,
            "greenplayer3Code" : codeNamegc3,
            "redplayer4ID" : IDri4,  ##Red player 4 info
            "redplayer4Name" : firstrf4,
            "redplayer4Last" : lastrl4,
            "redplayer4Code" : codeNamerc4,
            "greenplayer4ID" : IDgi4,  ##Green player 4 info
            "greenplayer4Name" : firstgf4, 
            "greenplayer4Last" : lastgl4,
            "greenplayer4Code" : codeNamegc4,
            "redplayer5ID" : IDri5,  ##Red player 5 info
            "redplayer5Name" : firstrf5,
            "redplayer5Last" : lastrl5,
            "redplayer5Code" : codeNamerc5,
            "greenplayer5ID" : IDgi5,  ##Green player 4 info
            "greenplayer5Name" : firstgf5,
            "greenplayer5Last" : lastgl5,
            "greenplayer5Code" : codeNamegc5,
            "events" : msg,
        }
        
        ##Send player dictionary as json object to javascript
        return jsonify(totalDict)
