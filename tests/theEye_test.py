import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../theEye')))

from theEye import get_training_data
from theEye import DataPoint

class TestTheEye(unittest.TestCase):

    def test_training_data(self):
        test_data = DataPoint(input_array = [1,1,1,1])
        self.assertEqual(get_training_data()[0].input_array, test_data.input_array)

if __name__ == '__main__':
    unittest.main()