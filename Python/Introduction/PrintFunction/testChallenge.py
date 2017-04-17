import unittest
import challenge


class TestChallenge(unittest.TestCase):

    def testCreateNumStr1(self):
        a = challenge.createNumStr(1)
        e = "1"
        self.assertEqual(a,e)

    def testCreateNumStr5(self):
        a = challenge.createNumStr(5)
        e = "12345"
        self.assertEqual(a,e)

if __name__ == "__main__":
    unittest.main()