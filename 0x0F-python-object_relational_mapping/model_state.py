#!/usr/bin/python3
""" Define a class State """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ state class inherits from Base

    id: represents a column of an auto-generated, unique int
        and can't be null
    name: represents column of a string with 128 characters
            and can't be null
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
