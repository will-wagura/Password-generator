# lib/cli.py

from helpers import (exit_program, helper_1, helper_2)

Base = declarative_base()

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

    def login():
        print('Please enter your username:')
        print('Please enter your password:') 
        username = 'Group 6'
        password = '1234'
        action = input("Enter your username: ")
        action = input('Enter your password: ')
        if action != username and password:
            print("Invalid username. Please try again.")
        if action == username and password:
            menu()
        
    def menu():
        print("Welcome to Encrypto. What would you like to do?:")
        print('Please select an option:')
        print("0. Help")
        print("1. Create a new password")
        print("2. Manage passwords")


start_screen()
login()
