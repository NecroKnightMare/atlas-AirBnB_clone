import unittest
from models.city import City

class TestCity(unittest.TestCase):
    '''
    tests for City class
    def test_initialization(self):
        
        test to check if City is from City and if name is empty
        
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")
    '''
    def test_atters(self):
        '''
        test attributtes for city
        '''
        city = City(name="Tulsa", state_id="OK")
        self.assertEqual(city.name, "Tulsa")
        self.assertEqual(city.state_id, "OK")

    def test_to_dict_method(self):
        '''
        tests to check if part of dictionary
        '''
        city = City(name="Tulsa", state_id="OK")
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['name'], "Tulsa")
        self.assertEqual(city_dict['state_id'], "OK")

    def test_save_method(self):
        '''
        test to see if save works properly
        '''
        city = City(name="Tulsa", state_id="OK")
        old_updated_at = city.updated_at 
        city.save()
        self.assertNotEqual(city.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()

