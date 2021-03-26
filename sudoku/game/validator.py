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
