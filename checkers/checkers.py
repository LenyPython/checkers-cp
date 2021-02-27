import pygame as pg
from data.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from data.board import Board
from data.logic import Game

FPS = 60
WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('CHECKERS')

def getMousePosition(pos):
	x, y = pos
	col = x // SQUARE_SIZE
	row = y // SQUARE_SIZE
	return row, col

def main():
	run = True
	clock = pg.time.Clock()
	game = Game(WIN)

	while run:
		clock.tick(FPS)

		if game.winner():
			game.winner()

		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False

			if event.type == pg.MOUSEBUTTONDOWN:
				pos = pg.mouse.get_pos()
				row, col = getMousePosition(pos)
				game.select(row, col)
	
		game.update()
	pg.quit()


if __name__ == '__main__':

	main()

