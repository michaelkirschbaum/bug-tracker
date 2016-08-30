import os
import unittest
import tempfile
from ..app import app

class AppTest(unittest.TestCase):

  def setUp(self):
    self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    self.app = app.test_client()
    # app.init_db()

  def tearDown(self):
    os.close(self.db_fd)
    os.unlink(app.config['DATABASE'])

  def test_empty(self): pass

if __name__ == '__main__':
  unittest.main()
