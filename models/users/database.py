#!/usr/bin/env python3
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.engine import URL
import os
from . import models
from sqlalchemy.orm import Session


load_dotenv()

class DataStorage:
    url_object = URL.create(
    'mysql+mysqldb',
    username=os.getenv('DATABASE_USER'),
    password=os.getenv("DATABASE_PASS"),
    host=os.getenv("HOST"),
    database=os.getenv("DATABASE"),
)

    def __init__(self):
        """
        Initializes the data storage class and creates the engine connector, session and models
        """
        self.engine = create_engine(DataStorage.url_object, echo=True)
        self.session = Session(bind=self.engine)
        self.models = models

    def add(self, data):
        """
        Adds new objects to the database
        """
        try:
            self.session.add(data)
            self.session.commit()
        except:
            self.session.rollback()

    def get(self, model: models.Base, id):
        """
        Returns a single object from the database
        Args:
            model: The model to query
            id: The id of the object to return
        """
        try:
            return self.session.query(model).get(id)
        except:
            self.session.rollback()

    def filter(self, model: models.Base, **kwargs):
        """
        Returns a list of objects from the database
        Args:
            model: The model to query
            kwargs: The search parameters
        """
        try:
            return self.session.query(model).filter_by(**kwargs).all()
        except:
            self.session.rollback()

    def all(self, model: models.Base):
        """
        Returns all objects of a given model
        Args:
            model: The model to query

        """
        try:
            users = self.data_storage.all(models.Users)
            print(users)
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete(self, data):
        """
        Deletes a specified Object instance from the database
        Args:
            data: The object to delete
        """
        try:
            self.session.delete(data)
            self.session.commit()
        except:
            self.session.rollback()


    def update(self, data):
        """
        Updates a specified Object instance from the database
        Args:
            data: The object to update
        """
        self.session.commit()

    def close(self):
        """
        Closes the session and disposes the engine
        """
        self.session.close()
        self.engine.dispose()

    def count(self, model):
        """
        Returns the number of objects in the database
        """
        return self.session.query(model).count()
    
    def create(self):
        """
        Creates the database tables
        """
        self.models.Base.metadata.create_all(self.engine)