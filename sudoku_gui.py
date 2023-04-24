import pygame, sys
from constants import *

pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
mainImage = pygame.image.load("sudokumenu.jpg")
screen.blit(mainImage, (0, 0))

#maybe make class for this?
#text stuff
font = pygame.font.Font('Raleway-Black.ttf', 48)
title = font.render('Welcome to Sudoku', True, BLACK)
titleRect = title.get_rect()
titleRect = (60, 110)
screen.blit(title, titleRect)

font_2 = pygame.font.Font('Raleway-Black.ttf', 36)
selectMode = font_2.render('Select Game Mode:', True, BLACK)
selectModeRect = selectMode.get_rect()
selectModeRect = (122 , 300)
screen.blit(selectMode, selectModeRect)


button_1 = pygame.draw.rect(screen, ORANGE, pygame.Rect(25, 365, 150, 75))
button_2 = pygame.draw.rect(screen, ORANGE, pygame.Rect(225, 365, 150, 75))
buttons_3 = pygame.draw.rect(screen, ORANGE, pygame.Rect(425, 365, 150, 75))

font_3 = pygame.font.Font('Raleway-Black.ttf', 30)
easy = font_3.render('Easy', True, WHITE)
medium = font_3.render('Medium', True, WHITE)
hard = font_3.render('Hard', True, WHITE)
easyRect = easy.get_rect()
mediumRect = medium.get_rect()
hardRect = hard.get_rect()
easyRect = (65, 382)
mediumRect = (242,382)
hardRect = (465,382)
screen.blit(easy, easyRect)
screen.blit(medium, mediumRect)
screen.blit(hard, hardRect)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


