#!/usr/bin/env python3
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
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    email = Column(String(50), nullable=False)
    phone_no = Column(Integer(), nullable=False)
    password = Column(String(50), nullable=False)
    items_found = relationship('Items', backref='users')
    connected_items_owner = relationship('Connected_Items', foreign_keys='Connected_Items.owner_id', backref='owner')
    connected_items_reporter = relationship('Connected_Items', foreign_keys='Connected_Items.reporter_id', backref='reporter')

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}, {self.email}>'
    
class Items(Base):
    __tablename__ = 'items_found'

    id = Column(Integer, primary_key=True)
    date_found = Column(DateTime, default=datetime.now())
    location_found = Column(String(50))
    description = Column(Text(64000))
    filename = Column(String(50))
    category = Column(String(50))
    users_id = Column(Integer, ForeignKey('users.id'))


class Connected_Items(Base):
    __tablename__  = 'connected_items'
    item_id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    reporter_id = Column(Integer, ForeignKey('users.id'))
    date_connected = Column(DateTime)
    location_connected = Column(String(50))
