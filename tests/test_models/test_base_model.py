#!/usr/bin/python3
"""Unit test for BaseModel class"""
import os
import json
from models.base_model import BaseModel
import unittest
from datetime import datetime
from uuid import UUID
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel"""

    def setUp(self):
        """Set up testing environment"""
        self.storage = FileStorage()
        self.base_obj = BaseModel()
        self.file_path = 'file.json'

    def tearDown(self):
        """Tear down testing environment"""
        # Remove the file.json if it exists and clear the storage
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass
        self.storage.all().clear()

    def test_default(self):
        """Test default initialization of BaseModel"""
        i = BaseModel()
        self.assertEqual(type(i), BaseModel)

    def test_kwargs(self):
        """Test initialization with kwargs"""
        i = BaseModel()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)  # Ensure that new is a separate instance
        self.assertEqual(new.id, i.id)
        self.assertEqual(new.created_at, i.created_at)

    def test_kwargs_int(self):
        """Test that passing an invalid type in kwargs raises an error"""
        i = BaseModel()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test the save method to ensure proper serialization"""
        i = BaseModel()
        i.save()
        key = "BaseModel." + i.id
        with open(self.file_path, 'r') as f:
            j = json.load(f)
            self.assertIn(key, j)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test the string representation of BaseModel"""
        i = BaseModel()
        self.assertEqual(str(i), '[{}] ({}) {}'.format('BaseModel', i.id, i.__dict__))

    def test_todict(self):
        """Test to_dict method for proper conversion"""
        i = BaseModel()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)
        self.assertEqual(n["__class__"], "BaseModel")
        self.assertEqual(type(n["created_at"]), str)
        self.assertEqual(type(n["updated_at"]), str)

    def test_kwargs_none(self):
        """Test initialization with None in kwargs raises TypeError"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_id(self):
        """Test that id is a string in UUID format"""
        new = BaseModel()
        self.assertEqual(type(new.id), str)
        # Check if it's a valid UUID
        try:
            uuid_obj = UUID(new.id, version=4)
        except ValueError:
            self.fail("The ID is not a valid UUID.")

    def test_created_at(self):
        """Test that created_at is of type datetime"""
        new = BaseModel()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        """Test that updated_at is of type datetime and different from created_at after save"""
        new = BaseModel()
        original_updated_at = new.updated_at
        new.save()
        self.assertNotEqual(original_updated_at, new.updated_at)
        self.assertTrue(new.updated_at > original_updated_at)

    def test_attributes_after_reload(self):
        """Test that attributes persist after saving and reloading"""
        i = BaseModel()
        i.name = "My Test"
        i.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "BaseModel." + i.id
        self.assertIn(key, new_storage.all())
        reloaded_obj = new_storage.all()[key]
        self.assertEqual(reloaded_obj.name, "My Test")

if __name__ == '__main__':
    unittest.main()
