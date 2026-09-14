import unittest
import string_utils

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(string_utils.reverse_string("hello"), "olleh")

    def test_capitalize_string(self):
        self.assertEqual(string_utils.capitalize_string("hello"), "Hello")

    def test_is_capitalized(self):
        self.assertTrue(string_utils.is_capitalized("Hello"))

if __name__ == '__main__':
    unittest.main()