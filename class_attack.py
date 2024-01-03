import pygame
import const


class Attack(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = const.load_image('Ложка.png', -1)
        self.reverse = False
        self.pressed = False
        self.started = 0

    def draw(self, screen, player, tick):
        self.rect = player.rect
        if self.reverse == player.reverse:
            self.image = pygame.transform.flip(self.image, True, False)
            self.reverse = not self.reverse
        if player.reverse:
            self.rect = self.rect.move(-const.sprites, 0)
        else:
            self.rect = self.rect.move(const.sprites, 0)
        if self.pressed or tick in range(self.started, self.started + const.FPS // 5):
            screen.blit(self.image, (self.rect.x, self.rect.y))
            if pygame.sprite.spritecollide(self, const.enemy, True):  # Убийство яиц
                player.killed += 1
        self.pressed = False
