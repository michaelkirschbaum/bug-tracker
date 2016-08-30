import os
import unittest
import tempfile
from ..app import app

class AppTest(unittest.TestCase):

  def setUp(self):
    # self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    # app.config['TESTING'] = True

    # create test client
    self.app = app.test_client()
    self.app.testing = True
    # app.init_db()

  def tearDown(self): pass
    # os.close(self.db_fd)
    # os.unlink(app.config['DATABASE'])

  def test_getForm(self):
    response = self.app.get('/')
    self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
  unittest.main()
