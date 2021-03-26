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
	squares = [[], [], [], [], [], [], [], [], []]
	if any(n not in col for col in zip(*board) for n in range(1,10)): return False
	for i, row in enumerate(board):
		if any(n not in row for n in range(1,10)): return False
		if i < 3:
			squares[0].extend(row[:3])
			squares[1].extend(row[3:6])
			squares[2].extend(row[6:])
		elif i < 6:
			squares[3].extend(row[:3])
			squares[4].extend(row[3:6])
			squares[5].extend(row[6:])
		else:
			squares[6].extend(row[:3])
			squares[7].extend(row[3:6])
			squares[8].extend(row[6:])
	for square in squares:
		if any(n not in square for n in range(1,10)): return False
		
	return True
