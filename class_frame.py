import pygame
import const

FPS = const.FPS


class Frames:  # Класс фреймов, для подсчёта тиков
    def __init__(self):
        self.count = 0
        self.jump = False
        self.fall = False
        self.start_jump = 0
        self.start_fall = 0

    def check(self, player, buttons):
        if player.rect.y < const.height - const.floor[1][1] - const.sprites:  # Игрок не летит (нужно переработать)
            player.can_fall = True
        else:
            player.can_fall = False
        if buttons.start:
            self.count += 2  # Счёт фреймов
        if player.jump:  # Если прыгает
            if not self.jump:  # Прыжок только начинается или уже начат
                self.start_jump = self.count
                self.jump = True
            if self.count - self.start_jump < FPS // 2:  # Проверка на то, что игрок ещё должен подниматься
                player.moving('jump')
            else:  # Игрок должен начать падать
                self.start_jump = 0
                player.jump = False
                player.fall = True
                self.jump = False
                self.start_fall = self.count
        if player.fall:  # Если падает
            if not self.fall:  # Падение только началось или уже начато
                self.start_fall = self.count
                self.fall = True
            player.moving('fall', fall=(self.count - self.start_fall) // 2)
        if player.right:
            player.moving('right')
        if player.left:
            player.moving('left')
        if not player.can_fall:  # Проверка на то, что приземлился
            self.fall = False
            player.fall = False
