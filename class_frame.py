import pygame
import const
import class_enemy

FPS = const.FPS


class Frames:  # Класс фреймов, для подсчёта тиков
    def __init__(self):
        self.count = 10

        self.jump = False
        self.start_jump = 0
        self.start_fall = 0

        self.start_spawn = False
        self.first_spawn = 0
        self.angry = 0
        self.just_spawned = True

    def check(self, player, buttons, room):
        if buttons.start:
            self.count += 1  # Счёт фреймов
        self.make_enemy(room)
        self.angry = True
        player.can_move = self.moves(player, self.angry)
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
        const.enemy.update(player)

    def moves(self, player, angry):
        up, down, left, right = True, True, True, True
        if pygame.sprite.spritecollideany(player, const.up):
            down = False
        if pygame.sprite.spritecollideany(player, const.down):
            up = False
        if pygame.sprite.spritecollideany(player, const.left):
            right = False
        if pygame.sprite.spritecollideany(player, const.right):
            left = False

        if pygame.sprite.spritecollideany(player, const.dop_left) and angry:
            right = False
            up = False
        if pygame.sprite.spritecollideany(player, const.dop_right) and angry:
            left = False
            up = False
        return (up, down, left, right)

    def make_enemy(self, room):
        if self.angry:
            if self.count % (FPS * 30) == 0 or self.just_spawned:
                self.start_spawn = True
                self.first_spawn = self.count
                self.just_spawned = False
            if (self.count - self.start_spawn) % FPS == 0 and self.start_spawn:
                if room.enemys % 2 == 0:
                    const.enemy.add(class_enemy.Enemy('right'))
                else:
                    const.enemy.add(class_enemy.Enemy('left'))
                room.enemys += 1
            if room.enemys % 4 == 0 and room.enemys != 0:
                self.start_spawn = False
