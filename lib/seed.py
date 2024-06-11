from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import bcrypt
from cryptography.fernet import Fernet
from lib.cli import Base, User, Password, cipher_suite

# Generate a key for encryption and decryption
key = cipher_suite.key

# Create a new SQLAlchemy engine instance
engine = create_engine('sqlite:///passwords.db')

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Define sample data
sample_users = [
    {"username": "stephy_maina", "password": "Stunnagyal01"},
    {"username": "joseph_wanini", "password": "Juicewrld25"},
    {"username": "abdulbarik_mohamed", "password": "Isiolo254"},
    {"username": "victor_gachure", "password": "Wakadinali100"}
]

sample_passwords = [
    {"website": "example.com", "username": "user1", "password": "examplePass1", "user_id": "user1"},
    {"website": "test.com", "username": "user2", "password": "testPass2", "user_id": "user2"},
    {"website": "demo.com", "username": "user3", "password": "demoPass3", "user_id": "user3"},
]

# Insert sample data into the database
for user_data in sample_users:
    user = User(username=user_data["username"])
    user.set_password(user_data["password"])
    session.add(user)

session.commit()

for password_data in sample_passwords:
    password = Password(website=password_data["website"], username=password_data["username"], user_id=password_data["user_id"])
    password.set_password(password_data["password"])
    session.add(password)

session.commit()

print("Sample data added to the database successfully!")

# Close the session
session.close()
