# lib/helpers.py

#def helper_1():
    #print("Performing useful function#1.")


#def exit_program():
    #print("Goodbye!")
    #exit()

# helpers.py
import string
import secrets
from getpass import getpass

def generate_password(length=12):
    """Generate a secure password with a given length."""
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def get_user_input(prompt, hidden=False):
    """Get user input and optionally hide the input."""
    if hidden:
        return getpass(prompt)
    else:
        return input(prompt)

def print_menu(title, options):
    """Print a menu with a title and options."""
    print(f"\n{title}")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def get_menu_choice(options):
    """Get a valid menu choice from the user."""
    while True:
        choice = get_user_input(f"Enter your choice (1-{len(options)}): ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def show_all_passwords(passwords):
    """Print all passwords in a list."""
    if not passwords:
        print("No passwords found.")
    else:
        for password in passwords:
            print(f"ID: {password.id}, Username: {password.username}, Platform: {password.platform}, Password: {password.password}")