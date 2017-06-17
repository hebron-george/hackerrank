import unittest
import challenge

class TestChallenge(unittest.TestCase):

	'''
	In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
	In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
	In the third line, print True if  has any digits. Otherwise, print False. 
	In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
	In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
	'''

	def test_string_has_alphanumeric(self):
		e = True
		a = challenge.validate_string("123")[0]

		self.assertEquals(a, e)

	def test_string_has_alphabetical(self):
		e = True
		a = challenge.validate_string("abc")[1]

		self.assertEquals(a, e)

	def test_string_has_digits(self):
		e = True
		a = challenge.validate_string("123")[2]

		self.assertEquals(a, e)

	def test_string_has_lowercase(self):
		e = True
		a = challenge.validate_string("ABCa")[3]

		self.assertEquals(a, e)

	def test_string_has_uppercase(self):
		e = True
		a = challenge.validate_string("abcA")[4]

		self.assertEquals(a, e)

	def test_sample(self):
		e = [True, True, True, True, True]
		a = challenge.validate_string("qA2")

		self.assertEquals(a, e)


if __name__ == "__main__":
	unittest.main()
