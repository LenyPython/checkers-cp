from .validator import valid_input
import random
import numpy as np

def create_board():
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
	 fill_remaining_spots(board)
	 return board

def fill_remaining_spots(board, i = 0, j = 0):
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
			 if fill_remaining_spots(board, i, j + 1):
				 return True
		 board[i][j] = 0
	 return False

