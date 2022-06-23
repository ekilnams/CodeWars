import unittest
import Kata

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Kata.barista([]),0,'Sorry, but the smallest waiting time possible is: 0')

    def test_2(self):
        self.assertEqual(Kata.barista([2,10,5,3,9]),85,'Sorry, but the smallest waiting time possible is: 85')

    def test_3(self):
        self.assertEqual(Kata.barista([4,3,2]),22, 'Sorry, but the smallest waiting time possible is: 22')

    def test_4(self):
        self.assertEqual(Kata.barista([20,5]),32, 'Sorry, but the smallest waiting time possible is: 32')

    def test_5(self):
        self.assertEqual(Kata.barista([20,5,4,3,1,5,7,8]),211, 'Sorry, but the smallest waiting time possible is: 211')

    def test_6(self):
        self.assertEqual(Kata.barista([5,4,3,2,1]),55, 'Sorry, but the smallest waiting time possible is: 55')

if __name__ == '__main__':
    unittest.main()
