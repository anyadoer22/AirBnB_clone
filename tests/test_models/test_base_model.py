#!/usr/bin/python3
# unittest
"""unittest for base_model class"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unnittest.TestCase):
    """test properties of BaseModel object"""
    base_object = BaseModel() #instantiate  BaseModel class

    def testID(self):
        """test the unique id when object is created"""
        self.assertEqual(str(base_object.id), "placeholder", "unexpected object id")

    def test_created_at(self):
        """test the created at attribute of the object"""
        pass
    def test_updated_at(self):
        """test the datetime value of the object when updated"""
        pass

    def test_str_method(self):
        """Test string value returned when str nethod is called"""
        pass
    def test_save(self):
        """Test the value of updated at attribute
        when save method is called"""
        pass
    def test_to_dict(self):
        pass


if __name__ == "__main__":
    unittest.main()
