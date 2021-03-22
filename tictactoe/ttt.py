import pygame as pg
import time
from tic.board import Board
from tic.constants import WIDTH, HEIGHT, BG, RED, BLUE

pg.init()
WIN = pg.display.set_mode((WIDTH,HEIGHT))
font = pg.font.SysFont("cosmicsansms", 90)
pg.display.set_caption("TicTacToe")
FPS = 60

def drawGame(win, board):
	board.drawLines(win)
	board.drawXO(win)
	board.drawButtons(win)
	scoreX = font.render(f'X: {board.score["X"]}', True, BLUE)
	scoreO = font.render(f'O: {board.score["O"]}', True, BLUE)
	win.blit(scoreX, (620,0))
	win.blit(scoreO, (770,0))

def getWinner(win, board):
	winner = board.checkWinner()
	if winner:
		wins = font.render(f'{winner}\'s wins!', True, RED)
		win.blit(wins, (200, 200))
		pg.display.update()
		time.sleep(2)
		board.addScore(winner)
		board.reset()

	#if non moves left set tie and reset after few sec
	if not board.left:
		tie = font.render('!!!TIE!!!', True, RED)
		win.blit(tie, (200, 200))
		pg.display.update()
		time.sleep(2)
		board.reset()	

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

			current_player = board.turn[board.left % 2 - 1]
			#get mouse position at button down event
			if event.type == pg.MOUSEBUTTONDOWN:
				clickPosition = pg.mouse.get_pos()
				if clickPosition[0] <= 600:
					col, row = board.getRowCol(clickPosition)
					#if position is diffrent than 0 show error
					if board.board[row][col]:
						board.error(WIN, clickPosition)
					#if position is empty/0 place player sign
					else:
						board.placeSign(row, col)
				else:
					for button in board.buttons:
						if button.x < clickPosition[0] < button.x + button.width and button.y < clickPosition[1] < button.y + button. height:
							button.function()

		drawGame(WIN, board)
		pg.display.update()
		getWinner(WIN, board)

	pg.quit()

if __name__ == '__main__':
	main()
