from random import random

class Password:
    """
    New password generator
    """
    Password_list = []

    def __init__(self, username, email, password):
        """
        Create instances of the major class
        """
        self.username = username
        self.email = email
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
        pass