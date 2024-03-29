# -*- coding: utf-8 -*-

import random

def board_reader(board):
    """
    Used for visual testing - Prints boards out
    :param board: Sudoku board in the form of an array - Doesn't need to be completed
    """
    size = len(board)
    for row in range(size):  # Prints rows from top to bottom
        print(board[row])
    print()
    return

def board_checker(board):
    """
    :param board: Completed sudoku in the form of an array
    :return: False if any row/column/box has a duplicate value, True otherwise
    """
    box_width, box_height, size = characteristics(board)
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
            i_row = pos // box_width + box // box_height * box_height
            i_col = pos % box_height + box % box_height * box_height
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
    box_width, box_height, size = characteristics(board)
    box = box_height * (row // box_height) + (col // box_width)
    box_nums = []
    for pos in range(size):
        i_row = pos // box_width + box // box_height * box_height
        i_col = pos % box_width + box % box_height * box_width
        box_nums.append(board[i_row][i_col])
    row_nums = [i for i in board[row] if i != 0]  # List of numbers in the row
    col_nums = [board[pos][col] for pos in range(size) if board[pos][col] != 0]  # List of numbers in the column
    box_nums = [i for i in box_nums if i != 0]  # List of numbers in the box
    used = list(set(box_nums + row_nums + col_nums))  # List of numbers the position can't be
    return [n for n in [i for i in range(1, size+1)] if n not in used]

def characteristics(board):
    size = len(board)
    if int(size ** (1 / 2)) == size ** (1 / 2):
        # For boards of size 4x4 and 9x9
        box_height, box_width = int(size ** (1 / 2)), int(size ** (1 / 2))
    else:
        # For boards of size 6x6 and 8x8
        box_height, box_width = 2, int(size / 2)
    return box_width, box_height, size


def number_of_solutions(board):
    """
    Returns the total number of solutions of the board
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
        if count > 3:
            return 2
    return count

def difficulty_sum(board):
    """
    Counts the number of possible values for each cell then sums it for the whole board
    :param board: Incomplete sudoku board
    :return: Difficulty value
    """
    total = 0
    for i_row, row in enumerate(board):
        for i_col, num in enumerate(row):
            total += len(check_usable(board, i_row, i_col))
    return total


def fill_board(board):
    """
    Fills a sudoku board of size N
    :param board: Recursively inputs itself to replace all 0's
    :return: Completed sudoku in the form of an array
    """
    if not empty_spot(board):
        return board
    i_row, i_col = empty_spot(board)  # Gets index of first 0
    usable = check_usable(board, i_row, i_col)  # List of usable numbers for the position
    random.shuffle(usable)  # Adds randomness to the board completion
    for num in usable:
        board[i_row][i_col] = num
        if fill_board(board):
            # Recursion step - will get called if that number results in a full board
            return board
        board[i_row][i_col] = 0  # Backtrack


# Takes user input to adjust size/difficulty of sudoku board - N needs to be a square number
# dimension = int(input("What size sudoku would you like to try? Enter in form NxN: ").partition('x')[0])
# level = input("What difficulty would you like to try? Easy, Medium, or Hard: ")
# # Chunk below creates a board full of 0s then randomly creates a solved board
# random_solvable_board = remove_numbers(fill_board([[0 for _ in range(dimension)] for _ in range(dimension)]), level)
# board_reader(random_solvable_board)


one_solution_test = [[8, 0, 4, 9, 0, 3, 0, 7, 1],
                     [6, 3, 5, 8, 0, 7, 0, 2, 4],
                     [7, 1, 9, 0, 2, 4, 0, 5, 3],
                     [0, 8, 7, 0, 9, 1, 3, 0, 6],
                     [1, 0, 0, 7, 3, 6, 0, 0, 9],
                     [3, 0, 6, 4, 8, 0, 2, 1, 7],
                     [0, 6, 0, 5, 4, 0, 7, 3, 8],
                     [4, 7, 0, 3, 0, 2, 1, 9, 5],
                     [9, 5, 0, 1, 0, 8, 4, 0, 2]]
# print(number_of_solutions(one_solution_test))
# solve_test = fill_board(one_solution_test)
# board_reader(solve_test)

test_1 = [[0, 0, 5, 0, 1, 7, 0, 0, 0],
          [7, 2, 0, 3, 9, 4, 0, 0, 1],
          [0, 9, 1, 0, 0, 0, 0, 0, 0],
          [9, 0, 0, 4, 0, 0, 5, 6, 0],
          [0, 0, 7, 0, 5, 0, 3, 4, 2],
          [2, 0, 0, 0, 3, 0, 1, 0, 7],
          [0, 0, 9, 1, 2, 3, 6, 0, 5],
          [0, 0, 0, 0, 0, 9, 7, 0, 4],
          [0, 3, 8, 7, 0, 6, 0, 0, 9]]
test_2 = [[0, 0, 0, 9, 0, 0, 0, 0, 0],
          [8, 3, 0, 0, 7, 0, 6, 0, 0],
          [0, 4, 0, 0, 0, 0, 8, 0, 7],
          [0, 0, 0, 7, 5, 4, 0, 0, 8],
          [1, 5, 7, 0, 0, 0, 0, 9, 6],
          [2, 8, 0, 1, 0, 0, 0, 0, 0],
          [0, 6, 0, 0, 9, 0, 1, 0, 5],
          [4, 1, 0, 0, 8, 0, 0, 0, 0],
          [9, 0, 8, 0, 0, 0, 0, 7, 0]]
test_3 = [[3, 0, 0, 0, 0, 6, 1, 0, 0],
          [0, 5, 0, 3, 0, 9, 0, 0, 0],
          [0, 2, 0, 8, 0, 0, 5, 4, 3],
          [0, 0, 5, 0, 2, 0, 0, 0, 9],
          [0, 4, 0, 0, 0, 0, 7, 0, 0],
          [0, 0, 1, 0, 8, 0, 0, 0, 0],
          [0, 3, 7, 0, 0, 8, 0, 6, 0],
          [0, 8, 6, 1, 0, 0, 0, 0, 0],
          [0, 1, 0, 7, 6, 0, 8, 0, 5]]
test_4 = [[1, 3, 0, 5, 0, 0, 0, 7, 0],
          [0, 0, 0, 0, 3, 0, 0, 0, 2],
          [7, 6, 0, 9, 0, 0, 5, 0, 0],
          [0, 0, 0, 0, 0, 0, 9, 0, 3],
          [9, 0, 0, 0, 0, 3, 0, 8, 0],
          [0, 0, 0, 0, 9, 1, 0, 0, 4],
          [8, 7, 0, 6, 0, 0, 3, 0, 5],
          [0, 0, 0, 0, 0, 4, 0, 0, 0],
          [0, 0, 9, 1, 5, 0, 0, 0, 6]]
test_5 = [[4, 0, 7, 1, 0, 3, 0, 0, 0],
          [9, 1, 0, 0, 0, 0, 0, 0, 0],
          [6, 0, 0, 0, 0, 4, 0, 9, 0],
          [1, 3, 0, 0, 0, 0, 0, 0, 5],
          [0, 9, 8, 0, 0, 2, 7, 0, 0],
          [7, 0, 0, 0, 5, 8, 2, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 3],
          [0, 0, 9, 0, 7, 6, 0, 5, 0],
          [0, 0, 0, 4, 0, 5, 0, 0, 0]]
test_6 = [[0, 9, 6, 0, 7, 0, 0, 4, 0],
          [7, 4, 0, 2, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 8, 4, 0, 7, 0, 0, 0],
          [0, 0, 0, 9, 1, 5, 0, 0, 7],
          [0, 0, 0, 0, 0, 0, 0, 5, 0],
          [0, 6, 0, 0, 0, 0, 0, 0, 9],
          [3, 0, 0, 0, 0, 0, 1, 0, 2],
          [0, 0, 0, 0, 0, 4, 0, 0, 0]]
test_7 = [[0, 7, 0, 8, 0, 0, 2, 0, 0],
          [0, 0, 0, 5, 0, 0, 0, 0, 1],
          [0, 0, 4, 0, 7, 1, 3, 0, 0],
          [0, 5, 0, 0, 2, 9, 0, 0, 3],
          [0, 0, 0, 1, 0, 0, 0, 0, 0],
          [6, 0, 0, 0, 0, 0, 4, 0, 0],
          [0, 0, 5, 0, 0, 0, 0, 2, 0],
          [0, 0, 0, 0, 8, 0, 0, 0, 0],
          [0, 2, 0, 0, 3, 7, 0, 0, 9]]
test_8x8 = [[4, 0, 0, 2, 1, 0, 3, 0],
            [0, 7, 0, 0, 0, 2, 0, 0],
            [0, 0, 2, 0, 5, 0, 7, 0],
            [7, 0, 0, 5, 0, 0, 0, 3],
            [6, 0, 0, 0, 3, 0, 0, 1],
            [0, 1, 0, 3, 0, 8, 0, 0],
            [0, 0, 7, 0, 0, 0, 8, 0],
            [0, 6, 0, 8, 4, 0, 0, 5]]

