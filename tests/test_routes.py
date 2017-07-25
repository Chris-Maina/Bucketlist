"""test_routes.py"""
import unittest
from app import app

class TestCasesRoutes(unittest.TestCase):
    """Test status code of index page
        Test status code of login page
        Test status code of Registatration page
    """
    def setUp(self):
        """
        """
        self.app = app.test_client()
    def tearDown(self):
        pass

    def test_index_page(self):
        """Checks if index page has a success status code
        """
        msg = self.app.get('/')
        self.assertEqual(msg.status_code, 200)

    def test_registration_page(self):
        """Checks if register page has a success status code
        """
        msg = self.app.get('/register')
        self.assertEqual(msg.status_code, 200)
        msg = self.app.post('/register')
        self.assertEqual(msg.status_code, 400)
    def test_login_page(self):
        """Checks if login page has a success status code
        """
        msg = self.app.get('/login')
        self.assertEqual(msg.status_code, 200)
        msg = self.app.post('/login')
        self.assertEqual(msg.status_code, 400)

    def test_bucket_page(self):
        """Checks if login page has a success status code
        """
        msg = self.app.get('/bucketlist-bucket')
        self.assertEqual(msg.status_code, 200)
        msg = self.app.post('/bucketlist-bucket')
        self.assertEqual(msg.status_code, 200)

    def test_activity_page(self):
        """Checks if login page has a success status code
        """
        msg = self.app.get('/bucketlist-activity/<bucketname>')
        self.assertEqual(msg.status_code, 200)
        # posting with a bucket name
        msg = self.app.post('/bucketlist-activity/<bucketname>')
        self.assertEqual(msg.status_code, 200)
