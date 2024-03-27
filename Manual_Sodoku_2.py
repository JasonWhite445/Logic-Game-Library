import sys
import sudoku_game9x9
import sudoku_game_nxn
import pygame
import time
import Sudoku

grid = None
WIDTH = 550
HEIGHT = 550
background_color = (255, 255, 255)
original_grid_element_color = (91, 114, 138)
buffer = 5
timer_on = False
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (217, 247, 250)

# Create font objects

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


# https://github.com/PiyushG14/Pygame-sudoku - API based Sudoku board, very helpful in creating and reading inputs
# inserting numbers into grid
def insert(win, position):
    i, j = position[1], position[0]
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == 48 or event.key == 8:  # checking if space is 0, will return blank
                    grid[i - 1][j - 1] = 0
                    pygame.draw.rect(win, background_color, (
                        position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    pygame.display.update()
                    # print_grid(grid)  # Print the updated grid
                    return

                if 0 < event.key - 48 < len(grid) + 1:  # checking for valid input
                    pygame.draw.rect(win, background_color, (
                        position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    value = myfont.render(str(event.key - 48), True, (0, 0, 0))
                    win.blit(value, (position[0] * 50 + 15, position[1] * 50))
                    grid[i - 1][j - 1] = event.key - 48
                    pygame.display.update()
                    # print_grid(grid)  # Print the updated grid
                else:
                    highlight_cell(win, position, (255, 255, 255))
                return


# prints board for debugging

def print_grid(grid):
    for row in grid:
        print(row)
    print("\n")


def sudoku_manual_main():
    width, height, size = characteristics(grid)
    pygame.init()
    win = pygame.display.set_mode((50 * (size + 2), 50 * (size + 2)))
    pygame.display.set_caption("Manual Sodoku")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    text_finished = myfont.render("Done", True, BLACK)
    print(text_finished)

    text_rect_done = text_finished.get_rect(center=(((size + 2)*25), 25))
    print(text_rect_done)
    win.blit(text_finished, text_rect_done)
    pygame.draw.rect(win, BLACK, text_rect_done, 1)

    def send_manual_grid():
        win.blit(text_finished, text_rect_done)
        pygame.draw.rect(win, BLACK, text_rect_done, 1)
        sudoku_game_nxn.grid = grid
        sudoku_game_nxn.sudoku_nxn_main()

    # https://www.pygame.org/docs/ref/draw.html
    # Drawing gridlines
    for i in range(0, size + 1):
        # Drawing sub-grids thicker
        if i % width == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 50 * (size + 1)), 4)
        if i % height == 0:
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (50 * (size + 1), 50 + 50 * i), 4)

        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, (size + 1) * 50), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (50 * (size + 1), 50 + 50 * i), 2)
    pygame.display.update()

    # displaying initial grid values
    for i in range(0, size):
        for j in range(0, size):
            if 0 < grid[i][j] < size + 1:
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos[0] // 50, pos[1] // 50)   # prints position for debugging
                selected_cell = (pos[0] // 50, pos[1] // 50)  # Update selected cell position

                # Ensures insert is in range of the grid
                if (((pos[0] // 50) >= 1) and ((pos[0] // 50) <= 9)) and (((pos[1] // 50) >= 1) and ((pos[1] // 50) <= 9)):
                    highlight_cell(win, selected_cell, (255, 0, 0))
                    insert(win, (pos[0] // 50, pos[1] // 50))

                # if event.type == pygame.QUIT:
                #     running = False
                #     pygame.quit()
                #     sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    if text_rect_done.collidepoint(mouse_pos):
                        send_manual_grid()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

            if event.type == pygame.QUIT:
                return
        pygame.display.update()

# sudoku_manual_main()







