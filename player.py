class Player(object):
	#charsLeft = 0

	def add_char(self, id_char):
		self.listChars.append(id_char)
		self.charsLeft = self.charsLeft + 1

	def printTeam(self):
		print "TEAM:"
		for i in range(0, len(self.listChars)):
			print str(i) + " " + self.listChars[i]

	def __init__(self, numberPicks):
		self.numberPicks = numberPicks
		self.charsLeft = 0
		self.listChars = []
		self.team = numberPicks
		self.currentchar = 0

	def set_char(self, char_id):
		self.currentchar = char_id

	def get_char_name(self):
		return self.listChars[self.currentchar]

	def get_char_id(self):
		return self.currentchar

	def remove_char(self):
		self.listChars.remove(self.listChars[self.currentchar])
		self.team = self.team-1
		return self.team



