#! /usr/bin/python
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "whatever floats your boat"

# SQLAlchemy object
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)

# Models
class Stuff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.Text)
    email = db.Column(db.String(60))

# Views
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def main():

    return render_template('index.html')



if __name__== '__main__':
    app.run(debug=True)
