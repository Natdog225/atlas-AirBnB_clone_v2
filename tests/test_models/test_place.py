#!/usr/bin/python3
"""Unit tests for the Place class"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import unittest

class TestPlace(test_basemodel):
    """Test cases for the Place class"""

    def __init__(self, *args, **kwargs):
        """Initialize TestPlace class"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test that city_id is a string"""
        new = self.value()
        self.assertTrue(hasattr(new, "city_id"))
        self.assertEqual(type(new.city_id), str)
        self.assertEqual(new.city_id, "")

    def test_user_id(self):
        """Test that user_id is a string"""
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))
        self.assertEqual(type(new.user_id), str)
        self.assertEqual(new.user_id, "")

    def test_name(self):
        """Test that name is a string"""
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(type(new.name), str)
        self.assertEqual(new.name, "")

    def test_description(self):
        """Test that description is a string"""
        new = self.value()
        self.assertTrue(hasattr(new, "description"))
        self.assertEqual(type(new.description), str)
        self.assertEqual(new.description, "")

    def test_number_rooms(self):
        """Test that number_rooms is an integer"""
        new = self.value()
        self.assertTrue(hasattr(new, "number_rooms"))
        self.assertEqual(type(new.number_rooms), int)
        self.assertEqual(new.number_rooms, 0)

    def test_number_bathrooms(self):
        """Test that number_bathrooms is an integer"""
        new = self.value()
        self.assertTrue(hasattr(new, "number_bathrooms"))
        self.assertEqual(type(new.number_bathrooms), int)
        self.assertEqual(new.number_bathrooms, 0)

    def test_max_guest(self):
        """Test that max_guest is an integer"""
        new = self.value()
        self.assertTrue(hasattr(new, "max_guest"))
        self.assertEqual(type(new.max_guest), int)
        self.assertEqual(new.max_guest, 0)

    def test_price_by_night(self):
        """Test that price_by_night is an integer"""
        new = self.value()
        self.assertTrue(hasattr(new, "price_by_night"))
        self.assertEqual(type(new.price_by_night), int)
        self.assertEqual(new.price_by_night, 0)

    def test_latitude(self):
        """Test that latitude is a float"""
        new = self.value()
        self.assertTrue(hasattr(new, "latitude"))
        self.assertEqual(type(new.latitude), float)
        self.assertEqual(new.latitude, 0.0)

    def test_longitude(self):
        """Test that longitude is a float"""
        new = self.value()
        self.assertTrue(hasattr(new, "longitude"))
        self.assertEqual(type(new.longitude), float)
        self.assertEqual(new.longitude, 0.0)

    def test_amenity_ids(self):
        """Test that amenity_ids is a list"""
        new = self.value()
        self.assertTrue(hasattr(new, "amenity_ids"))
        self.assertEqual(type(new.amenity_ids), list)
        self.assertEqual(new.amenity_ids, [])

    def test_place_kwargs(self):
        """Test initialization with kwargs for Place"""
        new = self.value(city_id="0001", user_id="0002", name="Beach House")
        self.assertEqual(new.city_id, "0001")
        self.assertEqual(new.user_id, "0002")
        self.assertEqual(new.name, "Beach House")

    def test_save_place(self):
        """Test that Place object is saved correctly"""
        new = self.value(city_id="0001", user_id="0002", name="Beach House")
        new.save()
        self.assertNotEqual(new.created_at, new.updated_at)

    def test_to_dict_place(self):
        """Test that Place to_dict method includes correct attributes"""
        new = self.value(name="Cabin", city_id="0003", user_id="0004")
        place_dict = new.to_dict()
        self.assertEqual(place_dict["name"], "Cabin")
        self.assertEqual(place_dict["city_id"], "0003")
        self.assertEqual(place_dict["user_id"], "0004")
        self.assertEqual(place_dict["__class__"], "Place")

if __name__ == '__main__':
    unittest.main()
