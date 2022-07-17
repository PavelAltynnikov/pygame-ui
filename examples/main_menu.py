import os
import sys

EXAMPLES_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH = os.path.dirname(EXAMPLES_PATH)
sys.path.append(ROOT_PATH)

import pygame
from pygame_ui.button import Button
from pygame_ui.geometry import Point
from pygame_ui.sound import Sound
from pygame_ui.animations import Animation

RESOURCE_PATH = os.path.join(EXAMPLES_PATH, 'resources', 'main_menu')
BUTTON_PICTURES = os.path.join(RESOURCE_PATH, 'buttons', 'pictures')
BUTTON_SOUNDS = os.path.join(RESOURCE_PATH, 'buttons', 'sounds')
SCREEN_PICTURES = os.path.join(RESOURCE_PATH, 'screen', 'pictures')
SCREEN_SOUNDS = os.path.join(RESOURCE_PATH, 'screen', 'sounds')
FPS = 10


class MainMenu:
    def __init__(self, screen, caption=''):
        pygame.display.set_caption(caption)
        self._screen = screen
        self._image = pygame.image.load(os.path.join(SCREEN_PICTURES, 'space.jpg'))
        self._rect = self._image.get_rect()
        self._show = True
        self._controls: list[Button] = []
        self._initialize_components()
        self._play_sound()

    def set_start_click_handler(self, handler):
        self._btn_start.click += handler

    def set_settings_click_handler(self, handler):
        self._btn_settings.click += handler

    def set_exit_click_handler(self, handler):
        self._btn_exit.click += handler

    def show(self):
        clock = pygame.time.Clock()
        while self._show:
            self._screen.blit(self._image, self._rect)
            events = pygame.event.get()
            self._determine_focused_control()
            self._event_handler(events)
            self._update()
            self._draw()
            clock.tick(FPS)
            pygame.display.update()

    def _initialize_components(self):
        rigth_offset = 250
        vertical_line = self._screen.get_width() - rigth_offset

        self._btn_start = Button()
        self._btn_start.text = 'start'
        self._btn_start.location = Point(x=vertical_line, y=170)
        self._btn_start.image = pygame.image.load(
            os.path.join(BUTTON_PICTURES, 'start', 'button_start_0.png')
        )
        self._btn_start.sound = Sound(
            click=os.path.join(BUTTON_SOUNDS, 'select.wav'),
            select=os.path.join(BUTTON_SOUNDS, 'click.wav')
        )
        self._btn_start.animation = Animation(
            os.path.join(BUTTON_PICTURES, 'start', 'button_start.png'),
            os.path.join(BUTTON_PICTURES, 'start'),
        )
        # self._btn_start.click += self._btn_start.sound['click'].play

        self._btn_settings = Button()
        self._btn_settings.text = 'settings'
        self._btn_settings.location = Point(x=vertical_line, y=230)
        self._btn_settings.image = pygame.image.load(
            os.path.join(BUTTON_PICTURES, 'settings', 'button_settings_0.png')
        )
        self._btn_settings.sound = Sound(
            click=os.path.join(BUTTON_SOUNDS, 'select.wav'),
            select=os.path.join(BUTTON_SOUNDS, 'click.wav')
        )
        self._btn_settings.animation = Animation(
            os.path.join(BUTTON_PICTURES, 'settings', 'button_settings.png'),
            os.path.join(BUTTON_PICTURES, 'settings'),
        )

        self._btn_exit = Button()
        self._btn_exit.text = 'exit'
        self._btn_exit.location = Point(x=vertical_line, y=290)
        self._btn_exit.image = pygame.image.load(
            os.path.join(BUTTON_PICTURES, 'exit', 'button_exit_0.png')
        )
        self._btn_exit.sound = Sound(
            click=os.path.join(BUTTON_SOUNDS, 'select.wav'),
            select=os.path.join(BUTTON_SOUNDS, 'click.wav')
        )
        self._btn_exit.animation = Animation(
            os.path.join(BUTTON_PICTURES, 'exit', 'button_exit.png'),
            os.path.join(BUTTON_PICTURES, 'exit'),
        )

        self._controls.append(self._btn_start)
        self._controls.append(self._btn_settings)
        self._controls.append(self._btn_exit)

    def _play_sound(self):
        sound = pygame.mixer.Sound(
            os.path.join(SCREEN_SOUNDS, '8-Bit - OST Alien 3  (Dendy) - Level 1 (musicpro.me).mp3')
        )
        sound.set_volume(0.3)
        sound.play()

    def _determine_focused_control(self):
        mx, my = pygame.mouse.get_pos()
        for control in self._controls:
            if control.mouse_on_me(mx, my):
                if not control.is_focused:
                    control.is_focused = True
            else:
                control.is_focused = False

    def _update(self):
        for control in self._controls:
            control.update()

    def _draw(self):
        for control in self._controls:
            control.draw(self._screen)

    def _is_quit_event(self, event):
        if event.type == pygame.QUIT:
            return True
        return False

    def _is_click_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            return True
        return False

    def _event_handler(self, events):
        for event in events:
            if self._is_quit_event(event):
                self._show = False
                break
            elif self._is_click_event(event):
                for control in self._controls:
                    if control.is_focused:
                        control.click(control.text)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 500))
    window = MainMenu(screen, 'asdf')
    window.show()
