import unittest
import challenge


class TestChallenge(unittest.TestCase):

    def setUp(self):
        pass

    def test_swap_case_single_word(self):
        e = "tEST"
        a = challenge.swap_case("Test")
        self.assertEqual(a, e)

    def test_swap_with_spaces_and_numbers(self):
        e = "hELLO wORLD 1234!"
        a = challenge.swap_case("Hello World 1234!")
        self.assertEqual(a, e)

if __name__ == "__main__":
    unittest.main()
