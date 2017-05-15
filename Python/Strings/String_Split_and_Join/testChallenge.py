import unittest
import challenge

class TestChallenge(unittest.TestCase):

    def setUp(self):
        pass

    def test_split_and_join_no_spaces(self):
        e = "teststringwithnospaces"
        a = challenge.split_and_join("teststringwithnospaces")
        self.assertEqual(a, e)

    def test_split_and_join_sample_input(self):
        e = "this-is-a-string"
        a = challenge.split_and_join("this is a string")
        self.assertEqual(a, e)

if __name__ == "__main__":
    unittest.main()