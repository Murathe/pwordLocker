from random import random

class Password:
    """
    New password generator
    """
    Password_list = []

    def __init__(self, site, username, password):
        """
        Create instances of the major class
        """
        self.site = site
        self.username = username
        self.password = password

    def save_password(self):
        """
        Save newly generated passwords to the array
        """
        Password.password_list.append(self)

    def show_passwords(self):
        """
        Display a list of passwords
        """
        return self.Password_list

    def remove_password(self):
        """
        This function removes a password from the saved list
        """
        Password.Password_list.remove(self)

    @classmethod
    def password_exist(cls, email):
        """
        Query along to see if password exists
        """
        for password in cls.password_list:
            if password_site.lower() == site.lower():
                return true
            return False