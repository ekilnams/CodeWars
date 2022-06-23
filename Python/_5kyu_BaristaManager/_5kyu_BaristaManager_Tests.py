import unittest
import Kata

class Tests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Kata.barista([0,0,1], 1), 1)

    def test_2(self):
        self.assertEqual(Kata.barista([2,3,4], 1), 22)

    def test_3(self):
        self.assertEqual(Kata.barista([2,3,4], 2), 13)

    def test_4(self):
        self.assertEqual(Kata.barista([2,3,4], 3), 9)

if __name__ == '__main__':
    unittest.main()
