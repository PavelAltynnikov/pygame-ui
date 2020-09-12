import pygame
from typing import Callable


class Button:
    def __init__(self):
        self._size = (100, 50)
        self._location = (0, 0)
        self._center = self._calculate_center_point()
        self._text = ''
        self._font = pygame.font.SysFont('arial', 30)
        self._color = (188, 188, 188)
        self._focused = False
        self.animation = None
        self.sound = None
        self.image = None
        self.rect = pygame.rect.Rect(self._calculate_rect())
        self.click_handler: Callable[[str], None]

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, (tuple, list)):
            self._size = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if isinstance(value, (tuple, list)):
            self._location = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if isinstance(value, str):
            self._text = value
        else:
            self._text = str(value)

    @property
    def focuse(self):
        return self._focused

    @focuse.setter
    def focuse(self, is_focused):
        if is_focused:
            self._focused = True
            if self.sound:
                self.sound['select'].play()
        else:
            self._focused = False

    def _calculate_rect(self):
        return (
            self._location[0], self._location[1],
            self._location[0] + self._size[0], self._location[1] + self._size[1]
        )

    def _calculate_center_point(self):
        return self._location[0] + self._size[0] / 2, self._location[1] + self._size[1] / 2

    def on_click(self):
        if self.sound:
            self.sound['click'].play()
        if self.click_handler:
            self.click_handler(self._text)

    def update(self):
        self._center = self._calculate_center_point()
        self.rect.center = self._center
        self.rect.width = self._size[0]
        self.rect.height = self._size[1]

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, self._color, self.rect)
            if self._text:
                render = self._font.render(self._text, True, (0, 0, 0))
                screen.blit(render, render.get_rect(center=(self._center)))


if __name__ == '__main__':
    import os
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

    def is_mouse_on_control(event, control):
        if control.rect.x <= event.pos[0] <= control.rect.x + control.rect.w and \
                control.rect.y <= event.pos[1] <= control.rect.h + control.rect.y:
            return True
        return False

    def event_handler(events):
        global show
        for event in events:
            if is_quit_event(event):
                show = False
            if is_mouse_event(event):
                for control in controls:
                    if is_mouse_on_control(event, control):
                        if not control.focuse:
                            control.focuse = True
                    else:
                        control.focuse = False
                if is_click_event(event):
                    for control in controls:
                        if control.focuse:
                            control.on_click()

    FPS = 60
    show = True
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('space sandbox')
    clock = pygame.time.Clock()

    button = Button()
    button.text = 'qwert'
    button.size = (200, 100)
    button.location = (200, 100)
    # button.image = create_image_object(
    #     r'resources\main_menu\buttons\pictures\start\button_start_0.png'
    # )
    button.sound = Sound(
        click=r'resources\main_menu\buttons\sounds\click.wav',
        select=r'resources\main_menu\buttons\sounds\select.wav'
    )
    button.animation = Animation(
        r'resources\main_menu\buttons\pictures\start\button_start.png',
        r'resources\main_menu\buttons\pictures\start'
    )
    button.click_handler = some_handler

    controls = [button]

    def game_loop():
        while show:
            clock.tick(FPS)

            screen.fill([0, 0, 0])

            events = pygame.event.get()
            event_handler(events)

            button.update()
            button.draw(screen)
            pygame.display.update()

    game_loop()
