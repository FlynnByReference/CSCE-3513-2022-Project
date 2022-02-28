# #  CSCE 3513 Back End Code
# #
# #  To-Do
# #  Link to DataBase (Heroku)
# #  Add 2 Players (I think)
# #
# # Start of Code

# from flask import Flask
# from flask import request
# from flask import render_template
# from flask import jsonify
# from flask import json
# from midhand import connectToHeroku 

# app = Flask(__name__)
# mh = connectToHeroku()
# playerID = 0
# #mh.addPlayer(11, "Jase", "Cornett", "Jazer")

# # @app.route("/")
# # def home():
# #     return render_template('splitPlayers.html')

# # @app.route('/test', methods = ['GET', 'POST'])
# # def addPlayerThroughMH():
# #     if(request.method == 'POST'):
# #         id = 1
# #         first_name = request.form.get('first')
# #         last_name = request.form.get('last')
# #         codename = request.form.get('code')
# #         mh.addPlayer(id, first_name, last_name, codename)
# #         # playerinfo = {id, first_name, last_name, codename}
# #         # return jsonify(playerinfo)

# @app.route("/")
# def home():
#     return render_template('splitPlayers.html')

# @app.route('/test', methods = ['POST'])
# def addPlayerThroughMH():
#     if request.method == "POST":
#         playerID = 1
#         first_name = request.form["first"]
#         last_name = request.form["last"]
#         codename = request.form["code"]
#         mh.addPlayer(playerID, first_name, last_name, codename)
    
#     # jsdata = request.form['javaScriptData']
#     # return json.loads(jsdata)[0]
    
    
    
#         #yemh.addPlayer(id, first_name, last_name, codename)
#         # playerinfo = {id, first_name, last_name, codename}
#         # return jsonify(playerinfo)


#  CSCE 3513 Back End Code
#
#  To-Do
#  Link to DataBase (Heroku)
#  Add 2 Players (I think)
#
# Start of Code

from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask import json
from midhand import connectToHeroku 
import webapp2 

app = Flask(__name__)
mh = connectToHeroku()
mh.addPlayer(1, "NICK", "BROWN", "NFB")
playerID = 0


@app.route("/")
def home():
    return render_template('splash.html')

@app.route("/game")
def game():
    return render_template('splitPlayers.html')

@app.route('/submit', methods = ['POST'])
def addPlayerThroughMH():
    playerInfo = []
    if request.method == 'POST':
        playerData = request.get_json(force=True)
        for i in playerData.keys():
            for j in playerData.values():
                playerInfo.append(i)
                playerInfo.append(j)
        playerID = playerData["redplayerID"]
        first_name = playerData["redfirstName"]
        last_name = playerData["redlastName"]
        codename = playerData["redcodeName"]
        mh.addPlayer(playerID, first_name, last_name, codename)
        playerID = playerData["playerID"]
        first_name = playerData["firstName"]
        last_name = playerData["lastName"]
        codename = playerData["codeName"]
        mh.addPlayer(playerID, first_name, last_name, codename)