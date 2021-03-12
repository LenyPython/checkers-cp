import pygame as pg
import time
from tic.board import Board
from tic.constants import WIDTH, HEIGHT, BG

WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("TicTacToe")
FPS = 60

def main():
	clock = pg.time.Clock()
	run = True
	board = Board()

	while run:
		clock.tick(FPS)
		
		#fill background with RGB color
		WIN.fill(BG)

		#main event loop
		for event in pg.event.get():
			#geting close signal
			if event.type == pg.QUIT:
				run = False

			#get mouse position at button down event
			if event.type == pg.MOUSEBUTTONDOWN:
				clickPosition = pg.mouse.get_pos()
				col, row = board.getRowCol(clickPosition)
				val = 0
				if row < 3 and col < 3:
					val = board.board[row][col]
					#if position is diffrent than 0 show error
					if val:
						board.error(WIN, clickPosition)
					#if position is empty/0 place player sign
					else:
						board.placeSign(row, col)

		#draw lines and X's and O's
		board.drawLines(WIN)
		board.drawXO(WIN)
				
		#update display
		pg.display.update()
		#check if ther is any space left or if ther is a winner
		winner = board.checkWinner()

		####################### show winner
		if winner:
			pass
		#if non moves left set tie and reset after few sec
		if not board.left:
			time.sleep(2)
			board.reset()	
			
	
	pg.quit()

if __name__ == '__main__':
	main()
