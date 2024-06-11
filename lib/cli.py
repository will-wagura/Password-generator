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
            login()
        
    def menu():
        print("Welcome to Encrypto. What would you like to do?:")
        print("0. Help")
        print("1. Store a new password")
        print("2. Manage passwords")
        print("3. Sign Out")
        print("4. Quit")
        action = input("Please select an option: ")



start_screen()
login()
