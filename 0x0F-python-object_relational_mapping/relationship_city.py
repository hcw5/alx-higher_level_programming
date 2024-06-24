#!/usr/bin/python3
"""Write a Python file similar to model_state.py named
model_city.py that contains the class definition of a City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """class City"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      unique=True, nullable=False)

    def __str__(self):
        """string representation of class"""
        return ("{}: {}".format(self.id, self.name))
