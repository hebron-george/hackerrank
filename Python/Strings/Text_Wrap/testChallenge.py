import unittest
import challenge


class TestChallenge(unittest.TestCase):

	def test_sample(self):
		e = 'ABCD\nEFGH\nIJKL\nMNOP\nQRST\nUVWX\nYZ'
		a = challenge.wrap('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4)

		self.assertEquals(a, e)


if __name__ == "__main__":
	unittest.main()
