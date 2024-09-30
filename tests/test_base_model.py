import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''
    unittest for BaseModel
    '''
    def test_instance(self):
        '''
        test class inheritance
        '''
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model, id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        
    def test_save(self):
        '''
        test for save method
        '''
        model = BaseModel()
        old_update_at = model_updated_at
        model.save()
        self.assertEqual(model_updated_at, old_updated_at)

        
    def test_to_dict(self):
        '''
        test to see if its equal outputs
        '''
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], BaseModel)
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at']model.updated_at.isoformat())
    
if __name__ == '__main__':
    unittest.main()
