import math
import random
import pygame, sys

from constants import *


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
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

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
        for row in range(self.row_length):
            for col in range(self.row_length):
                print(self.board[row][col], end=" ")
            print()

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
        return (self.valid_in_row(row, num) and self.valid_in_col(col, num) and
                self.valid_in_box(row - row % self.box_length, col - col % self.box_length, num))

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box
	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	Return: None
    '''

    def fill_box(self, row_start, col_start):
        num = 0
        for row in range(self.box_length):
            for col in range(self.box_length):
                while True:
                    num = random.randrange(1, 10)
                    if self.valid_in_box(row_start, col_start, num):
                        break
                self.board[row_start + row][col_start + col] = num


    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)
	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        for start in range(0, self.row_length, self.box_length):
            self.fill_box(start, start)

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
        if col >= self.row_length and row < self.row_length - 1:
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
        count = self.removed_cells

        while count != 0:
            row = random.randrange(0, 9)
            col = random.randrange(0, 9)
            if self.board[row][col] != 0:
                count -= 1
                self.board[row][col] = 0
    
    '''
    Testing for if SudokuGenerator Class works

if __name__ == "__main__":
    N = 9
    K = 40
    sudoku = SudokuGenerator(N, K)
    sudoku.fill_values()
    sudoku.remove_cells()
    sudoku.print_board()
    '''

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
#def generate_sudoku(size, removed):
    #sudoku = SudokuGenerator(size, removed)
    #sudoku.fill_values()
    #board = sudoku.get_board()
    #sudoku.remove_cells()
    #board = sudoku.get_board()
    #return board

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


    def draw(self):
        '''
        Draws this cell, along with the value inside it.
        If this cell has a nonzero value, that value is displayed.
        Otherwise, no value is displayed in the cell.
        The cell is outlined red if it is currently selected.
        '''
        num_font = pygame.font.Font(None, 25)
        chip_1_surf = num_font.render('1', 0, NUM_COLOR)  # sudoku 1-9
        # 3. text drawing: define the location
        chip_2_surf = num_font.render('2', 0, NUM_COLOR)
        chip_3_surf = num_font.render('3', 0, NUM_COLOR)
        chip_4_surf = num_font.render('4', 0, NUM_COLOR)
        chip_5_surf = num_font.render('5', 0, NUM_COLOR)
        chip_6_surf = num_font.render('6', 0, NUM_COLOR)
        chip_7_surf = num_font.render('7', 0, NUM_COLOR)
        chip_8_surf = num_font.render('8', 0, NUM_COLOR)
        chip_9_surf = num_font.render('9', 0, NUM_COLOR)

        if self.value == 1:
            # draw 'x' or 'o' as text in the window/ board
            # 2. text drawing: define the text
            chip_1_rect = chip_1_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_1_surf, chip_1_rect)
        elif self.value == 2:
            chip_2_rect = chip_2_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_2_surf, chip_2_rect)
        elif self.value == 3:
            chip_3_rect = chip_3_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_3_surf, chip_3_rect)
        elif self.value == 4:
            chip_4_rect = chip_4_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_4_surf, chip_4_rect)
        elif self.value == 5:
            chip_5_rect = chip_5_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(chip_5_surf, chip_5_rect)
        elif self.value == 6:
            chip_6_rect = chip_6_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_6_surf, chip_6_rect)
        elif self.value == 7:
            chip_7_rect = chip_7_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_7_surf, chip_7_rect)
        elif self.value == 8:
            chip_8_rect = chip_8_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_8_surf, chip_8_rect)
        elif self.value == 9:
            chip_9_rect = chip_9_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            # 4. text drawing: blit
            screen.blit(chip_9_surf, chip_9_rect)
        else:
            print("None")


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
        self.board = self.initialize_board()
        self.selected_row = 0
        self.selected_col = 0
        self.original_board = generate_sudoku(9, difficulty)
        self.cells = [] # going to go through everything in original board, and 3change from integers to cell objects
        row = []
        for i in range(0,9):
            for j in range(0,9):
                row.append(Cell(self.original_board[i][j], i, j, screen))
            self.cells.append(row)
            row = []


    def initialize_board(self):
        # 1st approach
        return [["0" for i in range(9)] for j in range(9)]


    def draw(self):
        self.screen.fill(BG_COLOR)
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
        for i in range(0, BOARD_COLS, 3):
            pygame.draw.line(screen,
                             LINE_COLOR,
                             (0, i * SQUARE_SIZE),
                             (WIDTH, i * SQUARE_SIZE),
                             LINE_WIDTH * 2)
            for j in range(0, BOARD_ROWS, 3):
                pygame.draw.line(screen,
                                LINE_COLOR,
                                (j * SQUARE_SIZE, 0),
                                (SQUARE_SIZE * j, HEIGHT),
                                LINE_WIDTH * 2)
        for i in range(0, BOARD_ROWS):
            for j in range(0, BOARD_COLS):
                self.cells[i][j].draw()
                #self.cells[BOARD_COLS].draw()
        '''
        Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        Draws every cell on this board.
        '''

    def select(self,row,col):
        row = self.selected_row
        col = self.selected_col
        box_rect = (row, col, WIDTH // 9, HEIGHT // 9)
        screen.blit(box_rect)
        '''
        Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value
        '''

    def click(self, x, y):
        '''
        If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        of the cell which was clicked. Otherwise, this function returns None
        '''
        if x >= 1 or x <= 9:
            row = (y // SQUARE_SIZE) + 1
            col = (x // SQUARE_SIZE) + 1

            return row, col
        return None


    def clear(self):
        if self.original_board[self.selected_row][self.selected_col] == 0:
            self.cells[self.selected_row][self.selected_col].set_cell_value(0)
            self.cells[self.selected_row][self.selected_col].set_sketched_value(0)
        '''
        Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        filled by themselves.
        '''

    def sketch(self, value):
        if self.original_board[self.selected_row][self.selected_col] == 0:
            self.cells[self.selected_row][self.selected_col].set_sketched_value(value)
        '''
        Sets the sketched value of the current selected cell equal to user entered value.
        It will be displayed at the top left corner of the cell using the draw() function.
        '''

    def place_number(self, value):
        if self.original_board[self.selected_row][self.selected_col] == 0:
            self.cells[self.selected_row][self.selected_col].set_cell_value(value)
        '''
        Sets the value of the current selected cell equal to user entered value.
        Called when the user presses the Enter key.
        '''

    def reset_to_original(self):
        self.cells = []  # going to go through everything in original board, and 3change from integers to cell objects
        row = []
        for i in range(0, 8):
            for j in range(0, 8):
                row.append(Cell(self.original_board[i][j], i, j, screen))
            self.cells.append(row)
            row = []

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
        #WHAT IS THE PURPOSE OF THIS FUNCTION
        pass
        '''
        Updates the underlying 2D board with the values in all cells.
        '''



    def find_empty(self):
        '''
        Finds an empty cell and returns its row and col as a tuple (x, y).
        '''
        for i in range(0, len(BOARD_ROWS-1)):   # may need more work
            for j in range(0, len(BOARD_COLS-1)):
                if self.cells[i][j]:
                    return i, j


    def check_board(self):
        for i in range(0,8):
            for j in range(0,8):
                if not self.is_valid(i, j, self.cells[i][j].value):
                    return False
        return True


    def valid_in_row(self, row, num):
        for col in range(0, 8):
            if self.cells[row][col].value == num:
                return False
        return True


    def valid_in_col(self, col, num):
        for row in range(0, 8):
            if self.cells[row][col].value == num:
                return False
        return True


    def valid_in_box(self, row_start, col_start, num):
        for row in range(0, 2):
            for col in range(0, 2):
                if self.cells[row_start + row][col_start + col].value == num:
                    return False
        return True


    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and self.valid_in_col(col, num) and
                self.valid_in_box(row - row % 3, col - col % 3, num))



class Main:
    # MUST MAKE DIFFICULTY A NUMBER (30 FOR EASY, 40 FOR MED, 50 FOR HARD)
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


pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, GAME_HEIGHT))
mainImage = pygame.image.load("sudokumenu.jpg")
screen.blit(mainImage, (0, 0))
