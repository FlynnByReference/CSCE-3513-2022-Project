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
        playerID = playerData["redplayerID"]
        first_name = playerData["redfirstName"]
        last_name = playerData["redlastName"]
        codename = playerData["redcodeName"]
        
        ##Call addPlayer method from midhand.py for green player 1
        mh.addPlayer(playerID, first_name, last_name, codename)
        
        ##Variables to pass into database for green player 1        
        playerID = playerData["playerID"]
        first_name = playerData["firstName"]
        last_name = playerData["lastName"]
        codename = playerData["codeName"]
        
        ##Call addPlayer method from midhand.py for green player 1
        mh.addPlayer(playerID, first_name, last_name, codename)
        
    return jsonify(playerData)


