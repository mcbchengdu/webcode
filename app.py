#coding: utf-8

from flask import Flask
from flask.templating import render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap=Bootstrap(app)



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/test')
def test():
    return render_template('test.html')

