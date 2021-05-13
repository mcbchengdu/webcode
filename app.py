#coding: utf-8

from flask import Flask
from flask.templating import render_template
app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)


