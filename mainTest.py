from main import Password
import unittest

class TestPassword(unittest.TestCase):
    """
    This class tests the password functionality
    """
    def setUp(self):
        """
        This function creates new instance Password before each test
        """
        self.password = Password("fcc","murathe","0011")
    def tearDown(self):
        """
        Clear every password after every test for next test.
        """