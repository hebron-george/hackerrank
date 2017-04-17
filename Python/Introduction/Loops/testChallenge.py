import unittest
import challenge


class TestChallenge(unittest.TestCase):

    def test_get_1_squares(self):
        a = challenge.get_n_squares(1)
        e = [0]
        self.assertEqual(a, e)

    def test_get_2_squares(self):
        a = challenge.get_n_squares(2)
        e = [0, 1]
        self.assertEqual(a, e)

    def test_get_5_squares(self):
        a = challenge.get_n_squares(5)
        e = [0, 1, 4, 9, 16]
        self.assertEqual(a,e)

if __name__ == "__main__":
    unittest.main()