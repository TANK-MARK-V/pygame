import pygame


def buttons(screen):  # Функция создания кнопок
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 120)

    play = font.render("Играть", True, pygame.Color('yellow'))
    ekcit = font.render("Выйти", True, pygame.Color('yellow'))
    # Написание текста

    otstup = 20  # Левый верхний угол для вертикального расположения кнопок

    screen.blit(play, (otstup, otstup))
    screen.blit(ekcit, (otstup, play.get_height() + otstup + 10))
    # Отрисовка на экране

    # Список координат, ( Длина и высота "Играть", Длина и высота "Выйти", отступ)
    return ((play.get_width(), play.get_height()), (ekcit.get_width(), ekcit.get_height()), otstup)


def check_do(pos, coords):  # Функция для нажатия кнопок
    if pos[0] in range(coords[2], coords[2] + coords[0][0]) and pos[1] in range(coords[2], coords[2] + coords[0][1]):
        return 'Играть'
    elif pos[0] in range(coords[2], coords[2] + coords[1][0]) and pos[1] in range(coords[0][1] + coords[2] + 10,
                                                                                  (coords[0][1] + coords[2] + 10) +
                                                                                  coords[1][1]):
        return 'Выйти'


def check_pos(screen, pos, coords):  # Функция для отрисовки прямоугольников при наведении на кнопку
    if pos[0] in range(coords[2], coords[2] + coords[0][0]) and pos[1] in range(coords[2], coords[2] + coords[0][1]):
        pygame.draw.rect(screen, pygame.Color('yellow'), (coords[2], coords[2], coords[0][0], coords[0][1]), 1)
    else:
        pygame.draw.rect(screen, pygame.Color('black'), (coords[2], coords[2], coords[0][0], coords[0][1]), 1)
    if pos[0] in range(coords[2], coords[2] + coords[1][0]) and pos[1] in range(coords[0][1] + coords[2] + 10,
                                                                                (coords[0][1] + coords[2] + 10) +
                                                                                coords[1][1]):
        pygame.draw.rect(screen, pygame.Color('yellow'),
                         (coords[2], coords[0][1] + coords[2] + 10, coords[1][0], coords[1][1]), 1)
    else:
        pygame.draw.rect(screen, pygame.Color('black'),
                         (coords[2], coords[0][1] + coords[2] + 10, coords[1][0], coords[1][1]), 1)


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    while running:
        for event in pygame.event.get():
            coords = buttons(screen)  # Создание кнопок
            check_pos(screen, pygame.mouse.get_pos(), coords)  # Проверка на наводку на кнопку
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                answer = check_do(pygame.mouse.get_pos(), coords)  # Нажатие на кнопку
                if answer == 'Играть':
                    print('Играть')
                elif answer == 'Выйти':
                    running = False
        pygame.display.flip()
    pygame.quit()
