import random
import pygame
import math
import sys
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
show_solution = False
text_rect_solution = pygame.Rect(0, 0, 0, 0)

pygame_icon = pygame.image.load('Smaller_Ean.png')
pygame.display.set_icon(pygame_icon)


def main():
    global SQUARE_DIMENSION
    global size
    global text_rect_solution
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

    def solution(scale):
        global show_solution
        font_size = int(.4 * scale)
        my_font = pygame.font.SysFont('Comic Sans MS', font_size)
        if not show_solution:
            show_solution = True
            # Displaying grid numbers
            for i in range(0, size):
                for j in range(0, size):
                    pos_1, pos_2 = 2 * scale * (j+.75), 2 * scale * (i+.75)
                    value = my_font.render(str(grid[i][j]), True, (0, 0, 0))
                    win.blit(value, value.get_rect(center=(pos_1, pos_2)))
        else:
            show_solution = False
            # Hiding grid numbers
            for i in range(0, size):
                for j in range(0, size):
                    pygame.draw.rect(win, background_color,
                                     (2 * scale * (i + .53), 2 * scale * (j + .53), scale * .9, scale * .9))


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

    def highlight_cell(window, position, color, buffer):
        pygame.draw.rect(window, color, (buffer * (20 * position[0] + 11), buffer * (20 * position[1] + 11),
                                         8 * buffer, 8 * buffer), int(buffer * .6))
        pygame.display.update()

    def insert(window, position, buffer):
        pass

    def draw_grid(scale):
        global text_rect_solution
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

        # Drawing Solution Button
        button_font = pygame.font.SysFont('Comic Sans MS', int(SCALE * .5))
        text_surface_solution = button_font.render("Show/Hide Solution", True, (0, 0, 0))
        position = (SQUARE_DIMENSION / 2, SCALE / 2)
        text_rect_solution = text_surface_solution.get_rect(center=position)
        pygame.draw.rect(win, (0, 0, 0), text_rect_solution, 1)
        win.blit(text_surface_solution, text_rect_solution)


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

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                cell = ((mouse_pos[0] // SCALE - 1) / 2, (mouse_pos[1] // SCALE - 1) / 2)
                if ((int(cell[0]) == cell[0] and int(cell[1]) == cell[1])
                        and cell[0] < size and cell[1] < size):
                    print(cell)
                    highlight_cell(win, cell, (255, 0, 0), .1 * SCALE)
                if text_rect_solution.collidepoint(mouse_pos):
                    solution(SCALE)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()


# main()
