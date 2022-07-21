import resources
import pygame
from pygame_ui.button import Button
from pygame_ui.geometry import Point
from pygame_ui.sound import Sound
from pygame_ui.animations import Animation

FPS = 10


class MainMenu:
    def __init__(self, screen: pygame.surface.Surface, caption=''):
        pygame.display.set_caption(caption)
        self._screen = screen
        self._image = resources.SPACE
        self._rect = self._image.get_rect()
        self._show = True
        self._controls: list[Button] = []
        self._initialize_components()
        self._play_sound()

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

        self._controls.append(self._btn_start)
        self._controls.append(self._btn_settings)
        self._controls.append(self._btn_exit)

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
        self._show = False

    def _play_sound(self):
        sound = resources.ALIEN
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
                        control.click()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 500))
    window = MainMenu(screen, 'asdf')
    window.show()
