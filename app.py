from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #to get rid of warning
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")