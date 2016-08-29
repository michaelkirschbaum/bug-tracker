#!/usr/bin/python

import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# setup flask
app = Flask(__name__)

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Feature(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128))
  description = db.Column(db.String(128))
  client = db.Column(db.String(128))
  priority = db.Column(db.String(128))
  date = db.Column(db.String(128))
  url = db.Column(db.String(128))
  area = db.Column(db.String(128))

# routes
@app.route("/")
def getForm():
  return render_template('form.html')

@app.route("/submit", methods=['POST'])
def request(): pass

if __name__ == "__main__":
  app.run()
