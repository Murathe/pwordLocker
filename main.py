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

    