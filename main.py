__author__ = 'Tony'
import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMERATE_CAP = 60
BACKGROUND_COLOR = (105, 192, 255)


# initializes pygame and window properties.
def startup():
	pygame.init()
	window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
	pygame.display.set_caption("Game")
	window.fill(BACKGROUND_COLOR)


def main():
	startup()
	clock = pygame.time.Clock()

	running = True
	try:
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

			# ===== update
			clock.tick(FRAMERATE_CAP)

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