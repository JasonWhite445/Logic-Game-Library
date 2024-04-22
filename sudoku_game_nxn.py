import copy
import sys
import pygame
import time
# import Sudoku

grid = []
won = False
size = len(grid)
difficulty = ""
# WIDTH = 550
# HEIGHT = 550
background_color = (255, 255, 255)
original_grid_element_color = (91, 114, 138)
timer_on = True
BLACK = (0, 0, 0)
SQUARE_DIMENSION = 0

# input will eventually come from make_random_board function
# grid = Sudoku.generate_hard_board()

# Check if the board is a valid solution
def board_checker(board):
    global size
    width, height, size = characteristics(board)
    numbers = [i+1 for i in range(size)]
    for row in range(size):
        if sorted(board[row]) != numbers:
            return False
    for col in range(size):
        if sorted([board[i][col] for i in range(size)]) != numbers:
            return False
    for box in range(size):
        if sorted([board[pos // width + box // height * height][pos % width + box % height * width]
                   for pos in range(size)]) != numbers:
            return False
    return True


def characteristics(board):
    grid_size = len(board)
    if int(grid_size ** (1 / 2)) == grid_size ** (1 / 2):
        # For boards of size 4x4 and 9x9
        box_height, box_width = int(grid_size ** (1 / 2)), int(grid_size ** (1 / 2))
    else:
        # For boards of size 6x6 and 8x8
        box_height, box_width = 2, int(grid_size / 2)
    return box_width, box_height, grid_size


def highlight_cell(win, position, color, buffer):
    pygame.draw.rect(win, color,
                     (buffer * (10 * position[0] + 1), buffer * (10 * position[1] + 1),
                      8 * buffer, 8 * buffer), int(buffer * .6))
    pygame.display.update()


def launch_win_screen(win):
    global won
    won = True
    SCALE = SQUARE_DIMENSION / (size+2)
    win.fill(background_color)
    font = pygame.font.SysFont('Comic Sans MS', int(SCALE))
    image = pygame.image.load('./Smaller_Ean.png')
    image = pygame.transform.scale(image, (SQUARE_DIMENSION * .85, SQUARE_DIMENSION * .85))
    text = font.render('You Win!', True, (0, 0, 0))
    text_rect = text.get_rect(center=(SQUARE_DIMENSION // 2, SCALE // 2))

    win.blit(text, text_rect)
    win.blit(image, (SCALE, SCALE))
    global timer_on
    timer_on = False
    pygame.display.update()


# https://github.com/PiyushG14/Pygame-sudoku - API based Sudoku board, very helpful in creating and reading inputs
# inserting numbers into grid
def insert(win, position, buffer):
    i, j = position[1], position[0]
    myfont = pygame.font.SysFont('Comic Sans MS', int(7 * buffer))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == 48 or event.key == 8:  # checking if space is 0, will return blank
                    grid[i - 1][j - 1] = 0
                    pygame.draw.rect(win, background_color, (
                        buffer * (10 * position[0] + 1), buffer * (10 * position[1] + 1), 8 * buffer, 8 * buffer))
                    highlight_cell(win, position, (255, 255, 255), buffer)
                    # print_grid(grid)  # Print the updated grid
                if 0 < event.key - 48 < len(grid) + 1:  # checking for valid input
                    pygame.draw.rect(win, background_color, (
                        buffer * (10 * position[0] + 1), buffer * (10 * position[1] + 1), 8 * buffer, 8 * buffer))
                    value = myfont.render(str(event.key - 48), True, (0, 0, 0))
                    win.blit(value, (10 * buffer * (position[0] + .3), 10 * buffer * position[1]))
                    grid[i - 1][j - 1] = event.key - 48
                    highlight_cell(win, position, (255, 255, 255), buffer)
                    # print_grid(grid)  # Print the updated grid
                    if board_checker(grid):
                        launch_win_screen(win)
                    return
                else:
                    highlight_cell(win, position, (255, 255, 255), buffer)
                return


def get_given_indexes(board):
    indexes = []
    for y, row in enumerate(board):
        for x, i in enumerate(row):
            if i != 0:
                indexes.append((x+1, y+1))
    return indexes

# prints board for debugging
def print_grid(board):
    for row in board:
        print(row)
    print("\n")


def sudoku_nxn_main():
    global SQUARE_DIMENSION
    global size
    grid_given = get_given_indexes(grid)
    original = copy.deepcopy(grid)
    width, height, size = characteristics(grid)
    SCALE = SQUARE_DIMENSION / (size+2)
    pygame.init()
    win = pygame.display.set_mode((SQUARE_DIMENSION, SQUARE_DIMENSION), pygame.RESIZABLE)
    pygame.display.set_caption(f"{size}x{size} sudoku")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', int(0.7 * SCALE))
    myfontsmall = pygame.font.SysFont('Comic Sans MS', int(0.5 * SCALE))
    bottomright = ((SCALE / 2 * (size + 2)), (SCALE * (size + 1.5)))

    difficulty_level = myfontsmall.render("Difficulty: " + difficulty, True, BLACK)
    difficulty_rect_done = difficulty_level.get_rect(center=bottomright)
    win.blit(difficulty_level, difficulty_rect_done)

    # Initialize timer
    start_time = time.time()

    def draw_gridlines(givens):
        # https://www.pygame.org/docs/ref/draw.html
        # Drawing gridlines
        for i in range(0, size + 1):
            # Drawing sub-grids thicker
            if i % width == 0:
                pygame.draw.line(win, (0, 0, 0), (SCALE * (i + 1), SCALE),
                                 (SCALE * (i + 1), SCALE * (size+1)), 4)
            if i % height == 0:
                pygame.draw.line(win, (0, 0, 0), (SCALE, SCALE * (i + 1)),
                                 (SCALE * (size+1), SCALE * (i + 1)), 4)
            pygame.draw.line(win, (0, 0, 0), (SCALE * (i + 1), SCALE),
                             (SCALE * (i + 1), SCALE * (size+1)), 2)
            pygame.draw.line(win, (0, 0, 0), (SCALE, SCALE * (i + 1)),
                             (SCALE * (size + 1), SCALE * (i + 1)), 2)
        # pygame.display.update()
        # displaying initial grid values
        for i in range(0, size):
            for j in range(0, size):
                if 0 < grid[i][j] < size + 1:
                    value = myfont.render(str(grid[i][j]), True, BLACK)
                    win.blit(value, ((j + 1.3) * SCALE, (i + 1) * SCALE))
                if 0 < givens[i][j] < size + 1:
                    value = myfont.render(str(givens[i][j]), True, original_grid_element_color)
                    win.blit(value, ((j + 1.3) * SCALE, (i + 1) * SCALE))
        pygame.display.update()

    draw_gridlines(original)

    while True:
        if timer_on:
            # Calculate elapsed time
            elapsed_time = time.time() - start_time

            # Clear previous timer text
            pygame.draw.rect(win, background_color,
                             (0, 0, SQUARE_DIMENSION, 0.84 * SCALE))

            # Display timer
            timer_text = myfont.render(f"Time: {elapsed_time:.0f}", True, (0, 0, 0))
            win.blit(timer_text, timer_text.get_rect(center=(SQUARE_DIMENSION / 2, SCALE / 2)))

        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                # Calculate the new size while keeping the aspect ratio square
                if event.w == SQUARE_DIMENSION:
                    SQUARE_DIMENSION = event.h
                elif event.h == SQUARE_DIMENSION:
                    SQUARE_DIMENSION = event.w
                else:
                    SQUARE_DIMENSION = max(event.w, event.h)
                SCALE = SQUARE_DIMENSION / (size + 2)
                win = pygame.display.set_mode((SQUARE_DIMENSION, SQUARE_DIMENSION), pygame.RESIZABLE)
                if won:
                    launch_win_screen(win)
                else:
                    win.fill(background_color)
                    myfont = pygame.font.SysFont('Comic Sans MS', int(0.7 * SCALE))
                    myfontsmall = pygame.font.SysFont('Comic Sans MS', int(0.5 * SCALE))
                    bottomright = ((SCALE / 2 * (size + 2)), (SCALE * (size + 1.5)))
                    difficulty_level = myfontsmall.render("Difficulty: " + difficulty, True, BLACK)
                    difficulty_rect_done = difficulty_level.get_rect(center=bottomright)
                    win.blit(difficulty_level, difficulty_rect_done)
                    draw_gridlines(original)


            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                # print(pos[0] // 50, pos[1] // 50)   # prints position for debugging
                selected_cell = (pos[0] // SCALE, pos[1] // SCALE)  # Update selected cell position
                if ((((pos[0] // SCALE) >= 1)
                     and ((pos[0] // SCALE) <= size))
                        and (((pos[1] // SCALE) >= 1)
                             and ((pos[1] // SCALE) <= size))):
                    if selected_cell not in grid_given:
                        highlight_cell(win, selected_cell, (255, 0, 0), 0.1 * SCALE)
                        insert(win, (pos[0] // int(SCALE), pos[1] // int(SCALE)), 0.1 * SCALE)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.display.set_caption("Make Your Choice")
                return

            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

# sudoku_nxn_main()
