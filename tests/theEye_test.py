import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../theEye')))

from theEye import get_training_data

class TestTheEye(unittest.TestCase):

    def test_training_data(self):
        self.assertEqual(get_training_data(), [1,0,1,0])

if __name__ == '__main__':
    unittest.main()