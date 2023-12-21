import pygame
import os
import sys

FPS = 50
size = width, height = 1920, 1080
pause_size = 50
pause_size = (width - pause_size * 2, pause_size)

player_group = pygame.sprite.Group()
enemy = pygame.sprite.Group()

sprites = 256

barotraum = 700


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

# Нужные переменные и функции
