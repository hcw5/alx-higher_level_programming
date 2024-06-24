#!/usr/bin/python3
"""Defines a script that prints a `State` object with name passed as arg."""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker


def print_state(usr, pwd, dB, state_name):
    """Has logic to print a `State` object with name passed as arg."""

    engine = create_engine(f'mysql+mysqldb://{usr}:{pwd}@localhost:3306/{dB}')

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).order_by(State.id)
    state = rows.filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print('Not found')


if __name__ == '__main__':
    user_name, password, db_name, state_name = sys.argv[1:]
    print_state(user_name, password, db_name, state_name)
