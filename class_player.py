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

        self.hp = 3

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(pygame.transform.flip(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)), True, False))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

    def moving(self, todo, fall=0):
        if todo == 'jump':
            self.rect = self.rect.move(0, -2)
        if todo == 'fall' and self.can_fall:
            self.rect = self.rect.move(0, fall)
        if todo == 'right':
            self.rect = self.rect.move(FPS // 5, 0)
        if todo == 'left':
            self.rect = self.rect.move(-FPS // 5, 0)
        if self.frem % (FPS // 10) == 0:
            self.update()

    def hit(self, dmg):
        if pygame.sprite.spritecollideany(self, const.enemy):
            self.hp -= dmg
