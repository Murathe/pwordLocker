from main import Password
from user import User
import getpass
import random

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
    print("You welcome to Pword Locker.\n")
    print("-"*20, "Sign up", "-"*20, "\n")

    name = input("Your name\n")
    print("*" *4,f"Welcome {name} . What's next?", "*"*4, "\n")

    while True:
        command = input(
            "Here: 'gen' for an account with a ready password, 'gent' for an account with your preffered password, del' to delete a password, 'addnew' to add an existing password, 'viewall' to view all your generated passwords or, 'exit' to leave:( \n"
        )
        command = input().lower()
        if command == 'addnew':
            print("Now that you here, let's build a password \n")
            site = input("The site you want a passwor dfor is?\n")
            user_name = input("A unique username please?\n")
            password = getpass.getpass("You unique password is?\n")
            
            add_password(password)
        elif command == 'gent':
            print("New passwords are secure\n")
            site = input("The site you want a passwor dfor is?\n")
            user_name = input("A unique username please?\n")
            password = input()
            print("\n")
            print(f"Your {site} account with a username of {user_name} and '{password}' as password has been created & saved")
            print("*" *30)
            # length = input("How long do you want it to be?\n")
            # try:
            #     add_password(password)
            #     print(f"Password generated for {site}\n")
            # except ValueError:
            #     print("The length value should be a number\n")
        elif command == 'gen':
            print("Let's build an account with the safest passowrd\n")
            site = input("Site name\n")
            user_name = input("Preffered username\n")

            m = "nhjk34juyFRGNhDG./)9("
            password = "".join(random.sample(m, 10))
            print("-"*20)
            print(f"Your {site} account with a username of {user_name} and '{password}' as password has been created & saved")
            print("*" *30)
        elif command == 'viewall':
            if view_passwords():
                for password in Password.Password_list:
                    print("-"*4, view_passwords().index(password)+1, "-"*4, "\n")
                    print(f"Username --> {password.username}\n")
                    print(f"Password --> {password.password}\n")
            else:
                print("Save some passwords and I'll have some to display next time\n")
        elif command =='del':
            print("This the original rabbit hole, you sure want to delete it?\n")
            pass_word = getpass.getpass("May I hav the password to be deleted?\n")
            if pass_word == user_pass:
                site = input("Give me the site name you no longer needs\n")
                if password_exists(site):
                    delete_password(site)
                    print(f"{site} password has been deleted\n")
                else:
                    print("That site and password does not exist\n")
            else:
                print("Wrong password, give it another trial\n")
        elif command == 'exit':
            break      

if __name__ == "__main__":
    main()





