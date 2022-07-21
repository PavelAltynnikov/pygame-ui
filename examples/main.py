import pygame
pygame.init()

from main_menu import MainMenu

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_CAPTION = 'SPACE SANDBOX'


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window = MainMenu(screen, SCREEN_CAPTION)
window.show()
