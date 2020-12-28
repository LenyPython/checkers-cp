import pygame as pg
from .constants import ROWS,BLACK,RED,SQUARE_SIZE

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
