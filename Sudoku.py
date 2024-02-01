# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:35:34 2024

@author: Adam
"""

import pygame
import random

# Test input - will later become user input
valid_sudoku_board = [[8, 2, 7, 1, 5, 4, 3, 9, 6],
                      [9, 6, 5, 3, 2, 7, 1, 4, 8],
                      [3, 4, 1, 6, 8, 9, 7, 5, 2],
                      [5, 9, 3, 4, 6, 8, 2, 7, 1],
                      [4, 7, 2, 5, 1, 3, 6, 8, 9],
                      [6, 1, 8, 9, 7, 2, 4, 3, 5],
                      [7, 8, 6, 2, 3, 5, 9, 1, 4],
                      [1, 5, 4, 7, 9, 6, 8, 2, 3],
                      [2, 3, 9, 8, 4, 1, 5, 6, 7]]

def board_reader(board):
    # Used for visual testing
    # Prints rows from top to bottom
    for row in range(9):
        print(board[row])
    print()
    # Prints columns from left to right
    for col in range(9):
        print([board[i][col] for i in range(9)])
    print()
    # Prints the boxes left to right, top to bottom
    for box in range(9):
        print([board[pos // 3 + box // 3 * 3][pos % 3 + box % 3 * 3] for pos in range(9)])
    print()
    return

def board_checker(board):
    # Checks if rows are valid
    for row in range(9):
        if sorted(board[row]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    # Checks if columns are valid
    for col in range(9):
        if sorted([board[i][col] for i in range(9)]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    # Checks if boxes are valid
    for box in range(9):
        if sorted([board[pos // 3 + box // 3 * 3][pos % 3 + box % 3 * 3] for pos in range(9)]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    return True

def make_random_board(board):
    if not empty_spot(board):
        # Gets called if there are no 0s in the board
        return board
    # Gets the index of the first 0
    i_row, i_col = empty_spot(board)
    if i_row == 0 and i_col == 0:
        # Shuffles numbers to randomize the first row
        row1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(row1)
        board[0] = row1
        for row in range(1, 9):
            # Shuffles numbers to randomize the first column
            board[row][0] = random.choice(check_usable(board, row, 0))
        return make_random_board(board)
    else:
        # Creates the list of usable numbers for specific position
        # Shuffles the list so that the board is random
        usable = check_usable(board, i_row, i_col)
        random.shuffle(usable)
        for num in usable:
            # Replaces the 0 with a usable number
            board[i_row][i_col] = num
            if make_random_board(board):
                # Recursion step - will get called if that number results in a full board
                return True
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

def check_usable(board, row, col):
    box = 3 * (row // 3) + (col // 3)
    box_nums = [board[pos // 3 + box // 3 * 3][pos % 3 + box % 3 * 3] for pos in range(9)]
    row_nums = [i for i in board[row] if i != 0]
    col_nums = [board[pos][col] for pos in range(9) if board[pos][col] != 0]
    box_nums = [i for i in box_nums if i != 0]
    used = list(set(box_nums + row_nums + col_nums))
    return [n for n in [1, 2, 3, 4, 5, 6, 7, 8, 9] if n not in used]


# board_reader(valid_sudoku_board)
# print(board_checker(valid_sudoku_board))

# Chunk below creates a board full of 0s then randomly creates a solved board
random_start = [[0 for i in range(9)] for j in range(9)]
make_random_board(random_start)
for row in random_start:
    print(row)
