import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Contains all tests regarding user module
    """
    def setUp(self):
        """
        Create new instance before any test
        """
        self.new_user = user("murathe", "2233")

    def test_init(self):
        """
        Check user validity
        """
        self.assertEqual(self.new_user, "murathe")
        self.assertEqual(self.new_password, "2233")

    def test_user_password(self):
        """
        Check password validity
        """
        
    
if __name__ == '__main__':
    unittest.main()