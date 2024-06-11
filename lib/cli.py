# lib/cli.py

from helpers import (exit_program, helper_1, helper_2)

Base = declarative_base()

#Added some SQLAlchemy imports for the user model to create a template
if __name__ == '__main__':
    engine = create_engine('sqlite:///passwords.db')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = Session()

    def main():
        while True:
            menu()
            choice = input("> ")
            if choice == "0":
                exit_program()
            elif choice == "1":
                helper_1()
            elif choice == "2":
                helper_2()
            else:
                print("Invalid choice")


    def start_screen():
        print('Welcome to Encrypto.')
        print('1. SignUp')
        print('2. Login')
        action = input ("Please select an option: ")

        if action == '1':
            sign_Up()
        elif action == '2':
            login()
        else:
            print('Invalid option. Please select a valid option.')
            start_screen()

    def sign_Up():
        print('Please enter your desired username:')
        username = input("> ")
        print('Please enter your desired password:')
        password = input("> ")

        #Add logic for SQAlchemy to link signup with the database to store username and password data and create a user model.

        print("Sign up successful! Please Login to continue.")
        start_screen()

    def login():
        print('Please enter your username:')
        username = input("> ")
        print('Please enter your password:') 
        password = input("> ")

        #Use SQAlchemy to query user model and see if the user and password match for now I have hardcoded the username and password. 
        if username == "Group 6" and password == "1234":
            print("Login successful!")
            menu()
        else:
            print("Invalid username or password. Please try again.")
            login()
        
    def menu():
        print("Welcome to Encrypto. What would you like to do?:")
        print("0. Help")
        print("1. Create a new password")
        print("2. Manage passwords")
        print("3. Quit")



start_screen()
login()
