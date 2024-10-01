import unittest
from models.amenity import Amenity

class TestState(unittest.Testcase):
    '''
    tests for Amenity class
    '''
    def test_initialization(self):
        '''
        test to check if Amenity is from models and if name is empty
        '''
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

    def test_atters(self):
        '''
        test attributtes for amenity
        '''
        amenity = Amenity()
        amenity.name = "Kitchen"
        self.assertEqual(amenity.name, "Kitchen")

    def test_to_dict_method(self):
        '''
        tests to check if part of dictionary
        '''
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], "")

    def test_save_method(self):
        '''
        test to see if save works properly
        '''
        amenity = Amenity()
        old_update_at = state.updated_at 
        amenity.save()
        self.assertNotEqual(amenity.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()

