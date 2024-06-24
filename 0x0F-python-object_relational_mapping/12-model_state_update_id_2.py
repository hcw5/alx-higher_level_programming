#!/usr/bin/python3
"""Defines a script changes the name of a `State` object from a db table"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update


def change_state_name(usr, pwd, dB):
    """Has logic to change the name of a `State` object to a db table"""

    engine = create_engine(f'mysql+mysqldb://{usr}:{pwd}@localhost:3306/{dB}')

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    stmt = (
        update(State).
        where(State.id == 2).
        values(name='New Mexico')
    )
    session.execute(stmt)
    session.commit()


if __name__ == '__main__':
    user_name, password, db_name = sys.argv[1:]
    change_state_name(user_name, password, db_name)
