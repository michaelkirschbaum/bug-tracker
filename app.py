#!/usr/bin/python

import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# setup flask
app = Flask(__name__)

# setup database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

# routes
@app.route("/")
def getForm():
  return render_template('form.html')

@app.route("/submit", methods=['POST'])
def request():
  from model import Request

if __name__ == "__main__":
  app.run()
