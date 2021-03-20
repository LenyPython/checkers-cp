import pygame as pg
from .constants import BLUE,ORANGE


class Button:
	pg.font.init()
	font = pg.font.SysFont("cosmicsansms", 50)
	
	def __init__(self, x, y, text='', func=None):
		self.x = x
		self.y = y
		self.img = self.font.render(text, True, BLUE)
		self.width = self.img.get_width() + 20
		self.height = self.img.get_height()  + 20
		self.background = pg.Rect(x - 10, y - 10, self.width, self.height)
		self.function = func

	def pressed(self):
		self.function()
	
	def drawButton(self, win):
		pg.draw.rect(win, ORANGE, self.background)
		win.blit(self.img, (self.x, self.y))

if __name__ == '__main__':
	pass
