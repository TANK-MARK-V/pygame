import pygame
import const

FPS = const.FPS


class Frames:  # Класс фреймов, для подсчёта тиков
    def __init__(self):
        self.count = 0
        self.jump = False

        self.start_jump = 0
        self.start_fall = 0

    def check(self, player, buttons):
        if buttons.start:
            self.count += 1  # Счёт фреймов
        player.can_move = self.moves(player)
        if player.jump:  # Если прыгает
            if not self.jump:  # Прыжок только начинается или уже начат
                self.start_jump = self.count
                self.jump = True
            if self.count - self.start_jump < FPS // 4:  # Проверка на то, что игрок ещё должен подниматься
                player.moving('jump')
            else:  # Игрок должен начать падать
                self.start_jump = 0
                player.jump = False
                self.jump = False
                self.start_fall = self.count
        if not player.jump and (player.can_move[1] or player.fall):  # Если падает и не прыгает
            player.moving('fall')
        if player.right:
            player.moving('right')
        if player.left:
            player.moving('left')
        if not player.can_move[1]:  # Проверка на то, что приземлился
            player.fall = False

    def moves(self, player):
        up, down, left, right = True, True, True, True
        if pygame.sprite.spritecollideany(player, const.up):
            down = False
        if pygame.sprite.spritecollideany(player, const.down):
            up = False
        if pygame.sprite.spritecollideany(player, const.left):
            right = False
        if pygame.sprite.spritecollideany(player, const.right):
            left = False
        return (up, down, left, right)
