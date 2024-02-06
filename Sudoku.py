# -*- coding: utf-8 -*-

import pygame
import random

# Takes user input to adjust size of sudoku board - N needs to be a square number
size = int(input("What size sudoku would you like to try? Enter in form NxN: ").partition('x')[0])

def board_reader(board, size):
    sqrt_size = int(size ** (1/2))
    # Used for visual testing
    # Prints rows from top to bottom
    for row in range(size):
        print(board[row])
    print()
    # Prints columns from left to right
    for col in range(size):
        print([board[i][col] for i in range(size)])
    print()
    # Prints the boxes left to right, top to bottom
    for box in range(size):
        print([board[pos // sqrt_size + box // sqrt_size * sqrt_size][pos % sqrt_size + box % sqrt_size * sqrt_size] for pos in range(size)])
    print()
    return

def board_checker(board, size):
    sqrt_size = int(size**(1/2))
    numbers = [i for i in range(1, size+1)]
    # Checks if rows are valid
    for row in range(size):
        if sorted(board[row]) != numbers:
            return False
    # Checks if columns are valid
    for col in range(size):
        if sorted([board[i][col] for i in range(size)]) != numbers:
            return False
    # Checks if boxes are valid
    for box in range(size):
        temp = []
        for pos in range(size):
            i_row = pos // sqrt_size + box // sqrt_size * sqrt_size
            i_col = pos % sqrt_size + box % sqrt_size * sqrt_size
            temp.append(board[i_row][i_col])
        if sorted(temp) != numbers:
            return False
    return True

def make_random_board(board, size):
    if not empty_spot(board):
        # Gets called if there are no 0s in the board
        return board
    # Gets the index of the first 0
    i_row, i_col = empty_spot(board)
    if i_row == 0 and i_col == 0:
        # Shuffles numbers to randomize the first row
        row1 = [i for i in range(1, size+1)]
        random.shuffle(row1)
        board[0] = row1
        for row in range(1, size):
            # Shuffles numbers to randomize the first column
            board[row][0] = random.choice(check_usable(board, size, row, 0))
        return make_random_board(board, size)
    else:
        # Creates the list of usable numbers for specific position
        # Shuffles the list so that the board is random
        usable = check_usable(board, size, i_row, i_col)
        random.shuffle(usable)
        for num in usable:
            # Replaces the 0 with a usable number
            board[i_row][i_col] = num
            if make_random_board(board, size):
                # Recursion step - will get called if that number results in a full board
                return board
            # If that number leads to a dead end
            board[i_row][i_col] = 0

def empty_spot(board):
    # Returns the row and column index of the first 0 in the board
    for i_row, row in enumerate(board):
        for i_col, num in enumerate(row):
            if num == 0:
                return i_row, i_col
    # Return None if the sudoku is full
    return None

def check_usable(board, size, row, col):
    sqrt_size = int(size ** (1/2))
    box = sqrt_size * (row // sqrt_size) + (col // sqrt_size)
    box_nums = [board[pos // sqrt_size + box // sqrt_size * sqrt_size][pos % sqrt_size + box % sqrt_size * sqrt_size] for pos in range(size)]
    row_nums = [i for i in board[row] if i != 0]
    col_nums = [board[pos][col] for pos in range(size) if board[pos][col] != 0]
    box_nums = [i for i in box_nums if i != 0]
    used = list(set(box_nums + row_nums + col_nums))
    return [n for n in [i for i in range(1, size+1)] if n not in used]


# Chunk below creates a board full of 0s then randomly creates a solved board
valid_sudoku_board = make_random_board([[0 for i in range(size)] for j in range(size)], size)

board_reader(valid_sudoku_board, size)
print(board_checker(valid_sudoku_board, size))

