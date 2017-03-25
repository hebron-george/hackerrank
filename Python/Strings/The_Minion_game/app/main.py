
class MinionGame():
	def __init__(self, string="Test"):
		self.s = string

	def getWinner(self):
	    # your code goes here
	    kevins_chars = self.get_kevins_character_indices()
	    stuarts_chars = self.get_stuarts_character_indices()
	    s = []
	    
	    for i in kevins_chars:
	    	s += self.getSubstringsFromIndex(i)
	    kevins_substrings = s

	    s = []

	    for i in stuarts_chars:
	    	s += self.getSubstringsFromIndex(i)
	    stuarts_substrings = s

	    stuarts_points = 0
	    kevins_points = 0

	    for i in set(stuarts_substrings):
	    	stuarts_points += stuarts_substrings.count(i)

	    for i in set(kevins_substrings):
	    	kevins_points += kevins_substrings.count(i)

	    if stuarts_points == kevins_points:
	    	return "Draw"
	    elif stuarts_points > kevins_points:
	    	return "Stuart {}".format(stuarts_points)
	    else:
	    	return "Kevin {}".format(kevins_points)


	def get_kevins_character_indices(self):
		return [index for index, c in enumerate(self.s) if self.isVowel(c)]

	def get_stuarts_character_indices(self):
		return [index for index, c in enumerate(self.s) if not self.isVowel(c)]

	def isVowel(self, s):
		if s.lower() in ['a','e','i','o','u']:
			return True
		return False

	def getSubstringsFromIndex(self, start):
		subs = []
		i = len(self.s)
		while (start < i):
			subs.append(self.s[start:i])
			i -= 1
		if len(subs) > 0:
			return subs
		return None

if __name__ == '__main__':
	s = raw_input()
	m = MinionGame(s)
	print "{}".format(m.getWinner())