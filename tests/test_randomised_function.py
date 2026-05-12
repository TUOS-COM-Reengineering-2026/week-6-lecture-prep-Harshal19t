import unittest
from unittest.mock import patch
from lecture import randomised_function

class MyTestCase(unittest.TestCase):

    @patch('lecture.randint')
    def test_randomised_function_software(self, mock_randint):
        mock_randint.return_value = 2
        self.assertEqual('software', randomised_function())

    @patch('lecture.randint')
    def test_randomised_function_engineering(self, mock_randint):
        mock_randint.return_value = 8
        self.assertEqual('engineering', randomised_function())