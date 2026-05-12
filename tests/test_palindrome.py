import unittest
from lecture import test_palindrome_long
from lecture import is_palindrome

class MyTestCase(unittest.TestCase):
    def test_palindrome0(self):
        s = 'a'
        self.assertTrue(is_palindrome(s))

    def test_palindrome1(self):
        s = 'hello'
        self.assertFalse(is_palindrome(s))

    def test_palindrome2(self):
        s = 'madam'
        self.assertTrue(is_palindrome(s))

    def test_palindrome3(self):
        s = '0111111111111111110'
        self.assertTrue(is_palindrome(s))

    def test_palindrome_long(self):
        long_s = "1" * 2000
        self.assertTrue(verify_palindrome_long(long_s))