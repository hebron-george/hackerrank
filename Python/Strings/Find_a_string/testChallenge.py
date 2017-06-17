import unittest
import challenge

class TestChallenge(unittest.TestCase):

    def setUp(self):
        pass

    def test_substr_count(self):
        e = 2
        a = challenge.count_substring('ABCDCDC', 'CDC')

        self.assertEquals(a, e)


if __name__ == "__main__":
    unittest.main()
