import numpy as np
import random
import pygame as pg
from .validator import valid_solution
from .button import Button
from .constants import WIDTH, HEIGHT, BLACK, GREY
from .creator import create_board

class Board:
	def __init__(self):
		self.board = []
		self.selected = None
		self.buttons = [Button(750, 15, 'Create board', width=350, border=5, func=self.create_game),
						Button(750, 115, 'Show creation', width=350, border=5,func=self.print_board),
						Button(750, 215, 'Check solution', width=350, border=5, func=self.solution_check),
						Button(750, 315, 'Backtrack solution', width=350, border=5),
						Button(750, 415, 'Clear board', width=350, border=5)]
	
	def create_game(self):
		self.board = create_board()

	def solution_check(self):
		if valid_solution(self.board):
			print('solution is valid')
		else:
			print('Wrong')
	
	def print_board(self):
		print(self.board)
		 
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



