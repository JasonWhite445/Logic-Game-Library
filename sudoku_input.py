import copy
import sudoku_game_nxn
import pygame
import Sudoku

grid = []
solver = False
# WIDTH = 550
# HEIGHT = 550
background_color = (255, 255, 255)
original_grid_element_color = (91, 114, 138)
timer_on = False
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (217, 247, 250)
SQUARE_DIMENSION = 0

# Create font objects

# Check if the board is a valid solution
def board_checker(board):
    width, height, size = characteristics(board)
    # numbers = [i+1 for i in range(size)]
    for row in range(size):
        full_row = [i for i in board[row] if i != 0]
        if sorted(full_row) != sorted(list(set(full_row))):
            return False
    for col in range(size):
        full_column = [board[i][col] for i in range(size) if board[i][col] != 0]
        if sorted(full_column) != sorted(list(set(full_column))):
            return False
    for box in range(size):
        full_box = [board[pos // width + box // height * height][pos % width + box % height * width]
                    for pos in range(size)
                    if board[pos // width + box // height * height][pos % width + box % height * width] != 0]
        if sorted(full_box) != sorted(list(set(full_box))):
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


def highlight_cell(win, position, color, buffer):
    pygame.draw.rect(win, color, (buffer * (10 * position[0] + 1), buffer * (10 * position[1] + 1),
                                  8 * buffer, 8 * buffer), int(buffer * .6))
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
                    pygame.display.update()
                    # print_grid(grid)  # Print the updated grid
                    return

                if 0 < event.key - 48 < len(grid) + 1:  # checking for valid input
                    pygame.draw.rect(win, background_color, (
                        buffer * (10 * position[0] + 1), buffer * (10 * position[1] + 1), 8 * buffer, 8 * buffer))
                    value = myfont.render(str(event.key - 48), True, (0, 0, 0))
                    win.blit(value, (10 * buffer * (position[0] + .3), 10 * buffer * position[1]))
                    grid[i - 1][j - 1] = event.key - 48
                    highlight_cell(win, position, (255, 255, 255), buffer)
                    pygame.display.update()
                    # print_grid(grid)  # Print the updated grid
                else:
                    highlight_cell(win, position, (255, 255, 255), buffer)
                return


# prints board for debugging

def print_grid(board):
    for row in board:
        print(row)
    print("\n")


def sudoku_manual_main():
    global SQUARE_DIMENSION
    width, height, size = characteristics(grid)
    SCALE = SQUARE_DIMENSION / (size+2)
    pygame.init()
    win = pygame.display.set_mode((SQUARE_DIMENSION, SQUARE_DIMENSION), pygame.RESIZABLE)
    pygame.display.set_caption("Manual Input")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', int(.7 * SCALE))
    # mysmallfont = pygame.font.SysFont('Comic Sans MS', 25)

    text_finished = myfont.render("Done", True, BLACK)

    text_rect_done = text_finished.get_rect(center=(SQUARE_DIMENSION / 2, SCALE / 2))
    win.blit(text_finished, text_rect_done)
    pygame.draw.rect(win, BLACK, text_rect_done, 1)

    def send_manual_grid():
        if solver:  # Prints a solution to the board the user input
            for i in range(0, size):
                for j in range(0, size):
                    if grid[i][j] == 0:
                        pygame.draw.rect(win, (255, 255, 255),
                                         ((j + 1.1) * SCALE, (i + 1.1) * SCALE,
                                          0.8 * SCALE, 0.8 * SCALE), int(SCALE / 2))
                        pos_value = myfont.render(str(solution[i][j]), False, original_grid_element_color)
                        win.blit(pos_value, ((j + 1.3) * SCALE, (i + 1) * SCALE))
            pygame.display.update()
        else:  # Sends user to screen where they can try to solve their input
            difficulty_percent = round(Sudoku.difficulty_sum(grid) / (len(grid)**3), 2)
            if difficulty_percent <= .25:
                difficulty = "Easy"
            elif .38 > difficulty_percent > .25:
                difficulty = "Medium"
            else:
                difficulty = "Hard"
            sudoku_game_nxn.difficulty = difficulty
            win.blit(text_finished, text_rect_done)
            pygame.draw.rect(win, BLACK, text_rect_done, 1)
            sudoku_game_nxn.grid = grid
            sudoku_game_nxn.sudoku_nxn_main()

    def draw_gridlines():
        # https://www.pygame.org/docs/ref/draw.html
        # Drawing gridlines
        for i in range(0, size + 1):
            # Drawing sub-grids thicker
            if i % width == 0:
                pygame.draw.line(win, (0, 0, 0),
                                 (SCALE * (i + 1), SCALE), (SCALE * (i + 1), SCALE * (size + 1)), 4)
            if i % height == 0:
                pygame.draw.line(win, (0, 0, 0),
                                 (SCALE, SCALE * (i + 1)), (SCALE * (size + 1), SCALE * (i + 1)), 4)

            pygame.draw.line(win, (0, 0, 0),
                             (SCALE * (i + 1), SCALE), (SCALE * (i + 1), (size + 1) * SCALE), 2)
            pygame.draw.line(win, (0, 0, 0),
                             (SCALE, SCALE * (i + 1)), (SCALE * (size + 1), SCALE * (i + 1)), 2)
        pygame.display.update()

        # displaying grid values
        for i in range(0, size):
            for j in range(0, size):
                if 0 < grid[i][j] < size + 1:
                    value = myfont.render(str(grid[i][j]), False, BLACK)
                    win.blit(value, ((j + 1.3) * SCALE, (i + 1) * SCALE))
        pygame.draw.rect(win, background_color,
                         (0, SCALE * (size + 1.1), SCALE * (size + 2), 42))
        pygame.display.update()

    draw_gridlines()

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
                SCALE = SQUARE_DIMENSION / (size + 2)
                win = pygame.display.set_mode((SQUARE_DIMENSION, SQUARE_DIMENSION), pygame.RESIZABLE)
                win.fill(background_color)
                myfont = pygame.font.SysFont('Comic Sans MS', int(.7 * SCALE))
                text_finished = myfont.render("Done", True, BLACK)
                text_rect_done = text_finished.get_rect(center=(SQUARE_DIMENSION / 2, SCALE / 2))
                win.blit(text_finished, text_rect_done)
                pygame.draw.rect(win, BLACK, text_rect_done, 1)
                draw_gridlines()

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                # print(pos[0] // 50, pos[1] // 50)   # prints position for debugging
                selected_cell = (pos[0] // SCALE, pos[1] // SCALE)  # Update selected cell position
                # Ensures insert is in range of the grid
                if ((((pos[0] // SCALE) >= 1)
                    and ((pos[0] // SCALE) <= size))
                        and (((pos[1] // SCALE) >= 1)
                             and ((pos[1] // SCALE) <= size))):
                    draw_gridlines()
                    highlight_cell(win, selected_cell, (255, 0, 0), .1 * SCALE)
                    insert(win, (pos[0] // int(SCALE), pos[1] // int(SCALE)), .1 * SCALE)

                else:
                    mouse_pos = pygame.mouse.get_pos()
                    if text_rect_done.collidepoint(mouse_pos):
                        if not board_checker(grid):
                            # Tells the user there is no solution to their board
                            text_bad = myfont.render("No Solution", True, RED)
                            text_rect_bad = text_bad.get_rect(
                                center=(SQUARE_DIMENSION / 2, SQUARE_DIMENSION - SCALE / 2))
                            win.blit(text_bad, text_rect_bad)
                        else:  # Ordered this way because Sudoku.fill_board can sometimes take a while
                            solution = Sudoku.fill_board(copy.deepcopy(grid))
                            if solution:
                                send_manual_grid()
                            else:
                                # Tells the user there is no solution to their board
                                text_bad = myfont.render("No Solution", True, RED)
                                text_rect_bad = text_bad.get_rect(
                                    center=(SQUARE_DIMENSION / 2, SQUARE_DIMENSION - SCALE / 2))
                                win.blit(text_bad, text_rect_bad)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

            if event.type == pygame.QUIT:
                return
        pygame.display.update()

# sudoku_manual_main()







