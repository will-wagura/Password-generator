# Encrypto
**Encrypto** is a simple command-line tool for managing passwords securely. Users can sign up with a username and password, and then log in to create, edit, and manage their passwords.

## Getting Started
Fork and clone the repository to your local machine

### Install Required Dependencies
While in the activated virtual environment, install the necessary dependencies using pip:
```bash
pipenv install
```
Now that your environment is set up, run : 
```bash
pipenv shell
```

### Set up the database
Create a new SQLite database file named `passwords.db` in the project directory.

`cd` into the `lib/db` directory, then run:
```bash
alembic init migrations
```
Modify line 63 in `alembic.ini` to point to the database you intend to create
```py
sqlalchemy.url = sqlite:///..
```
Regularly run 
```bash
alembic revision --autogenerate -m'<descriptive message>'
``` 
and
```bash
alembic upgrade head
```
to track your modifications to the database and create checkpoints in case you ever need to roll those modifications back.

### Run the Application
Once everything is set up Encrypto is ready to go. You can run it with Python:
```bash
python cli.py
```

### Running the tests 
To run the tests of your project, use the following command:
```bash
pytest
```

## Requirements
- Python 3.x (compatible with 3.8 and above)
- Visual studio code

## Example
Upon running the application (cli.py), you will be prompted to:
```bash
Welcome to Encrypto. What would you like to do ?

0. Help
1. Create a new password
2. Manage passwords
3. Manage accounts
4. Sign Out
5. Quit

Please select an option:
```

## Usage
### Creating a New Password
Select option 1 and follow the prompts to enter a new password for a specific service or account.

### Managing Passwords
Select option 2 to view, edit, or delete existing passwords. Follow the prompts to choose the action you want to perform.
```bash
Welcome to the password Manage section
What would you like to do ?

1. View stored passwords
2. Edit stored password
3. Delete stored password
4. Search password
5. Quit

Please select an option:
```

## Troubleshooting
- If you encounter any issues with database connections, check that your 'DATABASE_URL' environment variable has been set correctly.

- If you encounter issues with encryption, ensure that you have the latest version of 'cryptography' installed.

## Contributing
If you would like to contribute to Encrypto, please follow these guidelines:

- Fork the repository and create a new branch for your feature or fix.
- Write tests for your changes and ensure they pass.
- Submit a pull request with a clear description of your changes.

## Authors
- [Stephy Kamau](https://github.com/KWSTEPHY)
- [Abdulbarik Mohamed](https://github.com/Abdulbariky)
- [William Ndirangu](https://github.com/will-wagura)
- [Joseph Wanini](https://github.com/jwathika)
- [Victor Gachure](https://github.com/Gachure)

## Contact Information:

- Email: HexaForce

## License
- License: MIT License
