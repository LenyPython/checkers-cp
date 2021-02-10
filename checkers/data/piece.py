from .constants import RED, SQUARE_SIZE, YELLOW, GREEN
import pygame as pg

class Piece:
	PADDING = 13
	OUTLINE = 2

	def __init__(self, row, col, color):
		self.row = row
		self.col = col
		self.color = color
		self.king = False
		self.position = [0,0]
		self.findPosition()

	def findPosition(self):
		self.position[0] = SQUARE_SIZE * self.col + SQUARE_SIZE//2
		self.position[1] = SQUARE_SIZE * self.row + SQUARE_SIZE//2
	
	def makeKing(self):
		self.king = True
	
	def draw(self, win):
		radius = SQUARE_SIZE // 2 - self.PADDING
		pg.draw.circle(win, GREEN, (self.position[0], self.position[1]), radius)
		pg.draw.circle(win, self.color, (self.position[0], self.position[1]), radius - self.OUTLINE)
		if self.king:
			pg.draw.circle(win, YELLOW, (self.position[0], self.position[1]), radius // 2)
	
	def changePosition(self, row, col):
		self.row = row
		self.col = col
		self.findPosition()


	def __repr__(self):
		return str(self.color)
