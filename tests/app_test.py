import os
import unittest
import tempfile
from ..app import app

class AppTest(unittest.TestCase):
  def setUp(self):
    app.config['TESTING'] = True
    self.app = app.test_client()

  def tearDown(self): pass

  def test_get_form(self):
    response = self.app.get('/')
    self.assertEqual(response.status_code, 200)

  def test_submit_feature(self): pass

if __name__ == '__main__':
  unittest.main()
