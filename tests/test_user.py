import unittest
import os
from models.user import User
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestUser(unittest.Testcase):
    '''
    
    '''
    def SetUp(self):
        '''
        sets up env for tests
        '''
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            
    def teardown(self):
        '''
        cleans environment
        '''
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        
    def test_all_method(self):
        '''
        tests that all returns object dictionary
        '''
        self.assertEqual(self.storage.all())
        
    def test_new_method(self):
        '''
        tests new adds object to objects
        '''
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        
    def test_save_method(self):
        '''
        tests if save saves right
        '''
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assetTrue(os.path.exists(self.file_path))
        
    def test_reload_method(self):
        '''
        tests if reload deserializes objects correctly from json file
        '''
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)
        
    def test_serialization(self):
        '''
        test for reload deserializing objects from json files
        '''
        user = User()
        user.email = "airbnb2@mail.com"
        user.first_name = "Betty"
        user.last_name = "Bar"
        self.storage.new(user)
        self.storage.save()
        self.storage.reload()
        key = f"User.{user.id}"
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], User)
        self.assertEqual(self.storage.all()[key].email, "airbnb@mail.com")
        self.assertEqual(self.storage.all()[key].first_name, "Betty")
        self.assertEqual(self.storage.all()[key].last_name, "Bar")

if __name__ == '__main__':
    unittest.main()