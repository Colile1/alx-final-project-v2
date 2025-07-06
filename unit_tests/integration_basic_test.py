import unittest
from plant_care_dashboard.backend.app import app

class IntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_backend_root_and_frontend_render(self):
        # Test backend root endpoint
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

        # Frontend rendering test would normally require a browser environment or JS test framework
        # Here we just confirm the frontend app file exists
        import os
        frontend_app_path = 'plant_care_dashboard/frontend/my-plant-app/src/App.svelte'
        self.assertTrue(os.path.exists(frontend_app_path), f"{frontend_app_path} should exist")

if __name__ == '__main__':
    unittest.main()
