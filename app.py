#!/usr/bin/python

'''
Feature request server.
'''

from flask import Flask, render_template, request, redirect, url_for
from flask.ext.login import LoginManager

# setup flask
app = Flask(__name__)

# setup user management
login = LoginManager()
login.init_app(app)

# routes
@app.route("/")
def form():
  return render_template('form.html')

from manage import db, Feature

@app.route("/submit", methods=['POST'])
def submit():
  # receive JSON object
  params = request.get_json()

  # reorganize priorities if this feature takes precedence
  features = Feature.query.filter_by(client=params['selectedClient'])\
    .order_by(Feature.priority).all()

  if params['priority'] > len(features):
    params['priority'] = len(features) + 1
  else:
    for i, ftr in enumerate(features):
      if params['priority'] == ftr.priority:
        for ftr in features[i:]:
          ftr.priority += 1
        break

  # store new feature
  feature = Feature(params['title'], params['description'], params['selectedClient'], \
                params['priority'], params['date'], params['url'], params['selectedArea'])
  db.session.add(feature)
  db.session.commit()
  return redirect(url_for('form'))

@app.route("/show")
def show(): pass

if __name__ == "__main__":
  app.run()
