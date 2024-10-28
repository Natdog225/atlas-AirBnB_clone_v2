#!/usr/bin/python3
"""Unit tests for BaseModel with DBStorage"""

import unittest
from datetime import datetime
from uuid import UUID
from models.base_model import BaseModel
from models import storage

class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel with SQLAlchemy DBStorage."""

    def setUp(self):
        """Set up a testing environment for DBStorage"""
        self.base_obj = BaseModel()
        storage.new(self.base_obj)
        storage.save()

    def tearDown(self):
        """Clean up by deleting the BaseModel instance from DBStorage."""
        storage.delete(self.base_obj)
        storage.save()
        storage.reload()

    def test_default(self):
        """Test default initialization of BaseModel."""
        self.assertIsInstance(self.base_obj, BaseModel)

    def test_kwargs(self):
        """Test initialization with keyword arguments."""
        copy = self.base_obj.to_dict()
        new_obj = BaseModel(**copy)
        self.assertEqual(new_obj.id, self.base_obj.id)
        self.assertEqual(new_obj.created_at, self.base_obj.created_at)

    def test_save(self):
        """Test the save method to ensure changes in updated_at."""
        original_updated_at = self.base_obj.updated_at
        self.base_obj.save()
        self.assertNotEqual(original_updated_at, self.base_obj.updated_at)

    def test_str(self):
        """Test the string representation of BaseModel."""
        self.assertIn("[BaseModel]", str(self.base_obj))
        self.assertIn(self.base_obj.id, str(self.base_obj))

    def test_todict(self):
        """Test to_dict method for proper conversion to dictionary."""
        dictionary = self.base_obj.to_dict()
        self.assertEqual(dictionary["__class__"], "BaseModel")
        self.assertEqual(dictionary["id"], self.base_obj.id)
        self.assertIsInstance(dictionary["created_at"], str)
        self.assertIsInstance(dictionary["updated_at"], str)

    def test_id_is_valid_uuid(self):
        """Test that id is a string in UUID format."""
        try:
            uuid_obj = UUID(self.base_obj.id, version=4)
        except ValueError:
            self.fail("The ID is not a valid UUID.")

    def test_created_at_type(self):
        """Test that created_at is of type datetime."""
        self.assertIsInstance(self.base_obj.created_at, datetime)

    def test_updated_at(self):
        """Test that updated_at changes after save."""
        original_updated_at = self.base_obj.updated_at
        self.base_obj.save()
        self.assertNotEqual(original_updated_at, self.base_obj.updated_at)

    def test_attributes_after_reload(self):
        """Test that attributes persist after reloading from storage."""
        self.base_obj.name = "Test"
        self.base_obj.save()
        storage.reload()
        reloaded_obj = storage.get(BaseModel, self.base_obj.id)
        self.assertEqual(reloaded_obj.name, "Test")

if __name__ == '__main__':
    unittest.main()
