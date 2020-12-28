from .constants import RED,SQUARE_SIZE,YELLOW
import pygame as pg
class Piece:
	PADDING = 10
	OUTLINE = 2

	def __init__(self,row,col,color):
		self.row = row
		self.col = col
		self.color = color
		self.king = False

		if self.color == RED:
			self.direction = -1
		else:
			self.direction = 1

		self.position = [0,0]
		self.findPositon()

	def findPositon(self):
		self.position[0] = SQUARE_SIZE * self.col + SQUARE_SIZE//2
		self.position[1] = SQUARE_SIZE * self.row + SQUARE_SIZE//2
	
	def makeKing(self):
		self.king = True
	
	def draw(self, win):
		radius = SQUARE_SIZE//2 - self.PADDING
		pg.draw.circle(win, YELLOW, (self.position[0],self.position[1]), radius)
		pg.draw.circle(win, self.color, (self.position[0],self.position[1]), radius-self.OUTLINE)

	def __repr__(self):
		return str(self.color)
