from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
import pandas as pd

app = Flask(__name__)

# # enable debugging mode
# app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


# Root URL
@app.route('/')
def index():
     # Set The upload HTML template '\templates\index.html'
    return render_template('index.html')


# Get the uploaded files
@app.route("/", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
          # save the file
      return redirect(url_for('index'))

if (__name__ == "__main__"):
     app.run(port = 5000)

def parseCSV(filePath):
      # CVS Column Names
      col_names = ['Id','UserId','HelpfulnessNumerator', 'HelpfulnessDenominator', 'Score']
      # Use Pandas to parse the CSV fil
      csvData = pd.read_csv(filepath = '/home/labuser/Desktop/Project/Reviews.csv',names=col_names, header=None)
      # Loop through the Rows
      for i,row in csvData.iterrows():
           print(i, row['Id'], row['UserId'], row['HelpfulnessNumerator'], row['HelpfulnessDenominator'], row['Score'], )

