import pygame as pg
from tic.board import Board

WIDTH, HEIGHT = 1000, 600
WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("TicTacToe")
FPS = 60

def main():
	clock = pg.time.Clock()
	run = True
	ttt = Board()
	print(ttt.board)


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
				col, row = ttt.getRowCol(clickPosition)
				pos = ttt.board[row][col]
				#if position is diffrent than 0 show error
				if pos:
					##############need debugging
					pg.draw.circle(WIN,(255,0,0), clickPosition, 15)

				#if position is empty/0 place player sign
				else:
					ttt.placeSign(row, col)
				
				for x in ttt.board:
					print(x)
				print(f'click:{clickPosition}, row: {row}, col: {col}\n \
					pos: {pos}')
				

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
