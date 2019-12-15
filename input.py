from main import Password
from user import User
import getpass

def new_user(login, Password):
    """
    Creates new user on every login
    Args:
        login - user_name
        password - generated password
    Return:
        new user instance
    """
    user = user(login, password)
    return user

def add_password(password):
    """
    Append new password to passwords list
    """
    Password.save_password(password)

def generate_password(length):
    """
    Generate a random password
    Args:
        length - password length
    Return:
        display generated password
    """
    return Password.generate_pass(length)

def view_passwords():
    """
    DIsplay all generated passwords
    """
    return Password.display_passwords()

def dlete_password(site):
    """
    Delete password for specific site
    """
    Password.delete_password(site)

def password_exists(site):
    """
    Check is password exist and return True or False
    """
    return Password.password_exist(site)

def main():
    """
    Run major functions
    """
    print("\n")
    print("You welcome to Pword Locker. Here to guranatee you a safe storage of your important security aspect\n")
    print("-"*6, "Sign up", "-"*6, "\n")

    user_name = input("Username\n")
    user_pass = getpass.getpass("Password:\n")

    """
    New user login
    """

    print(f"Welcome back {user_name}\n")
    print("What's next?")

    while True:
        command = input(
            "Here you can 'generate' to generate a new password, 'del' to delete a password, 'add' to add an existing password, 'view' to view all your generated passwords or, 'exist' to leave:( \n"
        )
        if command == "add":
            print("Not that you here, let's build a password \n")
            site = input("The site you want a passwor dfor is?\n")
            user_name = input("A unique username please?")
            password = getpass.getpass("You unique password is?\n")
            
            add_password(password)









