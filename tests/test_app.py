import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Hello, Agile World!'})

    def test_status(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'OK', 'version': '1.0.0'})

if __name__ == '__main__':
    unittest.main()
