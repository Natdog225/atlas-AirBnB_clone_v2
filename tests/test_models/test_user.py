#!/usr/bin/python3
"""Unit tests for the User class"""



import unittest

from tests.test_models import test_base_model

class TestUser(test_base_model):
    """Test cases for the User class"""

    def __init__(self, *args, **kwargs):
        """Initialize TestUser class"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test that first_name is a string and has the correct default value"""
        new = self.value()
        self.assertTrue(hasattr(new, "first_name"))
        self.assertEqual(type(new.first_name), str)
        self.assertEqual(new.first_name, "")

    def test_last_name(self):
        """Test that last_name is a string and has the correct default value"""
        new = self.value()
        self.assertTrue(hasattr(new, "last_name"))
        self.assertEqual(type(new.last_name), str)
        self.assertEqual(new.last_name, "")

    def test_email(self):
        """Test that email is a string and has the correct default value"""
        new = self.value()
        self.assertTrue(hasattr(new, "email"))
        self.assertEqual(type(new.email), str)
        self.assertEqual(new.email, "")

    def test_password(self):
        """Test that password is a string and has the correct default value"""
        new = self.value()
        self.assertTrue(hasattr(new, "password"))
        self.assertEqual(type(new.password), str)
        self.assertEqual(new.password, "")

    def test_user_kwargs(self):
        """Test initialization with kwargs for User"""
        new = self.value(first_name="John", last_name="Doe", email="john@example.com", password="secure123")
        self.assertEqual(new.first_name, "John")
        self.assertEqual(new.last_name, "Doe")
        self.assertEqual(new.email, "john@example.com")
        self.assertEqual(new.password, "secure123")

    def test_save_user(self):
        """Test that User object is saved correctly"""
        new = self.value(first_name="Jane", email="jane@example.com")
        new.save()
        self.assertNotEqual(new.created_at, new.updated_at)

    def test_to_dict_user(self):
        """Test that User to_dict method includes correct attributes"""
        new = self.value(first_name="Alice", last_name="Wonder", email="alice@example.com")
        user_dict = new.to_dict()
        self.assertEqual(user_dict["first_name"], "Alice")
        self.assertEqual(user_dict["last_name"], "Wonder")
        self.assertEqual(user_dict["email"], "alice@example.com")
        self.assertEqual(user_dict["__class__"], "User")

if __name__ == "__main__":
    unittest.main()
