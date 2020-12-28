import pygame as pg
from data.constants import WIDTH,HEIGHT
from data.board import Board

FPS = 60
WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('CHECKERS')


def main():
	run = True
	clock = pg.time.Clock()
	board = Board()

	while run:
		clock.tick(FPS)

		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False

			if event.type == pg.MOUSEBUTTONDOWN:
				pass
	
		board.drawBoard(WIN)
		pg.display.update()
	
	pg.quit()


if __name__ == '__main__':

	main()

