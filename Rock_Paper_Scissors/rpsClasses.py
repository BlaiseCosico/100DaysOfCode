class Player:
	def __init__(self, name):
		self.name = name


class Roll:
	def __init__(self, name, defeated_by_self):
		self.name = name
		self.defeated_by_self = defeated_by_self
		

class Rock(Roll):
	def can_defeat(self, p2_roll):
		if p2_roll in self.defeated_by_self:
			return True
		return False

class Paper(Roll):
	def can_defeat(self, p2_roll):
		if p2_roll in self.defeated_by_self:
			return True
		return False

class Scissors(Roll):

	def can_defeat(self, p2_roll):
		if p2_roll in self.defeated_by_self:
			return True
		return False