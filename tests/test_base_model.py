import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    '''
    unittest for BaseModel
    ''' 
    def test_save(self):
        
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(mmodel.updated_at, old_updated_at)

    def test_instance(self):
        '''
        test class inheritance
        '''
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict(self):
        '''
        test to see if its equal outputs
        '''
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['id'], base_model.id)
        self.assertEqual(base_model_dict['created_at'], base_model.created_at.isoformat())
        self.assertEqual(base_model_dict['updated_at'], base_model.updated_at.isoformat())
        '''
        dict_repr = self.__dict__.copy()
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        dict_repr['__class__'] = self.__class__.__name__
        return dict_repr
        '''
if __name__ == '__main__':
    unittest.main()

