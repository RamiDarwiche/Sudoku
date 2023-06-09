import pygame, sys
from constants import *
from sudoku_generator_whole import Board


class Button():
    def __init__(self, leftBox, topBox, width, height, color, text,xText,yText):
        #init variables and make a rect
        self.rect = pygame.Rect(leftBox,topBox,width,height)
        self.leftBox = leftBox
        self.topBox = topBox
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.xText = xText
        self.yText = yText
        #check if its one of the 3 buttons
        self.difficulty = None
        #draws rectangle, init font, center text, draw
        pygame.draw.rect(screen, self.color, pygame.Rect(self.leftBox,self.topBox,self.width,self.height))
        t = font_3.render(f"{self.text}", True, WHITE)
        center = (self.xText,self.yText)
        screen.blit(t,center)

    def clicking_button(self, event):


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):

                if self.text == "Easy":
                    screen.fill((0,0,0))
                    #Board.draw()
                    #draw generated board, init with diff
                    self.difficulty = True #used for gui

                elif self.text == "Medium":
                    screen.fill((0,0,0))
                    #draw generated board, init with diff
                    self.difficulty = True

                elif self.text == "Hard":
                    screen.fill((0,0,0))
                    #draw generated board, init with diff
                    self.difficulty = True
                    pass

                elif self.text == "Reset" and easy.difficulty == True:
                    #board.clear
                    pass

                elif self.text == "Restart" and easy.difficulty == True:
                    #board.reset_to_original
                    pygame.display.update()

                elif self.text == "Exit" and easy.difficulty == True:
                    pygame.quit()
                    sys.exit()


pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
mainImage = pygame.image.load("sudokumenu.jpg")
screen.blit(mainImage, (0, 0))

#maybe make class for this?
#text stuff
#is this updating real time? - Ramzi
#it should because of the pygame.display.update() in the while True loop
#if not we can make a class for the text too and move it into the while True loop
"""font = pygame.font.Font('Raleway-Black.ttf', 48)
title = font.render('Welcome to Sudoku', True, BLACK)
titleRect = title.get_rect()
titleRect = (60, 110)
screen.blit(title, titleRect)

font_2 = pygame.font.Font('Raleway-Black.ttf', 36)
selectMode = font_2.render('Select Game Mode:', True, BLACK)
selectModeRect = selectMode.get_rect()
selectModeRect = (122 , 300)
screen.blit(selectMode, selectModeRect)"""

font_3 = pygame.font.Font('Raleway-Black.ttf', 30)

easy = Button(25,365,150,75,ORANGE,"Easy",65,382)
medium = Button(225,365,150,75,ORANGE,"Medium",242,382)
hard = Button(425,365,150,75,ORANGE,"Hard",465,382)
'''button_1 = pygame.draw.rect(screen, ORANGE, pygame.Rect(25, 365, 150, 75))
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
'''

def game_over_update(game_over):
    mainImage = pygame.image.load("sudokumenu.jpg")
    if game_over == True:
        screen.fill(mainImage)
        end_text = "Game Won!"
        exit = Button(425, 450, 150, 75, RED, "Exit", 470, 477)
    else:
        end_text = "Game Over :("
        restart = Button(25, 450, 150, 75, RED, "Restart", 45, 477)

    end_surf = font_3.render(end_text, 0, LINE_COLOR)
    end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(end_surf, end_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #x, y = event.pos
            #row = y // SQUARE_SIZE
            #col = x // SQUARE_SIZE
            #game_over = False
            #if Board.check_board():
                #game_over = True
            #if game_over:
                #pygame.display.update()
                #pygame.time.delay(1000)
                #game_over_update(game_over)

            #if click on a cell that is not randomly generated/deleted
                #highlight it? it is suppose to be outlined red in the draw function in the class
                #type in int in the box in a different font using sketch
                #if selected cell has a sketched value and pygame.ENTER?
                    #place_number
                #if is_full is true:
                    #if check_board is true:
                        #draw you win
                    #else:
                        #draw you lose
                #update_board with inserted int
            pass


    easy.clicking_button(event)
    medium.clicking_button(event)
    hard.clicking_button(event)
    pygame.display.update()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG_COLOR)  # sets the background color
    board = Board(3, 3, WIDTH, HEIGHT)
    board.draw()
    if easy.difficulty == True or medium.difficulty == True or hard.difficulty == True:
        #make boxes better looking
        restart = Button(25,450,150,75,RED,"Restart",45,477)
        reset = Button(225,450,150,75,RED,"Reset",257,477)
        exit = Button(425,450,150,75,RED,"Exit",470,477)
        pass
