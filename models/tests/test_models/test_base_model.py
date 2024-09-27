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
        
        """
        needs more test
        """