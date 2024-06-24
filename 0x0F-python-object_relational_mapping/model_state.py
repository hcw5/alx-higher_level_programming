#!/usr/bin/python3
"""Contains definition of class State"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
import sys

Base = declarative_base()


class State(Base):
    """Represents a State"""
    __tablename__ = 'states'

    id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        autoincrement=True
        )
    name = Column(String(128), nullable=False)
