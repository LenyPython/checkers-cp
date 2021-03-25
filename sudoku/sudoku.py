import pygame as pg
from game.constants import WIDTH, HEIGHT, WHITE, GREY
from game.board import Board

def mark_spot(board, x, y):
	if not board.selected:
		board.select_spot(y, x)
	elif x == board.selected['x'] and y == board.selected['y']:
		board.unselect()
	else:
		board.select_spot(y, x)

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
				x_pos, y_pos = pg.mouse.get_pos()
				if 10 < x_pos < 685 and 10 < y_pos < 685:
					x_pos = (x_pos - 10) // 75
					y_pos = (y_pos - 10) // 75
					mark_spot(game, x_pos, y_pos)
	
		if game.selected:
			pg.draw.circle(WIN, GREY, ((game.selected['x'] * 75) + 48, (game.selected['y'] * 75) + 48), 35)
			print(game.board)

		game.draw_buttons(WIN)
		game.draw_lines(WIN)
		pg.display.update()
	pg.quit()

if __name__ == '__main__':
	main()
