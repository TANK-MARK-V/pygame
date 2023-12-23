import pygame
import os
import sys

FPS = 50
size = width, height = 1920, 1080
pause_size = 50
pause_size = (width - pause_size * 2, pause_size)
sprites = 128
barotraum = height - sprites - 50
floor = 80
bloks = (300, 100, 150)
bloks = ((0, height - floor - bloks[2] - bloks[1], bloks[0], height - floor - bloks[2]),
         # (bloks[0], height - floor - bloks[2], bloks[0] + bloks[2], height - floor),
         (width - bloks[0], height - floor - bloks[2] - bloks[1], width, height - floor - bloks[2]),
         # (width - bloks[0] - bloks[2], height - floor - bloks[2], width - bloks[0], height - floor),
         (bloks[0] + 150, height - floor - bloks[2] * 2 - bloks[1] - height // 19,
          width - bloks[0] - 150, height - floor - bloks[2] * 2 - height // 19))
floor = ((0, height - floor), (width, floor))

player_group = pygame.sprite.Group()
enemy = pygame.sprite.Group()
down = pygame.sprite.Group()
up = pygame.sprite.Group()
left = pygame.sprite.Group()
right = pygame.sprite.Group()


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
