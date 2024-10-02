import unittest
from models.state import State

class TestState(unittest.TestCase):
    '''
    tests for State class
    '''
    def test_initialization(self):
        '''
        test attributtes for state
        '''
        state = State()
        state.name = ""
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()

