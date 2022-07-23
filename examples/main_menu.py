import resources
import pygame
from pygame_ui.animations import Animation
from pygame_ui.button import Button
from pygame_ui.form import Form
from pygame_ui.geometry import Point
from pygame_ui.sound import Sound

FPS = 10


class MainMenu(Form):
    def __init__(self, screen: pygame.surface.Surface, caption=''):
        super().__init__(screen, caption)
        self.background_image = resources.SPACE
        self.rectangle = self.background_image.get_rect()
        self._initialize_components()
        self._play_sound()

    def _initialize_components(self):
        rigth_offset = 250
        vertical_line = self.width - rigth_offset

        self._btn_start = Button()
        self._btn_start.text = 'start'
        self._btn_start.location = Point(x=vertical_line, y=170)
        self._btn_start.image = resources.BUTTON_START_0
        self._btn_start.sound = Sound(click=resources.SELECT, select=resources.CLICK)
        self._btn_start.animation = Animation(
            resources.BUTTON_START_PATH,
            resources.BUTTON_START_ROOT_PATH
        )
        self._btn_start.click += self._on_start_click

        self._btn_settings = Button()
        self._btn_settings.text = 'settings'
        self._btn_settings.location = Point(x=vertical_line, y=230)
        self._btn_settings.image = resources.BUTTON_SETTINGS_0
        self._btn_settings.sound = Sound(click=resources.SELECT, select=resources.CLICK)
        self._btn_settings.animation = Animation(
            resources.BUTTON_SETTINGS_PATH,
            resources.BUTTON_SETTINGS_ROOT_PATH,
        )
        self._btn_settings.click += self._on_settings_click

        self._btn_exit = Button()
        self._btn_exit.text = 'exit'
        self._btn_exit.location = Point(x=vertical_line, y=290)
        self._btn_exit.image = resources.BUTTON_EXIT_0
        self._btn_exit.sound = Sound(click=resources.SELECT, select=resources.CLICK)
        self._btn_exit.animation = Animation(
            resources.BUTTON_EXIT_PATH,
            resources.BUTTON_EXIT_ROOT_PATH,
        )
        self._btn_exit.click += self._on_exit_click

        self.add_control(self._btn_start)
        self.add_control(self._btn_settings)
        self.add_control(self._btn_exit)

    def _on_start_click(self, sender, event_args):
        self._btn_start.sound['click'].play()
        if isinstance(sender, Button):
            print(sender.text)

    def _on_settings_click(self, sender, event_args):
        self._btn_start.sound['click'].play()
        if isinstance(sender, Button):
            print(sender.text)

    def _on_exit_click(self, sender, event_args):
        self._btn_start.sound['click'].play()
        if isinstance(sender, Button):
            print(sender.text)
        self.close()

    def _play_sound(self):
        sound = resources.ALIEN
        sound.set_volume(0.3)
        sound.play()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 500))
    window = MainMenu(screen, 'asdf')
    window.show()
