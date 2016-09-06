#!/usr/bin/python

'''
Database and migrations build script.
'''

import os
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import UserMixin

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# setup migrations script
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# models
class Feature(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(32))
  description = db.Column(db.String(1000))
  client = db.Column(db.String(8))
  priority = db.Column(db.Integer)
  date = db.Column(db.Date)
  url = db.Column(db.String(32))
  area = db.Column(db.String(10))

  def __init__(self, title, description, client, priority, date, url, area):
    self.title = title
    self.description = description
    self.client = client
    self.priority = priority
    self.date = date
    self.url = url
    self.area = area

class trackerUser(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(32))
  name = db.Column(db.String(32))
  password = db.Column(db.String(32))

  def __init__(self, email, name, password):
    self.email = email
    self.name = name
    self.password = password

if __name__ == '__main__':
    manager.run()
