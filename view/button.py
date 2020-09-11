import os
import pygame
from typing import Callable


class Button:
    def __init__(self, size, image_path, sound, animation, text):
        self._start_image = self._create_image_object(image_path)
        self._current_image = self._start_image
        self._rect = self._create_rect(size)
        self._text = text
        self._focused = False
        self._animation = animation
        self._sound = sound
        self.click_handler: Callable[[str], None]

    def draw(self, screen):
        if self._current_image:
            screen.blit(self._current_image, self._rect)

    def update(self, events, tick):
        for event in events:
            if self._is_mouse_event(event):
                if self._is_mouse_on_button(event):
                    self._get_focuse(tick)
                    if self._is_mouse_click(event):
                        self._on_button_click()
                else:
                    self._reset_main_states()
                break

    def _is_mouse_event(self, event):
        if hasattr(event, 'pos'):
            return True
        return False

    def _is_mouse_on_button(self, event):
        if self._rect.x <= event.pos[0] <= self._rect.x + self._rect.w and \
                self._rect.y <= event.pos[1] <= self._rect.h + self._rect.y:
            return True
        return False

    def _is_mouse_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True
        return False

    def _get_focuse(self, tick):
        self._animation.animated = True
        self._animation.play(tick)
        if not self._focused:
            self._focused = True
            self._sound['select'].play()

    def _reset_main_states(self):
        self._focused = False
        self._current_image = self._start_image

    def _on_button_click(self):
        self._sound['click'].play()
        if self.click_handler:
            self.click_handler(self._text)

    def _create_image_object(self, path):
        if os.path.exists(path):
            return pygame.image.load(path)
        return None

    def _create_rect(self, size):
        if self._current_image:
            rect = self._current_image.get_rect()
            rect.x = size[0]
            rect.y = size[1]
            return rect
        return None

    def _create_sound_object(self, path):
        if os.path.exists(path):
            return pygame.mixer.Sound(path)
        return None


if __name__ == '__main__':
    import sys
    sys.path.append(r'D:\Development\Programming\Python\my_dev\space_sandbox')
    from model.animations import Animation
    from model.sound import Sound

    MAIN_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    RESOURCE_PATH = os.path.join(MAIN_PATH, 'resources', 'main_menu')
    FPS = 60
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('space sandbox')
    clock = pygame.time.Clock()
    button = Button(
        size=(200, 150),
        image_path=r'resources\main_menu\buttons\pictures\start\button_start_0.png',
        sound=Sound(
            click=r'resources\main_menu\buttons\sounds\click.wav',
            select=r'resources\main_menu\buttons\sounds\select.wav'
        ),
        animation=Animation(
            r'resources\main_menu\buttons\pictures\start\button_start.png',
            r'resources\main_menu\buttons\pictures\start'
        ),
        text='test'
    )

    def some_handler(text):
        print(text)

    button.click_handler = some_handler
    show = True

    def event_handler(events):
        global show
        for event in events:
            if event.type == pygame.QUIT:
                show = False

    def game_loop():
        while show:
            tick = clock.tick(FPS)

            screen.fill([0, 0, 0])

            events = pygame.event.get()
            event_handler(events)

            button.update(events, tick)
            button.draw(screen)
            pygame.display.update()

    game_loop()
