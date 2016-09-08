import os
import unittest
import tempfile
from ..app import app
from ..manage import db, Feature, trackerUser

class AppTest(unittest.TestCase):
  def setUp(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_TEST_URL")
    app.config['TESTING'] = True
    self.app = app.test_client()
    db.create_all()

    # login user
    self.app.post('/new', content_type='application/json', \
        data='{"email": "testuser@gmail.com", "name": "test", \
        "password": "test_password"}')

  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_login(self):
    res = self.app.get('/login')
    self.assertEqual(res.status_code, 302)

  def test_logout(self):
    res = self.app.get('/logout')
    self.assertEqual(res.status_code, 302)

  def test_register_form(self):
    response = self.app.get('/register')
    self.assertEqual(response.status_code, 200)

  def test_get_form(self):
    response = self.app.get('/')
    self.assertEqual(response.status_code, 200)

  def test_new_user(self):
    user = trackerUser("testuser@gmail.com", "test", "test_password")
    user2 = trackerUser.query.get(1)

    self.assertEqual(user.email, user2.email)
    self.assertEqual(user.name, user2.name)
    self.assertEqual(user.password, user2.password)

  def test_submit_feature(self):
    response = self.app.post('/submit', content_type='application/json', \
        data='{"title": "Feature", "description": "New feature request.", \
        "selectedClient": "Client A", "priority": 1, "date": "09/01/2016", \
        "url": "http://localhost", "selectedArea": "Reports"}')

    self.assertEqual(response.status_code, 302)

    feature = Feature("Feature", "New feature request.", "Client A", 1, \
        "09/01/2016", "http://localhost", "Reports")
    feature2 = Feature.query.get(1)

    self.assertEqual(feature.title, feature2.title)
    self.assertEqual(feature.description, feature2.description)
    self.assertEqual(feature.client, feature2.client)
    self.assertEqual(feature.priority, feature2.priority)
    self.assertEqual(feature.area, feature2.area)

  def test_priority_uniqueness(self):
    self.app.post('/submit', content_type='application/json', \
        data='{"title": "Feature 1", "description": "New feature request.", \
        "selectedClient": "Client A", "priority": 1, "date": "09/01/2016", \
        "url": "http://localhost", "selectedArea": "Reports"}')

    self.app.post('/submit', content_type='application/json', \
        data='{"title": "Feature 2", "description": "New feature request.", \
        "selectedClient": "Client A", "priority": 1, "date": "09/01/2016", \
        "url": "http://localhost", "selectedArea": "Reports"}')

    self.app.post('/submit', content_type='application/json', \
        data='{"title": "Feature 3", "description": "New feature request.", \
        "selectedClient": "Client B", "priority": 1, "date": "09/01/2016", \
        "url": "http://localhost", "selectedArea": "Reports"}')

    self.app.post('/submit', content_type='application/json', \
        data='{"title": "Feature 4", "description": "New feature request.", \
        "selectedClient": "Client A", "priority": 1, "date": "09/01/2016", \
        "url": "http://localhost", "selectedArea": "Reports"}')

    featuresA = Feature.query.filter_by(client='Client A').all()
    priorities = map(lambda x: x.priority, featuresA)

    self.assertEquals(len(set(priorities)), len(featuresA))

    featuresB = Feature.query.filter_by(client='Client B').first()

    self.assertEquals(featuresB.priority, 1)

    self.app.post('/submit', content_type='application/json', \
        data='{"title": "Feature 5", "description": "New feature request.", \
        "selectedClient": "Client A", "priority": 10, "date": "09/01/2016", \
        "url": "http://localhost", "selectedArea": "Reports"}')

    feature = Feature.query.filter_by(title="Feature 5").first()

    self.assertEquals(feature.priority, len(featuresA) + 1)

  def test_request_display(self): pass

if __name__ == '__main__':
  unittest.main()
