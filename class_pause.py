import pygame

class Pause:  # Класс вызова паузы
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size

    def draw_pause(self):  # Отрисовка паузы
        pygame.draw.rect(self.screen, pygame.Color('grey'),
                         ((self.size[0], self.size[1]), (self.size[1], self.size[1])), 2)
        pygame.draw.line(self.screen, pygame.Color('grey'),
                         (self.size[0] + self.size[1] // 3, self.size[1] + self.size[1] // 5), (
                             self.size[0] + self.size[1] // 3,
                             self.size[1] * 2 - self.size[1] // 5), 9)
        pygame.draw.line(self.screen, pygame.Color('grey'), (
            (self.size[0] + self.size[1]) - (self.size[1] // 3),
            self.size[1] + self.size[1] // 5), (
                             (self.size[0] + self.size[1]) - (self.size[1] // 3),
                             self.size[1] * 2 - self.size[1] // 5), 9)

    def check_do(self, pos, coords):  # Функция для нажатия кнопок
        if pos[0] in range(coords[0], coords[0] + coords[1]) and pos[1] in range(coords[1], coords[1] * 2):
            return True
        return False