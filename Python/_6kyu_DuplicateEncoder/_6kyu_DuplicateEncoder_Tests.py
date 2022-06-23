import unittest
import Kata

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Kata.duplicate_encode("din"),"(((")

    def test_2(self):
        self.assertEqual(Kata.duplicate_encode("recede"),"()()()")

    def test_3(self):
        self.assertEqual(Kata.duplicate_encode("Success"),")())())","should ignore case")

    def test_4(self):
        self.assertEqual(Kata.duplicate_encode("(( @"),"))((")

if __name__ == '__main__':
    unittest.main()