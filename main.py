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

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('PlayerScreen.html')





