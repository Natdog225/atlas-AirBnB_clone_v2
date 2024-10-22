#!/usr/bin/python3
"""Unit tests for the Review class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest

class TestReview(test_basemodel):
    """Test cases for the Review class"""

    def __init__(self, *args, **kwargs):
        """Initialize TestReview class"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test that place_id is a string and has the correct default value"""
        new = self.value()
        self.assertTrue(hasattr(new, "place_id"))
        self.assertEqual(type(new.place_id), str)
        self.assertEqual(new.place_id, "")

    def test_user_id(self):
        """Test that user_id is a string and has the correct default value"""
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))
        self.assertEqual(type(new.user_id), str)
        self.assertEqual(new.user_id, "")

    def test_text(self):
        """Test that text is a string and has the correct default value"""
        new = self.value()
        self.assertTrue(hasattr(new, "text"))
        self.assertEqual(type(new.text), str)
        self.assertEqual(new.text, "")

    def test_review_kwargs(self):
        """Test initialization with kwargs for Review"""
        new = self.value(place_id="1234", user_id="5678", text="Great place!")
        self.assertEqual(new.place_id, "1234")
        self.assertEqual(new.user_id, "5678")
        self.assertEqual(new.text, "Great place!")

    def test_save_review(self):
        """Test that Review object is saved correctly"""
        new = self.value(place_id="1234", user_id="5678", text="Lovely spot!")
        new.save()
        self.assertNotEqual(new.created_at, new.updated_at)

    def test_to_dict_review(self):
        """Test that Review to_dict method includes correct attributes"""
        new = self.value(place_id="1234", user_id="5678", text="Perfect getaway!")
        review_dict = new.to_dict()
        self.assertEqual(review_dict["place_id"], "1234")
        self.assertEqual(review_dict["user_id"], "5678")
        self.assertEqual(review_dict["text"], "Perfect getaway!")
        self.assertEqual(review_dict["__class__"], "Review")

if __name__ == '__main__':
    unittest.main()
