import pygame
import const

FPS = const.FPS

class Frames:  # Класс фреймов, для подсчёта тиков
    def __init__(self):
        self.count = 0
        self.jump = False
        self.start_jump = 0
        self.fall = False
        self.start_fall = 0

    def check(self, player):
        self.count += 1
        if player.jump:
            self.start_jump = True
            player.jump = False
            self.start_jump = self.count
        if player.fall:
            self.fall = True
            player.fall = False
            self.start_fall = self.count
        if self.jump and self.count - self.start_jump < FPS:
            player.moving('jump')
        if self.fall:
            player.moving('fall', fall=self.count - self.start_fall)