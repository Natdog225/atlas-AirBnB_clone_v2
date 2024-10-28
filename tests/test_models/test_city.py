#!/usr/bin/python3
"""Unit tests for the City class"""
import unittest
from models.city import City
from models.state import State
from models import storage

class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up a valid State instance and City instance for testing."""
        self.state = State(name="California")
        storage.new(self.state)
        storage.save()
        self.city = City(name="Los Angeles", state_id=self.state.id)
        storage.new(self.city)
        storage.save()

    def tearDown(self):
        """Clean up after tests."""
        storage.delete(self.city)
        storage.delete(self.state)
        storage.save()

    def test_state_id(self):
        """Test that state_id is a string."""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(type(self.city.state_id), str)
        self.assertEqual(self.city.state_id, self.state.id)

    def test_name(self):
        """Test that name is a string."""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(self.city.name, "Los Angeles")

    def test_city_kwargs(self):
        """Test initialization with kwargs for City."""
        new_city = City(name="San Francisco", state_id=self.state.id)
        self.assertEqual(new_city.name, "San Francisco")
        self.assertEqual(new_city.state_id, self.state.id)

    def test_save_city(self):
        """Test that City object is saved correctly."""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_city(self):
        """Test that City to_dict method includes correct attributes."""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["name"], "Los Angeles")
        self.assertEqual(city_dict["state_id"], self.state.id)
        self.assertEqual(city_dict["__class__"], "City")

if __name__ == '__main__':
    unittest.main()
