import pygame


def draw_death_screen(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text_w = screen.get_width()
    text_h = screen.get_height()
    death_screen = font.render("Поражение!", True, pygame.Color("red"))
    return death_screen
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    dscr = draw_death_screen(screen)
    screen.blit(dscr, (20, 200))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
    pygame.quit()
