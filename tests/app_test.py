import os
import unittest
import tempfile
from ..app import app
from ..manage import db, Feature

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
    response = self.app.post('/submit', content_type='application/json', \
        data='{"title": "Feature", "description": "New feature request.", \
        "selectedClient": "Client A", "priority": 1, "date": "09/01/2016", \
        "url": "http://localhost", "selectedArea": "Reports"}')

    self.assertEqual(response.status_code, 302)

    feature = Feature("Feature", "New feature request.", "Client A", 1, \
        "09/01/2016", "http://localhost", "Reports")

    assert feature in db.session

  def test_priority_uniqueness(self):
    self.app.post('/submit', content_type='application/json', \
        data='{"title": "Feature", "description": "New feature request.", \
        "selectedClient": "Client A", "priority": 1, "date": "09/01/2016", \
        "url": "http://localhost", "selectedArea": "Reports"}')

    self.app.post('/submit', content_type='application/json', \
        data='{"title": "Feature", "description": "New feature request.", \
        "selectedClient": "Client A", "priority": 1, "date": "09/01/2016", \
        "url": "http://localhost", "selectedArea": "Reports"}')

    self.app.post('/submit', content_type='application/json', \
        data='{"title": "Feature", "description": "New feature request.", \
        "selectedClient": "Client B", "priority": 1, "date": "09/01/2016", \
        "url": "http://localhost", "selectedArea": "Reports"}')

    self.app.post('/submit', content_type='application/json', \
        data='{"title": "Feature", "description": "New feature request.", \
        "selectedClient": "Client A", "priority": 1, "date": "09/01/2016", \
        "url": "http://localhost", "selectedArea": "Reports"}')

    features = Feature.query.filter_by(client='Client A').all()
    priorities = map(lambda x: x.priority, features)

    self.assertEquals(len(set(priorities)), len(features))

    features = Feature.query.filter_by(client='Client B').first()

    self.assertEquals(features.priority, 1)

if __name__ == '__main__':
  unittest.main()
