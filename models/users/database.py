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

    def all(self, model: models.Base):
        """
        Returns all objects of a given model
        Args:
            model: The model to query

        """
        try:
            return self.session.query(model).all()
        except:
            self.session.rollback()
            raise Exception("An error occured")

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
    
    def create(self):
        """
        Creates the database tables
        """
        self.models.Base.metadata.create_all(self.engine)