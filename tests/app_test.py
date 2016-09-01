import os
import unittest
import tempfile
from ..app import app
from ..manage import db, Feature
from werkzeug.test import EnvironBuilder

class AppTest(unittest.TestCase):
  def setUp(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_TEST_URL")
    app.config['TESTING'] = True
    self.app = app.test_client()
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_get_form(self):
    response = self.app.get('/')
    self.assertEqual(response.status_code, 200)

  def test_submit_feature(self):
    self.app.post('/submit', content_type='application/json', \
        data='{"title": "Feature", "description": "New feature request.", \
        "client": "Client A", "priority": "1", "date": "09/01/2016", \
        "url": "http://localhost", "area": "Reports"}')

if __name__ == '__main__':
  unittest.main()
