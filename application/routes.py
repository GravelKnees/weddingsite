from application import app, db
from flask import render_template

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/location')
def location():
    return render_template("location.html")

@app.route('/registry')
def registry():
    return render_template("registry.html")

@app.route('/plusonerequest')
def plusonerequest():
    return render_template("plusonerequest.html")

@app.route('/rspv')
def rspv():
    return render_template("rspv.html")

@app.route('/songrequests')
def songrequests():
    return render_template("songrequests.html")