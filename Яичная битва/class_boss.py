import pygame
import const


class Boss(pygame.sprite.Sprite):  # Класс босса
    def __init__(self):
        super().__init__()
        self.angry = False  # К боссу нельзя подняться
        self.damage = 0  # Сколько ударов получил босс (один удар равняется 100 урона)
        self.hits = 0  # Сколько ударов подрят получил босс
        self.update(True)

    def update(self, angry):  # Менять картинку в зависимости от злости
        if not self.angry and angry:  # Не был злым и стал
            self.image = pygame.transform.scale(const.load_image('Король_3.png', -1),
                                                (const.sprites * 2, const.sprites * 2))
            self.angry = True
            self.rect = pygame.Rect(const.width // 2 - const.sprites, const.bloks[2][1] - const.sprites * 3,
                                    const.sprites * 2, const.sprites * 2)
        elif self.angry and not angry:  # Был злым и успокоился
            self.image = pygame.transform.scale(const.load_image('Король.png', -1),
                                                (const.sprites * 2, const.sprites * 2))
            self.angry = False
            self.rect = pygame.Rect(const.width // 2 - const.sprites, const.bloks[2][1] - const.sprites * 2,
                                    const.sprites * 2, const.sprites * 2)
