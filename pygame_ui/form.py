import pygame

class Form:
    def __init__(self, screen: pygame.surface.Surface, title='', fps=60):
        pygame.display.set_caption(title)
        self._screen = screen
        self._fps = fps
        self._show = True
        self._image = None
        self._rect = None
        self._controls = []

    def show(self):
        clock = pygame.time.Clock()

        while self._show:
            self._determine_focused_control()
            self._event_handler()
            self._update()
            self._draw()
            clock.tick(self._fps)
            pygame.display.update()

    def _determine_focused_control(self):
        mx, my = pygame.mouse.get_pos()
        for control in self._controls:
            if control.mouse_on_me(mx, my):
                if not control.is_focused:
                    control.is_focused = True
            else:
                control.is_focused = False

    def _event_handler(self):
        events = pygame.event.get()
        for event in events:
            if self._is_quit_event(event):
                self._show = False
                break
            elif self._is_click_event(event):
                for control in self._controls:
                    if control.is_focused:
                        control.click()

    def _is_quit_event(self, event):
        if event.type == pygame.QUIT:
            return True
        return False

    def _is_click_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            return True
        return False

    def _update(self):
        for control in self._controls:
            control.update()

    def _draw(self):
        if self._image:
            self._screen.blit(self._image, self._rect)
        for control in self._controls:
            control.draw(self._screen)


if __name__ == '__main__':
    pygame.init()
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 500
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    f = Form(screen)
    f.show()
