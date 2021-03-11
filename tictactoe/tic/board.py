import pygame as pg
from .constants import WIDTH, HEIGHT

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

	def drawLines(self, win):
		for x in range(1,4):
			pg.draw.line(win, (255,255,255), (200 * x,0), (200 * x,HEIGHT), 5)
			if x < 3:
				pg.draw.line(win, (255,255,255), (0,200 * x), (600,200 * x), 5)
