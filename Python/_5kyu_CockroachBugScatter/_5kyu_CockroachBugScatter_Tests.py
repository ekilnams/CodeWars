import unittest
import Kata

class Tests(unittest.TestCase):
    def test_1(self):
        expected = [1,2,2,5,0,0,0,0,0,0]
        room=["+----------------0---------------+",
              "|                                |",
              "|                                |",
              "|          U        D            |",
              "|     L                          |",
              "|              R                 |",
              "|           L                    |",
              "|  U                             1",
              "3        U    D                  |",
              "|         L              R       |",
              "|                                |",
              "+----------------2---------------+"]
        self.assertEqual(Kata.cockroaches(room), expected)

    def test_2(self):
        expected = [0,2,2,3,2,1,1,0,0,0]
        room=["+----4----------0------5-------6-+",
              "|                                |",
              "|                                |",
              "|          U        D       U    |",
              "|     L                          |",
              "|              R                 |",
              "|           L                    |",
              "|  U                             1",
              "3        U    D                  |",
              "|         L              R       |",
              "|                                |",
              "+----------------2---------------+"]
        self.assertEqual(Kata.cockroaches(room), expected)

    def test_3(self):
        expected = [0,0,1,0,0,0,0,0,0,0]
        room=["123",
              "8U4",
              "765"]
        self.assertEqual(Kata.cockroaches(room), expected)

    def test_4(self):
        expected = [0,1,1,2,0,0,0,0,0,0]
        room=["+-----123---+",
              "|           |",
              "|           |",
              "|    UUUU   |",
              "|           |",
              "+-----------+"]
        self.assertEqual(Kata.cockroaches(room), expected)

if __name__ == '__main__':
    unittest.main()
