import unittest
from challenge import ArithmeticOperator


class TestChallenge(unittest.TestCase):

    def setUp(self):
        self.math = ArithmeticOperator()

    def test_sum_neg3_and_5(self):
        actual = self.math.sum(-3,5)
        expected = 2
        self.assertEqual(actual, expected)

    def test_subtract_neg4_and_12(self):
        actual = self.math.subtract(-4, 12)
        expected = -16
        self.assertEqual(actual, expected)

    def test_multiple_neg3_and_8(self):
        actual = self.math.multiply(-3, 8)
        expected = -24
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()