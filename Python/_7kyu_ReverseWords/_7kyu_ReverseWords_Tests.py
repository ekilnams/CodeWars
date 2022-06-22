import unittest
import Kata

class Tests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Kata.reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')

    def test_2(self):
        self.assertEqual(Kata.reverse_words('apple'), 'elppa')

    def test_3(self):
        self.assertEqual(Kata.reverse_words('a b c d'), 'a b c d')

    def test_4(self):
        self.assertEqual(Kata.reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')

    def test_5(self):
        self.assertEqual(Kata.reverse_words(''), '')

if __name__ == '__main__':
    unittest.main()