import pygame
import const
import class_enemy


class Frames:  # Класс фреймов, для подсчёта тиков
    def __init__(self):
        self.count = 10  # Счёт фреймов начинаем с 10, на всякий случай

        self.jump = False  # Игрок начал прыгать
        self.start_jump = 0  # Тик начала прыжка
        self.start_fall = 0  # Тик начала падения

        self.start_spawn = False  # Начать спавн врагов
        self.first_spawn = 0  # Тик начала спавна врагов
        self.angry = True  # Игрок не может пройти к боссу
        self.just_spawned = True  # Первый спавн врагов

    def check(self, player, buttons, room):  # Основная функция
        if buttons.start:
            self.count += 1  # Счёт фреймов
        self.make_enemy(player, room)  # Спавн врагов
        player.can_move = self.moves(player)  # Проверка на возможность передвижения
        if player.jump:  # Если прыгает
            if not self.jump:  # Прыжок только начинается или уже начат
                self.start_jump = self.count
                self.jump = True
            if self.count - self.start_jump < const.FPS // 4:  # Проверка на то, что игрок ещё должен подниматься
                player.moving('jump')
            else:  # Игрок должен начать падать
                self.start_jump = 0
                player.jump = False
                self.jump = False
                self.start_fall = self.count
        if not player.jump and player.can_move[1]:  # Если падает и не прыгает
            player.moving('fall')
        if player.right:
            player.moving('right')
        if player.left:
            player.moving('left')
        const.enemy.update(player)
        if pygame.sprite.spritecollide(player, const.enemy, True):  # Получение урона
            player.hp -= 1
            player.killed += 1

    def moves(self, player):  # Проверка на коллилию
        up, down, left, right = True, True, True, True  # Возможность передвигаться по направлениям

        if pygame.sprite.spritecollideany(player, const.up):
            down = False
        if pygame.sprite.spritecollideany(player, const.down):
            up = False
        if pygame.sprite.spritecollideany(player, const.left):
            right = False
        if pygame.sprite.spritecollideany(player, const.right):
            left = False

        if pygame.sprite.spritecollideany(player, const.dop_left) and self.angry:
            right = False
            up = False
        if pygame.sprite.spritecollideany(player, const.dop_right) and self.angry:
            left = False
            up = False
        return up, down, left, right

    def make_enemy(self, player, room):  # Спавн врагов
        # Если прошло определённое кол-во времени ИЛИ это первый спавн И к боссу нельзя пройти
        if (self.count % (const.FPS * 8) == 0 or self.just_spawned) and self.angry:
            self.start_spawn = True  # Начать спавнить
            self.first_spawn = self.count  # Запомнить тик
            self.just_spawned = False
            room.enemys = 0  # Начать новый рейд
        if (self.count - self.start_spawn) % const.FPS == 0 and self.start_spawn:
            if room.enemys % 2 == 0:  # Спавн с двух сторон по очереди
                const.enemy.add(class_enemy.Enemy('right'))
            else:
                const.enemy.add(class_enemy.Enemy('left'))
            room.enemys += 1  # Враг заспавнился
        if room.enemys % 4 == 0 and room.enemys != 0 and self.start_spawn:  # Конец спавна после 4 яйца
            self.start_spawn = False
            room.rade += 1
        if room.rade % 3 == 0 and room.rade != 0 and player.killed % 4 == 0:  # Если игрок убил всех и прошло 3 рейда
            self.angry = False

    def draw_hp(self, screen, player):
        if player.hp <= 0:
            return False
        for i in range(1, player.hp + 1):
            screen.blit(const.load_image("Здоровье.png", -1), (const.sprites * (i - 1), 0))
        return True
