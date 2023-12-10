import pygame
import class_button

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    buttons = class_button.Buttons(screen)
    while running:
        for event in pygame.event.get():
            running = buttons.menu(screen, event)  # Открытие меню
            if event.type == pygame.QUIT:
                running = False
            if not running:
                break
            if buttons.start:  # Игрок нажал "Играть"
                buttons = class_button.Buttons(screen, pause=True)  # "Играть" меняется на "Продолжить"
                running = False
                # Вместо последней строки будет открытие другого класса для первого уровня,
                # который будет принимать то же самое
    pygame.quit()
