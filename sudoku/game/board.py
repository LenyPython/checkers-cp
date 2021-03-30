import numpy as np
import random
import time
import pygame as pg
from .validator import valid_solution, valid_input
from .button import Button
from .constants import WIDTH, HEIGHT, BLACK, GREY, RED, WHITE
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
						Button(750, 315, 'Backtrack solution', width=350, border=5, func=self.backtrack),
						Button(750, 415, 'Clear board', width=350, border=5, func=self.clear)]
	
	def create_game(self, show=None):
		'''Creates board game withou displaing the process'''
		self.board = np.zeros((9,9), dtype=np.int8)
		self.user_input = np.zeros((9,9), dtype=np.int8)
		create_board(self.board, show)
	
	def backtrack(self):
		def solution(x = 0, y = 0):
			# go to the next row after reaching last col
			if x < 9 and y >= 9 : x,y = x + 1, 0
			#after reaching end return True
			if x >= 8 and y >= 8: return True
			for num in range(1,10):
				#if we get a filled spot move to next one
				if self.board[x][y]: solution(x, y + 1) 
				else:
					if valid_input(self.board, x, y, num):
						self.board[x][y] = num
						self.show()
						if solution(x, y + 1):
							return True
					self.board[x][y] = 0
			return False
		solution()
	
	def show(self):
		'''display function for inner use of algorithms/methods'''
		self.draw_all()
		pg.display.update()
		time.sleep(0.1)
		
	def show_alg(self):
		'''create game with show function passed in'''
		self.create_game(self.show)

	def clear(self):
		'''clears user input'''
		self.user_input = np.zeros((9,9), dtype=np.int8)


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
					

	def draw_all(self):
		win = pg.display.get_surface()
		win.fill(WHITE)
		self.draw_buttons(win)
		self.draw_lines(win)
		self.draw_numbers(win)
		if self.selected:
			pg.draw.circle(win, GREY, ((self.selected['x'] * 75) + 48, (self.selected['y'] * 75) + 48), 35)
