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
    def test_city_attributes(self):
        '''
        test attributtes for city
        '''
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")
    '''
    def test_to_dict_method(self):
        '''
        '''
        city = City(name="Tulsa", state_id="OK")
        city_dict = city.to_dict()
        self.assertEqual(city_dict['name'], "Tulsa")
        self.assertEqual(city_dict['state_id'], "OK")
    '''
        

if __name__ == '__main__':
    unittest.main()

