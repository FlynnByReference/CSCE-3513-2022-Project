#  CSCE 3513 Back End Code
#
#  To-Do
#  
#  
#
# Start of Code

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
playerID = 0

# mh.addPlayer(4, 'Testing', 'Main.py', 'test')

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
        
        
        print(playerData)

        
    return jsonify(playerData)


##When path is /action change to the game screen
@app.route("/action")
def action():
    return render_template('playerAction.html')

    ##Probably need this later
    #in html
    #{id}
    #return render_template('playerAction.html',id = test[0],fname = test[1],lname = test[2],cname = test[3])


##Get info from database to Action screen this should probably go in the action about ^^
def retrievePlayer():
    ##Loop through db for each player and their information
    for i in range(1, 11):
        test = mh.getPlayer(i)
        print('Player ID: ' + str(test[0]))
        print("Player First Name: " + test[1])
        print("Player Last Name: " + test[2])
        print("Player Code Name: " + test[3])
        
        
retrievePlayer()
