import unittest
from app import app #This line imports the flask application intance from app module
import json

class TestFlaskApp(unittest.TestCase):
    def setUp(self): #this is the start of setup method which is a special method in unit test that is run before each test method in the class
        # Create a test client
        self.app = app.test_client() 
        self.app.testing = True

    def test_home_route(self): #this line defines a test method that starts with the word test
        # Send a GET request to the home route
        response = self.app.get('/')
        
        # Convert the response data from bytes to string and then to JSON
        data = json.loads(response.data.decode('utf-8'))
        
        # Assert the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Assert the returned message matches expected
        self.assertEqual(data['message'], 'Hello level 400 FET, Quality Assurance!')
        
    def test_home_route_content_type(self):
        # Test if the response is JSON
        response = self.app.get('/')
        self.assertEqual(response.content_type, 'application/json')

if __name__ == '__main__':
    unittest.main()