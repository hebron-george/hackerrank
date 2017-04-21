import unittest
import challenge


class TestChallenge(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_second_largest_1to5(self):
        a = challenge.get_second_largest([1, 2, 3, 4, 5])
        e = 4
        self.assertEqual(a, e)

    def test_get_second_largest_unordered_array(self):
        a = challenge.get_second_largest([100, 2, 8, -100, 42, -84, 99])
        e = 99
        self.assertEqual(a, e)

    def test_get_second_largest_hackerrank_input(self):
        a = challenge.get_second_largest([2, 3, 6, 6, 5])
        e = 5
        self.assertEqual(a, e)

if __name__ == "__main__":
    unittest.main()
