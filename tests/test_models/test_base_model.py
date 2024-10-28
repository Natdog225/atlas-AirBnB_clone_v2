# tests/test_models/test_base_model.py

import unittest
from datetime import datetime
from uuid import UUID
from models.base_model import BaseModel, Base
from models import storage
from models.engine.db_storage import DBStorage
from sqlalchemy import Column, String

# Concrete subclass for testing purposes
class TestModel(BaseModel, Base):
    __tablename__ = 'test_model'
    name = Column(String(128), nullable=False)

class TestBaseModelStorage(unittest.TestCase):
    """Test cases for BaseModel using TestModel with DBStorage."""

    @classmethod
    def setUpClass(cls):
        """Set up the class by creating tables if DB storage is used."""
        if isinstance(storage, DBStorage):
            Base.metadata.create_all(storage._DBStorage__engine)

    def setUp(self):
        """Set up a new TestModel instance for testing."""
        self.obj = TestModel(name="Test Name")
        
        # Only add to storage if DB storage is active
        if isinstance(storage, DBStorage):
            storage.new(self.obj)
            storage.save()

    def tearDown(self):
        """Clean up after tests based on storage type."""
        if isinstance(storage, DBStorage):
            storage.delete(self.obj)
            storage.save()

    def test_instance_creation(self):
        """Test instance creation."""
        self.assertIsInstance(self.obj, TestModel)

    def test_id_is_valid_uuid(self):
        """Test that id is a string in UUID format."""
        try:
            uuid_obj = UUID(self.obj.id, version=4)
        except ValueError:
            self.fail("The ID is not a valid UUID.")

    def test_created_at_type(self):
        """Test that created_at is a datetime object."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_to_dict(self):
        """Test to_dict contains correct information."""
        dictionary = self.obj.to_dict()
        self.assertEqual(dictionary["__class__"], "TestModel")
        self.assertEqual(dictionary["id"], self.obj.id)
        self.assertIsInstance(dictionary["created_at"], str)
        self.assertIsInstance(dictionary["updated_at"], str)

if __name__ == "__main__":
    unittest.main()
