import json
import os
from flask import Flask, request
from werkzeug.utils import secure_filename
import nltk
nltk.download('stopwords')
from pyresparser import ResumeParser

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/parse', methods = ['POST'])
def upload_file():
      print(request.files)
      f = request.files['file']
      f.save(secure_filename(f.filename))
      data = ResumeParser(f.filename).get_extracted_data()
      
      # delete the file after parsing
      os.remove(f.filename)
      
      # return stringified json object of data
      return json.dumps(data)
