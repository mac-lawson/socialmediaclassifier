from flask import render_template, abort, url_for, Flask, request
from models.classify import classify
from models.process import Process
import requests


app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        url_to_scan = str(request.form.get("urlinput"))
        content = str(classify(url_to_scan))
        print(content)
        processor = Process(content)
        return render_template("site/index.html", classifier=str(content), judgement=str(processor.sentiment(str(processor.judge()))))
        
    return render_template("site/index.html", classifier="", judgement="")

def team():
    return render_template("site/team.html")
def about():
    return render_template("site/about.html")

if __name__ == "__main__":
    app.run()