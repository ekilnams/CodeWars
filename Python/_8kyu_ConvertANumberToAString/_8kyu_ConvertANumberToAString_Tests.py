import unittest
import Kata

class Tests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Kata.number_to_string(67), '67')

    def test_2(self):
        self.assertEqual(Kata.number_to_string(79585), '79585')

    def test_3(self):
        self.assertEqual(Kata.number_to_string(79585), "79585")

    def test_4(self):
        self.assertEqual(Kata.number_to_string(1+2), '3')

    def test_5(self):
        self.assertEqual(Kata.number_to_string(1-2), '-1')

if __name__ == '__main__':
    unittest.main()
