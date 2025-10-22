import unittest
import json
from main import app

class FlaskApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_suma(self):
        response = self.app.get('/suma?a=2&b=3')
        data = json.loads(response.data)
        self.assertEqual(data['result'], 5)

    def test_multiplicacion(self):
        response = self.app.post('/multiplicacion', json={'a':4, 'b':5})
        data = json.loads(response.data)
        self.assertEqual(data ['result'], 20)

if __name__ == '__main__':
    unittest.main