import numpy as np
import random
import pygame as pg
from .constants import WIDTH, HEIGHT, BLACK, GREY

class Board:
	def __init__(self):
		self.board = self._create_board()
		self.selected = None
	
	def _create_board(self):
		 board = np.zeros((9,9), dtype=np.int8)
		 
		 
	def select_spot(self, row, col):
		self.selected = {'x': col, 'y': row}
	
	def unselect(self):
		self.selected = None


	def draw_lines(self, win):
		for i in range(10):
			pg.draw.line(win, BLACK, (10, 10 + 75 * i), (685, 10 + 75 * i), width=5)
			pg.draw.line(win, BLACK, (10 + 75 * i, 10), (10 + 75 * i, 685), width=5)
	
	def draw_board(self, win):
		pass

	def valid_solution(board):
		check = [[], [], [], [], [], [], [], [], []]
		for i, row in enumerate(board):
			if not all(n in row for n in range(1,10)): return False
			if i < 3:
				check[0] += row[:3]
				check[1] += row[3:6]
				check[2] += row[6:]
			elif i < 6:
				check[3] += row[:3]
				check[4] += row[3:6]
				check[5] += row[6:]
			else:
				check[6] += row[:3]
				check[7] += row[3:6]
				check[8] += row[6:]
		for sub in check:
			if not all(n in sub for n in range(1,10)): return False
		check = [[x[i] for x in board] for i in range(9)]
		for sub in check:
			if not all(n in sub for n in range(1,10)): return False
		return True


