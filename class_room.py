import pygame
import const


class Room:  # Класс для основной игры
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(const.load_image("Яичное место.png"), const.size)
        self.bloks = const.bloks  # Координаты блоков
        self.enemys = 0  # Счёт спавна врагов (обновляется при новом рейде)
        self.rade = 0  # Сколько раз спавнились враги (по 4 штуки, т.е спавн 12 яиц равняется 3 рейдам)

    def drawing(self):  # Все объекты
        self.screen.blit(self.image, (0, 0))
        self.draw_bloks(self.bloks)
        const.player_group.draw(self.screen)
        const.enemy.draw(self.screen)

    def draw_bloks(self, bloks):  # Блоки земли, на которые можно наступать
        grass = pygame.Color(16, 82, 36)  # Цвет блоков
        pygame.draw.rect(self.screen, grass, const.floor, 0)
        pygame.draw.rect(self.screen, grass,
                         ((bloks[0][0], bloks[0][1]), (bloks[0][2] - bloks[0][0], bloks[0][3] - bloks[0][1])), 0)
        pygame.draw.rect(self.screen, grass,
                         ((bloks[1][0], bloks[1][1]), (bloks[1][2] - bloks[1][0], bloks[1][3] - bloks[1][1])), 0)
        pygame.draw.rect(self.screen, grass,
                         ((bloks[2][0], bloks[2][1]), (bloks[2][2] - bloks[2][0], bloks[2][3] - bloks[2][1])), 0)
