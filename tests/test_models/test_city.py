#!/usr/bin/python3
"""Unit tests for the City class"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest

class TestCity(test_basemodel):
    """Test cases for the City class"""

    def __init__(self, *args, **kwargs):
        """Initialize TestCity class"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test that state_id is a string"""
        new = self.value()
        self.assertTrue(hasattr(new, "state_id"))
        self.assertEqual(type(new.state_id), str)
        # Test if `state_id` defaults to an empty string if not set
        self.assertEqual(new.state_id, "")

    def test_name(self):
        """Test that name is a string"""
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(type(new.name), str)
        # Test if `name` defaults to an empty string if not set
        self.assertEqual(new.name, "")

    def test_city_kwargs(self):
        """Test initialization with kwargs for City"""
        new = self.value(name="San Francisco", state_id="CA")
        self.assertEqual(new.name, "San Francisco")
        self.assertEqual(new.state_id, "CA")

    def test_save_city(self):
        """Test that City object is saved correctly"""
        new = self.value(name="Los Angeles", state_id="CA")
        new.save()
        self.assertNotEqual(new.created_at, new.updated_at)

    def test_to_dict_city(self):
        """Test that City to_dict method includes correct attributes"""
        new = self.value(name="New York", state_id="NY")
        city_dict = new.to_dict()
        self.assertEqual(city_dict["name"], "New York")
        self.assertEqual(city_dict["state_id"], "NY")
        self.assertEqual(city_dict["__class__"], "City")

if __name__ == '__main__':
    unittest.main()
