#!/usr/bin/python3
"""script 14-model_city_fetch_by_state.py that prints all
City objects from the database hbtn_0e_14_usa"""
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker


def model_city():
    """initializate function model_state for db"""
    city_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)

    # associate it with our custom Session class
    Base.metadata.create_all(city_engine)
    city_session = sessionmaker()
    city_session.configure(bind=city_engine)
    session = city_session()

    rows = session.query(City, State)\
                  .filter(City.state_id == State.id)\
                  .order_by(City.id)

    for city, state in rows:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()


if __name__ == '__main__':
    model_city()
