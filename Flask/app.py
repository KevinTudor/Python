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
Directory -> C:\Kevin\FAU\Fall 2021\Python\Homework\HW6
C:\> set FLASK_APP=p3_Tudor_Kevin
C:\> set FLASK_ENV=development
C:\> flask run
"""