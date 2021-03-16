import pygame as pg
from .constants import BLUE


class Button:
	pg.font.init()
	font = pg.font.SysFont("cosmicsansms", 20)
	
	def __init__(self, x, y, text='', func=None):
		self.x = x
		self.y = y
		self.img = self.font.render(text, True, BLUE)
		self.background = img.get_rect() 
		self.function = func

	def pressed(self):
		self.function()
	
	def drawButton(self, win):
		pg.draw.rect(win, self.img, BLUE, self.background)

if __name__ == '__main__':
	pass
