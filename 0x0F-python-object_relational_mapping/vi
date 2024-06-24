#!/usr/bin/python3
"""Write a python file that contains the class definition
   of a State and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """class State"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)

    # the class attribute cities must represent a relationship
    # with the class City
    cities = relationship("City", cascade="all")

    def __str__(self):
        """String representation"""
        return ("{}: {}".format(self.id, self.name))
