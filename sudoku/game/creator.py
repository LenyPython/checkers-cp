from .validator import valid_input
import random
import numpy as np

def create_board(board, show=None):

	'''sudoku creation algorithm. first filling the diagonal squares. then recursively
	adding other spots. Afterwards removing random i number of them. You can display this
	algorithm by passing a function show as argument'''
	for square in range(3):
		fill_the_square(board, square, show)
	fill_remaining_spots(board, show)
	remove_random_spots(board, show)

def remove_random_spots(board, show=None, i = 46):
	'''Remove i items form the borad of dimmentions 9x9'''
	while i:
		x, y = random.randint(0,8), random.randint(0,8)
		if board[x][y]:
			board[x][y] = 0
			if show: show()
			i -= 1


def fill_the_square(board, square, show=None):
	 '''Fill the three diagonal squares with randomly generated numbers'''
	 while 0 in board[3 * square:3 * square + 3,3 * square:3 * square + 3]:
		 for num in range(1,10):
			 num_not_in = True
			 while num_not_in:
				 x, y = random.randint(3 * square,3 * square +2), random.randint(3 * square, 3 * square + 2)
				 if not board[x][y]:
					 board[x][y] = num
					 if show: show()
					 num_not_in = False

def fill_remaining_spots(board, show=None, i = 0, j = 0):
	 '''fill the sudoku board recursively'''

	 #change row after reaching last column
	 if i < 9 and j >= 9: i, j = i + 1, 0
	 if i >= 8 and j >= 6: return True
	 #pass first filled diagonal square
	 if i < 3 and j < 3: j = 3
	 #pass second diagonal square
	 if 2 < i < 6 and 2 < j < 6: j += 3
	 #pass last diagonal square
	 if 5 < i and 5 < j: 
		 j = 0
		 i += 1

	 for num in range(1,10):
		 if valid_input(board, i, j, num):
			 board[i][j] = num
			 if show: show()
			 if fill_remaining_spots(board, show, i, j + 1):
				 return True
		 board[i][j] = 0
	 return False

