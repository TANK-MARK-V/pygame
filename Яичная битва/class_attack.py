import pygame
import const


class Attack(pygame.sprite.Sprite):  # Атака врагов
    def __init__(self):
        super().__init__()
        self.image = const.load_image('Ложка.png', -1)
        self.reverse = False  # Сторона, в которую смотрит ложка
        self.pressed = False  # Кнопка была нажата
        self.started = 0  # Тик, на котором была нажата кнопка

    def draw(self, screen, player, boss, tick):  # Отрисовка ложки
        self.rect = player.rect  # Ложка получает координаты игрока
        if self.reverse == player.reverse:  # Ложка поворачивается в сторону игрока
            self.image = pygame.transform.flip(self.image, True, False)
            self.reverse = not self.reverse
        if player.reverse:  # Отдаление ложки от персонажа, в зависимости от направления игрока
            self.rect = self.rect.move(-const.sprites, 0)
        else:
            self.rect = self.rect.move(const.sprites, 0)
        if self.pressed or tick in range(self.started, self.started + const.FPS // 5):  # Ложка должна быть на экране
            screen.blit(self.image, (self.rect.x, self.rect.y))
            if pygame.sprite.spritecollide(self, const.enemy, True):  # Убийство яиц
                player.killed += 1
        if self.pressed and pygame.sprite.spritecollide(self, const.boss_group, False):  # Урон боссу
            boss.damage += 1
            boss.hits += 1
        self.pressed = False
