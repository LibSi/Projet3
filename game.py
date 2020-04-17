"""


"""


import pygame
import random
from pygame.locals import * 

from classes import *
from constantes import *


pygame.init()


'''pygame window opening'''
window = pygame.display.set_mode((side_window, side_window))
icone = pygame.image.load(image_icone_perso)
pygame.display.set_icon(icone)
pygame.display.set_caption(title_window)
pygame.key.set_repeat(1000, 1)
 
 
'''main loop'''
main_loop = True

while main_loop:
    '''load and display homepage'''
    homepage = pygame.image.load(image_homepage).convert()
    window.blit(homepage, (0, 0))
    pygame.display.flip()

    '''reset variable'''
    continue_homepage = True
    continue_game = True
    you_win = False
    you_loose = False
    count_stuff = 0
    
    '''homepage loop'''
    while continue_homepage:
        
        for event in pygame.event.get():
        
            '''check choice user'''
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continue_homepage = False
                main_loop = False
                continue_game = False
                you_win = False
                you_loose = False
                
            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    continue_homepage = False
                    choix = 'n1' 
    '''if the user press f1, then the level is launche '''               
    if choix != False:
        fond = pygame.image.load(image_fond).convert()
        window.blit(fond, (0,0))
        level = Level(choix)
        level.generer()
        level.afficher(window)
        '''create Macguyver'''
        perso = Mcg("ressource/images/macgyver.png", level)
        
        
        '''random placement of objects'''
        position = level.random(3)
        
        #Stuff 1
        etherposition = position[0]
        etherf = Stuff(ether, etherposition[0], etherposition[1])
       
        #Stuff 2 
        tubeposition = position[1]
        tubef = Stuff(tube, tubeposition[0], tubeposition[1])
        
        #Stuff 3
        needleposition = position[2]
        needlef = Stuff(needle, needleposition[0], needleposition[1])
        
    '''loop game'''    
    while continue_game:
        pygame.time.Clock().tick(30)
        
        for event in pygame.event.get():
            
            if event.type == QUIT: 
                continue_homepage = False
                main_loop = False
                continue_game = False
                you_win = False
                you_loose = False
                
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continue_game = 0
                elif event.key == K_RIGHT:
                    perso.move('right')
                elif event.key == K_LEFT:
                    perso.move('left')
                elif event.key == K_UP:
                    perso.move('up')
                elif event.key == K_DOWN:
                    perso.move('down')
                    
        '''inventary'''           
        if (perso.x, perso.y) == (etherf.x, etherf.y):
            etherf = Stuff(ether, 150, 0)
            count_stuff = count_stuff + 1

        if (perso.x, perso.y) == (tubef.x, tubef.y):
            tubef = Stuff(tube, 180, 0)
            count_stuff = count_stuff + 1

        if (perso.x, perso.y) == (needlef.x, needlef.y):
            needlef = Stuff(needle, 210, 0)
            count_stuff = count_stuff + 1
        
        '''compare counter, if mcg inventary is 3 then user win if not it's loose'''
        if level.structure[perso.case_y][perso.case_x] == 'a':
            if count_stuff == 3:
                continue_game = 0
                you_win = True
            else:
                continue_game = False
                you_loose = True
                
        '''display new position and stuff'''       
        window.blit(fond, (0,0))
        level.afficher(window)
        window.blit(perso.direction, (perso.x, perso.y))
        window.blit(etherf.direction, (etherf.x, etherf.y))
        window.blit(tubef.direction, (tubef.x, tubef.y))
        window.blit(needlef.direction, (needlef.x, needlef.y))
        pygame.display.flip()
        
       
                
    '''if the user to win'''           
    while you_win:
        fond = pygame.image.load(image_win).convert()
        window.blit(fond, (0,0))  
        pygame.display.flip()        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continue_homepage = False
                    main_loop = False
                    continue_game = False
                    you_win = False
                    you_loose - False
                elif event.key == K_SPACE:
                    continue_game = False
                    you_win = False
                    you_loose = False
            
    '''game over'''               
    while you_loose:
        fond = pygame.image.load(image_loose).convert()
        window.blit(fond, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continue_homepage = False
                    main_loop = False
                    continue_game = False
                    you_loose = False
                    you_win = False
                elif event.key == K_SPACE:
                    continue_game = False
                    you_win = False
                    you_loose = False
        
                
            
                    
 
        
        
