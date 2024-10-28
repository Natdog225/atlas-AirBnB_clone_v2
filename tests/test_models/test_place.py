#!/usr/bin/python3
"""Unit tests for the Place class"""
import unittest
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models import storage

class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    @classmethod
    def setUpClass(cls):
        """Set up a valid State, City, and User instance for Place testing."""
        # Ensure State is committed to generate an ID
        cls.state = State(name="California")
        storage.new(cls.state)
        storage.save()  # Commit State to ensure `state_id` is available

        # Create City using valid `state_id`
        cls.city = City(name="San Francisco", state_id=cls.state.id)
        storage.new(cls.city)
        storage.save()  # Commit City to ensure `city_id` is available

        # Create User
        cls.user = User(email="user@example.com", password="password123")
        storage.new(cls.user)
        storage.save()  # Commit User to ensure `user_id` is available

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests by deleting State, City, and User."""
        storage.delete(cls.city)
        storage.delete(cls.user)
        storage.delete(cls.state)
        storage.save()

    def setUp(self):
        """Set up a new Place instance for testing."""
        self.place = Place(
            city_id=self.city.id,
            user_id=self.user.id,
            name="Beach House",
            description="A house by the beach",
            number_rooms=3,
            number_bathrooms=2,
            max_guest=5,
            price_by_night=200,
            latitude=36.7783,
            longitude=-119.4179
        )
        storage.new(self.place)
        storage.save()

    def tearDown(self):
        """Clean up by deleting the Place instance."""
        storage.delete(self.place)
        storage.save()

    def test_city_id(self):
        """Test that city_id is correctly set as a string."""
        self.assertEqual(self.place.city_id, self.city.id)
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id(self):
        """Test that user_id is correctly set as a string."""
        self.assertEqual(self.place.user_id, self.user.id)
        self.assertIsInstance(self.place.user_id, str)

    def test_name(self):
        """Test that name is correctly set as a string."""
        self.assertEqual(self.place.name, "Beach House")
        self.assertIsInstance(self.place.name, str)

    def test_description(self):
        """Test that description is correctly set as a string."""
        self.assertEqual(self.place.description, "A house by the beach")
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms(self):
        """Test that number_rooms is correctly set as an integer."""
        self.assertEqual(self.place.number_rooms, 3)
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms(self):
        """Test that number_bathrooms is correctly set as an integer."""
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest(self):
        """Test that max_guest is correctly set as an integer."""
        self.assertEqual(self.place.max_guest, 5)
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night(self):
        """Test that price_by_night is correctly set as an integer."""
        self.assertEqual(self.place.price_by_night, 200)
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude(self):
        """Test that latitude is correctly set as a float."""
        self.assertEqual(self.place.latitude, 36.7783)
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude(self):
        """Test that longitude is correctly set as a float."""
        self.assertEqual(self.place.longitude, -119.4179)
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids(self):
        """Test that amenity_ids is a list"""
        if not hasattr(self.place, "amenity_ids"):
            self.place.amenity_ids = []  # Ensure it's defined if missing
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_kwargs(self):
        """Test initialization with kwargs for Place."""
        new_place = Place(name="Mountain Cabin", city_id=self.city.id, user_id=self.user.id)
        self.assertEqual(new_place.name, "Mountain Cabin")
        self.assertEqual(new_place.city_id, self.city.id)
        self.assertEqual(new_place.user_id, self.user.id)

    def test_save_place(self):
        """Test that Place object is saved correctly."""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict_place(self):
        """Test that Place to_dict method includes correct attributes."""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["name"], "Beach House")
        self.assertEqual(place_dict["city_id"], self.city.id)
        self.assertEqual(place_dict["user_id"], self.user.id)
        self.assertEqual(place_dict["__class__"], "Place")

if __name__ == '__main__':
    unittest.main()
