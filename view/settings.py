# import menues.main_menu
import pygame
from pygame import display, time


class MainMenu:
    def __init__(self, width, heigth, caption):
        display.set_mode((width, heigth))
        display.set_caption('space sandbox')
        self._clock = time.Clock()
        self._FPS = 60

    def main_loop(self):
        while True:
            self._clock.tick(self._FPS)

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    return

            display.update()


if __name__ == '__main__':
    pygame.init()
    window = MainMenu(1000, 500, 'asdf')
    window.main_loop()
