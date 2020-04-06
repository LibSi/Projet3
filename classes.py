

import pygame
import random
from pygame.locals import *
from constantes import *

class Level:
    #creation level
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

        
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
        wall = pygame.image.load(image_wall).convert()
        guardian = pygame.image.load(image_guardian).convert()
        fond = pygame.image.load(image_fond).convert()
       
        
        num_ligne = 0
        for ligne in self.structure:
            num_case = 0
            for sprite in ligne:
                x = num_case * sprite_size
                y = num_ligne * sprite_size
                if sprite == 'm':
                    window.blit(wall, (x,y))
                elif sprite == 'a':
                    window.blit(guardian, (x,y))
                elif sprite == '0':
                    window.blit(fond, (x,y))
                    
                num_case += 1
            num_ligne +=1
            
#for the random position of the items
    def random (self, number):
        num_ligne = 0
        counter = 0
        for ligne in self.structure:

            num_case = 0
            for sprite in ligne:

                x = num_case * sprite_size
                y = num_ligne * sprite_size
                if sprite == '0':
                    counter += 1
                    if counter == number:
                        return (x, y)
                        
                num_case += 1
            num_ligne += 1
 
#Macguyver 
class Mcg:
    def __init__(self, right, level):
        self.right = pygame.image.load(macgyver).convert_alpha()

        
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        
        self.direction = self.right
        self.level = level
        
    def move(self, direction):
    
        if direction == 'right':
            if self.case_x < (nb_sprite - 1):
                if self.level.structure[self.case_y][self.case_x+1] != 'm':
                    self.case_x += 1
                    self.x = self.case_x * sprite_size
            self.direction = self.right
            
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * sprite_size
            self.direction = self.right
            
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * sprite_size
            self.direction = self.right
            
        if direction == 'down':
            if self.case_y < (nb_sprite -1):
                if self.level.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * sprite_size
            self.direction = self.right
            
            
class Stuff:
    #Class to create a character

    def __init__(self, stuff, x, y):
        
        self.stuff = pygame.image.load(stuff).convert_alpha()
        
        self.x = x
        self.y = y
        self.direction = self.stuff
    
    
            