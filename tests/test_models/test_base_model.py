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
        '''
        model = BaseModel()
        old_updated_at = model.updated_at
        new_updated_at = model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(new_updated_at > old_updated_at)
        self.assertIn(f"BaseModel.{model.id}, storage.all()")
        '''
        self.updated_at = datetime.now()

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
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], BaseModel)
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())
        '''
        dict_repr = self.__dict__.copy()
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        dict_repr['__class__'] = self.__class__.__name__
        return dict_repr

if __name__ == '__main__':
    unittest.main()