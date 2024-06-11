# lib/cli.py

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    username = Column(String, primary_key=True)
    password = Column(String)

if __name__ == '__cli__':
    engine = create_engine('sqlite:///passwords.db')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = Session()

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

        user = session.query(User).filter_by(username=username).first()
        if user:
            print('Username already exists. Please choose a different username.')
            sign_Up()
        else:
            new_user = User(username=username, password=password)
            session.add(new_user)
            session.commit()
            print('Account created successfully. Login to continue')
            start_screen()

    def login():
        print('Please enter your username:')
        username = input("> ")
        print('Please enter your password:') 
        password = input("> ")

        user = session.query(User).filter_by(username=username, password=password).first()
        if user:
            print("Login successful!")
            menu()
        else:
            print("Invalid username or password. Please try again.")
            print("If you forgot your password, type 'Reset' to reset your password")
            action = input("> ")
            if action.lower() == 'reset':
                reset_Password(username)
            else:
                login()

    def reset_Password(username):
        print("Reset password for", username)
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm new password: ")

        if new_password == confirm_password:
            user = session.query(User).filter_by(username=username).first()
            user.password = new_password
            session.commit()
            print("Password reset successfully. Please login again.")
            login()
        else:
            print("Passwords do not match. Please try again.")
            reset_Password(username)

    def menu():
        print("Welcome to Encrypto. What would you like to do?:")
        print("0. Help.")
        print("1. Store a new password.")
        print("2. Manage passwords.")
        print("3. Sign Out.")
        print("4. Quit.")
        action = input("Please select an option: ")

        if action == "0":
            help_Section()
        elif action == "1":
            store_Password()
        elif action == "2":
            manage_Passwords()
        elif action == "3":
            start_screen()
        elif action == "4":
            quit()
        else:
            print("Invalid option. Please try again.")
    
    def help_Section():
        print("Welcome to the Help Section!")
        print("Here are some tips to get you started:")
        print("")
        print("1. SignUp: Create a new account by selecting the SignUp option.")
        print("   - Enter a unique username and password to create your account.")
        print("   - You will be prompted to login after creating your account.")
        print("")
        print("2. Login: Login to your existing account by selecting the Login option.")
        print("   - Enter your username and password to access your account.")
        print("   - If you forget your password, you can try resetting it.")
        print("")
        print("3. Store a new password: Store a new password by selecting the Store a new password option.")
        print("   - Enter the website or application name, username, and password to store.")
        print("   - You can view your stored passwords by selecting the Manage passwords option.")
        print("")
        print("4. Manage passwords: Manage your stored passwords by selecting the Manage passwords option.")
        print("   - You can view, edit, or delete your stored passwords.")
        print("   - You can also search for specific passwords using the search function.")
        print("")
        print("5. Sign Out: Sign out of your account by selecting the Sign Out option.")
        print("   - You will be logged out of your account and returned to the login screen.")
        print("")
        print("6. Quit: Quit the application by selecting the Quit option.")
        print("   - You will be prompted to confirm before quitting the application.")
        print("")
        print("If you need further assistance, please contact our support team. Group 6")
        print("Thank you for using Encrypto!")

        print("Press Enter to go back to the menu when you are done :D")
        input()
        menu()

start_screen()
