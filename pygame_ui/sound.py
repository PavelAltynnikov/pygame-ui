import pygame


class Sound:
    def __init__(self, **kwargs):
        self._sounds = self._create_sounds(kwargs)

    def _create_sounds(self, _dict):
        sounds = {}
        for key, path in _dict.items():
            sounds[key] = pygame.mixer.Sound(path)
        return sounds

    def __getitem__(self, key):
        return self._sounds[key]


class NullableSound(Sound):
    def __init__(self):
        pass
