#!/usr/bin/python

'''
Feature request server.
'''

from flask import Flask, render_template, request

# setup flask
app = Flask(__name__)

# routes
@app.route("/")
def getForm():
  return render_template('form.html')

# store form
from manage import db, Feature
@app.route("/submit", methods=['POST'])
def submit_feature():
  feature = Feature()
  db.session.add(feature)
  db.session.commit()

if __name__ == "__main__":
  app.run()
