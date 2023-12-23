import pygame
import const


class Border(pygame.sprite.Sprite):  # Граница блока
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self.rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
