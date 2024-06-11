# lib/cli.py

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, Session
import bcrypt

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    username = Column(String, primary_key=True)
    password_hash = Column(String)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

class Password(Base):
    __tablename__ = 'passwords'
    id = Column(Integer, primary_key=True)
    website = Column(String)
    username = Column(String)
    password = Column(String)
    user_id = Column(String, ForeignKey('users.username'))
    user = relationship("User", backref="passwords")

if __name__ == '__main__':
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
        print('Confirm your password:')
        confirm_password = input("> ")

        if password != confirm_password:
            print("Passwords do not match!. Please try again.")
            sign_Up()
        else:
            user = session.query(User).filter_by(username=username).first()
            if user:
                print('Username already exists. Please choose a different username.')
                sign_Up()
            else:
                new_user = User(username=username)
                new_user.set_password(password)
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
        if user and user.check_password(password):
            print("Login successful!")
            current_user = user
            menu(current_user)
        else:
            print("Invalid username or password. Please try again.")
            print("If you forgot your password, type 'Reset' to reset your password")
            action = input("> ")
            if action.lower() == 'reset':
                reset_Password(username)
            else:
                login()

    def reset_Password(username):
        user = session.query(User).filter_by(username=username).first()
        if user:
            print("Reset password for", username)
            new_password = input("Enter new password: ")
            confirm_password = input("Confirm new password: ")

            if new_password == confirm_password:
                user.password = new_password
                session.commit()
                print("Password reset successfully. Please login again.")
                login()
            else:
                print("Passwords do not match. Please try again.")
                reset_Password(username)
        else:
            print("User not found. Please try again.")
            login()

    def menu(current_user):
        print("Welcome to Encrypto. What would you like to do?:")
        print("0. Help.")
        print("1. Create a new password.")
        print("2. Manage passwords.")
        print("3. Sign Out.")
        print("4. Quit.")
        action = input("Please select an option: ")

        if action == "0":
            help_Section()
        elif action == "1":
            create_Password(current_user)
        elif action == "2":
            manage_Passwords(current_user)
        elif action == "3":
            start_screen()
        elif action == "4":
            quit()
        else:
            print("Invalid option. Please try again.")
            menu(current_user)
    
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
        print("If you need further assistance, please contact our support team @HexaForce :D")
        print("Thank you for using Encrypto!")

        print("Press Enter to go back to the menu when you are done :D")
        input()
        menu()

    def create_Password(current_user):
        print("Welcome to the Create Password Section!")
        print("Please enter the following details to create a new password:")
        website = input("Website/Application Name: ")
        username = input("Username: ")
        password = input("Password: ")

        password_obj = Password(website=website, username=username, password=password, user_id=current_user.username)
        session.add(password_obj)
        session.commit()
        print("Password stored successfully!")
        print("Press Enter to go back to the menu when you are done :D")
        input()
        menu()

    def manage_Passwords():
        print("Welcome to the Manage Passwords Section!")
        print("What would you like to do:")
        print("1. View stores passwords")
        print("2. Update stored passwords")
        print("3. Delete stored passwords")
        print("4. Search for passwords")
        print("5. Back to menu")
        action = input("Please select an option: ")

        if action == "1":
           view_passwords()
        elif action == "2":
            edit_password()
        elif action == "3":
            delete_password()
        elif action == "4":
            search_password()
        elif action == "5":
            menu()
        else:
            print("Invalid option. Please try again.")
            manage_Passwords()

    def view_passwords(current_user):
        print("Here are your stored passwords:")
        passwords = session.query(Password).filter_by(user_id=current_user.username).all()
        for password in passwords:
            print(f"Website: {password.website}, Username: {password.username}, Password: {password.password}")
        print("Press Enter to go back to the menu when you are done :D")
        input()
        manage_Passwords(current_user)
    
    def edit_password(current_user):
        print("Edit Password Section!")
        website = input("Enter the website of the password you want to edit: ")
        password_obj = session.query(Password).filter_by(website=website, user_id=current_user.username).first()
        if password_obj:
            new_password = input("Enter the new password: ")
            password_obj.password = new_password
            session.commit()
            print("Password updated successfully!")
            print("Press Enter to go back to the menu when you are done :D")
            input()
            manage_Passwords(current_user)
        else:
            print("Password not found. Please try again.")
            edit_password(current_user)

    def delete_password(current_user):
        print("Delete Password Section!")
        website = input("Enter the website of the password you want to delete: ")
        password_obj = session.query(Password).filter_by(website=website, user_id=current_user.username).first()
        if password_obj:
            session.delete(password_obj)
            session.commit()
            print("Password deleted successfully!")
            print("Press Enter to go back to the menu when you are done :D")
            input()
            manage_Passwords(current_user)
        else:
            print("Password not found. Please try again.")
            delete_password(current_user)

    def search_password(current_user):
        print("Search Password Section!")
        website = input("Enter the website of the password you want to search: ")
        password_obj = session.query(Password).filter_by(website=website, user_id=current_user.username).first()
        if password_obj:
            print(f"Website: {password_obj.website}, Username: {password_obj.username}, Password: {password_obj.password}")
            print("Press Enter to go back to the menu when you are done :D")
            input()
            manage_Passwords(current_user)
        else:
            print("Password not found. Please try again.")
            search_password(current_user)

start_screen()