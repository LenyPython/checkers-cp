
class Board:
	"""Class board for game logic"""

	def __init__(self):
		self._createBoard()

	def _createBoard(self):
		self.board = [[0, 0, 0],
						[0, 0, 0],
						[0, 0, 0]]
		self.turn = ['X', 'O']
		self.wins = {'X': 0, 'Y': 0}
	
	def changeTurn(self):
		self.wins.reverse()
	
	def getRowCol(self, x, y):
		return x // 200, y // 200
