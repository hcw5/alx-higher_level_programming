#!/usr/bin/python3
"""Defines a script that lists `states` with letter `a` in a MySQL db table"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker


def print_states_with_letter_a(usr, pwd, dB):
    """Has logic to print `State` objects having letter `a`"""

    engine = create_engine(f'mysql+mysqldb://{usr}:{pwd}@localhost:3306/{dB}')

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).order_by(State.id)
    rows = rows.filter(State.name.like(f'%a%'))
    for state in rows:
        print(f'{state.id}: {state.name}')


if __name__ == '__main__':
    user_name, password, db_name = sys.argv[1:]
    print_states_with_letter_a(user_name, password, db_name)
