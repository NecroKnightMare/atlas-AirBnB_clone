import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    '''
    tests for Amenity class
    '''
    def test_amenity_name(self):
        amenity = Amenity(name="WiFi")
        self.assertEqual(amenity.name, "WiFi")
        


if __name__ == '__main__':
    unittest.main()


