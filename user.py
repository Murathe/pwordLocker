class User:
    """
    Major user usgae details
    """

    def __init__(self, login, password):
        """
        Definitions
        """
        self.login = login
        self.password = password

    def user_exist(self, password):
        """
        Confirm user exists on query to show password - return true or false
        """
        if self.password == password:
            return True
        else:
            return False