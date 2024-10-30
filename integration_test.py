import unittest
import requests

class TestFlaskApiIntegration(unittest.TestCase):
    def setUp(self):
        self.BASE_URL = 'http://localhost:5000'
        
    def test_home_endpoint_integration(self):
        # Test the home endpoint
        response = requests.get(f"{self.BASE_URL}/")
        
        # Check status code
        self.assertEqual(response.status_code, 200)
        
        # Check response content
        data = response.json()
        self.assertEqual(data['message'], 'Hello level 400 FET, Quality Assurance!')

if __name__ == '__main__':
    unittest.main()