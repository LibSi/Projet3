"""


"""


import pygame
from pygame.locals import * 
from constantes import *

pygame.init()


#pygame window opening
window = pygame.display.set_mode((side_window, side_window))
#icon
icone = pygame.image.load(image_icone_perso)
pygame.display.set_icon(icone)
#title
pygame.display.set_caption(title_window)
 
 
#main loop
continue_game = 1

while continue_game:
    #load and display homepage
    homepage = pygame.image.load(image_homepage).convert()
    window.blit(homepage, (0,0))
    #refresh
    pygame.display.flip()
    #reset variable
    continue_homepage = 1
    #homepage loop
    while continue_homepage:
        
        for event in pygame.event.get():
        
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continue_homepage = 0
                continue_game = 0
                in_game = 0
                choix = 0
            