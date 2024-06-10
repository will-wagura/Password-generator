from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from texttable import Texttable

Base = declarative_base()

class DisplayTable(Base):

    __tablename__ = 'passwords'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


    def __repr__(self):
        return f"Password(id={self.id}, username='{self.username}', password='{self.password}')"

if __name__ == '__main__':
