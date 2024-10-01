import unittest
from models.state import State

class TestState(unittest.Testcase):
    '''
    tests for State class
    '''
    def test_initialization(self):
        '''
        test to check if State is from State and if name is empty
        '''
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(stat.name, "")

    def test_atters(self):
        '''
        test attributtes for state
        '''
        state = State()
        state.name = "Texas"
        self.assertEqual(state.name, "Texas")

    def test_to_dict_method(self):
        '''
        tests to check if part of dictionary
        '''
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], "")

    def test_save_method(self):
        '''
        test to see if save works properly
        '''
        state = State()
        old_update_at = state.updated_at 
        state.save()
        self.assertNotEqual(state.uodated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
