import pygame
import const


class Introduce:  # Класс для показа вступления
    def __init__(self):
        self.ready = False
        self.question = False

    def show(self, screen, player):
        if not self.ready:
            screen.blit(const.load_image('fon_nachalo_1.png').convert_alpha(), (0, 0))
            const.player_group.draw(screen)
            screen.blit(const.load_image('враг.png', -1).convert_alpha(),
                        (const.width - const.sprites - 50, const.barotraum))
            if player.rect.x + const.sprites < const.width - const.sprites - 50:
                player.moving('right')
            else:
                self.give_quest(screen)
                self.question = True

    def give_quest(self, screen):
        font = pygame.font.Font(None, 30)
        yes = font.render('Да (нажмите "Y")', True, pygame.Color('yellow'))
        no = font.render('Нет (нажмите "N")', True, pygame.Color('yellow'))
        font = pygame.font.Font(None, 50)
        quest = font.render("Яйца растут на деревьях?", True, pygame.Color('yellow'))
        screen.blit(yes, ((const.width // 2 - 220), const.height - 100))
        screen.blit(no, ((const.width // 2 + 50, const.height - 100)))
        screen.blit(quest, ((const.width // 2 - quest.get_width() // 2, const.height - 200)))
