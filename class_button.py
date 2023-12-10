import pygame


class Buttons:  # Функция создания кнопок
    def __init__(self, screen, pause=False):
        screen.blit(pygame.image.load('zqwt.png').convert_alpha(), (0, 0))
        font = pygame.font.Font(None, 120)
        self.start = False

        if not pause:
            self.play = font.render("Играть", True, pygame.Color('yellow'))
        else:
            self.play = font.render("Продолжить", True, pygame.Color('yellow'))
        self.ekcit = font.render("Выйти", True, pygame.Color('yellow'))
        # Написание текста

        self.otstup = 20  # Левый верхний угол для вертикального расположения кнопок

        screen.blit(self.play, (self.otstup, self.otstup))
        screen.blit(self.ekcit, (self.otstup, self.play.get_height() + self.otstup + 10))
        # Отрисовка на экране

        self.coords = (
            (self.play.get_width(), self.play.get_height()), (self.ekcit.get_width(), self.ekcit.get_height()),
            self.otstup)
        # Список координат, ( Длина и высота "Играть" или "Продолжить", Длина и высота "Выйти", отступ)

    def check_do(self, pos, coords):  # Функция для нажатия кнопок
        if pos[0] in range(coords[2], coords[2] + coords[0][0]) and pos[1] in range(coords[2],
                                                                                    coords[2] + coords[0][1]):
            return 'Играть'
        elif pos[0] in range(coords[2], coords[2] + coords[1][0]) and pos[1] in range(coords[0][1] + coords[2] + 10,
                                                                                      (coords[0][1] + coords[2] + 10) +
                                                                                      coords[1][1]):
            return 'Выйти'

    def check_pos(self, screen, pos, coords):  # Функция для отрисовки прямоугольников при наведении на кнопку
        if pos[0] in range(coords[2], coords[2] + coords[0][0]) and pos[1] in range(coords[2],
                                                                                    coords[2] + coords[0][1]):
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

    def menu(self, screen, event):
        if not self.start:
            self.check_pos(screen, pygame.mouse.get_pos(), self.coords)  # Проверка на наводку на кнопку
            if event.type == pygame.MOUSEBUTTONDOWN:
                answer = self.check_do(pygame.mouse.get_pos(), self.coords)  # Проверка на нажатие на кнопку
                if answer == 'Играть':
                    self.start = True
                elif answer == 'Выйти':
                    return False
            pygame.display.flip()
        return True
