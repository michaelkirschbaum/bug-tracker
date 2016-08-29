#!/usr/bin/python

import os
from flask import Flask, render_template

# setup flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# routes
@app.route("/")
def getForm():
  return render_template('form.html')

@app.route("/submit", methods=['POST'])
def request(): pass

if __name__ == "__main__":
  app.run()
