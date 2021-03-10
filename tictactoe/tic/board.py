
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
		self.turn.reverse()
	
	def getRowCol(self, tup):
		"""gets tuple argument and returns row and col in list"""
		return tup[0] // 200, tup[1] // 200

	def placeSign(self, row, col):
		self.board[row][col] = self.turn[0]
		self.changeTurn()

