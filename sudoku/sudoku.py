import pygame as pg
from game.constants import WIDTH, HEIGHT, WHITE, GREY
from game.board import Board


def main():
	WIN = pg.display.set_mode((WIDTH, HEIGHT))
	pg.display.set_caption('Sudoku')
	FPS = 60
	clock = pg.time.Clock()
	run = True
	game = Board()

	while run:
		clock.tick(FPS)
		WIN.fill(WHITE)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False
			if event.type == pg.MOUSEBUTTONDOWN:
				clickPosition = pg.mouse.get_pos()
				x_pos, y_pos = clickPosition
				if 10 < x_pos < 685 and 10 < y_pos < 685:
					x_pos = (x_pos - 10) // 75
					y_pos = (y_pos - 10) // 75
					if not game.selected:
						game.select_spot(y_pos, x_pos)
					elif x_pos == game.selected['x'] and y_pos == game.selected['y']:
						game.unselect()
					else:
						game.select_spot(y_pos, x_pos)
	
		if game.selected:
			pg.draw.circle(WIN, GREY, ((game.selected['x'] * 75) + 48, (game.selected['y'] * 75) + 48), 35)
		game.draw_lines(WIN)
		pg.display.update()
	pg.quit()

if __name__ == '__main__':
	main()
