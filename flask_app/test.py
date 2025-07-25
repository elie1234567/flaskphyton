import unittest
import app

class TestHello(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.client = app.app.test_client()

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.data, b'Hello World!\n')

    def test_hello_user(self):
        response = self.client.get('/hello/Lahatra')
        self.assertEqual(response.status, '200 OK')
        self.assertIn(b'Lahatra', response.data)

if __name__ == '__main__':
    unittest.main()