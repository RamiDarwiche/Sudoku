import math,random
import pygame, sys
from constants import *



"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/
"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length
	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed
	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range (row_length)] # not sure if this is corcret
        self.box_length = math.sqrt(row_length)

    '''
	Returns a 2D python list of numbers which represents the board
	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes
	Parameters: None
	Return: None
    '''
    def print_board(self):
        print(self.board)

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True
	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        for col in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True
	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True
	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box
	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        for row in range(self.box_length):
            for col in range(self.box_length):
                if self.board[row_start + row][col_start + col] == num:
                    return False
        return True

    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box
	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell
	Return: boolean
    '''
    def is_valid(self, row, col, num):
        pass

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box
	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	Return: None
    '''
    def fill_box(self, row_start, col_start):
        pass
    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)
	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        pass

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell
	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining
	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again
	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        pass

class Cell:

    def __init__(self, value, row, col, screen):
        # Constructor for the Cell class
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen


    def set_cell_value(self, value):
        # Setter for this cell’s value
        self.value = value
        return self.value


    def set_sketched_value(self, value):
        pygame.init()
        pygame.display.set_caption("Sudoku")
        font = pygame.font.Font(None, 40)
        '''
        Setter for this cell’s sketched value
        '''
        pass

    def draw(self):
        '''
        Draws this cell, along with the value inside it.
        If this cell has a nonzero value, that value is displayed.
        Otherwise, no value is displayed in the cell.
        The cell is outlined red if it is currently selected.
        '''
        num_font = pygame.font.Font(None, 40)
        chip_1_surf = num_font.render('1', 0, NUM_COLOR)   # sudoku 1-9
        chip_2_surf = num_font.render('2', 0, NUM_COLOR)
        chip_3_surf = num_font.render('3', 0, NUM_COLOR)
        chip_4_surf = num_font.render('4', 0, NUM_COLOR)
        chip_5_surf = num_font.render('5', 0, NUM_COLOR)
        chip_6_surf = num_font.render('6', 0, NUM_COLOR)
        chip_7_surf = num_font.render('7', 0, NUM_COLOR)
        chip_8_surf = num_font.render('8', 0, NUM_COLOR)
        chip_9_surf = num_font.render('9', 0, NUM_COLOR)
        screen = pygame.display.set_mode((WIDTH, HEIGHT))


        if self.value == '1':
            # draw 'x' or 'o' as text in the window/ board
            # 2. text drawing: define the text
            chip_1_rect = chip_1_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_1_surf, chip_1_rect)
        elif self.value == '2':
            chip_2_rect = chip_2_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_2_surf, chip_2_rect)
        elif self.value == '3':
            chip_3_rect = chip_3_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_3_surf, chip_3_rect)
        elif self.value == '4':
            chip_4_rect = chip_4_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_4_surf, chip_4_rect)
        elif self.value == '5':
            chip_5_rect = chip_5_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(chip_5_surf, chip_5_rect)
        elif self.value == '6':
            chip_6_rect = chip_6_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_6_surf, chip_6_rect)
        elif self.value == '7':
            chip_7_rect = chip_7_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_7_surf, chip_7_rect)
        elif self.value == '8':
            chip_8_rect = chip_8_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_8_surf, chip_8_rect)
        elif self.value == '9':
            chip_9_rect = chip_9_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_9_surf, chip_9_rect)

class Board:
    def __init__(self, width, height, screen, difficulty):
        '''
        Constructor for the Board class.
        screen is a window from PyGame.
        difficulty is a variable to indicate if the user chose easy, medium, or hard
        '''
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell("0", BOARD_ROWS, BOARD_COLS, SQUARE_SIZE, SQUARE_SIZE) for BOARD_COLS in range(BOARD_COLS)] for BOARD_ROWS in
                      range(BOARD_ROWS)]
        self.board = self.initialize_board()



    def initialize_board(self):
        # 1st approach
        return [["0" for i in range(9)] for j in range(9)]


    def draw(self):
        self.screen.fill(BG_IMAGE)
        # draw horizontal lines
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(screen,
                             LINE_COLOR,
                             (0, i * SQUARE_SIZE),
                             (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        for i in range(1, BOARD_COLS):
            pygame.draw.line(screen,
                             LINE_COLOR,
                             (i * SQUARE_SIZE, 0),
                             (SQUARE_SIZE * i, HEIGHT),
                             LINE_WIDTH)
        for i in range(1, BOARD_COLS, 3):
            pygame.draw.line(screen,
                             LINE_COLOR
                             (i * SQUARE_SIZE, 0),
                             (SQUARE_SIZE * i, HEIGHT),
                             LINE_WIDTH)
        for i in range(1, BOARD_ROWS, 3):
            pygame.draw.line(screen,
                             LINE_COLOR
                             (i * SQUARE_SIZE, 0),
                             (SQUARE_SIZE * i, HEIGHT),
                             LINE_WIDTH)
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                self.cells[i][j].draw(self.screen)
        '''
        Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        Draws every cell on this board.
        '''


    def select(self,row,col):
        '''
        Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value.
        '''
        pass

    def click(self, x, y):
        '''
        If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        of the cell which was clicked. Otherwise, this function returns None
        '''
        pass

    def clear(self):
        '''
        Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        filled by themselves.
        '''
        pass

    def sketch(self, value):
        '''
        Sets the sketched value of the current selected cell equal to user entered value.
        It will be displayed at the top left corner of the cell using the draw() function.
        '''
        pass

    def place_number(self, value):
        '''
        Sets the value of the current selected cell equal to user entered value.
        Called when the user presses the Enter key.
        '''
        pass

    def reset_to_original(self):
        '''
        Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)
        '''
        pass

    def is_full(self):
        '''
        Returns a Boolean value indicating whether the board is full or not.
        '''
        for BOARD_ROWS in self.board:
            for num in BOARD_ROWS:
                if num == "0":
                    return False
        return True


    def update_board(self):
        '''
        Updates the underlying 2D board with the values in all cells.
        '''
        self.cells = [[Cell(self.board[BOARD_ROWS][BOARD_COLS], BOARD_ROWS, BOARD_COLS, SQUARE_SIZE, SQUARE_SIZE) for BOARD_COLS in range(BOARD_COLS)] for
                      BOARD_COLS in range(BOARD_ROWS)]


    def find_empty(self):
        '''
        Finds an empty cell and returns its row and col as a tuple (x, y).
        '''
        pass

    def check_board(self):
        '''
        Check whether the Sudoku board is solved correctly.
        '''
        pass


class Main:
    pass

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution
Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)
Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


BG_IMAGE = pygame.image.load('background.jpeg').convert   # trying to imporit the photo but its not working
BG_IMAGE = pygame.transform.smoothscale(BG_IMAGE, pygameDisplay.get_size())
pygame.Display.blit(BG_IMAGE, (0, 0))
screen = pygame.display.set_mode((WIDTH, HEIGHT))