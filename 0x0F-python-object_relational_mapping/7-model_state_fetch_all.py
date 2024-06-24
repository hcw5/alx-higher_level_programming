#!/usr/bin/python3
"""Defines a script that lists all State objects from a MySQL database"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker


def print_all_states(u, p, dB):
    """Has logic to print all `State` objects from a MySQL database"""

    engine = create_engine(f'mysql+mysqldb://{u}:{p}@localhost:3306/{dB}')

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).order_by(State.id).all()
    for state in rows:
        print(f'{state.id}: {state.name}')


if __name__ == '__main__':
    user_name, password, db_name = sys.argv[1:]
    print_all_states(user_name, password, db_name)
