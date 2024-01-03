import pygame
import os
import sys
import class_borders
import class_frame
import class_introduce
import class_button
import class_pause
import class_room
import class_attack

FPS = 50
if 1:
    size = width, height = 1920, 1080
else:  # Другое разрешение
    size = width, height = 1600, 900
pause_size = 50
pause_size = (width - pause_size * 2, pause_size)
sprites = int(width * 0.067)
barotraum = height - sprites - 50
floor = 80
bloks = (300, 100, 150)
bloks = ((0, height - floor - bloks[2] - bloks[1], bloks[0], height - floor - bloks[2]),
         (width - bloks[0], height - floor - bloks[2] - bloks[1], width, height - floor - bloks[2]),
         (bloks[0] + 150, height - floor - bloks[2] * 2 - bloks[1] - height // 19,
          width - bloks[0] - 150, height - floor - bloks[2] * 2 - height // 19))
floor = ((0, height - floor), (width, floor))

player_group = pygame.sprite.Group()
enemy = pygame.sprite.Group()
down = pygame.sprite.Group()
up = pygame.sprite.Group()
left = pygame.sprite.Group()
right = pygame.sprite.Group()
dop_left = pygame.sprite.Group()
dop_right = pygame.sprite.Group()


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


def make_bloks():
    for blok in bloks:  # Границы блоков
        x1, y1, x2, y2 = blok
        class_borders.Border(x1 + 1, y1, x2 - 1, y1 + 1).add(up)
        class_borders.Border(x1 + 1, y2 - 1, x2 - 1, y2).add(down)
        class_borders.Border(x1, y1 + 1, x1 + 1, y2 - 1).add(left)
        class_borders.Border(x2 - 1, y1 + 1, x2, y2 - 1).add(right)
    x1, y1, x2, y2 = floor[0][0], floor[0][1], floor[0][0] + floor[1][0], floor[0][1] + floor[1][1]
    class_borders.Border(x1, y1, x2, y1 + 1).add(up)  # Границы пола
    class_borders.Border(x1, y2 - 1, x2, y2).add(down)
    class_borders.Border(x1, y1, x1 + 1, y2).add(left)
    class_borders.Border(x2 - 1, y1, x2, y2).add(right)

    # Запрет игроку на выход из локации
    class_borders.Border(bloks[0][2] - 1, bloks[0][3], bloks[0][2], floor[0][1]).add(right)
    class_borders.Border(bloks[1][0] + 1, bloks[0][3], bloks[1][0], floor[0][1]).add(left)

    class_borders.Border(width - 1, 0, width, height).add(left)
    class_borders.Border(1, 0, 0, height).add(right)
    class_borders.Border(0, 0, width, 1).add(down)
    class_borders.Border(0, height - floor[1][1], width, height).add(up)

    # Дополнительная коллизия, если босс не готов получать урон
    class_borders.Border(bloks[1][0] - 1, bloks[2][3], bloks[1][0], bloks[1][1]).add(dop_left)
    class_borders.Border(bloks[0][2] + 1, bloks[2][3], bloks[0][2], bloks[0][1]).add(dop_right)


def make_prep(screen, button=False):  # Создание классов
    if not button:
        return class_button.Buttons(screen), class_introduce.Introduce(), class_pause.Pause(screen, pause_size), \
            class_frame.Frames(), class_room.Room(screen), class_attack.Attack()
    else:
        return class_button.Buttons(screen, pause=True)

# Нужные переменные и функции
