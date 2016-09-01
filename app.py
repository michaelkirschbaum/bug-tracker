#!/usr/bin/python

'''
Feature request server.
'''

from flask import Flask, render_template, request
import json

# setup flask
app = Flask(__name__)

# routes
@app.route("/")
def get_form():
  return render_template('form.html')

from manage import db, Feature

@app.route("/submit", methods=['POST'])
def submit_feature():
  # receive JSON object
  params = request.get_json()

  # store new feature
  feature = Feature(params['title'], params['description'], params['selectedClient'], \
                params['priority'], params['date'], params['url'], params['selectedArea'])
  db.session.add(feature)
  db.session.commit()
  return render_template('form.html')

if __name__ == "__main__":
  app.run()
