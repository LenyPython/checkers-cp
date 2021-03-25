import numpy as np
import random
import pygame as pg
from game.validator import valid_input, valid_solution
from game.button import Button
from .constants import WIDTH, HEIGHT, BLACK, GREY

class Board:
	def __init__(self):
		self.board = self._create_board()
		self.selected = None
		self.buttons = [Button(750, 15, 'Create board', width=350, border=5),
						Button(750, 115, 'Clear board', width=350, border=5),
						Button(750, 215, 'Check solution', width=350, border=5),
						Button(750, 315, 'Backtrack solution', width=350, border=5),
						Button(750, 415, 'Random', width=350, border=5)]
	
	def _create_board(self):
		 board = np.zeros((9,9), dtype=np.int8)
		 #first fill the diagonal squares with number from 1-9
		 for square in range(3):
			 while 0 in board[3 * square:3 * square + 3,3 * square:3 * square + 3]:
				 r_num = random.randint(1,9)
				 if r_num not in board[3 * square:3 * square + 3,3 * square:3 * square + 3]:
					 num_not_in = True
					 while num_not_in:
						 i,j = random.randint(3 * square,3 * square +2), random.randint(3 * square, 3 * square + 2)
						 if not board[i][j]:
							 board[i][j] = r_num
							 num_not_in = False
		 #fill rest of the board with random numbers meeting the requirements
		 for i, row in enumerate(board):
			 for j, value in enumerate(row):
				 if not value:
					 for num in range(1,10):
						 if valid_input(board, i, j, num):
							 board[i][j] = num
							 break
		 return board
		 
	def select_spot(self, row, col):
		self.selected = {'x': col, 'y': row}
	
	def unselect(self):
		self.selected = None

	def draw_lines(self, win):
		for i in range(10):
			pg.draw.line(win, BLACK, (10, 10 + 75 * i), (685, 10 + 75 * i), width=5)
			pg.draw.line(win, BLACK, (10 + 75 * i, 10), (10 + 75 * i, 685), width=5)
			
	def draw_buttons(self, win):
		 for button in self.buttons:
			 button.draw_button(win)
	
	def draw_board(self, win):
		pass



