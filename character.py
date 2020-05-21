import pygame

from pygame.locals import *
from constantes import *


class Mcg:
    '''
    Class to create playable characters.
    '''

    def __init__(self, right, level):
        self.right = pygame.image.load(MACGYVER).convert_alpha()

        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

        self.direction = self.right
        self.level = level

    def move(self, direction):
        '''
        Class who manage main character movements on the maze
        '''

        if direction == 'right':
            if self.case_x < (NB_SPRITE - 1):
                if self.level.structure[self.case_y][self.case_x + 1] != 'm':
                    self.case_x += 1
                    self.x = self.case_x * SPRITE_SIZE
            self.direction = self.right

        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * SPRITE_SIZE
            self.direction = self.right

        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * SPRITE_SIZE
            self.direction = self.right

        if direction == 'down':
            if self.case_y < (NB_SPRITE - 1):
                if self.level.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * SPRITE_SIZE
            self.direction = self.right
