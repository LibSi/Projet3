"""


"""


import pygame
import random

from pygame.locals import *
from classes import *
from character import *
from stuff import *
from constantes import *


def main():
    # initialize pygame
    pygame.init()

    # pygame window opening
    window = pygame.display.set_mode((SIDE_WINDOW, SIDE_WINDOW))
    icone = pygame.image.load(IMAGE_ICONE_PERSO)
    pygame.display.set_icon(icone)
    pygame.display.set_caption(TITLE_WINDOW)
    pygame.key.set_repeat(1000, 1)

    main_loop = True

    while main_loop:
        # load and display homepage
        homepage = pygame.image.load(IMAGE_HOMEPAGE).convert()
        window.blit(homepage, (0, 0))
        pygame.display.flip()

        continue_homepage = True
        continue_game = True
        you_win = False
        you_loose = False
        count_stuff = 0

        while continue_homepage:
            # quiting the game
            for event in pygame.event.get():
                if (event.type == QUIT or event.type == KEYDOWN
                        and event.key == K_ESCAPE):
                    continue_homepage = False
                    main_loop = False
                    continue_game = False
                    you_win = False
                    you_loose = False

                elif event.type == KEYDOWN:
                    if event.key == K_F1:
                        continue_homepage = False
                        choix = 'n1'
        # display level
        if choix != False:
            fond = pygame.image.load(IMAGE_FOND).convert()
            window.blit(fond, (0, 0))
            level = Level(choix)
            level.generer()
            level.afficher(window)
            perso = Mcg(MACGYVER, level)

            position = level.random_pos(3)

            # Stuff 1
            etherposition = position[0]
            etherf = Stuff(ETHER, etherposition[0], etherposition[1])

            # Stuff 2
            tubeposition = position[1]
            tubef = Stuff(TUBE, tubeposition[0], tubeposition[1])

            # Stuff 3
            needleposition = position[2]
            needlef = Stuff(NEEDLE, needleposition[0], needleposition[1])

        while continue_game:

            for event in pygame.event.get():

                # quiting the game
                if event.type == QUIT:
                    continue_homepage = False
                    main_loop = False
                    continue_game = False
                    you_win = False
                    you_loose = False

                # keydown events
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

            # inventary
            if (perso.x, perso.y) == (etherf.x, etherf.y):
                etherf = Stuff(ETHER, 150, 0)
                count_stuff = count_stuff + 1

            if (perso.x, perso.y) == (tubef.x, tubef.y):
                tubef = Stuff(TUBE, 180, 0)
                count_stuff = count_stuff + 1

            if (perso.x, perso.y) == (needlef.x, needlef.y):
                needlef = Stuff(NEEDLE, 210, 0)
                count_stuff = count_stuff + 1

            # if mcg position is equal to guardian position and
            # if mcg inventary is 3 then user win if not it's loose
            if level.structure[perso.case_y][perso.case_x] == 'a':
                if count_stuff == 3:
                    continue_game = 0
                    you_win = True
                else:
                    continue_game = False
                    you_loose = True

            window.blit(fond, (0, 0))
            level.afficher(window)
            window.blit(perso.direction, (perso.x, perso.y))
            window.blit(etherf.direction, (etherf.x, etherf.y))
            window.blit(tubef.direction, (tubef.x, tubef.y))
            window.blit(needlef.direction, (needlef.x, needlef.y))
            pygame.display.flip()

        # Display victory screen
        while you_win:
            fond = pygame.image.load(IMAGE_WIN).convert()
            window.blit(fond, (0, 0))
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

        # Display game-over screen
        while you_loose:
            fond = pygame.image.load(IMAGE_LOOSE).convert()
            window.blit(fond, (0, 0))
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


if __name__ == "__main__":
    main()
