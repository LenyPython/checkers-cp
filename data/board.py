import pygame as pg
from .constants import COLS,ROWS,BLACK,RED,SQUARE_SIZE,WHITE
from .piece import Piece

class Board:
	def __init__(self):
		self.board = []
		self.piece = None
		self.redPieces = self.whitePieces = 12
		self.redKings = self.whiteKings = 0

	def drawBoard(self, board):
		board.fill(BLACK)	
		for row in range(ROWS):
			for col in range(row % 2, ROWS, 2):
				pg.draw.rect(board, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
	
	def placePieces():
		for row in range(ROWS):
			self.board.append([])
			for col in range(COLS):
				if col % 2 == ((row +1) % 2):
					if row < 3:
						self.board[row].append(Piece(row,col,WHITE)
					elif row >4:
						self.board[row].append(Piece(row,col,RED)
					else:
						self.borad[row].append(0)
				else:
					self.board[row].append(0)
