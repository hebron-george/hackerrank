import unittest
import challenge


class TestChallenge(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_second_lowest_scorers(self):
        a = challenge.get_second_lowest_scorers([[15.0, "Hebron"], [6.2, "George"], [18.0, "Thomas"]])
        e = ["Hebron"]
        self.assertEqual(a, e)

    def test_tied_for_second(self):
        a = challenge.get_second_lowest_scorers([[15.0, "Hebron"], [15.0, "Albert"], [6.2, "George"], [18.0, "Thomas"]])
        e = ["Albert", "Hebron"]
        self.assertEqual(a, e)

if __name__ == "__main__":
    unittest.main()
