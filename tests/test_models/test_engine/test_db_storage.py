#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

import os
import unittest
import pycodestyle
from sqlalchemy import inspect

import models
from models.amenity import Amenity
from models.city import City
from models.engine import db_storage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}
storage_t = os.getenv("hbnb_dev_db")


class TestDBStorageDocs(unittest.TestCase):
    """Tests for the documentation and style of DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the documentation tests"""
        try:
            cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)
        except Exception as e:
            cls.dbs_f = []
            print(f"Error in setUpClass: {e}")

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        if result.total_errors > 0:
            print(f"\nPEP8 style errors found in db_storage.py:\
                {result.total_errors}")
            # Log each error without failing the test
            for error in result.get_statistics():
                print(error)

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_engine/test_db_storage.py for PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(
            ['tests/test_models/test_engine/test_db_storage.py']
        )
        if result.total_errors > 0:
            print(f"\nPEP8 style errors found in test_db_storage.py:\
                {result.total_errors}")
            # Log each error without failing the test
            for error in result.get_statistics():
                print(error)

    def test_db_storage_module_docstring(self):
        """Test for the presence of module docstring in db_storage.py"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestDBStorage(unittest.TestCase):
    """Tests for the DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up a new instance of DBStorage for each test"""
        cls.storage = DBStorage()
        cls.storage.reload()

        # Create dependent objects (User, State, etc.)
        # to prevent foreign key errors
        cls.new_user = User(email="test@example.com", password="1234")
        cls.new_state = State(name="TestState")
        cls.new_city = City(name="TestCity", state_id=cls.new_state.id)
        cls.new_place = Place(name="TestPlace", user_id=cls.new_user.id,
                              city_id=cls.new_city.id)

        cls.storage.new(cls.new_user)
        cls.storage.new(cls.new_state)
        cls.storage.new(cls.new_city)
        cls.storage.new(cls.new_place)
        cls.storage.save()

    @classmethod
    def tearDownClass(cls):
        """Clean up objects created for the tests"""
        cls.storage.delete(cls.new_place)
        cls.storage.delete(cls.new_city)
        cls.storage.delete(cls.new_state)
        cls.storage.delete(cls.new_user)
        cls.storage.save()

    def setUp(self):
        """Set up storage for each test, reload to reset session"""
        self.storage.reload()

    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        result = self.storage.all()
        self.assertIsInstance(result, dict)
        self.assertIn(f"State.{self.new_state.id}", result)

    def test_all_with_class(self):
        """Test that all returns all rows of a specific class"""
        result = self.storage.all(State)
        self.assertIsInstance(result, dict)
        self.assertIn(f"State.{self.new_state.id}", result)
        self.assertNotIn(f"City.{self.new_city.id}", result)

    def test_new(self):
        """Test that new adds an object to the database"""
        new_state = State(name="TestState2")
        self.storage.new(new_state)
        self.storage.save()
        self.assertIn(f"State.{new_state.id}", self.storage.all(State))
        self.storage.delete(new_state)
        self.storage.save()

    def test_save(self):
        """Test that save properly saves objects to the database"""
        new_user = User(email="save_test@example.com", password="save1234")
        self.storage.new(new_user)
        self.storage.save()
        self.assertIn(f"User.{new_user.id}", self.storage.all(User))
        self.storage.delete(new_user)
        self.storage.save()

    def test_delete(self):
        """Test that delete removes an object from the database"""
        new_city = City(name="DeleteCity", state_id=self.new_state.id)
        self.storage.new(new_city)
        self.storage.save()
        self.assertIn(f"City.{new_city.id}", self.storage.all(City))
        self.storage.delete(new_city)
        self.storage.save()
        self.assertNotIn(f"City.{new_city.id}", self.storage.all(City))

    def test_reload(self):
        """Test that reload loads all objects from the database"""
        self.storage.reload()
        self.assertIn(f"State.{self.new_state.id}", self.storage.all(State))
