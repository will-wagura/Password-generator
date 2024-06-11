from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.cli import Base, User, Password, cipher_suite

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
    {"username": "stephy_maina", "password": "Abcd12345"},
    {"username": "joseph_wanini", "password": "Abcd12345"},
    {"username": "abdulbarik_mohamed", "password": "Abcd12345"},
    {"username": "victor_gachure", "password": "Abcd12345"}
]

sample_passwords = [
    {"website": "example.com", "username": "user2@example.com", "password": "examplePass1", "user_id": "stephy_maina"},
    {"website": "test.com", "username": "user3@test.com", "password": "testPass2", "user_id": "joseph_wanini"},
    {"website": "demo.com", "username": "user4@demo.com", "password": "demoPass3", "user_id": "abdulbarik_mohamed"},
    {"website": "facebook.com", "username": "user5@facebook.com", "password": "fbUser1Pass", "user_id": "victor_gachure"},
    {"website": "twitter.com", "username": "user2@twitter.com", "password": "twUser2Pass", "user_id": "stephy_maina"},
    {"website": "linkedin.com", "username": "user3@linkedin.com", "password": "lnUser3Pass", "user_id": "joseph_wanini"},
    {"website": "github.com", "username": "user4@github.com", "password": "ghUser1Pass", "user_id": "abdulbarik_mohamed"},
    {"website": "gmail.com", "username": "user5@gmail.com", "password": "gmailUser2Pass", "user_id": "victor_gachure"},
    {"website": "yahoo.com", "username": "user2@yahoo.com", "password": "yahooUser3Pass", "user_id": "stephy_maina"},
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
