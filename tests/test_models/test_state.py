#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
#!/usr/bin/python3

import unittest, os
from models.state import State

class TestState(unittest.TestCase):

    def test_state__init__(self):
        new_state = State()
        self.assertEqual(new_state.name, "")

if __name__ == "__main__":
    unittest.main()