#!/usr/bin/python

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

# setup migrations
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Request(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128))
  description = db.Column(db.String(128))
  client = db.Column(db.String(128))
  priority = db.Column(db.String(128))
  date = db.Column(db.String(128))
  url = db.Column(db.String(128))
  area = db.Column(db.String(128))

if __name__ == '__main__':
    manager.run()
