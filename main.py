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
from midhand import connectToHeroku 

app = Flask(__name__)
mh = connectToHeroku(11, "David", "Hammons", "Davy Gravy")
mh.addPlayer()

@app.route("/")
def home():
    return render_template('PlayerScreen.html')

def addPlayerThroughMH():
    pass