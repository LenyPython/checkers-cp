import numpy as np

def valid_input(board, row, col, num):
	if num in board[row] or num in board[:, col:col + 1]: return False
	for r in range(3,10,3):
		if row < r:
			for c in range(3,10,3):
				if col < c:
					if num in board[r - 3:r, c - 3:c]: return False
					return True


def valid_solution(board):
	if any(n not in row for row in board for n in range(1,10)): return False
	temp = zip(*board)
	if any(n not in col for col in temp for n in range(1,10)): return False
	for x in range(0,7,3):
		if any(n not in board[x * 3:x * 3 + 3,x * 3:x * 3 + 3] for n in range(1,10)):
			print('failed')
			return False

	return True
