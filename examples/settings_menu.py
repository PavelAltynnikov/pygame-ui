import pygame
from pygame_ui.form import Form

class SettingsMenu(Form):
    def __init__(self, screen: pygame.surface.Surface, fps=60):
        super().__init__(screen, fps=fps)
