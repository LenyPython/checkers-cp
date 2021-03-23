import pygame as pg
from game.constants import WIDTH, HEIGHT, WHITE


def main():
	WIN = pg.display.set_mode((WIDTH, HEIGHT))
	pg.display.set_caption('Sudoku')
	FPS = 60
	clock = pg.time.Clock()
	run = True

	while run:
		clock.tick(FPS)
		WIN.fill(WHITE)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False

		pg.display.update()
	pg.quit()

if __name__ == '__main__':
	main()
