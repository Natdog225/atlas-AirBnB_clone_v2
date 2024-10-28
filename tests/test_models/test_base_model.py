# tests/test_models/test_base_model.py
import unittest
from os import getenv
from datetime import datetime
from models.base_model import BaseModel
from models import storage

class TestBaseModelStorage(unittest.TestCase):
    """Test BaseModel with dynamic storage (FileStorage or DBStorage)."""

    def setUp(self):
        """Set up a new BaseModel instance and save it to storage."""
        self.obj = BaseModel()
        storage.new(self.obj)
        storage.save()

    def tearDown(self):
        """Clean up the test instance from storage."""
        storage.delete(self.obj)
        storage.save()

    def test_instance_creation(self):
        """Test creation of a BaseModel instance in storage."""
        self.assertIn(self.obj, storage.all().values())

    def test_save_updates_timestamp(self):
        """Test that save updates the updated_at timestamp."""
        old_timestamp = self.obj.updated_at
        self.obj.save()
        self.assertNotEqual(old_timestamp, self.obj.updated_at)

    def test_delete_removes_instance(self):
        """Test that delete removes the instance from storage."""
        storage.delete(self.obj)
        storage.save()
        self.assertNotIn(self.obj, storage.all().values())

    def test_to_dict(self):
        """Test to_dict contains correct information."""
        obj_dict = self.obj.to_dict()
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], self.obj.id)
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)

    def test_id_is_valid_uuid(self):
        """Test that id is in a valid UUID format."""
        import uuid
        try:
            uuid_obj = uuid.UUID(self.obj.id, version=4)
        except ValueError:
            self.fail("ID is not a valid UUID.")

    def test_created_at_type(self):
        """Test that created_at is a datetime object."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_updated_at_type(self):
        """Test that updated_at is a datetime object."""
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_reload(self):
        """Test reload functionality based on storage type."""
        storage.reload()
        key = f"BaseModel.{self.obj.id}"
        self.assertIn(key, storage.all().keys())

if __name__ == "__main__":
    unittest.main()
