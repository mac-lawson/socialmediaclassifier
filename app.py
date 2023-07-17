from flask import render_template, abort, url_for, Flask, request
from models.classify import classify
from models.process import Process
import requests


app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def home():
    # if request.method == "POST":

    return render_template("index.html")
