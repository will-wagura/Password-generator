# lib/cli.py

from helpers import (exit_program, helper_1, helper_2)


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
    username = 'Group 6'
    action = input("Enter your username: ")
    if action != username:
        print("Invalid username. Please try again.")
    if action == username:
        menu()

    print('Please enter your password:')
    password = '1234'
    action = input('Enter your password: ') 
    if action != password:
        print('Invalid credentials. Please try again.')
    if action == password:
        menu()
    
def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("2. Create new account")


if __name__ == "__main__":
    main()
