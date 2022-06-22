import unittest
import Kata

class Tests(unittest.TestCase):
    def test_1(self):
        pangram = "The quick, brown fox jumps over the lazy dog!"
        self.assertTrue(Kata.is_pangram(pangram))

    def test_2(self):
        pangram = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(Kata.is_pangram(pangram))

    def test_3(self):
        pangram = ""
        self.assertFalse(Kata.is_pangram(pangram))

    def test_4(self):
        pangram = "abcdefghijklmnopqrstuvwxy"
        self.assertFalse(Kata.is_pangram(pangram))

    def test_5(self):
        pangram = "    23423(*£!)*( abcdefghijklmnopqrstuvwxyz     "
        self.assertTrue(Kata.is_pangram(pangram))

if __name__ == '__main__':
    unittest.main()
