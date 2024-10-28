# tests/test_models/test_amenity.py

import unittest
from models.amenity import Amenity
from models import storage

class TestAmenity(unittest.TestCase):
    """Unit tests for Amenity model and BaseModel integration"""

    def setUp(self):
        """Set up test instance for Amenity"""
        self.amenity = Amenity(name="Pool")
        storage.new(self.amenity)
        storage.save()

    def tearDown(self):
        """Clean up after tests"""
        storage.delete(self.amenity)
        storage.save()

    def test_save_amenity(self):
        """Test saving and reloading an Amenity instance"""
        self.amenity.save()
        storage.reload()
        key = f"Amenity.{self.amenity.id}"
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key].name, "Pool")

    def test_updated_at(self):
        """Test that updated_at changes on save"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)
