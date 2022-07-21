import os
import sys
import pygame

EXAMPLES_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH = os.path.dirname(EXAMPLES_PATH)

sys.path.append(ROOT_PATH)

RESOURCE_PATH = os.path.join(EXAMPLES_PATH, 'resources', 'main_menu')
BUTTON_PICTURES = os.path.join(RESOURCE_PATH, 'buttons', 'pictures')
BUTTON_SOUNDS = os.path.join(RESOURCE_PATH, 'buttons', 'sounds')
SCREEN_PICTURES = os.path.join(RESOURCE_PATH, 'screen', 'pictures')
SCREEN_SOUNDS = os.path.join(RESOURCE_PATH, 'screen', 'sounds')

SPACE = pygame.image.load(os.path.join(SCREEN_PICTURES, 'space.jpg'))

CLICK = os.path.join(BUTTON_SOUNDS, 'click.wav')
SELECT = os.path.join(BUTTON_SOUNDS, 'select.wav')
ALIEN = pygame.mixer.Sound(
    os.path.join(SCREEN_SOUNDS, '8-Bit - OST Alien 3  (Dendy) - Level 1 (musicpro.me).mp3')
)

BUTTON_START_ROOT_PATH = os.path.join(BUTTON_PICTURES, 'start')
BUTTON_START_0_PATH = os.path.join(BUTTON_START_ROOT_PATH, 'button_start_0.png')
BUTTON_START_0 = pygame.image.load(BUTTON_START_0_PATH)
BUTTON_START_PATH = os.path.join(BUTTON_START_ROOT_PATH, 'button_start.png')

BUTTON_SETTINGS_ROOT_PATH = os.path.join(BUTTON_PICTURES, 'settings')
BUTTON_SETTINGS_0_PATH = os.path.join(BUTTON_SETTINGS_ROOT_PATH, 'button_settings_0.png')
BUTTON_SETTINGS_0 = pygame.image.load(BUTTON_SETTINGS_0_PATH)
BUTTON_SETTINGS_PATH = os.path.join(BUTTON_SETTINGS_ROOT_PATH, 'button_settings.png')

BUTTON_EXIT_ROOT_PATH = os.path.join(BUTTON_PICTURES, 'exit')
BUTTON_EXIT_0_PATH = os.path.join(BUTTON_EXIT_ROOT_PATH, 'button_exit_0.png')
BUTTON_EXIT_0 = pygame.image.load(BUTTON_EXIT_0_PATH)
BUTTON_EXIT_PATH = os.path.join(BUTTON_EXIT_ROOT_PATH, 'button_exit.png')
