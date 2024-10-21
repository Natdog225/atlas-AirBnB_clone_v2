#!/usr/bin/python3
"""
Module to test the Amenity class of things
"""

import unittest
from models.amenity import Amenity
from tests.test_models.test_base_model import test_basemodel



class test_Amenity(test_basemodel):
    """Test cases"""

    def __init__(self, *args, **kwargs):
        """go go tester """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test that the name actually is a string """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_default_name(self):
        """Test that the default name is an empty string"""
        new = self.value()
        self.assertEqual(new.name, "")

    def test_setting_name(self):
        """Test setting the name attribute"""
        new = self.value()
        new.name = "Pool"
        self.assertEqual(new.name, "Pool")

    def test_save_amenity(self):
        """Test saving and reloading an Amenity instance"""
        new = self.value()
        new.name = "Wi-Fi"
        new.save()
        storage.reload()
        all_objs = storage.all()
        key = f"{self.name}.{new.id}"
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key].name, "Wi-Fi")
        
        def test_kwargs_instantiation(self):
            """ testing instantiation with kwargs"""
            new = self.value(name="Gym")
            self.assertEqual(new.name, "Gym")
