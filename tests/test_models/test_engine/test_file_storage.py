#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models import storage
import os
import json


class TestFileStorage(unittest.TestCase):
    """Class to test the FileStorage method"""

    def setUp(self):
        """Set up test environment"""
        storage._FileStorage__objects.clear()
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Remove storage file at end of tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """__objects is initially empty"""
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """New object is correctly added to __objects"""
        new = BaseModel()
        storage.new(new)
        self.assertIn(f"BaseModel.{new.id}", storage.all())

    def test_all_returns_dict(self):
        """all() returns the __objects dictionary"""
        new = BaseModel()
        self.assertIsInstance(storage.all(), dict)

    def test_all_with_class_filter(self):
        """all(cls) returns only instances of the specified class"""
        user = User(email="user@example.com", password="pass")
        state = State(name="California")
        storage.new(user)
        storage.new(state)
        filtered = storage.all(User)
        self.assertIn(f"User.{user.id}", filtered)
        self.assertNotIn(f"State.{state.id}", filtered)

    def test_save_creates_file(self):
        """FileStorage save method creates a file.json"""
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_content(self):
        """File content after save matches the __objects dictionary"""
        new = BaseModel()
        storage.new(new)
        storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        self.assertIn(f"BaseModel.{new.id}", data)

    def test_reload(self):
        """Storage file is successfully loaded to __objects"""
        new = BaseModel()
        storage.new(new)
        storage.save()
        storage.reload()
        self.assertIn(f"BaseModel.{new.id}", storage.all())

    def test_reload_from_empty_file(self):
        """Reloading from an empty file should do nothing"""
        open("file.json", "w").close()
        storage.reload()
        self.assertEqual(storage.all(), {})

    def test_reload_invalid_json(self):
        """Reload handles invalid JSON format gracefully"""
        with open("file.json", "w") as f:
            f.write("{invalid json")
        storage.reload()
        self.assertEqual(storage.all(), {})

    def test_delete(self):
        """Test that delete removes object from __objects"""
        new = BaseModel()
        storage.new(new)
        storage.save()
        storage.delete(new)
        self.assertNotIn(f"BaseModel.{new.id}", storage.all())

    def test_delete_persistence(self):
        """Test that deleted object is not in storage after reload"""
        new = BaseModel()
        storage.new(new)
        storage.save()
        storage.delete(new)
        storage.save()
        storage.reload()
        self.assertNotIn(f"BaseModel.{new.id}", storage.all())

    def test_key_format(self):
        """Key is properly formatted as <class name>.<object id>"""
        new = BaseModel()
        storage.new(new)
        key_format = f"BaseModel.{new.id}"
        self.assertIn(key_format, storage.all())

    def test_storage_var_created(self):
        """FileStorage object storage is created"""
        from models.engine.file_storage import FileStorage
        self.assertIsInstance(storage, FileStorage)

if __name__ == "__main__":
    unittest.main()
