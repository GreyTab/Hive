"""
	This file is responsible for combining game logic and
	loading content onto display
"""
import pygame
from block import *
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMERATE_CAP = 60
BACKGROUND_COLOR = (105, 192, 255)  # skyblue color


def main():
	pygame.init()
	pygame.display.set_caption("Game")
	window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
	window.fill(BACKGROUND_COLOR)

	running = True
	clock = pygame.time.Clock()
	try:
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

			# ===== update
			clock.tick(FRAMERATE_CAP)

			# block test (floor)
			block_list = pygame.sprite.Group()
			for x in range(20):
				block_list.add(Block(0+(40*x), 500, 40, 100))  # 40 x 100 blocks to create a "floor"
			block_list.draw(window)

			# level
			# player

			pygame.display.update()
			# ===== end of update

		# End the game if the user calls QUIT event
		pygame.display.quit()
		pygame.quit()

	except SystemExit:
		pygame.display.quit()
		pygame.quit()

main()
