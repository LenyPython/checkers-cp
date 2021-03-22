import random

class Player:
	def __init__(self, sign):
		self.sign = sign

class Human(Player):
	def __init__(self, sign):
		super().__init__(sign)

	def make_move(self, game):
		pass
		
class Ai(Player):
	def __init__(self, sign):
		super().__init__(sign)
	
	def make_move(self, game):
		return random.choice(game.getMoves())






