#!/usr/bin/python3
"""Defines a script that lists the first State object from a MySQL table"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker


def print_first_state(usr, pwd, dB):
    """Has logic to print first `State` object from a MySQL database table"""

    engine = create_engine(f'mysql+mysqldb://{usr}:{pwd}@localhost:3306/{dB}')

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_row = session.query(State).order_by(State.id).first()
    if first_row:
        print(f'{first_row.id}: {first_row.name}')
    else:
        print('Nothing')


if __name__ == '__main__':
    user_name, password, db_name = sys.argv[1:]
    print_first_state(user_name, password, db_name)
