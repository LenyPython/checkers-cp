import pygame as pg
from .constants import COLS, ROWS, BLACK, RED, SQUARE_SIZE, WHITE, GREEN
from .piece import Piece

class Board:
	'''
	Contains:
	board list for pieces position
	number of white and red pieces
	method for placing pieces at init
	method for drawing a board
	'''

	def __init__(self):
		self.board = []
		self.piece = None
		self.redPieces = self.whitePieces = 12
		self.redKings = self.whiteKings = 0
		self.placePieces()

	def placePieces(self):
		for row in range(ROWS):
			self.board.append([])
			for col in range(COLS):
				if col % 2 == ((row +1) % 2):
					if row < 3:
						self.board[row].append(Piece(row, col, WHITE))
					elif row > 4:
						self.board[row].append(Piece(row, col, RED))
					else:
						self.board[row].append(0)
				else:
					self.board[row].append(0)

	# draw red and black squares
	def drawBoard(self, win):
		win.fill(BLACK)	
		for row in range(ROWS):
			for col in range(row % 2, ROWS, 2):
				pg.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

	# draw pieces placed in self.board 
	def drawPieces(self, win):
		for row in range(ROWS):
			for col in range(COLS):
				piece = self.board[row][col]
				if piece != 0:
					piece.draw(win)

	def selectPiece(self, row, col):
		return self.board[row][col]
	
	# change piece position by placing it in correct row and column
	# in self.board
	def movePiece(self, piece, row, col):
		self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
		piece.changePosition(row, col)

		if row == ROWS - 1 or row == 0:
			piece.makeKing()
			if piece.color == WHITE:
				self.whiteKings += 1
			else:
				self.redKings += 1
	
	# remove piece by changing correct row and col in self.board
	# from class Piece to 0
	def remove(self, pieces):
		for piece in pieces:
			self.board[piece.row][piece.col] = 0
			if piece != 0:
				if piece.color == RED:
					self.redPieces -= 1
				else:
					self.whitePieces -= 1

	# validate moves for selected piece
	def validMoves(self, piece):
		moves = {}
		left = piece.col - 1
		right = piece.col + 1
		up = -1
		down = 1
		row = piece.row

		if piece.color == RED or piece.king:
			moves.update(self._check_movements(row + up, max(row + up * 3, up), up, piece.color, left))
			moves.update(self._check_movements(row + up, max(row + up * 3, up), up, piece.color, right))
		if piece.color == WHITE or piece.king:
			moves.update(self._check_movements(row + down, min(row + down * 3, ROWS), down, piece.color, left))
			moves.update(self._check_movements(row + down, min(row + down * 3, ROWS), down, piece.color, right))

		return moves

	# hidden method for searchig valid moves for selected piece
	def _check_movements(self, start, stop, step, color, position, skip=[]):
		moves = {}
		last = []
		for r in range(start, stop, step):
			if position < 0 or position >= len(self.board[0]): break
			current = self.board[r][position]
			if current == 0:
				if skip and not last: break
				elif skip:
					moves[(r, position)] = last + skip
				else:
					moves[(r, position)] = last

				if last:
					if step == -1:
						row = max(r - 3, 0)
					else:
						row = min(r + 3, ROWS)
					moves.update(self._check_movements(r + step, row, step, color, position - 4, skip))
					moves.update(self._check_movements(r + step, row, step, color, position - 4, skip))
				break
			elif current.color == color:
				break
			else:
				last = [current]

			position += step

		return moves

