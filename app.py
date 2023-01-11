from flask import Flask, redirect, render_template, request


app = Flask(__name__)


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

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')