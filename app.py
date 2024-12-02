from flask import Flask, render_template, redirect, Blueprint
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/playing')
def gametime():
    return render_template('waiting.html')



@app.errorhandler(HTTPException)
def misc_error(e):
    return render_template("error.html", error=e), e.code

