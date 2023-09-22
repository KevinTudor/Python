# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor
Homework 6 Problem 3

Problem 3. Web Comment Board Application
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

"""
*In Powershell:*

Navigate to Directory
- Set flask app:  $env:FLASK_APP = "Flask\app.py"
- Check:          echo $env:FLASK_APP
- Run:            python -m flask run

Running on http://127.0.0.1:5000

*In terminal:*

Navigate to directory
- C:\> set FLASK_APP=app
- C:\> set FLASK_ENV=development
- C:\> flask run

Running on http://127.0.0.1:5000
"""