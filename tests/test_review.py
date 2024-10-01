import unittest
from models.review import Review

class TestState(unittest.TestCase):
    '''
    tests for Review class
    '''
    def review_aatters(self):
        '''
        test to check if review is from model and if name is empty
        '''
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    ''' def test_atters(self):
    '''
    '''
        review = Review()
        review.place_id = ""
        review.user_id =
        review.text = "Good"
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_to_dict_method(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], '')
        self.assertEqual(review_dict['place_id'], "")
        self.assertEqual(review_dict['user_id'], "")
        self.assertEqual(review_dict['text'], "")

    def test_save_method(self):
    '''
    '''
    review = Review()
        old_update_at = review.updated_at 
        review.save()
        self.assertNotEqual(review.updated_at, old_updated_at)
'''
if __name__ == '__main__':
    unittest.main()

