class Player(object):
	#charsLeft = 0

	def add_char(self, id_char):
		self.listChars.append(id_char)
		self.charsLeft = self.charsLeft + 1

	def printTeam(self):
		print "TEAM:"
		for i in range(0, len(self.listChars)):
			print self.listChars[i]

	def __init__(self, numberPicks):
		self.numberPicks = numberPicks
		self.charsLeft = 0
		self.listChars = []


