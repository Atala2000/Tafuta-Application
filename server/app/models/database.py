#!/usr/bin/env python3
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
from app import db
load_dotenv()

class DataStorage:
    url_object = URL.create(
        "mysql+mysqldb",
        username=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASS"),
        host=os.getenv("HOST"),
        database=os.getenv("DATABASE"),
    )

    def __init__(self, app=None):
        """
        Initializes the data storage class and creates the engine connector, session and models
        """
        self.engine = create_engine(DataStorage.url_object, echo=False)
        self.session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.session_factory)

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Initialize with the Flask app
        """
        app.teardown_appcontext(self.teardown)

    def teardown(self, exception):
        self.close()

    def add(self, data):
        """
        Adds new objects to the database
        """
        try:
            self.Session.add(data)
            self.Session.commit()
        except Exception as e:
            self.Session.rollback()
            print(f"An error occurred while adding data: {e}")

    def get(self, model, id):
        """
        Returns a single object from the database
        Args:
            model: The model to query
            id: The id of the object to return
        """
        try:
            return self.Session.query(model).get(id)
        except Exception as e:
            self.Session.rollback()
            print(f"An error occurred while fetching data: {e}")

    def filter(self, model, **kwargs):
        """
        Returns a list of objects from the database
        Args:
            model: The model to query
            kwargs: The search parameters
        """
        try:
            return self.Session.query(model).filter_by(**kwargs).all()
        except Exception as e:
            self.Session.rollback()
            print(f"An error occurred while filtering data: {e}")

    def all(self, model):
        """
        Returns all objects of a given model
        Args:
            model: The model to query
        Returns:
            list: List of objects of the given model
        """
        try:
            objects = self.Session.query(model).all()
            return objects
        except Exception as e:
            print(f"An error occurred while fetching objects: {e}")
            return []

    def delete(self, data):
        """
        Deletes a specified Object instance from the database
        Args:
            data: The object to delete
        """
        try:
            self.Session.delete(data)
            self.Session.commit()
        except Exception as e:
            self.Session.rollback()
            print(f"An error occurred while deleting data: {e}")

    def update(self):
        """
        Updates a specified Object instance from the database
        """
        try:
            self.Session.commit()
        except Exception as e:
            self.Session.rollback()
            print(f"An error occurred while updating data: {e}")

    def close(self):
        """
        Closes the session
        """
        self.Session.remove()

    def count(self, model):
        """
        Returns the number of objects in the database
        """
        try:
            return self.Session.query(model).count()
        except Exception as e:
            print(f"An error occurred while counting data: {e}")
            return 0

    def create(self):
        """
        Creates the database tables
        """
        try:
            db.create_all(bind=self.engine)
        except Exception as e:
            print(f"An error occurred while creating tables: {e}")

    def to_dict(self, obj):
        if isinstance(obj, list):
            return [self.to_dict(item) for item in obj]
        else:
            return {col.name: getattr(obj, col.name) for col in obj.__table__.columns}
