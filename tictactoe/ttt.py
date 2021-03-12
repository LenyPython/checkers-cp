import pygame as pg
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

		#draw lines and X's and O's
		board.drawLines(WIN)
		board.drawXO(WIN)

	
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
				
				for x in board.board:
					print(x)
				print(f'click:{clickPosition}, row: {row}, col: {col}\n \
						val: {val}')
				
			
			#update display
			pg.display.update()
	
	pg.quit()

if __name__ == '__main__':
	main()
