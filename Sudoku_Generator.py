
import random
import copy

dimension = int(input("What size sudoku would you like to try? Enter in form NxN: ").partition('x')[0])
challenge = input("What difficulty would you like to try? Easy, Medium, or Hard: ")

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

def number_of_solutions(board, want):
    """
    Ideally we only want to work with single solution boards
    :param board: Incomplete sudoku board
    :param want: True or False, decides when to break the loop
    :return: Number of possible solutions
    """
    if not empty_spot(board):
        return 1  # If there are no empty cells, puzzle is solved
    if want:
        # Want to see the number of solutions
        i_row, i_col = empty_spot(board)
        count = 0
        usable = check_usable(board, i_row, i_col)
        for num in usable:
            board[i_row][i_col] = num
            count += number_of_solutions(board, True)
            board[i_row][i_col] = 0  # Backtrack
    else:
        # This case ends as soon as the count gets above 1
        i_row, i_col = empty_spot(board)
        count = 0
        usable = check_usable(board, i_row, i_col)
        for num in usable:
            board[i_row][i_col] = num
            count += number_of_solutions(board, False)
            board[i_row][i_col] = 0  # Backtrack
            if count > 1:
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

def remove_numbers(board, difficulty):
    # Easy, Medium, and Hard values are based off of test cases
    # Need to make this code more efficient
    size = len(board)
    if difficulty.lower()[0] == "e":
        difficulty = int((size ** 3) * .24)
    elif difficulty.lower()[0] == "m":
        difficulty = int((size ** 3) * .33)
    elif difficulty.lower()[0] == "h":
        difficulty = int((size ** 3) * .38)
    while difficulty_sum(board) < difficulty:
        row, col = random.randrange(size), random.randrange(size)
        while board[row][col] == 0:
            # Saves some time by preventing replacing 0s in the board
            row, col = random.randrange(size), random.randrange(size)
        temp, board[row][col] = board[row][col], 0
        if number_of_solutions(board, False) > 1:
            # Puts number back if there becomes more solutions
            board[row][col] = temp
    return board


"""
solution is the what the user should get to
random_board is the starting point the user receives
"""
solution = fill_board([[0 for _ in range(dimension)] for _ in range(dimension)])
random_board = remove_numbers(copy.deepcopy(solution), challenge)
