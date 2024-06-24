#!/usr/bin/python3
"""Contains the class definition of a `City`"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Represents a City"""
    __tablename__ = 'cities'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )

    name = Column(String(128), nullable=False)

    state_id = Column(
        Integer,
        ForeignKey(State.id),
        nullable=False
    )
