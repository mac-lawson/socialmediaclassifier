from random import randint
from flask import render_template, abort, url_for, Flask, request
import csv

def add_to_dataset(image_url, description):
    # Open the CSV file in append mode
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the image URL and description as a single row with a comma between them
        writer.writerow([f'{image_url},{description}'])

def get_dataset():
    # Create an empty list to store the rows
    rows = []
    
    # Open the CSV file
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        
        # Iterate over each row in the CSV and add it to the list
        for row in reader:
            rows.append(row)
    
    # Return the list of rows
    return rows

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def rhlf():
    testurl = "https://loremflickr.com/320/240/world?lock="+str(randint(1, 100000))
    if request.method == "POST":
       # getting input
       human_identify = request.form.get("text")
       print(human_identify)
       add_to_dataset(testurl, human_identify)
       get_dataset()

    return render_template('rlhf.html', imgurl = testurl)

@app.route('/getdata')
def data():
    return render_template('blank.html', data=get_dataset())


if __name__ == "__main__":
    app.run()
