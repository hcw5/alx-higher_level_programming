#!/usr/bin/python3
"""Defines a script that adds a `State` object `Louisiana` to db table"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker


def add_state(usr, pwd, dB):
    """Has logic to add a `State` object to a db table"""

    engine = create_engine(f'mysql+mysqldb://{usr}:{pwd}@localhost:3306/{dB}')

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    s_id = session.query(State.id).filter(State.name == 'Louisiana').first()
    print(s_id[0])


if __name__ == '__main__':
    user_name, password, db_name = sys.argv[1:]
    add_state(user_name, password, db_name)
