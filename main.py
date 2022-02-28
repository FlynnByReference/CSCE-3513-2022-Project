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
playerID = 0
#mh.addPlayer(11, "Jase", "Cornett", "Jazer")

# @app.route("/")
# def home():
#     return render_template('splitPlayers.html')

# @app.route('/test', methods = ['GET', 'POST'])
# def addPlayerThroughMH():
#     if(request.method == 'POST'):
#         id = 1
#         first_name = request.form.get('first')
#         last_name = request.form.get('last')
#         codename = request.form.get('code')
#         mh.addPlayer(id, first_name, last_name, codename)
#         # playerinfo = {id, first_name, last_name, codename}
#         # return jsonify(playerinfo)

@app.route("/")
def home():
    return render_template('splitPlayers.html')

@app.route('/', methods = ['POST'])
def addPlayerThroughMH():
    if request.method == "POST":
        playerID = 1
        first_name = request.form["first"]
        last_name = request.form["last"]
        codename = request.form["code"]
        mh.addPlayer(playerID, first_name, last_name, codename)
    
    # jsdata = request.form['javaScriptData']
    # return json.loads(jsdata)[0]
    
    
    
        #yemh.addPlayer(id, first_name, last_name, codename)
        # playerinfo = {id, first_name, last_name, codename}
        # return jsonify(playerinfo)
#class User_update(webapp2.RequestHandler):
#val_no = self.request.Post['no']
#val_name = self.request.POST['none']