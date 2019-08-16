""" Test a successful build of the flask application"""

import os
import sys
import unittest
from server import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestApp(unittest.TestCase):
    """ Test for a successful build of a flask app"""

    @classmethod
    def setUpClass(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage_status_code(self):
        """
        Sends an HTTP GET request to the application homepage and asserts
        it was successful
        """
        result = self.app.get('/')
        status_code = result.status_code
        self.assertEqual(status_code, 200,
                         msg='Home status code {code}. Should be 200'.format(code=status_code))

if __name__ == "__main__":
    unittest.main()
