import os
import pygame


class Animation:
    def __init__(self, host_image, sprites_path):
        self._hosts_image = host_image
        self._sprites = self._create_sprites(sprites_path)
        self._current_sprite_index = 0
        self._work_time = 0
        self.animated = False

    def _create_sprites(self, path):
        sprites = []
        for image_path in os.listdir(path):
            sprites.append(pygame.image.load(os.path.join(path, image_path)))
        return sprites

    def _state_reset(self):
        self._current_sprite_index = 0
        self._work_time = 0
        self.animated = False

    def play(self, tick, speed=1):
        # if self.animated:
        #     self._work_time += tick
        #     self._current_sprite_index = self._work_time // len(self._sprites) * speed
        #     if self._current_sprite_index >= len(self._sprites):
        #         self._state_reset()
        #     return self._sprites[int(self._current_sprite_index)]
        if self.animated:
            self._current_sprite_index += 0.4
            # print(int(self._current_sprite_index))
            if self._current_sprite_index >= len(self._sprites):
                self._current_sprite_index = 0
                self.animated = False
            self._hosts_image = self._sprites[int(self._current_sprite_index)]


class NullableAnimation(Animation):
    def __init__(self):
        pass

    def play(self, tick, speed=1):
        pass
