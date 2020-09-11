import os
import pygame
from typing import Callable


class Button:
    def __init__(self, size, image, sound, animation, text):
        self.image = image
        self.rect = self._create_rect(size)
        self._befault_image = image
        self._text = text
        self._focused = False
        self._animation = animation
        self._sound = sound
        self.click_handler: Callable[[str], None]

    def _create_rect(self, size):
        if self.image:
            rect = self.image.get_rect()
            rect.x = size[0]
            rect.y = size[1]
            return rect
        return None

    @property
    def focuse(self):
        return self._focused

    @focuse.setter
    def focuse(self, is_focused):
        if is_focused:
            self._focused = True
            self._sound['select'].play()
        else:
            self._focused = False
            self.image = self.image

    def click(self):
        self._sound['click'].play()
        if self.click_handler:
            self.click_handler(self._text)

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)


if __name__ == '__main__':
    import sys
    sys.path.append(r'D:\Development\Programming\Python\my_dev\space_sandbox')
    from model.animations import Animation
    from model.sound import Sound

    def create_image_object(path):
        if os.path.exists(path):
            return pygame.image.load(path)
        return None

    def some_handler(text):
        print(text)

    def is_quit_event(event):
        if event.type == pygame.QUIT:
            return True
        return False

    def is_mouse_event(event):
        if hasattr(event, 'pos'):
            return True
        return False

    def is_click_event(event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True
        return False

    def is_mouse_on_button(event, button):
        if button.rect.x <= event.pos[0] <= button.rect.x + button.rect.w and \
                button.rect.y <= event.pos[1] <= button.rect.h + button.rect.y:
            return True
        return False

    def event_handler(events):
        global show
        for event in events:
            if is_quit_event(event):
                show = False
            if is_mouse_event(event):
                for control in controls:
                    if is_mouse_on_button(event, control):
                        if not control.focuse:
                            control.focuse = True
                    else:
                        control.focuse = False
                if is_click_event(event):
                    for control in controls:
                        if control.focuse:
                            control.click()

    FPS = 60
    show = True
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('space sandbox')
    clock = pygame.time.Clock()

    button = Button(
        size=(200, 150),
        image=create_image_object(
            r'resources\main_menu\buttons\pictures\start\button_start_0.png'
        ),
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
    button.click_handler = some_handler

    controls = [button]

    def game_loop():
        while show:
            clock.tick(FPS)

            screen.fill([0, 0, 0])

            events = pygame.event.get()
            event_handler(events)

            button.draw(screen)
            pygame.display.update()

    game_loop()
