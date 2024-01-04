import pygame
import const


class Enemy(pygame.sprite.Sprite):  # Класс игрока
    def __init__(self, rotation='right'):
        self.rect = pygame.Rect(0, 0, const.sprites, const.sprites)
        super().__init__()
        self.rotation = rotation  # Направление врага, которое зависит от расстояния до игрока
        if self.rotation == 'right':
            self.image = const.load_image('Рядовое яйцо.png', -1)
            self.rect = self.rect.move(0, const.floor[0][1] - const.sprites)
        if self.rotation == 'left':
            self.rect = self.rect.move(const.width - const.sprites, const.floor[0][1] - const.sprites)
            self.image = pygame.transform.flip(const.load_image('Рядовое яйцо.png', -1), True, False)

    def update(self, player):  # Враги идут в сторону игрока
        if self.rect.x < player.rect.x:
            if self.rotation == 'left':
                self.image = pygame.transform.flip(self.image, True, False)
                self.rotation = 'right'
            self.rect = self.rect.move(const.FPS // 10, 0)
        else:
            if self.rotation == 'right':
                self.image = pygame.transform.flip(self.image, True, False)
                self.rotation = 'left'
            self.rect = self.rect.move(-const.FPS // 10, 0)
