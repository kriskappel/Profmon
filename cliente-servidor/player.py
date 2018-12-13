class Player(object):
	#charsLeft = 0

	def add_char(self, id_char):
		self.listChars.append(id_char)
		self.charsLeft = self.charsLeft + 1

	def printTeam(self, id_team):
		print "TEAM, ", id_team, ":"
		for i in range(0, len(self.listChars)):
			print self.listChars[i]

	def get_char(self, id):
		return self.listChars[id]

	def get_current_char(self):
		return self.listChars[self.index]

	def update_index(self):
		self.index += 1
		if self.index == self.numberPicks:
			return True
		else:
			return False

	def __init__(self, numberPicks):
		self.numberPicks = numberPicks
		self.charsLeft = 0
		self.listChars = []
		self.index = 0


