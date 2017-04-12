import unittest

class TestIfElse(unittest.TestCase):

	def setUp(self):
		self.myobj = IfElse()

	def tearDown(self):
		pass

	def test_over_100(self):
		pass

	def test_at_1(self):
		actual = self.myobj.main(1)
		expected = "Weird"
		self.assertEqual(actual, expected)

	def test_at_100(self):
		actual = self.myobj.main(100)
		expected = "Not Weird"
		self.assertEqual(actual, expected)

	def test_even_between_6_and_20(self):
		actual = self.myobj.main(18)
		expected = "Weird"
		self.assertEqual(actual, expected)

	def test_even_between_2_and_5(self):
		actual = self.myobj.main(2)
		expected = "Not Weird"
		self.assertEqual(actual, expected)

	def test_less_than_1(self):
		actual = self.myobj.main(0)
		expected = "Error"
		self.assertEqual(actual, expected)

	def test_greater_than_100(self):
		actual = self.myobj.main(101)
		expected = "Error"
		self.assertEqual(actual, expected)


class IfElse(object):
	def main(self, num):
		if num < 1 or num > 100:
			return "Error"
		if num % 2 == 0 and (num < 6 or num > 20): #even
			return "Not Weird"
		else: #odd
			return "Weird"

if __name__ == "__main__":
	unittest.main()

