import pygame
import const


class Room:  # Класс для основной игры
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(const.load_image("Яичное место.png"), (const.size))
        self.bloks = const.bloks

    def drawing(self, park=False):  # Все объекты
        self.screen.blit(self.image, (0, 0))
        self.draw_bloks(self.bloks, park)
        const.player_group.draw(self.screen)

    def draw_bloks(self, bloks, park):  # Блоки земли, на которые можно наступать
        grass = pygame.Color(16, 82, 36)
        pygame.draw.rect(self.screen, grass, const.floor, 0)
        pygame.draw.rect(self.screen, grass,
                         ((bloks[0][0], bloks[0][1]), (bloks[0][2] - bloks[0][0], bloks[0][3] - bloks[0][1])), 0)
        pygame.draw.rect(self.screen, grass,
                         ((bloks[2][0], bloks[2][1]), (bloks[2][2] - bloks[2][0], bloks[2][3] - bloks[2][1])), 0)
        pygame.draw.rect(self.screen, grass,
                         ((bloks[4][0], bloks[4][1]), (bloks[4][2] - bloks[4][0], bloks[4][3] - bloks[4][1])), 0)
        if park:  # Если игрок добился того, что к боссу можно допрыгнуть
            pygame.draw.rect(self.screen, grass,
                             ((bloks[1][0], bloks[1][1]), (bloks[1][2] - bloks[1][0], bloks[1][3] - bloks[1][1])), 0)
            pygame.draw.rect(self.screen, grass,
                             ((bloks[3][0], bloks[3][1]), (bloks[3][2] - bloks[3][0], bloks[3][3] - bloks[3][1])), 0)
