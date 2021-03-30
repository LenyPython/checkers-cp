import pygame as pg
from game.constants import WIDTH, HEIGHT, WHITE, GREY
from game.board import Board

def mark_spot(board, x, y):
	if not board.board[y][x]: 
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
		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False
			if event.type == pg.KEYDOWN:
				if game.selected and pg.key.name(event.key) in '123456789':
					game.user_input[game.selected['y']][game.selected['x']] = str(event.key - 48)
					game.unselect()
					
			if event.type == pg.MOUSEBUTTONDOWN:
				x_pos, y_pos = pg.mouse.get_pos()
				if 10 < x_pos < 685 and 10 < y_pos < 685:
					x_pos = (x_pos - 10) // 75
					y_pos = (y_pos - 10) // 75
					mark_spot(game, x_pos, y_pos)
				else:
					for button in game.buttons:
						if button.x < x_pos < button.x + button.width and button.y < y_pos < button.y + button.height:
							button.function()


		game.draw_all()
		pg.display.update()
	pg.quit()

if __name__ == '__main__':
	main()
