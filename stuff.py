import pygame

from pygame.locals import *
from constantes import *


class Stuff:

    '''
    class to create a stuff
    '''

    def __init__(self, stuff, x, y):

        self.stuff = pygame.image.load(stuff).convert_alpha()

        self.x = x
        self.y = y
        self.direction = self.stuff
