#!/usr/bin/python3
"""script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa"""
from model_state import State, Base
from sqlalchemy import (create_engine)
from sys import argv
from sqlalchemy.orm import sessionmaker


def model_state():
    """initializate function model_state for db"""
    state_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)

    # associate it with our custom Session class
    Base.metadata.create_all(state_engine)

    State_Session = sessionmaker()
    State_Session.configure(bind=state_engine)
    session = State_Session()
    rows = session.query(State).order_by(State.id).all()

    name = argv[4]
    found = False

    for state in rows:
        if state.name == name:
            print('{}'.format(state.id))
            found = True
            break

    if found is False:
        print('Not found')

    session.close()


if __name__ == '__main__':
    model_state()
