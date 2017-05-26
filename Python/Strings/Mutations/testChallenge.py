import unittest
import challenge


class TestChallenge(unittest.TestCase):

    def setUp(self):
        pass

    def test_abrackdabra(self):
        e = 'abrackdabra'
        a = challenge.mutate_string('abracadabra', 5, 'k')
        self.assertEqual(a, e)

if __name__ == "__main__":
    unittest.main()
