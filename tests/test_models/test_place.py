import unittest
from models.city import City
from models.user import User
from models.place import Place

class TestUser(unittest.Testcase):
    '''
    unittest for Place
    '''
    def test_initialization(self):
        '''
        test if user is there and grabbing from BaseModel and equal to what it should be
        '''
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.name, 0.0)
        self.assertEqual(place.amenity_ids, [])
        
    def test_atters(self):
        '''
        test if attributes are right for User
        '''
        place = Place()
        place.city_id = "1234"
        place.user_id = "369"
        place.name = "Condo"
        place.description = "decent"
        place.number_rooms = 3
        place.number_bathrooms = 1
        place.max_guest 6
        place.price_by_night = 135
        place.latitude = 32.7767
        place.longitude = 96.7970
        place.name = "dallas"
        place.amenity_ids, ["Kitchen", "dishwasher"])

        self.assertEqual(place.city_id, "1234")
        self.assertEqual(place.user_id, "369")
        self.assertEqual(place.name, "Condo")
        self.assertEqual(place.description, "decent")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 135)
        self.assertEqual(place.latitude, 32.7767)
        self.assertEqual(place.longitude, 96.7970)
        self.assertEqual(place.name, "dallas")
        self.assertEqual(place.amenity_ids, ["Kitchen", "dishwasher"])
        
    def test_to_dict_method(self):
        '''
        test to ensure dictionary is equal    
        '''
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['city_id'], 'Place')
        self.assertEqual(place_dict['user_id'], "")
        self.assertEqual(place_dict['name'], "")
        self.assertEqual(place_dict['description'], "")
        self.assertEqual(place_dict['number_rooms'], 0)
        self.assertEqual(place_dict['number_bathrooms'], 0)
        self.assertEqual(place_dict['max_guest'], 0)
        self.assertEqual(place_dict['price_by_night'], 0)
        self.assertEqual(place_dict['latitude'], 0.0)
        self.assertEqual(place_dict['longitude'], 0.0)
        self.assertEqual(place_dict['amenity_ids'], [])
        
    def test_save_method(self):
        '''
        test for save method to save users
        '''
        place = Place()
        old_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(place.updated_at, old_updated_at)
        
if __name__== '__main__':
    unittest.main()
