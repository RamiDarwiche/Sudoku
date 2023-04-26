import pygame, sys

import sudoku_generator_whole
from constants import *
from sudoku_generator_whole import Board

def draw_game_easy(screen):
    #title font
    easy_title_font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font(None, 70)

    #bg
    mainImage = pygame.image.load("sudokumenu.jpg")
    mainImage = pygame.transform.scale(mainImage, (600,675))
    screen.blit(mainImage, (0, 0))

    #init and draw title
    title_surface = easy_title_font.render("Welcome to Sudoku", 0, BLACK)
    title_rectangle = title_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    #init and draw game mode
    game_font = pygame.font.Font(None, 75)
    game_mode = game_font.render("Select Game Mode:", 0, BLACK)
    game_rectangle = game_mode.get_rect(
        center=(WIDTH - 300, HEIGHT - 150))
    screen.blit(game_mode, game_rectangle)

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
        center = (WIDTH // 2-200, HEIGHT //2 + 250))
    medium_rect = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 250))
    hard_rect = hard_surface.get_rect(
        center = (WIDTH // 2 + 200, HEIGHT // 2 +250))

    # Draw buttons
    screen.blit(easy_surface, easy_rect)
    screen.blit(medium_surface, medium_rect)
    screen.blit(hard_surface,hard_rect)

    #button funct
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    #pick diff
                    return 30 # If the mouse is
                elif medium_rect.collidepoint(event.pos):
                    return 40
                elif hard_rect.collidepoint(event.pos):
                    return 50

        pygame.display.update()

    #game over screen
def draw_game_over(screen):
    game_over_font = pygame.font.Font(None, 80)
    mainImage = pygame.image.load("sudokumenu.jpg")
    mainImage = pygame.transform.scale(mainImage, (600, 675))
    screen.blit(mainImage, (0, 0))
    if winner != 0:
        text = 'Game Won!'
    else:
        text = "Game Over :("

    #same logic as easy screen
    game_over_surf = game_over_font.render(text, 0, BLACK)
    game_over_rect = game_over_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)
    # Restart button
    game_over_font = pygame.font.Font(None, 40)
    restart_text = game_over_font.render("Restart", 0, (BLACK))
    restart_surf = pygame.Surface((restart_text.get_size()[0] + 20,
                                   restart_text.get_size()[1] + 20))
    restart_rect = restart_surf.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 + 350))
    restart_surf.fill(LINE_COLOR)
    restart_surf.blit(restart_text, (10, 10))
    screen.blit(restart_surf, restart_rect)


    # Added key to return to main menu
    # Exit button
    exit_text = game_over_font.render("Exit", 0, (BLACK))
    exit_surf = pygame.Surface((exit_text.get_size()[0] + 20,
                                exit_text.get_size()[1] + 20))
    exit_rect = exit_surf.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 + 350))
    exit_surf.fill(LINE_COLOR)
    exit_surf.blit(exit_text, (10, 10))
    screen.blit(exit_surf, exit_rect)
    if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
        if exit_rect.collidepoint(event.pos):
            pygame.quit()
            sys.exit()
        elif restart_rect.collidepoint(event.pos):
            draw_game_easy(screen)
            screen.fill(WHITE)
            board = Board(WIDTH, HEIGHT, screen, difficulty)
            board.draw()
            screen.blit(restart_surf, restart_rect)
            screen.blit(reset_surf, reset_rect)
            screen.blit(exit_surf, exit_rect)
    pygame.display.update()




    #button funct
    """"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    pass # If the mouse is
                elif exit_rect.collidepoint(event.pos):
                    sys.exit()
                elif reset_rect.collidepoint(event.pos):
                    board.reset_to_original()
                    return
"""
if __name__ == '__main__':
    #starting variables
    game_over = False
    winner = False

    #init screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, GAME_HEIGHT))
    pygame.display.set_caption("Sudoku")

    #display start until button is clicked
    difficulty = draw_game_easy(screen)  # Calls function to draw easy screen

    #
    screen.fill(WHITE)
    board = Board(WIDTH, HEIGHT, screen, difficulty)
    board.draw()
    game_over_font = pygame.font.Font(None, 40)
    # Restart button
    restart_text = game_over_font.render("Restart", 0, (BLACK))
    restart_surf = pygame.Surface((restart_text.get_size()[0] + 20,
                                   restart_text.get_size()[1] + 20))
    restart_rect = restart_surf.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 + 350))
    restart_surf.fill(LINE_COLOR)
    restart_surf.blit(restart_text, (10, 10))
    screen.blit(restart_surf, restart_rect)

    # reset button
    reset_text = game_over_font.render("Reset", 0, (BLACK))
    reset_surf = pygame.Surface((reset_text.get_size()[0] + 20,
                                 reset_text.get_size()[1] + 20))
    reset_rect = reset_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 350))
    reset_surf.fill(LINE_COLOR)
    reset_surf.blit(reset_text, (10, 10))
    screen.blit(reset_surf, reset_rect)

    # exit button
    exit_text = game_over_font.render("Exit", 0, (BLACK))
    exit_surf = pygame.Surface((exit_text.get_size()[0] + 20,
                                exit_text.get_size()[1] + 20))
    exit_rect = exit_surf.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 + 350))
    exit_surf.fill(LINE_COLOR)
    exit_surf.blit(exit_text, (10, 10))
    screen.blit(exit_surf, exit_rect)
    pygame.display.flip()

    num = -1
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if reset_rect.collidepoint(event.pos):
                    board.reset_to_original()
                    board.draw()
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)
                    continue
                elif exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif restart_rect.collidepoint(event.pos):
                    draw_game_easy(screen)
                    screen.fill(WHITE)
                    board = Board(WIDTH, HEIGHT, screen, difficulty)
                    board.draw()
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)
                    continue


            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                clicked_row = int(event.pos[1] / SQUARE_SIZE)
                clicked_col = int(event.pos[0] / SQUARE_SIZE)
                board.selected_row = clicked_row
                board.selected_col = clicked_col
                board.cells[clicked_row][clicked_col].row = clicked_row
                board.cells[clicked_row][clicked_col].col = clicked_col

                print(clicked_row, clicked_col)






                # coords is supposed to take x,y of pos and print the row and col that is selected
                #you can use these print functions to test if it works
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    num = 1
                    print("kdhb")
                    print(board.cells[clicked_row][clicked_col].set_cell_value(num))

                    board.draw()
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_2:
                    num = 2
                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_3:
                    num = 3

                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_4:
                    num = 4

                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_5:
                    num = 5

                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_6:
                    num = 6

                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_7:
                    num = 7

                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_8:
                    num = 8

                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_9:
                    num = 9

                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_RETURN and num <= 9:
                    board.place_number(num)


                    if board.is_full() == True:
                        winner = 1
                        pygame.display.update()
                        pygame.time.delay(1000)
                        print(winner)
                        draw_game_over(screen)
                        continue

            pygame.display.update()

            #asks for number to sktech


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
        restart = Button(25, 450, 150, 75, RED, "Restart", 45, 477)
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
        restart = Button(25, 450, 150, 75, RED, "Restart", 45, 477)
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
        restart = Button(25,450,150,75,RED,"Restart",45,477)
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
