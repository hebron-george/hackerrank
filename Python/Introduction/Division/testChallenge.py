import unittest
from challenge import Divider


class TestChallenge(unittest.TestCase):

    def setUp(self):
        self.divider = Divider()

    def test_int_division_4_and_16(self):
        actual = self.divider.intDivide(4, 16)
        expected = 0
        self.assertEqual(actual, expected)

    def test_float_division_4_and_16(self):
        actual = self.divider.floatDivide(4, 16)
        expected = 0.25
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()