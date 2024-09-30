import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place

class TestFileStorage(unittest.TestCase):
    '''
    unittest for file_storage
    '''
    def setUp(self):
        '''
        Test for environment
        '''
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            
    def tearDown(self):
        '''
        remove env
        '''
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            
    def test_all(self):
        '''
        test if all returns objects dictionary
        '''
        self.assertEqual(self.storage.all(), {})
        
    def test_new(self):
        '''
        test for adding new object to storage
        '''
        obj = BaseModel
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        
    def test_save(self):
        '''
        test that saves correct serialized objects to json file
        '''
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, 'r') as f:
            data = json.loads(f)
        key = 
        self.assertIn(key, data)
        
    def test_reload(self):
        '''
        test that reloads correct deserialized obj from json files
        '''
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        
        
        
        """
        needs more test
        """
if __name__ == '__main__':
    unittest.main()