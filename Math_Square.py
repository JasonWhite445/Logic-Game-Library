import random
import pygame
import math
pygame.init()

"""
WORKS IN PROGRESS

-Edit the way operators are added
    Should be possible to get a / b * c where a / b is not an int
-Show/Hide solution button needed at some point
-Make more selection screens like Sudoku
"""

# Size will be changed later to be user input
size = 0
SQUARE_DIMENSION = 0
background_color = (255, 255, 255)
original_grid_element_color = (91, 114, 138)

pygame_icon = pygame.image.load('Smaller_Ean.png')
pygame.display.set_icon(pygame_icon)


# print(grid)


def main():
    global SQUARE_DIMENSION
    global size
    SCALE = round(SQUARE_DIMENSION / (2 * (size + 1.25)), 3)
    nums = [i + 1 for i in range(size ** 2)]
    random.shuffle(nums)
    # Grid is a random array of the numbers from 1 to size^2
    grid = [nums[size*i:size*(i+1)] for i in range(size)]
    operators = ['+', '-', '*', '/']
    row_operators, col_operators = [], []
    answers = []
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
        # print(f'{temp} = {int(eval(temp))}')
        # print(row_signs)

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
        # print(f'{temp} = {int(eval(temp))}')
        # print(col_signs)

    win = pygame.display.set_mode((SQUARE_DIMENSION, SQUARE_DIMENSION), pygame.RESIZABLE)
    pygame.display.set_caption(f"{size}x{size} Math Square")
    win.fill(background_color)

    def draw_grid(scale):
        font_size = int(.4 * scale)
        my_font = pygame.font.SysFont('Comic Sans MS', font_size)
        my_op_font = pygame.font.SysFont('Comic Sans Ms', int(.6 * scale))
        win.fill(background_color)
        # Drawing empty grid
        for i in range(0, 2 * size):
            # Main Grid
            pygame.draw.line(win, (0, 0, 0),
                             (scale * (i + 1), scale),
                             (scale * (i + 1), 2 * scale * size), 2)
            pygame.draw.line(win, (0, 0, 0),
                             (scale, scale * (i + 1)),
                             (2 * scale * size, scale * (i + 1)), 2)
            # Answer Cells
            pygame.draw.line(win, (0, 0, 0),
                             (2 * scale * (size + 0.25), scale * (i + 1)),
                             (2 * scale * (size + 0.75), scale * (i + 1)), 2)
            pygame.draw.line(win, (0, 0, 0),
                             (scale * (i + 1), 2 * scale * (size + 0.25)),
                             (scale * (i + 1), 2 * scale * (size + 0.75)), 2)
            pygame.draw.line(win, (0, 0, 0),
                             (2 * scale * (size + 0.25) + scale * (i // size), scale * (1 + 2 * (i % size))),
                             (2 * scale * (size + 0.25) + scale * (i // size), 2 * scale * (1 + (i % size))), 2)
            pygame.draw.line(win, (0, 0, 0),
                             (scale * (1 + 2 * (i % size)), 2 * scale * (size + 0.25) + scale * (i // size)),
                             (2 * scale * (1 + (i % size)), 2 * scale * (size + 0.25) + scale * (i // size)), 2)
        # Drawing black squares
        for i in range(0, (size - 1)**2):
            pygame.draw.rect(win, (0, 0, 0),
                             (2 * scale * ((i // (size - 1))+1) + 1,
                              2 * scale * ((i % (size - 1))+1) + 1,
                              scale, scale))
            pass

        # Displaying grid numbers - Only for testing
        for i in range(0, size):
            for j in range(0, size):
                pos_1, pos_2 = 2 * scale * (j+.75), 2 * scale * (i+.75)
                value = my_font.render(str(grid[i][j]), True, (0, 0, 0))
                win.blit(value, value.get_rect(center=(pos_1, pos_2)))

        # Displaying grid operators
        for i in range(0, size):
            for j in range(0, size - 1):
                x, y = 2 * scale * (j+1.25), 2 * scale * (i+.75)
                row_op = my_op_font.render(row_operators[i][j], True, (0, 0, 0))
                col_op = my_op_font.render(col_operators[i][j], True, (0, 0, 0))
                win.blit(row_op, row_op.get_rect(center=(x, y)))
                win.blit(col_op, col_op.get_rect(center=(y, x)))

        # Displaying answers
        for a in range(2*size):
            h, f = 2 * scale * (size + .5), 2 * scale * ((a % size) + .75)
            sol = my_font.render(str(answers[a]), True, (0, 0, 0))
            if sol.get_width() > .9 * scale:
                large = sol.get_width()
                ratio = large / (.9 * scale)
                new_font_size = math.floor(font_size / ratio)
                temp_font = pygame.font.SysFont('Comic Sans MS', new_font_size)
                sol = temp_font.render(str(answers[a]), True, (0, 0, 0))
            if a < size:
                win.blit(sol, sol.get_rect(center=(h, f)))
            else:
                win.blit(sol, sol.get_rect(center=(f, h)))
            pass

    draw_grid(SCALE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                # Calculate the new size while keeping the aspect ratio square
                if event.w == SQUARE_DIMENSION:
                    SQUARE_DIMENSION = event.h
                elif event.h == SQUARE_DIMENSION:
                    SQUARE_DIMENSION = event.w
                else:
                    SQUARE_DIMENSION = max(event.w, event.h)
                win = pygame.display.set_mode((SQUARE_DIMENSION, SQUARE_DIMENSION), pygame.RESIZABLE)
                SCALE = round(SQUARE_DIMENSION / (2 * (size + 1.25)), 3)
                draw_grid(SCALE)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

            if event.type == pygame.QUIT:
                return
        pygame.display.update()


# main()
