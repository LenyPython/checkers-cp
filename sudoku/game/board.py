import numpy as np
import pygame as pg
from .constants import WIDTH, HEIGHT, BLACK, GREY

class Board:
	def __init__(self):
		self.board = np.zeros((9,9))
		self.selected = None
	
	def draw_lines(self, win):
		for i in range(10):
			pg.draw.line(win, BLACK, (10, 10 + 75 * i), (685, 10 + 75 * i), width=5)
			pg.draw.line(win, BLACK, (10 + 75 * i, 10), (10 + 75 * i, 685), width=5)
	
	def draw_board(self, win):
		pass



