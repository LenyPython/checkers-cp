import pygame as pg
from .constants import GREY, BLACK


class Button:
	pg.font.init()
	font = pg.font.SysFont("cosmicsansms", 50)
	
	def __init__(self, x, y, text='', width=0, height=0, border=0, func=None):
		self.x = x
		self.y = y
		self.img = self.font.render(text, True, BLACK)
		if width > self.img.get_width() + 20:
			self.width = width
		else:
			self.width = self.img.get_width() + 20
		if height > self.img.get_height() + 20:
			self.height = self.img.get_height()  + 20
		else:
			self.height = self.img.get_height()  + 20
		self.background = pg.Rect(x - 10, y - 10, self.width, self.height)
		self.border = border
		self.function = func

	def pressed(self):
		self.function()
	
	def draw_button(self, win):
		if self.border:
			pg.draw.rect(win, BLACK, self.background, width=self.border)
		pg.draw.rect(win, GREY, self.background)
		win.blit(self.img, (self.x, self.y))

if __name__ == '__main__':
	pass
