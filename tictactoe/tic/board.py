import pygame as pg
from .constants import WIDTH, HEIGHT, RED, LBLUE, BLUE

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

	def drawXO(self, win):
		for y in range(3):
			for x in range(3):
				if self.board[y][x] == 'X':
					pg.draw.line(win, LBLUE, (25 + 200 * x, 25 + 200 * y), (175 + 200 * x, 175 + 200 * y), width = 10)
					pg.draw.line(win, LBLUE, (25 + 200 * x, 175 + 200 * y), (175 + 200 * x, 25 + 200 * y), width = 10)
				elif self.board[y][x] == 'O':
					pg.draw.circle(win, LBLUE,(100 + 200 * x,100 + 200 * y), 75, width = 10)

					

	def drawLines(self, win):
		for x in range(1,4):
			pg.draw.line(win, BLUE, (200 * x,0), (200 * x,HEIGHT), 5)
			if x < 3:
				pg.draw.line(win, BLUE, (0,200 * x), (600,200 * x), 5)

	def error(self, win, pos):
		pg.draw.circle(win, RED, pos, 20, width=5)
		pg.draw.line(win, RED, (pos[0] - 25, pos[1] - 25), (pos[0] + 25, pos[1] + 25), width = 5)
		pg.draw.line(win, RED, (pos[0] + 25, pos[1] - 25), (pos[0] - 25, pos[1] + 25), width = 5)



