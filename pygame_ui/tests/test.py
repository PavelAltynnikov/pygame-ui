# import menues.main_menu
import pygame

FPS = 60

pygame.init()
pygame.display.set_mode((600, 400))
pygame.display.set_caption('space sandbox')

clock = pygame.time.Clock()


def game_loop():
    while True:
        clock.tick(FPS)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                return

        pygame.display.update()


if __name__ == '__main__':
    game_loop()
