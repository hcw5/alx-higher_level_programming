#!/usr/bin/python3
"""Defines a script deletes `State` objects containing letter `a`"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete


def delete_states_with_letter_a(usr, pwd, dB):
    """Has logic to delete all `State` objects containing letter `a`"""

    engine = create_engine(f'mysql+mysqldb://{usr}:{pwd}@localhost:3306/{dB}')

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    stmt = (
        delete(State).
        where(State.name.like('%a%'))
    )
    session.execute(stmt)
    session.commit()


if __name__ == '__main__':
    user_name, password, db_name = sys.argv[1:]
    delete_states_with_letter_a(user_name, password, db_name)
