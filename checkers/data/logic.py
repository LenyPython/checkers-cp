import pygame as pg
from .constants import RED, WHITE, GREEN, SQUARE_SIZE
from .board import Board

class Game:
	'''
	Game logic holding board, checking for player turn,
	counting available player moves, drawing and updating game
	'''

	def __init__(self, win):
		self._init()
		self.win = win

	def _init(self):
		self.selected = None
		self.board = Board()
		self.turn = [RED, WHITE]
		self.valid_moves = {}

	def reset(self):
		self._init()
	
	# select and change self.selected to choosen piece
	def select(self, row, col):
		if self.selected:
			result = self._move(row, col)
			if not result:
				self.selected = None
				self.select(row, col)
		piece = self.board.selectPiece(row, col)
		if piece != 0 and piece.color == self.turn[0]:
			self.selected = piece
			self.valid_moves = self.board.validMoves(piece)
			return True
		return False

	# change piece position in it's in valid moves
	def _move(self, row, col):
		piece = self.board.selectPiece(row, col)
		if self.selected and piece == 0 and (row, col) in self.valid_moves:
			self.board.movePiece(self.selected, row, col)	
			skip = self.valid_moves[(row, col)]
			if skip:
				self.board.remove(skip)
			self.changeTurn()
		else:
			return False
		return True

	# draws a green circle in the valid moves squares
	def drawAvailableMoves(self, moves):
		for move in moves:
			row, col = move
			pg.draw.circle(self.win, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 10)

	def changeTurn(self):
		self.valid_moves = []
		self.turn.reverse()

	# draws board and acctual positon of pieces
	def update(self):
		self.board.drawBoard(self.win)
		self.board.drawPieces(self.win)
		self.drawAvailableMoves(self.valid_moves)
		pg.display.update()


	# check for match winner	
	def winner(self):
		if self.redPieces == 0:
			return WHITE
		elif self.whitePieces == 0:
			return RED
		return None
