import pygame
import random as rd

from pygame.locals import *
from constantes import *


class Level:
    '''
    class to Create the level
    '''

    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0
        self.free = 0

    def generer(self):
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            for ligne in fichier:
                ligne_niveau = []
                for sprite in ligne:
                    if sprite != '\n':
                        ligne_niveau.append(sprite)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau

    def afficher(self, window):
        '''
        Define the different structures of the maze
        '''
        wall = pygame.image.load(IMAGE_WALL).convert()
        guardian = pygame.image.load(IMAGE_GUARDIAN).convert()
        fond = pygame.image.load(IMAGE_FOND).convert()

        num_ligne = 0
        for ligne in self.structure:
            num_case = 0
            for sprite in ligne:
                x = num_case * SPRITE_SIZE
                y = num_ligne * SPRITE_SIZE
                if sprite == 'm':
                    window.blit(wall, (x, y))
                elif sprite == 'a':
                    window.blit(guardian, (x, y))
                elif sprite == '0':
                    window.blit(fond, (x, y))
                    self.free += 1
                num_case += 1
            num_ligne += 1

    def random_pos(self, n):
        '''
        For the random position of the items
        '''
        position = [i for i in range(1, self.free)]
        choice = rd.sample(position, 3)
        retour = []

        for j in range(n):
            num_ligne = 0
            counter = 0
            for ligne in self.structure:

                num_case = 0
                for sprite in ligne:

                    x = num_case * SPRITE_SIZE
                    y = num_ligne * SPRITE_SIZE
                    if sprite == '0':
                        counter += 1
                        if counter == choice[j]:
                            retour.append((x, y))

                    num_case += 1
                num_ligne += 1
        return retour
