# tests/test_models/test_amenity.py

import unittest
from datetime import datetime
from models.amenity import Amenity
from models import storage

class TestAmenity(unittest.TestCase):
    """Unit tests for Amenity model and BaseModel integration"""

    def setUp(self):
        """Set up method for each test"""
        self.amenity = Amenity()

    def test_default_name(self):
        """Test that the default name is an empty string"""
        self.assertEqual(self.amenity.name, "")

    def test_setting_name(self):
        """Test setting the name attribute"""
        self.amenity.name = "Pool"
        self.assertEqual(self.amenity.name, "Pool")

    def test_str_representation(self):
        """Test that the string representation of Amenity is correct"""
        expected_str = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected_str)

    def test_id_type(self):
        """Test that id is a string"""
        self.assertIsInstance(self.amenity.id, str)

    def test_created_at_type(self):
        """Test that created_at is a datetime object"""
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_updated_at_type(self):
        """Test that updated_at is a datetime object"""
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_save_amenity(self):
        """Test saving and reloading an Amenity instance"""
        self.amenity.name = "Wi-Fi"
        self.amenity.save()
        storage.reload()
        all_objs = storage.all()
        key = f"Amenity.{self.amenity.id}"
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key].name, "Wi-Fi")

    def test_updated_at(self):
        """Test that updated_at changes on save"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test that to_dict creates a dictionary with proper attributes"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], self.amenity.id)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
