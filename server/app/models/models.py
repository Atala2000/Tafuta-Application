#!/usr/bin/env python3
"""
Module for the user database
"""

from datetime import datetime
from app import db


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), nullable=False)
    phone_no = db.Column(db.Integer(), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    items_found = db.relationship("Items", backref="users")
    connected_items_owner = db.relationship(
        "Connected_Items", foreign_keys="Connected_Items.owner_id", backref="owner"
    )
    connected_items_reporter = db.relationship(
        "Connected_Items",
        foreign_keys="Connected_Items.reporter_id",
        backref="reporter",
    )

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}, {self.email}>"


class Items(db.Model):
    __tablename__ = "items_found"

    id = db.Column(db.Integer, primary_key=True)
    date_found = db.Column(db.DateTime, default=datetime.now())
    location_found = db.Column(db.String(50))
    description = db.Column(db.Text(64000))
    filename = db.Column(db.String(50))
    category = db.Column(db.String(50))
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))


class Connected_Items(db.Model):
    __tablename__ = "connected_items"
    item_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    reporter_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    date_connected = db.Column(db.DateTime)
    location_connected = db.Column(db.String(50))
