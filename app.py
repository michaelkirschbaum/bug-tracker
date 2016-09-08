#!/usr/bin/python

'''
Feature request server.
'''

from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user
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
    user = trackerUser.query.filter_by(email=request.form['email']).first()
    login_user(user)

  return redirect(url_for('form'))

@app.route("/logout")
@login_required
def logout():
  logout_user()

  return redirect(url_for('form'))

@app.route("/administer")
@login_required
def administer():
  return render_template('administration.html')

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

  login_user(user)

  return redirect(url_for('form'))

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

@app.route("/requests/<request>")
@login_required
def show_request():
  return render_template('query.html', features=Feature.query.filter_by(title=request).first())

@app.route("/clients/<client>")
@login_required
def show_client():
  return render_template('query.html', features=Feature.query.filter_by(client=client).order_by(Feature.priority).all())

@app.route("/requests")
@login_required
def show():
  return render_template('query.html', features=Feature.query.all())

if __name__ == "__main__":
  app.run()
