import pygame
from pygame_ui.form import Form

class SettingsMenu(Form):
    def __init__(self, screen: pygame.surface.Surface, fps=60):
        super().__init__(screen, fps=fps)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    sm = SettingsMenu(screen)
    sm.show()
