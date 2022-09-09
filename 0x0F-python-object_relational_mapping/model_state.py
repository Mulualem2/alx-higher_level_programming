#!/usr/bin/python3
"""Starts the link with the database"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """A class that links with MySQL table states"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
