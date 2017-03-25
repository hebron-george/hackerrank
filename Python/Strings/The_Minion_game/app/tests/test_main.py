import unittest, sys
from The_Minion_game.app.main import MinionGame

class MinionTest(unittest.TestCase):
	def setUp(self):
		self.minionGame = MinionGame()
	def test_isVowel(self):
		assert self.minionGame.isVowel('a') == True
	def test_isNotVowel(self):
		assert self.minionGame.isVowel('b') == False

if __name__ == "__main__":
	unittest.main()
