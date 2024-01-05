import pygame
import const
import os


class Over:  # Класс кнопок
    def __init__(self, screen, damage):
        screen.fill(pygame.Color('black'))

        file = open(os.path.join('data', 'best.txt'), encoding="utf8")
        best = int(file.read())  # Получение лучшего результата
        file.close()

        # Написание текста
        font = pygame.font.Font(None, 90)
        self.end = font.render("Игра окончена", True, pygame.Color('red'))
        self.your = font.render("Ваш результат:", True, pygame.Color('yellow'))
        self.best = font.render("Лучший:", True, pygame.Color('yellow'))
        self.your_num = font.render(f"{damage}", True, pygame.Color('yellow'))
        self.best_num = font.render(f"{best}", True, pygame.Color('yellow'))

        font = pygame.font.Font(None, 120)
        self.again = font.render("Главное меню", True, pygame.Color('yellow'))
        self.ekcit = font.render("Выйти", True, pygame.Color('yellow'))

        # Отрисовка на экране некликабельных текстов
        screen.blit(self.end, ((const.width - self.end.get_width()) // 2, 0))
        if damage > 0:
            screen.blit(self.your, ((const.width - self.your.get_width()) // 2, self.end.get_height() + const.sprites))
            screen.blit(self.your_num, ((const.width - self.your.get_width()) // 2,
                                        self.end.get_height() + const.sprites + self.your.get_height()))
        if best > 0:
            screen.blit(self.best, (const.width - self.best.get_width(), 0))
            screen.blit(self.best_num,
                        (const.width - self.best_num.get_width(), self.best.get_height()))

        # Отрисовка кликабельных текстов
        self.ekcit_coords = (
            const.width // 2 - self.ekcit.get_width() // 2, const.height - const.sprites - self.ekcit.get_height(),
            self.ekcit.get_width(), self.ekcit.get_height())
        self.again_coords = (
            const.width // 2 - self.again.get_width() // 2, self.ekcit_coords[1] - self.again.get_height(),
            self.again.get_width(), self.again.get_height())
        screen.blit(self.again, (self.again_coords[0], self.again_coords[1]))
        screen.blit(self.ekcit, (self.ekcit_coords[0], self.ekcit_coords[1]))

        if damage > best:  # Запись лучшего результата
            file = open(os.path.join('data', 'best.txt'), 'w', encoding="utf8")
            file.write(f'{damage}')
            file.close()

    def check_do(self, pos):  # Функция для нажатия кнопок
        if pos[0] in range(self.again_coords[0], self.again_coords[0] + self.again_coords[2]) and pos[1] in range(
                self.again_coords[1], self.again_coords[1] + self.again_coords[3]):
            return 'Заного'
        elif pos[0] in range(self.ekcit_coords[0], self.ekcit_coords[0] + self.ekcit_coords[2]) and pos[1] in range(
                self.ekcit_coords[1], self.ekcit_coords[1] + self.ekcit_coords[3]):
            return 'Выйти'
        else:
            return None

    def check_pos(self, screen, pos):  # Функция для отрисовки прямоугольников при наведении на кнопку
        if pos[0] in range(self.again_coords[0], self.again_coords[0] + self.again_coords[2]) and pos[1] in range(
                self.again_coords[1], self.again_coords[1] + self.again_coords[3]):
            pygame.draw.rect(screen, pygame.Color('yellow'), (
                self.again_coords[0], self.again_coords[1], self.again_coords[2], self.again_coords[3]), 1)
        else:
            pygame.draw.rect(screen, pygame.Color('black'), (
                self.again_coords[0], self.again_coords[1], self.again_coords[2], self.again_coords[3]), 1)
        if pos[0] in range(self.ekcit_coords[0], self.ekcit_coords[0] + self.ekcit_coords[2]) and pos[1] in range(
                self.ekcit_coords[1], self.ekcit_coords[1] + self.ekcit_coords[3]):
            pygame.draw.rect(screen, pygame.Color('yellow'), (
                self.ekcit_coords[0], self.ekcit_coords[1], self.ekcit_coords[2], self.ekcit_coords[3]), 1)
        else:
            pygame.draw.rect(screen, pygame.Color('black'), (
                self.ekcit_coords[0], self.ekcit_coords[1], self.ekcit_coords[2], self.ekcit_coords[3]), 1)

    def menu(self, screen, event):  # Работа всего меню
        self.check_pos(screen, pygame.mouse.get_pos())  # Проверка на наводку на кнопку
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.check_do(pygame.mouse.get_pos())  # Проверка на нажатие на кнопку
