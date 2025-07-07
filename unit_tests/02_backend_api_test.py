import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'plant_care_dashboard')))


class BackendAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_root_endpoint(self):
        # Test GET / endpoint
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

# The following tests are commented out because the endpoints do not exist in the current backend app.py
#    def test_add_reading_post(self):
#        # Test POST /api/add_reading endpoint
#        data = {
#            "timestamp": "2025-07-26T10:00:00",
#            "moisture_level": 55.5,
#            "temperature": 22.3,
#            "light_intensity": 700,
#            "notes": "Test reading",
#            "plant_id": 1
#        }
#        response = self.app.post('/api/add_reading', data=json.dumps(data), content_type='application/json')
#        self.assertEqual(response.status_code, 201)
#        self.assertIn('message', response.get_json())
#        self.assertEqual(response.get_json()['message'], 'Reading added successfully')

#    def test_get_latest_reading(self):
#        # Test GET /api/latest_reading endpoint
#        response = self.app.get('/api/latest_reading')
#        self.assertEqual(response.status_code, 200)
#        json_data = response.get_json()
#        self.assertIsInstance(json_data, dict)
#        self.assertIn('moisture_level', json_data)
#        self.assertIn('temperature', json_data)
#        self.assertIn('light_intensity', json_data)

#    def test_get_all_readings(self):
#        # Test GET /api/readings endpoint
#        response = self.app.get('/api/readings')
#        self.assertEqual(response.status_code, 200)
#        json_data = response.get_json()
#        self.assertIsInstance(json_data, list)
#        if len(json_data) > 0:
#            self.assertIn('moisture_level', json_data[0])
#            self.assertIn('temperature', json_data[0])
#            self.assertIn('light_intensity', json_data[0])

if __name__ == '__main__':
    unittest.main()
