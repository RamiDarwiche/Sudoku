import math
import random
import pygame
import sys
from constants import *


class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        return self.board

    def print_board(self):
        for row in range(self.row_length):
            for col in range(self.row_length):
                print(self.board[row][col], end=" ")
            print()

    def valid_in_row(self, row, num):
        for col in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for row in range(self.box_length):
            for col in range(self.box_length):
                if self.board[row_start + row][col_start + col] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and self.valid_in_col(col, num) and
                self.valid_in_box(row - row % self.box_length, col - col % self.box_length, num))

    def fill_box(self, row_start, col_start):
        num = 0
        for row in range(self.box_length):
            for col in range(self.box_length):
                while True:
                    num = random.randrange(1, 10)
                    if self.valid_in_box(row_start, col_start, num):
                        break
                self.board[row_start + row][col_start + col] = num

    def fill_diagonal(self):
        for start in range(0, self.row_length, self.box_length):
            self.fill_box(start, start)

    def fill_remaining(self, row, col):  # given to students
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

    def fill_values(self):  # given to students
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        count = self.removed_cells

        while count != 0:
            row = random.randrange(0, 9)
            col = random.randrange(0, 9)
            if self.board[row][col] != 0:
                count -= 1
                self.board[row][col] = 0


#     Testing for if SudokuGenerator Class works
#
# if __name__ == "__main__":
#     N = 9
#     K = 40
#     sudoku = SudokuGenerator(N, K)
#     sudoku.fill_values()
#     sudoku.remove_cells()
#     sudoku.print_board()

# DO NOT CHANGE
# Provided for students
# Given a number of rows and number of cells to remove, this function:
# 1. creates a SudokuGenerator
# 2. fills its values and saves this as the solved state
# 3. removes the appropriate number of cells
# 4. returns the representative 2D Python Lists of the board and solution
# Parameters:
# size is the number of rows/columns of the board (9 for this project)
# removed is the number of cells to clear (set to 0)
# Return: list[list] (a 2D Python list to represent the board)

#  def generate_sudoku(size, removed):
    #  sudoku = SudokuGenerator(size, removed)
    #  sudoku.fill_values()
    #  board = sudoku.get_board()
    #  sudoku.remove_cells()
    #  board = sudoku.get_board()
    #  return board

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

    def draw(self):
        num_font = pygame.font.Font(None, 10)
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
        else:
            print("None")


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = self.initialize_board()
        self.selected_row = None
        self.selected_col = None
        self.original_board = generate_sudoku(9, difficulty)
        self.cells = []  # going to go through everything in original board, and change from integers to cell objects
        row = []
        for i in range(0, 8):
            for j in range(0, 8):
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
        for i in range(0, BOARD_ROWS-2):
            for j in range(0, BOARD_COLS-2):
                self.cells[i][j].draw()
                #  self.cells[BOARD_COLS].draw()

    def select(self, row, col):
        self.selected_row = row
        self.selected_col = col

    def click(self, x, y):
        row = (y // SQUARE_SIZE) + 1
        col = (x // SQUARE_SIZE) + 1
        if x >= 1 or x <= 9:
            return row, col
        return None

    def clear(self):
        if self.original_board[self.selected_row][self.selected_col] == 0:
            self.cells[self.selected_row][self.selected_col].set_cell_value(0)
            self.cells[self.selected_row][self.selected_col].set_sketched_value(0)

    def sketch(self, value):
        if self.original_board[self.selected_row][self.selected_col] == 0:
            self.cells[self.selected_row][self.selected_col].set_sketched_value(value)

    def place_number(self, value):
        if self.original_board[self.selected_row][self.selected_col] == 0:
            self.cells[self.selected_row][self.selected_col].set_cell_value(value)

    def reset_to_original(self):
        self.cells = []  # going to go through everything in original board, and 3change from integers to cell objects
        row = []
        for i in range(0, 8):
            for j in range(0, 8):
                row.append(Cell(self.original_board[i][j], i, j, screen))
            self.cells.append(row)
            row = []

    def is_full(self):
        for BOARD_ROWS in self.board:
            for num in BOARD_ROWS:
                if num == "0":
                    return False
        return True

    def update_board(self):
        #  WHAT IS THE PURPOSE OF THIS FUNCTION
        pass

    def find_empty(self):
        for i in range(0, len(BOARD_ROWS-1)):   # may need more work
            for j in range(0, len(BOARD_COLS-1)):
                if self.cells[i][j]:
                    return i, j

    def check_board(self):
        for i in range(0, 9):
            for j in range(0, 9):
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
def generate_sudoku(size, removed): # given to students, don't change
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
