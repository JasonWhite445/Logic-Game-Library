# -*- coding: utf-8 -*-

import random

def board_reader(board):
    """
    Used for visual testing - Prints boards out
    :param board: Sudoku board in the form of an array - Doesn't need to be completed
    """
    size = len(board)
    sqrt_size = int(size ** (1/2))
    for row in range(size):  # Prints rows from top to bottom
        print(board[row])
    print()
    for col in range(size):  # Prints columns from left to right
        print([board[i][col] for i in range(size)])
    print()
    for box in range(size):  # Prints boxes left to right, then top to bottom
        temp = []
        for pos in range(size):
            i_row = pos // sqrt_size + box // sqrt_size * sqrt_size
            i_col = pos % sqrt_size + box % sqrt_size * sqrt_size
            temp.append(board[i_row][i_col])
        print(temp)
    print()
    return

def board_checker(board):
    """
    :param board: Completed sudoku in the form of an array
    :return: False if any row/column/box has a duplicate value, True otherwise
    """
    size = len(board)
    sqrt_size = int(size**(1/2))
    numbers = [i for i in range(1, size+1)]
    for row in range(size):  # Checks if rows are valid
        if sorted(board[row]) != numbers:
            return False
    for col in range(size):  # Checks if columns are valid
        if sorted([board[i][col] for i in range(size)]) != numbers:
            return False
    for box in range(size):  # Checks if boxes are valid
        temp = []
        for pos in range(size):
            i_row = pos // sqrt_size + box // sqrt_size * sqrt_size
            i_col = pos % sqrt_size + box % sqrt_size * sqrt_size
            temp.append(board[i_row][i_col])
        if sorted(temp) != numbers:
            return False
    return True

def empty_spot(board):
    """
    :param board: Sudoku board array
    :return: Row and column index of the first 0 in the board
    """
    for i_row, row in enumerate(board):
        for i_col, num in enumerate(row):
            if num == 0:
                return i_row, i_col
    # Return None if the sudoku is full
    return None

def check_usable(board, row, col):
    """
    :param board: Sudoku board array
    :param row: Row index of value being checked
    :param col: Column index of value being checked
    :return: List of usable numbers for that position
    """
    size = len(board)
    sqrt_size = int(size ** (1/2))
    box = sqrt_size * (row // sqrt_size) + (col // sqrt_size)
    box_nums = []
    for pos in range(size):
        i_row = pos // sqrt_size + box // sqrt_size * sqrt_size
        i_col = pos % sqrt_size + box % sqrt_size * sqrt_size
        box_nums.append(board[i_row][i_col])
    row_nums = [i for i in board[row] if i != 0]  # List of numbers in the row
    col_nums = [board[pos][col] for pos in range(size) if board[pos][col] != 0]  # List of numbers in the column
    box_nums = [i for i in box_nums if i != 0]  # List of numbers in the box
    used = list(set(box_nums + row_nums + col_nums))  # List of numbers the position can't be
    return [n for n in [i for i in range(1, size+1)] if n not in used]

def fill_board(board):
    """
    Fills a sudoku board of size N
    :param board: Recursively inputs itself to replace all 0's
    :return: Completed sudoku in the form of an array
    """
    if not empty_spot(board):
        return board, 1
    i_row, i_col = empty_spot(board)  # Gets index of first 0
    usable = check_usable(board, i_row, i_col)  # List of usable numbers for the position
    random.shuffle(usable)  # Adds randomness to the board completion
    for num in usable:
        board[i_row][i_col] = num
        if fill_board(board):
            # Recursion step - will get called if that number results in a full board
            return board
        board[i_row][i_col] = 0  # Backtrack


def number_of_solutions(board):
    """
    Ideally we only want to work with single solution boards
    :param board: Incomplete sudoku board
    :return: Number of possible solutions
    """
    if not empty_spot(board):
        return 1  # If there are no empty cells, puzzle is solved
    i_row, i_col = empty_spot(board)
    count = 0
    usable = check_usable(board, i_row, i_col)
    for num in usable:
        board[i_row][i_col] = num
        count += number_of_solutions(board)
        board[i_row][i_col] = 0  # Backtrack
    return count


# Takes user input to adjust size of sudoku board - N needs to be a square number
dimension = int(input("What size sudoku would you like to try? Enter in form NxN: ").partition('x')[0])
# Chunk below creates a board full of 0s then randomly creates a solved board
valid_sudoku_board = fill_board([[0 for _ in range(dimension)] for _ in range(dimension)])

board_reader(valid_sudoku_board)
print(board_checker(valid_sudoku_board))

one_solution_test = [[8, 0, 4, 9, 0, 3, 0, 7, 1],
                     [6, 3, 5, 8, 0, 7, 0, 2, 4],
                     [7, 1, 9, 0, 2, 4, 0, 5, 3],
                     [0, 8, 7, 0, 9, 1, 3, 0, 6],
                     [1, 0, 0, 7, 3, 6, 0, 0, 9],
                     [3, 0, 6, 4, 8, 0, 2, 1, 7],
                     [0, 6, 0, 5, 4, 0, 7, 3, 8],
                     [4, 7, 0, 3, 0, 2, 1, 9, 5],
                     [9, 5, 0, 1, 0, 8, 4, 0, 2]]
print(number_of_solutions(one_solution_test))
# solve_test = fill_board(one_solution_test)
# board_reader(solve_test)

multiple_solution_test = [[0, 0, 5, 7, 4, 3, 8, 6, 1],
                          [4, 3, 1, 8, 6, 5, 9, 0, 0],
                          [8, 7, 6, 1, 9, 2, 5, 4, 3],
                          [3, 8, 7, 4, 5, 9, 2, 1, 6],
                          [6, 1, 2, 3, 8, 7, 4, 9, 5],
                          [5, 4, 9, 2, 1, 6, 7, 3, 8],
                          [7, 6, 3, 5, 2, 4, 1, 8, 9],
                          [0, 0, 8, 6, 7, 1, 3, 5, 4],
                          [1, 5, 4, 9, 3, 8, 6, 0, 0]]
print(number_of_solutions(multiple_solution_test))

