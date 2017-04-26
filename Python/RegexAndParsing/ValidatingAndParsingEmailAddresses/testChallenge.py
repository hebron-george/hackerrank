import unittest
import challenge


class TestChallenge(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_proper_emails(self):
        a = challenge.get_proper_emails([('DEXTER', 'dexter@hotmail.com'), ('VIRUS', 'virus!@variable.:p')])
        e = ["DEXTER <dexter@hotmail.com>"]
        self.assertEqual(a, e)

    def test_invalid_username(self):
        a = challenge.is_valid_username("virus!")
        e = False
        self.assertEqual(a, e)

    def test_is_valid_username(self):
        a = challenge.is_valid_username("dexter")
        e = True
        self.assertEqual(a, e)

    def test_is_valid_domain(self):
        a = challenge.is_valid_domain("englishalphabetcharacters")
        e = True
        self.assertEqual(a, e)

    def test_invalid_domain_(self):
        a = challenge.is_valid_domain("variable430=")
        e = False
        self.assertEqual(a, e)

    def test_invalid_domain(self):
        a = challenge.is_valid_extension("adsfafasdfaf")
        e = False
        self.assertEqual(a, e)

    def test_is_valid_extension(self):
        a = challenge.is_valid_extension("com")
        e = True
        self.assertEqual(a, e)

if __name__ == "__main__":
    unittest.main()
