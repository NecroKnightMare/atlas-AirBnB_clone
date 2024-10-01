import unittest
from models.state import State

class TestState(unittest.TestCase):
    '''
    tests for State class
    '''
    def test_initialization(self):
        '''
        test to check if State is from State and if name is empty
        '''
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "")

    def test_atters(self):
        '''
        test attributtes for state
        '''
        state = State()
        state.name = "Oklahoma"
        self.assertEqual(state.name, "Oklahoma")

    def test_to_dict_method(self):
        '''
        tests to check if part of dictionary
        '''
        state = State(name="Oklahoma")
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], "Oklahoma")

    def test_save_method(self):
        '''
        test to see if save works properly
        '''
        state = State(name="Oklahoma")
        old_updated_at = state.updated_at 
        state.save()
        self.assertNotEqual(state.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()

