import pygame
import time

WIDTH = 550
background_color = (255, 255, 255)
original_grid_element_color = (91, 114, 138)
buffer = 5

# input will eventually come from make_random_board function
grid = [[0, 2, 7, 1, 5, 4, 3, 9, 6],
        [9, 6, 5, 3, 2, 7, 1, 4, 8],
        [3, 4, 1, 6, 8, 9, 7, 5, 2],
        [5, 9, 3, 0, 6, 8, 2, 7, 1],
        [4, 7, 2, 5, 1, 3, 6, 8, 9],
        [6, 1, 8, 9, 7, 2, 4, 3, 5],
        [7, 8, 6, 2, 3, 5, 9, 1, 4],
        [1, 5, 4, 7, 9, 6, 8, 2, 3],
        [0, 3, 9, 8, 4, 1, 5, 6, 0]]


grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]


# Check if the board is a valid solution
def board_checker(board):
    for row in range(9):
        if sorted(board[row]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    for col in range(9):
        if sorted([board[i][col] for i in range(9)]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    for box in range(9):
        if sorted([board[pos // 3 + box // 3 * 3][pos % 3 + box % 3 * 3] for pos in range(9)]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    return True


def highlight_cell(win, position):
    pygame.draw.rect(win, (255, 0, 0), (
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
                if grid_original[i - 1][j - 1] != 0:
                    return
                if event.key == 48:  # checking if space is 0, will return blank
                    grid[i - 1][j - 1] = event.key - 48
                    pygame.draw.rect(win, background_color, (
                        position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    pygame.display.update()
                    print_grid(grid)  # Print the updated grid
                    if board_checker(grid):
                        win.fill(background_color)
                        font = pygame.font.SysFont('Comic Sans MS', 40)
                        text = font.render('You Win!', True, (0, 0, 255))
                        win.blit(text, (50, 250))
                        pygame.display.update()
                    return

                if 0 < event.key - 48 < 10:  # checking for valid input
                    pygame.draw.rect(win, background_color, (
                    position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    value = myfont.render(str(event.key - 48), True, (0, 0, 0))
                    win.blit(value, (position[0] * 50 + 15, position[1] * 50))
                    grid[i - 1][j - 1] = event.key - 48
                    pygame.display.update()
                    print_grid(grid)  # Print the updated grid
                    if board_checker(grid):
                        win.fill(background_color)
                        font = pygame.font.SysFont('Comic Sans MS', 40)
                        text = font.render('You Win!', True, (0, 0, 255))
                        win.blit(text, (50, 250))
                        pygame.display.update()
                    return
                return


# prints board for debugging
def print_grid(grid):
    for row in grid:
        print(row)
    print("\n")


def sudoku_main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    # https://www.pygame.org/docs/ref/draw.html
    # Drawing gridlines
    for i in range(0, 10):
        # Drawing sub-grids thicker
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

    # displaying initial grid values
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if 0 < grid[i][j] < 10:
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos[0] // 50, pos[1] // 50)   # prints position for debugging
                selected_cell = (pos[0] // 50, pos[1] // 50)  # Update selected cell position
                if (((pos[0] // 50) >= 1) and ((pos[0] // 50) <= 9)) and (((pos[1] // 50) >= 1) and ((pos[1] // 50) <= 9)):
                    if grid_original[selected_cell[1] - 1][selected_cell[0] - 1] == 0:  # Check if cell is empty
                        highlight_cell(win, selected_cell)

                # Ensures insert is in range of the grid
                if (((pos[0] // 50) >= 1) and ((pos[0] // 50) <= 9)) and (((pos[1] // 50) >= 1) and ((pos[1] // 50) <= 9)):
                    insert(win, (pos[0] // 50, pos[1] // 50))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

            if event.type == pygame.QUIT:
                return


# sudoku_main()
