#!/usr/bin/python

'''
Feature request server.
'''

from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required
from login import LoginForm

# setup flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key' # change
app.debug = True

# setup login management
login_manager = LoginManager()
login_manager.init_app(app)

from manage import db, Feature, trackerUser

# routes
@login_manager.user_loader
def load_user(user_id):
    return trackerUser.query.get(int(user_id))

@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm(csrf_enabled=False)
  if form.validate_on_submit():
    login_user(trackerUser.query.get(10))

  return redirect(url_for('form'))

@app.route("/logout")
def logout():
  return redirect(url_for('form'))

@app.route("/register")
def register():
  return render_template('register.html')

@app.route("/")
def form():
  return render_template('form.html')

@app.route("/new", methods=['POST'])
def new():
  params = request.get_json()

  # verify passwords are equal

  user = trackerUser(params['email'], params['name'], params['password'])
  db.session.add(user)
  db.session.commit()

  return redirect(url_for('form'))

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
def show():
  features = Feature.query.all()

if __name__ == "__main__":
  app.run()
