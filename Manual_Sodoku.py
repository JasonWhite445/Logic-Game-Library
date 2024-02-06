"""
This is the beginning code for a manually inputed sododku
The goal is to for a user to input a 3x3, 9x9, 15x15 sodoku
row by row

WIP
"""
import numpy as np


def get_matrix_size(size):

    if size.__eq__("3x3") or size.__eq__("9x9"):
        return size[0]
    else:
        return size[0:2]

def acceptable_sodoku(user_input):

    if user_input.__eq__("3x3") or user_input.__eq__("9x9") or user_input.__eq__("15x15"):
        return True
    else:
        return False

def contains_negative_number(input_row):
    for x in input_row:
        if x < 0:
            return True
    return False

def exceeds_row_size(input_row):
    for x in input_row:
        if x > len(input_row):
            return True
    return False


def Sodoku_Construction():
    Rows = int(get_matrix_size(sodoku_size))
    Sodoku_Matrix = []
    print("Input rows until sodoku is complete.")
    for i in range(Rows):
        row_input = list(map(int, input().split()))
        if len(row_input) != Rows or contains_negative_number(row_input) or exceeds_row_size(row_input):
            unacceptable_row = True
            while unacceptable_row:
                print("That was not an acceptable row size, please try again")
                row_input = list(map(int, input().split()))
                negative_number = contains_negative_number(row_input)
                exceed_limit = exceeds_row_size(row_input)
                if len(row_input) == Rows and not negative_number and not exceed_limit:
                    unacceptable_row = False
        Sodoku_Matrix.append(row_input)
    return Sodoku_Matrix


user_decision = True

print("Hello! I hear that you want to make a sodoku\n"
      "we are currently offering 3x3, 9x9, 15x15 versions")

sodoku_size = input("Input your size please:")

while user_decision:
    if not acceptable_sodoku(sodoku_size):
        sodoku_size = input("That is not an acceptable sodoku, try again: ")
    else:
        print("Thank you for inputing that you want a " + sodoku_size +
              " sodoku we are going to now fill it in.")
        user_decision = False

finished_matrix = Sodoku_Construction()

for i in finished_matrix:
    print(str(i))







