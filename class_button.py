import pygame
import const


class Buttons:  # Класс кнопок
    def __init__(self, screen, pause=False):
        screen.blit(pygame.transform.scale(const.load_image('zqwt.png'), const.size), (0, 0))  # Задний фон меню
        font = pygame.font.Font(None, 120)
        self.start = False  # Игра может идти
        self.pause = pause  # Кнопка "Играть" или "Продолжить"

        if not pause:  # Если игрок ещё не начал игру
            self.play = font.render("Играть", True, pygame.Color('yellow'))
            self.ekcit = font.render("Выйти", True, pygame.Color('yellow'))
        else:
            self.play = font.render("Продолжить", True, pygame.Color('yellow'))
            self.ekcit = font.render("Завершить игру", True, pygame.Color('yellow'))
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
            if self.pause:
                return 'Закончить'
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

    def menu(self, screen, event):  # Работа всего меню
        self.check_pos(screen, pygame.mouse.get_pos(), self.coords)  # Проверка на наводку на кнопку
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.check_do(pygame.mouse.get_pos(), self.coords)  # Проверка на нажатие на кнопку
        return True
