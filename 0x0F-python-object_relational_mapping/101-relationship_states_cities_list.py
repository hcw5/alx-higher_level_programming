#!/usr/bin/python3
"""script that lists all State objects, and corresponding
City objects, contained in the database hbtn_0e_101_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State
from relationship_city import City


def list_state_cities():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()

    result = session.query(State).all()

    for state in result:
        print(str(state.id) + ': ' + state.name)
        for city in state.cities:
            print('\t' + str(city.id) + ': ' + city.name)


if __name__ == '__main__':
    list_state_cities()
