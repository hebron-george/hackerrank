import unittest
import challenge

class TestChallenge(unittest.TestCase):

	def test_print_1(self):
		e = " 1  1  1  1"
		a = challenge.print_formatted(1)

		self.assertEquals(a, e)


if __name__ == "__main__":
	unittest.main()
