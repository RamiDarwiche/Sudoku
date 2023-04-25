import pygame, sys

import sudoku_generator
from constants import *
from sudoku_generator import Board

def draw_game_easy(screen):
    #title font
    easy_title_font = pygame.font.Font(None,100)
    button_font = pygame.font.Font(None, 70)

    #bg
    mainImage = pygame.image.load("sudokumenu.jpg")
    screen.blit(mainImage, (0, 0))

    #init and draw title
    title_surface = easy_title_font.render("Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    #buttons
    #text first
    easy_text = button_font.render("Easy", 0 ,(255,255,255))
    medium_text = button_font.render("Medium", 0, (255,255,255))
    hard_text = button_font.render("Hard", 0 , (255,255,255))

    #button bg color & text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20,
                                    easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text,(10,10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20,
                                   medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text,(10,10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20,
                                   hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    #init button rect
    easy_rect = easy_surface.get_rect(
        center = (WIDTH // 2-200, HEIGHT //2 + 150))
    medium_rect = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    hard_rect = hard_surface.get_rect(
        center = (WIDTH // 2 + 200, HEIGHT // 2 +150))

    # Draw buttons
    screen.blit(easy_surface, easy_rect)
    screen.blit(medium_surface, medium_rect)
    screen.blit(hard_surface,hard_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    #pick diff
                    difficulty = 1
                    return  # If the mouse is
                elif medium_rect.collidepoint(event.pos):
                    difficulty =2
                    return
                elif hard_rect.collidepoint(event.pos):
                    difficulty = 3
                    return

        pygame.display.update()

    #game over screen
def draw_game_over(screen):
    game_over_font = pygame.font.Font(None, 40)
    screen.fill(pygame.image.load("sudokumenu.jpg"))
    if winner != 0:
        text = 'You win!'
    else:
        text = "You lose T_T"

    #same logic as easy screen
    game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)
    restart_surf = game_over_font.render(
        'Restart', 0, LINE_COLOR)
    restart_rect = restart_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(restart_surf, restart_rect)
    # Added key to return to main menu
    menu_surf = game_over_font.render(
        'Exit', 0, LINE_COLOR)
    menu_rect = menu_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(menu_surf, menu_rect)

if __name__ == '__main__':
    game_over = False
    winner = False
    difficulty = 0

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    #draw_game_easy(screen)  # Calls function to draw easy screen

    screen.fill(WHITE)
    # draw_lines()
    # middle_cell = Cell('o', 1, 1, 200, 200)
    # middle_cell.draw(screen)
    board = Board(WIDTH, HEIGHT, screen,difficulty)
    board.draw()
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                pass


"""
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

                elif self.text == "Reeasy" and easy.difficulty == True:
                    #board.reset_to_original
                    pass

                elif self.text == "Exit" and easy.difficulty == True:
                    pygame.medium()
                    sys.exit()

def end_screen(screen):
    pass


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


font_3 = pygame.font.Font('Raleway-Black.ttf', 30)

easy = Button(25,365,150,75,ORANGE,"Easy",65,382)
medium = Button(225,365,150,75,ORANGE,"Medium",242,382)
hard = Button(425,365,150,75,ORANGE,"Hard",465,382)




while True:
    game_over = False

    for event in pygame.event.get():
        if event.type == pygame.medium:
            pygame.medium()
            sys.exit()


    easy.clicking_button(event)
    medium.clicking_button(event)
    hard.clicking_button(event)
    pygame.display.update()
    if easy.difficulty == True:
        reeasy = Button(25, 450, 150, 75, RED, "Reeasy", 45, 477)
        reset = Button(225, 450, 150, 75, RED, "Reset", 257, 477)
        exit = Button(425, 450, 150, 75, RED, "Exit", 470, 477)
        gen = 0
        if gen == 0:
            # generate board once
            gen += 1
            generator = sudoku_generator.SudokuGenerator(9, 10)
            board = Board(100,100,screen,"Easy")
            board.draw()

    elif medium.difficulty == True:
        reeasy = Button(25, 450, 150, 75, RED, "Reeasy", 45, 477)
        reset = Button(225, 450, 150, 75, RED, "Reset", 257, 477)
        exit = Button(425, 450, 150, 75, RED, "Exit", 470, 477)
        gen = 0
        if gen == 0:
            # generate board once
            gen += 1
            generator = sudoku_generator.SudokuGenerator(9, 20)
            board = Board(100, 100, screen, "Medium")
            board.draw()

    elif hard.difficulty == True:
        reeasy = Button(25,450,150,75,RED,"Reeasy",45,477)
        reset = Button(225,450,150,75,RED,"Reset",257,477)
        exit = Button(425,450,150,75,RED,"Exit",470,477)
        gen = 0
        if gen == 0:
            #generate board once
            gen +=1
            generator = sudoku_generator.SudokuGenerator(9, 30)
            board = Board(100, 100, screen, "Hard")
            board.draw()



    pygame.display.update()

    if event.type == pygame.MOUSEBUTTONDOWN:
        # if click on a cell that is not randomly generated/deleted
        # highlight it? it is suppose to be outlined red in the draw function in the class
        # type in int in the box in a different font using sketch
        # if selected cell has a sketched value and pygame.ENTER?
        # place_number
        # if is_full is true:
        # if check_board is true:
        # draw you win
        # else:
        # draw you lose
        # update_board with inserted int
        pass



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
screen.blit(hard, hardRect)'
"""
