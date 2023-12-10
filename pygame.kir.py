import pygame


def draw(screen):
    screen.fill((0, 0, 0))
    # font = pygame.font.Font(None, 50)
    # text_w = screen.get_width()
    # text_h = screen.get_height()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
