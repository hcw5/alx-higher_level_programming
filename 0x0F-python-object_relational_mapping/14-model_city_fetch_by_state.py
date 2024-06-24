#!/usr/bin/python3
"""Defines a script that lists all `City` objects from a database"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker


def print_all_states(usr, pwd, dB):
    """Has logic to print all `City` objects from a database"""

    engine = create_engine(f'mysql+mysqldb://{usr}:{pwd}@localhost:3306/{dB}')

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).join(
        City, State.id == City.state_id
        ).order_by(City.id).all()

    for city, state in result:
        print(f'{state.name}: ({city.id}) {city.name}')


if __name__ == '__main__':
    user_name, password, db_name = sys.argv[1:]
    print_all_states(user_name, password, db_name)
