import os
import pygame
from .button import Button

MAIN_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
RESOURCE_PATH = os.path.join(MAIN_PATH, 'resources', 'main_menu')
BUTTON_PICTURES = os.path.join(RESOURCE_PATH, 'buttons', 'pictures')
BUTTON_SOUNDS = os.path.join(RESOURCE_PATH, 'buttons', 'sounds')
SCREEN_PICTURES = os.path.join(RESOURCE_PATH, 'screen', 'pictures')
SCREEN_SOUNDS = os.path.join(RESOURCE_PATH, 'screen', 'sounds')


class MainMenu:
    def __init__(self, screen, caption=''):
        self._screen = screen
        self._clock = pygame.time.Clock()
        self._fps = 60
        self._show = True
        self._rigth_offset = 250

        self._button_start = Button(
            screen=self._screen,
            x=screen.get_width() - self._rigth_offset,
            y=170,
            image_path=os.path.join(BUTTON_PICTURES, 'start', 'button_start_0.png'),
            select_sound_path=os.path.join(BUTTON_SOUNDS, 'select.wav'),
            click_sound_path=os.path.join(BUTTON_SOUNDS, 'click.wav'),
            text='start',
            animation_path=os.path.join(BUTTON_PICTURES, 'start')
            # animation_images=[
            #     pygame.image.load(os.path.join(BUTTON_PICTURES, 'button_start_1.png')),
            #     pygame.image.load(os.path.join(BUTTON_PICTURES, 'button_start_2.png')),
            #     pygame.image.load(os.path.join(BUTTON_PICTURES, 'button_start_3.png'))
            # ]
        )

        self._button_settings = Button(
            screen=self._screen,
            x=screen.get_width() - self._rigth_offset,
            y=230,
            image_path=os.path.join(BUTTON_PICTURES, 'settings', 'button_settings_0.png'),
            select_sound_path=os.path.join(BUTTON_SOUNDS, 'select.wav'),
            click_sound_path=os.path.join(BUTTON_SOUNDS, 'click.wav'),
            text='settings',
            animation_path=os.path.join(BUTTON_PICTURES, 'settings')
            # animation_images=[
            #     pygame.image.load(os.path.join(BUTTON_PICTURES, 'button_settings_1.png')),
            #     pygame.image.load(os.path.join(BUTTON_PICTURES, 'button_settings_2.png')),
            #     pygame.image.load(os.path.join(BUTTON_PICTURES, 'button_settings_3.png'))
            # ]
        )

        self._button_exit = Button(
            screen=self._screen,
            x=screen.get_width() - self._rigth_offset,
            y=290,
            image_path=os.path.join(BUTTON_PICTURES, 'exit', 'button_exit_0.png'),
            select_sound_path=os.path.join(BUTTON_SOUNDS, 'select.wav'),
            click_sound_path=os.path.join(BUTTON_SOUNDS, 'click.wav'),
            text='exit',
            animation_path=os.path.join(BUTTON_PICTURES, 'exit')
            # animation_images=[
            #     pygame.image.load(os.path.join(BUTTON_PICTURES, 'button_exit_1.png')),
            #     pygame.image.load(os.path.join(BUTTON_PICTURES, 'button_exit_2.png')),
            #     pygame.image.load(os.path.join(BUTTON_PICTURES, 'button_exit_3.png'))
            # ]
        )

        self._image = pygame.image.load(os.path.join(SCREEN_PICTURES, 'space.jpg'))
        self._rect = self._image.get_rect()
        self._screen.blit(self._image, self._rect)

        sound = pygame.mixer.Sound(
            os.path.join(SCREEN_SOUNDS, '8-Bit - OST Alien 3  (Dendy) - Level 1 (musicpro.me).mp3')
        )
        sound.set_volume(0.3)
        sound.play()

        pygame.display.set_caption(caption)
        pygame.display.update()

    def set_start_click_handler(self, handler):
        self._button_start.click_handler = handler

    def set_settings_click_handler(self, handler):
        self._button_settings.click_handler = handler

    def set_exit_click_handler(self, handler):
        self._button_exit.click_handler = handler

    def main_loop(self):
        while self._show:
            tick = self._clock.tick(self._fps)
            self._screen.blit(self._image, self._rect)

            events = pygame.event.get()
            self._event_handler(events)
            self._button_start.update(events, tick)
            self._button_settings.update(events, tick)
            self._button_exit.update(events, tick)

            self._button_start.draw(screen)
            self._button_settings.draw(screen)
            self._button_exit.draw(screen)
            pygame.display.update()

    def _event_handler(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self._show = False


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 500))
    window = MainMenu(screen, 'asdf')
    window.main_loop()
