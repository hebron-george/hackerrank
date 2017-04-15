import unittest
import challenge


class TestChallenge(unittest.TestCase):

    def setUp(self):
        pass

    def testIs1991DivisibleBy4(self):
        actual = challenge.isDivisibleBy4(1991)
        expected = False
        self.assertEqual(actual, expected)

    def test100000isDivisibleBy4(self):
        actual = challenge.isDivisibleBy4(100000)
        expected = True
        self.assertEqual(actual, expected)

    def testIs1990isDivisibleBy100(self):
        actual = challenge.isDivisibleBy100(1990)
        expected = False
        self.assertEqual(actual, expected)

    def testIs100000isDivisibleBy100(self):
        actual = challenge.isDivisibleBy100(100000)
        e = True
        self.assertEqual(actual, e)

    def test1900is_leap(self):
        a = challenge.is_leap(1900)
        e = False
        self.assertEqual(a, e)

    def test2200is_leap(self):
        a = challenge.is_leap(2200)
        e = False
        self.assertEqual(a, e)

if __name__ == "__main__":
    unittest.main()