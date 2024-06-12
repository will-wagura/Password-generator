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

    engine = create_engine('sqlite:///passwords.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(DisplayTable).all()
    textTable = Texttable()
    textTable.header(['Username', 'Password'])
    for datum in data:
        textTable.add_row([datum.username, datum.password])
        print(textTable.draw())
