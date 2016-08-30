import os
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# setup database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# setup migration
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Feature(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128))
  description = db.Column(db.String(128))
  client = db.Column(db.String(128))
  priority = db.Column(db.String(128))
  date = db.Column(db.String(128))
  url = db.Column(db.String(128))
  area = db.Column(db.String(128))

  def __init__(self, title, description, client, priority, date, url, area):
    self.title = title
    self.description = description
    self.client = client
    self.priority = priority
    self.date = date
    self.url = url
    self.area = area

if __name__ == '__main__':
    manager.run()
