import pygame as pg
from tic.board import board

WIDTH, HEIGHT = 1000, 600
WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("TicTacToe")
FPS = 60

def main():
	clock = pg.time.Clock()
	run = True
	Board = Board()


	while run:
		clock.tick(FPS)
	
		#main event loop
		for event in pg.event.get():
			#geting close signal
			if event.type == pg.QUIT:
				run = False

			#get mouse position at button down event
			if event.type == pg.MOUSEBUTTONDOWN:
				clickPosition = pg.mouse.get_pos()
				row, col = getRowCol(*clickPosition)
				pos = Board.board[row][col]
				#if position is diffrent than 0 show error
				if pos:

				#if position is empty/0 place player sign
				else:
					Board.placeSign(
				


			#fill background with RGB color
			WIN.fill((79,34,22,31))
			pg.draw.line(WIN, (255,255,255), (200,0), (200,HEIGHT), 5)
			pg.draw.line(WIN, (255,255,255), (400,0), (400,HEIGHT), 5)
			pg.draw.line(WIN, (255,255,255), (600,0), (600,HEIGHT), 5)
			pg.draw.line(WIN, (255,255,255), (0,200), (600,200), 5)
			pg.draw.line(WIN, (255,255,255), (0,400), (600,400), 5)
			

			#update display
			pg.display.update()
	
	pg.quit()

if __name__ == '__main__':
	main()
