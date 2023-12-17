import pygame


class Introduce:  # Класс для показа вступления
    def __init__(self):
        self.ready = False

    def show(self, screen, player, player_group):
        if not self.ready:
            screen.blit(pygame.image.load('fon_nachalo_1.png').convert_alpha(), (0, 0))
            player_group.draw(screen)
            player.moving('right')
