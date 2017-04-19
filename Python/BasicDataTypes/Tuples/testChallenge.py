import unittest
import challenge


class TestChallenge(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_hash(self):
        o = (1, 2, 3, 4, 5)
        a = challenge.create_hash(o)
        e = hash(o)
        self.assertEqual(a, e)

if __name__ == "__main__":
    unittest.main()
