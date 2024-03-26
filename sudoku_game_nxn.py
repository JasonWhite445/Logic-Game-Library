import pygame
import time

import Sudoku

grid = None
# WIDTH = 550
# HEIGHT = 550
background_color = (255, 255, 255)
original_grid_element_color = (91, 114, 138)
buffer = 5
timer_on = True
BLACK = (0, 0, 0)

# input will eventually come from make_random_board function
# grid = Sudoku.generate_hard_board()

# Check if the board is a valid solution
def board_checker(board):
    width, height, size = characteristics(board)
    numbers = [i+1 for i in range(size)]
    for row in range(size):
        if sorted(board[row]) != numbers:
            return False
    for col in range(size):
        if sorted([board[i][col] for i in range(size)]) != numbers:
            return False
    for box in range(size):
        if sorted([board[pos // width + box // height * height][pos % width + box % height * width] for pos in range(size)]) != numbers:
            return False
    return True


def characteristics(board):
    size = len(board)
    if int(size ** (1 / 2)) == size ** (1 / 2):
        # For boards of size 4x4 and 9x9
        box_height, box_width = int(size ** (1 / 2)), int(size ** (1 / 2))
    else:
        # For boards of size 6x6 and 8x8
        box_height, box_width = 2, int(size / 2)
    return box_width, box_height, size


def highlight_cell(win, position, color):
    pygame.draw.rect(win, color, (
        position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer), 3)
    pygame.display.update()


def launch_win_screen(win):
    win.fill(background_color)
    font = pygame.font.SysFont('Comic Sans MS', 40)
    text = font.render('You Win!', True, (0, 0, 255))
    win.blit(text, (50, 250))
    global timer_on
    timer_on = False
    pygame.display.update()


# https://github.com/PiyushG14/Pygame-sudoku - API based Sudoku board, very helpful in creating and reading inputs
# inserting numbers into grid
def insert(win, position, givens):
    grid_given = givens
    i, j = position[1], position[0]
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if position in grid_given:
                    return
                if event.key == 48 or event.key == 8:  # checking if space is 0, will return blank
                    grid[i - 1][j - 1] = 0
                    pygame.draw.rect(win, background_color, (
                        position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    highlight_cell(win, position, (255, 255, 255))
                    # print_grid(grid)  # Print the updated grid
                    if board_checker(grid):
                        launch_win_screen(win)
                    return

                if 0 < event.key - 48 < len(grid) + 1:  # checking for valid input
                    pygame.draw.rect(win, background_color, (
                        position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    value = myfont.render(str(event.key - 48), True, (0, 0, 0))
                    win.blit(value, (position[0] * 50 + 15, position[1] * 50))
                    grid[i - 1][j - 1] = event.key - 48
                    highlight_cell(win, position, (255, 255, 255))
                    # print_grid(grid)  # Print the updated grid
                    if board_checker(grid):
                        launch_win_screen(win)
                    return
                else:
                    highlight_cell(win, position, (255, 255, 255))
                return


def get_given_indexes(board):
    indexes = []
    for y, row in enumerate(board):
        for x, i in enumerate(row):
            if i != 0:
                indexes.append((x+1, y+1))
    return indexes

# prints board for debugging
def print_grid(grid):
    for row in grid:
        print(row)
    print("\n")


def sudoku_nxn_main():
    grid_given = get_given_indexes(grid)
    width, height, size = characteristics(grid)
    pygame.init()
    win = pygame.display.set_mode((50 * (size + 2), 50 * (size + 2)))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    myfontsmall = pygame.font.SysFont('Comic Sans MS', 25)
    bottomright = ((25 * (size + 2)), (25 * (size + 2)) + 25*(size) + 25)
    difficulty = Sudoku.difficulty_sum(grid)

    difficulty_sum = round(difficulty / 729, 2)
    print(difficulty_sum)

    if difficulty_sum <= .25:
        level = "Easy"
        difficulty_level = myfontsmall.render("Difficulty: " + level, True, BLACK)
        difficulty_rect_done = difficulty_level.get_rect(center=bottomright)
        win.blit(difficulty_level, difficulty_rect_done)
    elif .38 > difficulty_sum > .25:
        level = "Medium"
        difficulty_level = myfontsmall.render("Difficulty: " + level, True, BLACK)
        difficulty_rect_done = difficulty_level.get_rect(center=bottomright)
        win.blit(difficulty_level, difficulty_rect_done)
    elif 1 > difficulty_sum >= .38:
        level = "Hard"
        difficulty_level = myfontsmall.render("Difficulty: " + level, True, BLACK)
        difficulty_rect_done = difficulty_level.get_rect(center=bottomright)
        win.blit(difficulty_level, difficulty_rect_done)
    else:
        pass

    #pygame.draw.rect(win, BLACK, difficulty_rect_done, 1)

    # Initialize timer
    start_time = time.time()

    # https://www.pygame.org/docs/ref/draw.html
    # Drawing gridlines
    for i in range(0, size + 1):
        # Drawing sub-grids thicker
        if i % width == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 50*(size+1)), 4)
        if i % height == 0:
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (50*(size+1), 50 + 50 * i), 4)

        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, (size+1)*50), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (50*(size+1), 50 + 50 * i), 2)
    pygame.display.update()

    # displaying initial grid values
    for i in range(0, size):
        for j in range(0, size):
            if 0 < grid[i][j] < size + 1:
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()

    while True:
        if timer_on:
            # Calculate elapsed time
            elapsed_time = time.time() - start_time

            # Clear previous timer text
            pygame.draw.rect(win, background_color,
                             (25*size, 0, 25 * (size + 2), 40))

            # Display timer
            timer_text = myfont.render(f"Time: {elapsed_time:.0f}", True, (0, 0, 0))
            win.blit(timer_text, (25 * size, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos[0] // 50, pos[1] // 50)   # prints position for debugging
                selected_cell = (pos[0] // 50, pos[1] // 50)  # Update selected cell position
                if (((pos[0] // 50) >= 1) and ((pos[0] // 50) <= size)) and (((pos[1] // 50) >= 1) and ((pos[1] // 50) <= size)):
                    if selected_cell not in grid_given:
                        highlight_cell(win, selected_cell, (255, 0, 0))
                # Ensures insert is in range of the grid
                if (((pos[0] // 50) >= 1) and ((pos[0] // 50) <= size)) and (((pos[1] // 50) >= 1) and ((pos[1] // 50) <= size)):
                    insert(win, (pos[0] // 50, pos[1] // 50), grid_given)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

            if event.type == pygame.QUIT:
                return
        pygame.display.update()

# sudoku_nxn_main()