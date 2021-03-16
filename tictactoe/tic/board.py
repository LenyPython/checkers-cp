import pygame as pg
from .constants import WIDTH, HEIGHT, RED, LORANGE, ORANGE
from .button import Button

class Board:
	"""Class board for game logic"""

	def __init__(self):
		self._createBoard()
		self.buttons = [

				]

	def _createBoard(self):
		self.reset()
		self.wins = {'X': 0, 'O': 0}

	def reset(self):
		self.board = [[0, 0, 0],
						[0, 0, 0],
						[0, 0, 0]]
		self.turn = ['X', 'O']
		self.left = 9
	
	def changeTurn(self):
		self.turn.reverse()
	
	def getRowCol(self, tup):
		"""gets tuple argument and returns row and col in list"""
		return tup[0] // 200, tup[1] // 200

	def placeSign(self, row, col):
		self.board[row][col] = self.turn[0]
		self.changeTurn()
		self.left -= 1

	def drawXO(self, win):
		'''Draws X's and O's placed in board.board'''
		for y in range(3):
			for x in range(3):
				if self.board[y][x] == 'X':
					pg.draw.line(win, LORANGE, (25 + 200 * x, 25 + 200 * y), (175 + 200 * x, 175 + 200 * y), width = 10)
					pg.draw.line(win, LORANGE, (25 + 200 * x, 175 + 200 * y), (175 + 200 * x, 25 + 200 * y), width = 10)
				elif self.board[y][x] == 'O':
					pg.draw.circle(win, LORANGE,(100 + 200 * x,100 + 200 * y), 75, width = 10)

	def drawLines(self, win):
		'''Draw board lines, creates 3 rows and cols'''
		for x in range(1,4):
			pg.draw.line(win, ORANGE, (200 * x,0), (200 * x,HEIGHT), 5)
			if x < 3:
				pg.draw.line(win, ORANGE, (0,200 * x), (600,200 * x), 5)

	def error(self, win, pos):
		'''Shows a crossed circle if clicked on closed position'''
		pg.draw.circle(win, RED, pos, 20, width=5)
		pg.draw.line(win, RED, (pos[0] - 25, pos[1] - 25), (pos[0] + 25, pos[1] + 25), width = 5)
		pg.draw.line(win, RED, (pos[0] + 25, pos[1] - 25), (pos[0] - 25, pos[1] + 25), width = 5)

	#some debuging cuz 3rd row wins does not count correctly
	def checkWinner(self):
		for i in range(0, 3):
			if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0: return self.board[0][i]
			if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0: return self.board[i][0]
		if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:	return self.board[2][2]
		elif self.board[0][2] == self.board[1][1] == self.board[2][0] != 0: return self.board[2][0]

	def addScore(self, winner):
		self.wins[winner] += 1
