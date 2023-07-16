from random import randint
from flask import render_template, abort, url_for, Flask, request
import csv
import sys
from requests import get


dataset = []

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def rhlf():
    if request.method == "POST":
       # getting input
       human_identify = request.form.get("text")
       print(human_identify)
       dataset.append(human_identify)
       print(dataset)
    randomnum = str(randint(1, 100000))
    testurl = ("https://loremflickr.com/320/240/world?lock="+randomnum)
    jsonurl = get("https://loremflickr.com/json/g/320/240/world?lock="+randomnum)
    
    dataset.append(jsonurl.text)


    return render_template('rlhf.html', imgurl = testurl)

@app.route('/getdata')
def data():
    return dataset


if __name__ == "__main__":
    app.run()
