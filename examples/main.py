import pygame
pygame.init()

from main_menu import MainMenu

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_CAPTION = 'SPACE SANDBOX'


def function(message):
    print(message)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window = MainMenu(screen, SCREEN_CAPTION)
window.set_start_click_handler(function)
window.set_settings_click_handler(function)
window.set_exit_click_handler(function)
window.show()
