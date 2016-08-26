#!/usr/bin/python

from flask import Flask
from flask import render_template
import sqlalchemy

# setup flask
app = Flask(__name__)

# routes
@app.route("/")
def index():
  return render_template('index.html')

if __name__ == "__main__":
  app.run()
