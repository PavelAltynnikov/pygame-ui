import pygame
from pygame.font import SysFont
from pygame.rect import Rect
from pygame.surface import Surface
from model.sound import Sound, NullableSound
from model.animations import Animation, NullableAnimation
from view.geometry import Point, NullableSurface
from view.event import Event


class Button:
    def __init__(self):
        self.size: tuple[float, float] = (100, 50)
        self.location: Point = Point(x=0, y=0)
        self.text: str = ''
        self.sound: Sound = NullableSound()
        self.image: Surface = NullableSurface()
        self.animation: Animation = NullableAnimation()
        self.click = Event()
        self._rect: Rect = self._calculate_rect()
        self._center: tuple[float, float] = self._calculate_center_point()
        self._font = SysFont('arial', 30)
        self._color: tuple[int, int, int] = (188, 188, 188)
        self._focused: bool = False

    @property
    def is_focused(self):
        return self._focused

    @is_focused.setter
    def is_focused(self, is_focused):
        self._focused = is_focused
        if not is_focused:
            return
        if self.sound:
            self.sound['select'].play()

    def mouse_on_me(self, x: int, y: int) -> bool:
        return self._mouse_on_width(x) and self._mouse_on_height(y)

    def update(self):
        self._rect = self._calculate_rect()
        pass

    def draw(self, screen: pygame.surface.Surface):
        if self.image:
            screen.blit(self.image, self._rect)
        else:
            pygame.draw.rect(screen, self._color, self._rect)
            if self.text:
                render = self._font.render(self.text, True, (0, 0, 0))
                screen.blit(render, render.get_rect(center=(self._center)))

    def _mouse_on_width(self, x):
        return self.location.x <= x <= self._rect.width

    def _mouse_on_height(self, y):
        return self.location.y <= y <= self._rect.height

    def _calculate_rect(self):
        left = self.location.x
        top = self.location.y
        width = self.size[0]
        height = self.size[1]

        if not isinstance(self.image, NullableSurface):
            rect = self.image.get_rect()
            width = rect.width
            height = rect.height

        return Rect(left, top, left + width, top + height)

    def _calculate_center_point(self):
        return self.location.x + self.size[0] / 2, self.location.y + self.size[1] / 2


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(r'D:\Development\Programming\Python\games\space_sandbox')

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
                        if not control.is_focused:
                            control.is_focused = True
                    else:
                        control.is_focused = False
                if is_click_event(event):
                    for control in controls:
                        if control.is_focused:
                            control.click("сообщение")

    FPS = 60
    show = True
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('space sandbox')
    clock = pygame.time.Clock()

    button = Button()
    button.text = 'qwert'
    button.size = (200, 100)
    button.location = Point(200, 100)
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
    button.click += some_handler

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
