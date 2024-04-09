#!/usr/bin/en python3
"""
Module for the user database
"""

from datetime import datetime
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, DateTime, Integer, Text, ForeignKey

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50))
    phone_no = Column(Integer())
    password = Column(String(50))
    items_found = relationship('Items', backref='users')


class Items(Base):
    __tablename__ = 'items_found'

    id = Column(Integer, primary_key=True)
    date_found = Column(DateTime)
    location_found = Column(String(50))
    description = Column(Text(64000))
    filename = Column(String(50))
    category = Column(String(50))
    users_id = Column(Integer, ForeignKey('users.id'))


class Connected_Items(Base):
    __tablename__  = 'connected_items'
    item_id = Column(String(50), primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    reporter_id = Column(Integer, ForeignKey('users.id'))
    date_connected = Column(DateTime)
    location_connected = Column(String(50))
