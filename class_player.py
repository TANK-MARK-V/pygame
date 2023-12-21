import pygame
import const

FPS = const.FPS


class Player(pygame.sprite.Sprite):  # Класс игрока
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__()
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

        self.can_fall = False
        self.frem = 0
        self.jump = False
        self.fall = False
        self.right = False
        self.left = False
        self.reverse = False

        self.hp = 3

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(pygame.transform.scale(pygame.transform.flip(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)), True, False), (const.sprites, const.sprites)))

    def update(self, todo):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        if self.reverse:  # Если игрок шёл в другую сторону
            self.image = pygame.transform.flip(self.frames[self.cur_frame], True, False)
        else:
            self.image = self.frames[self.cur_frame]

    def moving(self, todo, fall=0):  # Двигать игрока
        if todo == 'jump':
            self.rect = self.rect.move(0, -12)
        if todo == 'fall' and self.can_fall:
            self.rect = self.rect.move(0, fall)
        if todo == 'right':
            self.reverse = False
            self.rect = self.rect.move(FPS // 5, 0)
        if todo == 'left':
            self.reverse = True
            self.rect = self.rect.move(-FPS // 5, 0)
        if self.frem % (FPS // 10) == 0:  # Обновление фрейма через определённое кол-во времени
            self.update(todo)

    def hit(self, dmg):  # Не реализованная на данный момент функция
        if pygame.sprite.spritecollideany(self, const.enemy):
            self.hp -= dmg
