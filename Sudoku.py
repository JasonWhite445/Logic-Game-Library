# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:35:34 2024

@author: Adam
"""

import pygame
import random


def board_reader(board):
    # Prints rows from top to bottom
    for row in range(9):
        print(board[row])
    print()
    # Prints columns from left to right
    for col in range(9):
        print([board[i][col] for i in range(9)])
    print()
    # Prints the boxes left to right, top to bottom
# =============================================================================
#   [[0][0], [0][1], [0][2], [1][0], [1][1], [1][2], [2][0], [2][1], [2][2]]
#   [[0][3], [0][4], [0][5], [1][3], [1][4], [1][5], [2][3], [2][4], [2][5]]
#   [[0][6], [0][7], [0][8], [1][6], [1][7], [1][8], [2][6], [2][7], [2][8]]
#   [[3][0], [3][1], [3][2], [4][0], [4][1], [4][2], [5][0], [5][1], [5][2]]
#   [[3][3], [3][4], [3][5], [4][3], [4][4], [4][5], [5][3], [5][4], [5][5]]
#   [[3][6], [3][7], [3][8], [4][6], [4][7], [4][8], [5][6], [5][7], [5][8]]
#   [[6][0], [6][1], [6][2], [7][0], [7][1], [7][2], [8][0], [8][1], [8][2]]
#   [[6][3], [6][4], [6][5], [7][3], [7][4], [7][5], [8][3], [8][4], [8][5]]
#   [[6][6], [6][7], [6][8], [7][6], [7][7], [7][8], [8][6], [8][7], [8][8]]
# =============================================================================
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

# def make_random_board():
#     # Work in progress
#     # Makes a solved board
#     board = [[(i + j) % 9 for i in range(9)] for j in range(9)]
#     # board = [[8, 2, 7, 1, 5, 4, 3, 9, 6],
#     #          [9, 6, 5, 3, 2, 7, 1, 4, 8],
#     #          [3, 4, 1, 6, 8, 9, 7, 5, 2],
#     #          [5, 9, 3, 4, 6, 8, 2, 7, 1],
#     #          [4, 7, 2, 5, 1, 3, 6, 8, 9],
#     #          [6, 1, 8, 9, 7, 2, 4, 3, 5],
#     #          [7, 8, 6, 2, 3, 5, 9, 1, 4],
#     #          [1, 5, 4, 7, 9, 6, 8, 2, 3],
#     #          [2, 3, 9, 8, 4, 1, 5, 6, 7]]
#     for vrow, row in enumerate(board):
#         for vcol, col in enumerate(row):
#             print(board[vrow], [board[row][vcol] for row in range(9)])
#             print(vrow, vcol, board[vrow][vcol], (vrow % 3), (vcol // 3))
            
    return board


valid_sudoku_board = [[8, 2, 7, 1, 5, 4, 3, 9, 6],
                      [9, 6, 5, 3, 2, 7, 1, 4, 8],
                      [3, 4, 1, 6, 8, 9, 7, 5, 2],
                      [5, 9, 3, 4, 6, 8, 2, 7, 1],
                      [4, 7, 2, 5, 1, 3, 6, 8, 9],
                      [6, 1, 8, 9, 7, 2, 4, 3, 5],
                      [7, 8, 6, 2, 3, 5, 9, 1, 4],
                      [1, 5, 4, 7, 9, 6, 8, 2, 3],
                      [2, 3, 9, 8, 4, 1, 5, 6, 7]]


board_reader(valid_sudoku_board)
print(board_checker(valid_sudoku_board))
# print(board_checker(make_random_board()))
