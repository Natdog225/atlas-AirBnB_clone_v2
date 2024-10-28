#!/usr/bin/python3
"""Unit tests for the Review class"""
import unittest
from models.review import Review
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models import storage

class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up dependencies for testing Review"""
        # Create a State instance
        cls.state = State(name="California")
        storage.new(cls.state)
        storage.save()

        # Create a City instance linked to the State
        cls.city = City(name="San Francisco", state_id=cls.state.id)
        storage.new(cls.city)
        storage.save()

        # Create a User instance
        cls.user = User(email="testuser@example.com", password="password")
        storage.new(cls.user)
        storage.save()

        # Create a Place instance linked to the City and User
        cls.place = Place(name="Beach House", city_id=cls.city.id, user_id=cls.user.id)
        storage.new(cls.place)
        storage.save()

    @classmethod
    def tearDownClass(cls):
        """Clean up dependencies after tests"""
        storage.delete(cls.place)
        storage.delete(cls.city)
        storage.delete(cls.state)
        storage.delete(cls.user)
        storage.save()

    def setUp(self):
        """Set up a Review instance for testing"""
        self.review = Review(place_id=self.place.id, user_id=self.user.id, text="Fantastic experience!")
        storage.new(self.review)
        storage.save()

    def tearDown(self):
        """Clean up after each test"""
        storage.delete(self.review)
        storage.save()

    def test_place_id(self):
        """Test that place_id is a string and matches the Place ID"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(self.review.place_id, self.place.id)

    def test_user_id(self):
        """Test that user_id is a string and matches the User ID"""
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(self.review.user_id, self.user.id)

    def test_text(self):
        """Test that text is a string and correctly set"""
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(self.review.text, "Fantastic experience!")

    def test_review_kwargs(self):
        """Test initialization with kwargs for Review"""
        review = Review(place_id=self.place.id, user_id=self.user.id, text="Perfect for a weekend!")
        self.assertEqual(review.place_id, self.place.id)
        self.assertEqual(review.user_id, self.user.id)
        self.assertEqual(review.text, "Perfect for a weekend!")

    def test_save_review(self):
        """Test that Review object is saved correctly and updated_at is modified"""
        old_updated_at = self.review.updated_at
        self.review.text = "Updated review text!"
        self.review.save()
        self.assertNotEqual(self.review.updated_at, old_updated_at)

    def test_to_dict_review(self):
        """Test that Review to_dict method includes correct attributes"""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["place_id"], self.place.id)
        self.assertEqual(review_dict["user_id"], self.user.id)
        self.assertEqual(review_dict["text"], "Fantastic experience!")
        self.assertEqual(review_dict["__class__"], "Review")

if __name__ == '__main__':
    unittest.main()
