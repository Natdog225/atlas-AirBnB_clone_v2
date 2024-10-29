#!/usr/bin/python3
"""Unit tests for the State class"""
import unittest
from models.state import State
from models import storage
from models.engine.db_storage import DBStorage


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    @classmethod
    def setUpClass(cls):
        """Set up resources required for the tests."""
        cls.state = State(name="Test State")
        storage.new(cls.state)
        storage.save()

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after tests."""
        storage.delete(cls.state)
        storage.save()

    def test_name_attribute(self):
        """Test that name is a string and is correctly assigned."""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(type(self.state.name), str)
        self.assertEqual(self.state.name, "Test State")

    def test_state_kwargs(self):
        """Test initialization with kwargs for State"""
        new_state = State(name="California")
        self.assertEqual(new_state.name, "California")

    def test_save_state(self):
        """Test that State object is saved correctly."""
        initial_updated_at = self.state.updated_at
        self.state.name = "Updated Test State"
        self.state.save()
        self.assertNotEqual(self.state.updated_at, initial_updated_at)

    def test_to_dict_state(self):
        """Test that State to_dict method includes correct attributes."""
        fresh_state = State(name="Test State")
        state_dict = fresh_state.to_dict()
        self.assertEqual(state_dict["name"], "Test State")
        self.assertEqual(state_dict["__class__"], "State")

    def test_storage_persistence(self):
        """Check if the state is persisted based on storage type."""
        state = State(name="Test State")
        storage.new(state)
        storage.save()
        
        retrieved_state = storage.get(State, state.id)
        self.assertEqual(retrieved_state.name, "Test State")
        
    def test_storage_persistence(self):
        """Check if the state is persisted based on storage type."""
        state = State(name="Test State")
        storage.new(state)
        storage.save()
        
        retrieved_state = storage.get(State, state.id)
        self.assertEqual(retrieved_state.name, "Test State")


if __name__ == "__main__":
    unittest.main()
