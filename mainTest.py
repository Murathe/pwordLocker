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
        Password.password = []
    def test_new_password(self):
        """
        Test if a new password is generated correctly
        """
        self.assertEqual(self.new_password.account, "fcc")
        self.assertEqual(self.new_password.username, "murathe")
        self.assertEqual(self.new_password.password, "0011")

    def test_save_new_password(self):
        """
        Test if new password has been added to initial list succesfuly
        """
        self.new_password.save_password()
        self.asserEqual(len(Password.password_list), 1)

    def test_add_generate_password(self):
        """
        Check if newly generated password is addesd to the list
        """
        new_password = Password("udacity", "1122", Password.generate_(6))
        new_password.save_password()
        self.assertEqual(len(Password.password))

    def save_password(self):
        self.new_password.save_password()
        new_pass = Password("udacity", "1122")
        new_password.save_password()
        self.assertEqual(len(Password.password),
                        len(Password.display_passwords()))

    def test_delete(self):
        """
        Confirm the delete function
        """
        self.new_password.save_password()
        new_password = Password("udacity", "1122")
        new_password.save_password()
        Password.delete_password("udemy")
        self.assertEqual(len(Password.Password_list), 1)

    def test_password_exist(self):
        """
        Confirm password query function if it works
        """
        self.new_password.save_password()
        self.assertEqual(len(Password.Password_list), 1)

    if __name__ == "__main__":
        unittest.main()