from pygame.surface import Surface


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class NullableSurface(Surface):
    def __init__(self):
        pass
