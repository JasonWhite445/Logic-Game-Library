import random
import pygame
pygame.init()

"""
WORKS IN PROGRESS

-Edit the way operators are added
    Should be possible to get a / b * c where a / b is not an int
-Scale the answers before they get drawn in their cells
-Empty cells in main grid should be black
-Show/Hide solution button needed at some point
-Make more selection screens like Sudoku
"""

background_color = (255, 255, 255)
original_grid_element_color = (91, 114, 138)
myfont = pygame.font.SysFont('Comic Sans MS', 35)
pygame_icon = pygame.image.load('Smaller_Ean.png')
pygame.display.set_icon(pygame_icon)
# Size will be changed later to be user input
size = 4
# width, height = 3, 3
nums = [i+1 for i in range(size**2)]
random.shuffle(nums)
# Grid is a random array of the numbers from 1 to size^2
grid = [nums[size*i:size*(i+1)] for i in range(size)]
print(grid)
operators = ['+', '-', '*', '/']
row_operators, col_operators = [], []
answers = []
# operators_easy = ['+', '-', '*']
# # n rows of n-1 operators
# row_operators = [[random.choice(operators) for _ in range(size-1)]for _ in range(size)]
# # n-1 rows of n operators
# col_operators = [[random.choice(operators) for _ in range(size)]for _ in range(size-1)]
# print(grid)
# print(row_operators)
# print(col_operators)
#
# # These two loops can make the equations and evaluate them
# # Need to modify so that we only get integer outputs
# bad = []  # Used for testing
# for r in range(size):
#     temp = ''
#     for n in range(size-1):
#         temp += f"{grid[r][n]}{row_operators[r][n]}"
#     temp += f"{grid[r][-1]}"
#     if eval(temp) != int(eval(temp)):
#         bad.append(f"Row {r+1}")
#     print(f"{temp} = {eval(temp)}")
# for c in range(size):
#     temp = ''
#     for n in range(size-1):
#         temp += f"{grid[n][c]}{col_operators[n][c]}"
#     temp += f"{grid[-1][c]}"
#     if eval(temp) != int(eval(temp)):
#         bad.append(f"Column {c+1}")
#     print(f"{temp} = {eval(temp)}")
# print(bad)
def main():
    for r in range(size):
        row_signs = []
        temp = f'{grid[r][0]}'
        n = 0
        while n < size-1:
            temp_op = random.choice(operators)
            new = f'{temp_op}{grid[r][n+1]}'
            if eval(temp+new) == int(eval(temp+new)):
                if temp_op == '/':
                    temp_op = chr(247)
                elif temp_op == '*':
                    temp_op = chr(215)
                row_signs += temp_op
                temp += new
                n += 1
        row_operators.append(row_signs)
        answers.append(int(eval(temp)))
        print(f'{temp} = {int(eval(temp))}')
        print(row_signs)

    for r in range(size):
        col_signs = []
        temp = f'{grid[0][r]}'
        n = 0
        while n < size-1:
            temp_op = random.choice(operators)
            new = f'{temp_op}{grid[n+1][r]}'
            if eval(temp+new) == int(eval(temp+new)):
                if temp_op == '/':
                    temp_op = chr(247)
                elif temp_op == '*':
                    temp_op = chr(215)
                col_signs += temp_op
                temp += new
                n += 1
        col_operators.append(col_signs)
        answers.append(int(eval(temp)))
        print(f'{temp} = {int(eval(temp))}')
        print(col_signs)

    print(row_operators, col_operators)
    print(answers)
    win = pygame.display.set_mode((100 * (size + 1.25), 100 * (size + 1.25)))
    pygame.display.set_caption(f"{size}x{size} Math Square")
    win.fill(background_color)

    # Drawing empty grid
    for i in range(0, 2 * size):
        # Main Grid
        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, size*100), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (100*size, 50 + 50 * i), 2)
        # Answer Cells
        pygame.draw.line(win, (0, 0, 0),
                         (100 * (size + 0.25), 50 + 50 * i),
                         (100 * (size + 0.75), 50 + 50 * i), 2)
        pygame.draw.line(win, (0, 0, 0),
                         (50 + 50 * i, 100 * (size + 0.25)),
                         (50 + 50 * i, 100 * (size + 0.75)), 2)
        pygame.draw.line(win, (0, 0, 0),
                         (100 * (size + 0.25) + 50 * (i // size), 50 + 100 * (i % size)),
                         (100 * (size + 0.25) + 50 * (i // size), 100 + 100 * (i % size)), 2)
        pygame.draw.line(win, (0, 0, 0),
                         (50 + 100 * (i % size), 100 * (size + 0.25) + 50 * (i // size)),
                         (100 + 100 * (i % size), 100 * (size + 0.25) + 50 * (i // size)), 2)
    for i in range(0, (size - 1)**2):
        pygame.draw.rect(win, (0, 0, 0),
                         (100 + 100 * (i // (size - 1)), 100 + 100 * (i % (size - 1)), 50, 50))
        pass

    # Displaying Solution
    for i in range(0, size):
        for j in range(0, size):
            value = myfont.render(str(grid[i][j]), True, (0, 0, 0))
            if grid[i][j] < 10:
                win.blit(value, ((j + 0.65) * 100, (i + 0.5) * 100))
            else:
                win.blit(value, ((j + 0.575) * 100, (i + 0.5) * 100))

    # Displaying grid operators
    for i in range(0, size):
        for j in range(0, size - 1):
            row_op = myfont.render(row_operators[i][j], True, (0, 0, 0))
            col_op = myfont.render(col_operators[i][j], True, (0, 0, 0))
            win.blit(row_op, ((j + 1.15) * 100, (i + 0.5) * 100))
            win.blit(col_op, ((i + 0.65) * 100, (j + 1) * 100))
    pygame.display.update()

    while True:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

            if event.type == pygame.QUIT:
                return
        pygame.display.update()

main()
