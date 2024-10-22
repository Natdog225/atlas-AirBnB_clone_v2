#!/usr/bin/python3
"""Unit tests for the State class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest

class TestState(test_basemodel):
    """Test cases for the State class"""

    def __init__(self, *args, **kwargs):
        """Initialize TestState class"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_attribute(self):
        """Test that name is a string and has the correct default value"""
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(type(new.name), str)
        self.assertEqual(new.name, "")

    def test_state_kwargs(self):
        """Test initialization with kwargs for State"""
        new = self.value(name="California")
        self.assertEqual(new.name, "California")

    def test_save_state(self):
        """Test that State object is saved correctly"""
        new = self.value(name="Texas")
        new.save()
        self.assertNotEqual(new.created_at, new.updated_at)

    def test_to_dict_state(self):
        """Test that State to_dict method includes correct attributes"""
        new = self.value(name="Nevada")
        state_dict = new.to_dict()
        self.assertEqual(state_dict["name"], "Nevada")
        self.assertEqual(state_dict["__class__"], "State")

if __name__ == "__main__":
    unittest.main()
