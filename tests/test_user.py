import unittest
from models.user import User

class TestUser(unittest.Testcase):
    '''
    unittest for User
    '''
    def test_initialization(self):
        '''
        test if user is there and grabbing from BaseModel and equal to what it should be
        '''
        user = User()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.password, "")
        
    def test_atters(self):
        '''
        test if attributes are right for User
        '''
        user = User()
        user.email = "airbnb2@mail.com"
        user.first_name = "Betty"
        user.last_name = "Bar"
        user.password = "root"
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.password, "")
        
    def test_to_dict_method(self):
        '''
        test to ensure dictionarfy is equal    
        '''
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")
        self.assertEqual(user_dict['password'], "")
        
    def test_save_method(self):
        '''
        test for save method to save users
        '''
        user = User()
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, old_updated_at)
        
if __name__== '__main__':
    unittest.main()
