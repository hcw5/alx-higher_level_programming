#!/usr/bin/python3
"""script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def relationship_state():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1],
                                  argv[2],
                                  argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    c = City(name='San Francisco')
    s = State(name='California', cities=[c])
    session.add(s)
    session.add(c)
    session.commit()
    session.close()


if __name__ == "__main__":
    relationship_state()
