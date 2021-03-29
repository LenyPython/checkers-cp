import numpy as np
import random
import pygame as pg
from .validator import valid_solution
from .button import Button
from .constants import WIDTH, HEIGHT, BLACK, GREY, RED
from .creator import create_board

class Board:
	pg.font.init()
	font = pg.font.SysFont("cosmicsansms", 100)

	def __init__(self):
		self.board = np.zeros((9,9), dtype=np.int8)
		self.user_input = np.zeros((9,9), dtype=np.int8)
		self.selected = None
		self.buttons = [Button(750, 15, 'Create board', width=350, border=5, func=self.create_game),
						Button(750, 115, 'Show creation', width=350, border=5,func=self.show_alg),
						Button(750, 215, 'Check solution', width=350, border=5, func=self.solution_check),
						Button(750, 315, 'Backtrack solution', width=350, border=5),
						Button(750, 415, 'Clear board', width=350, border=5)]
	
	def create_game(self):
		self.board = np.zeros((9,9), dtype=np.int8)
		self.user_input = np.zeros((9,9), dtype=np.int8)
		create_board(self.board)
	
	def show_alg(self):
		pass

	def solution_check(self):
		if valid_solution(self.board + self.user_input):
			print('Solution is valid')
		else:
			print('Wrong Solution')
		 
	def select_spot(self, row, col):
		self.selected = {'x': col, 'y': row}
	
	def unselect(self):
		self.selected = None

	def draw_lines(self, win):
		for i in range(10):
			w = 9 if i % 3 == 0 else 5
			pg.draw.line(win, BLACK, (10, 10 + 75 * i), (685, 10 + 75 * i), width=w)
			pg.draw.line(win, BLACK, (10 + 75 * i, 10), (10 + 75 * i, 685), width=w)
			
	def draw_buttons(self, win):
		 for button in self.buttons:
			 button.draw_button(win)
	
	def draw_numbers(self, win):
		for y, row in enumerate(self.board):
			for x, value in enumerate(row):
				if value:
					number = self.font.render(str(value), True, BLACK)
					win.blit(number, (30 + x * 75, 15 + y * 75))
				if self.user_input[y][x]:
					number = self.font.render(str(self.user_input[y][x]), True, RED)
					win.blit(number, (30 + x * 75, 15 + y * 75))
					

	def draw_all(self, win):
		self.draw_buttons(win)
		self.draw_lines(win)
		self.draw_numbers(win)

