#!/usr/bin/python

'''
Feature request server.
'''

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required
from Login import LoginForm

# setup flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'v.G8GyY*)>011nOp'
app.debug = True

# setup user management
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "form.html"

from manage import db, Feature, trackerUser

# routes
@login_manager.user_loader
def load_user(user_id):
  return trackerUser.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm(csrf_enabled=False)
  if form.validate_on_submit():
    user = trackerUser.query.filter_by(name=request.form['name']).first()
    login_user(user)

  flash("Log in successful")

  return render_template('form.html')

@app.route("/")
def form():
  return render_template('form.html')

@app.route("/submit", methods=['POST'])
@login_required
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
@login_required
def show(): pass

if __name__ == "__main__":
  app.run()
