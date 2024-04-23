import sys
import pygame
import sudoku_input
import Sudoku_Generator
import sudoku_game_nxn

size = 0
SQUARE_DIMENSION = 0
def user_options_main():
    global SQUARE_DIMENSION
    # initialize colors
    BLACK = (0, 0, 0)
    BLUE = (217, 247, 250)

    # initialize pygame
    pygame.init()

    # Initialize user options
    SCALE = round(SQUARE_DIMENSION / 11, 3)
    screen = pygame.display.set_mode((SQUARE_DIMENSION, SQUARE_DIMENSION), pygame.RESIZABLE)
    pygame.display.set_caption("Difficulty Select")

    # Create font objects
    font = pygame.font.SysFont('Comic Sans MS', int(SCALE))
    # buttons = ["Easy", "Medium", "Hard", "Solver", "Manual"]
    text_surface_easy = font.render("Easy", True, BLACK)
    text_rect_easy = text_surface_easy.get_rect(center=(SQUARE_DIMENSION//2, SQUARE_DIMENSION//2-4*SCALE))

    text_surface_medium = font.render("Medium", True, BLACK)
    text_rect_medium = text_surface_medium.get_rect(center=(SQUARE_DIMENSION//2, SQUARE_DIMENSION//2-2*SCALE))

    text_surface_hard = font.render("Hard", True, BLACK)
    text_rect_hard = text_surface_hard.get_rect(center=(SQUARE_DIMENSION//2, SQUARE_DIMENSION//2))

    text_surface_solver = font.render("Solver", True, BLACK)
    text_rect_solver = text_surface_solver.get_rect(center=(SQUARE_DIMENSION//2, SQUARE_DIMENSION//2+2*SCALE))

    text_surface_manual = font.render("Manual", True, BLACK)
    text_rect_manual = text_surface_manual.get_rect(center=(SQUARE_DIMENSION//2, SQUARE_DIMENSION//2+4*SCALE))

    def draw_user_screen_options():
        screen.fill(BLUE)
        pygame.draw.rect(screen, BLACK, text_rect_easy, 1)
        screen.blit(text_surface_easy, text_rect_easy)
        pygame.draw.rect(screen, BLACK, text_rect_medium, 1)
        screen.blit(text_surface_medium, text_rect_medium)
        pygame.draw.rect(screen, BLACK, text_rect_hard, 1)
        screen.blit(text_surface_hard, text_rect_hard)
        pygame.draw.rect(screen, BLACK, text_rect_solver, 1)
        screen.blit(text_surface_solver, text_rect_solver)
        pygame.draw.rect(screen, BLACK, text_rect_manual, 1)
        screen.blit(text_surface_manual, text_rect_manual)


    def option_screen(user_input):
        global SQUARE_DIMENSION
        if user_input:
            sudoku_input.SQUARE_DIMENSION = SQUARE_DIMENSION
            sudoku_input.sudoku_manual_main()
        else:
            sudoku_game_nxn.SQUARE_DIMENSION = SQUARE_DIMENSION
            sudoku_game_nxn.won = False
            sudoku_game_nxn.sudoku_nxn_main()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                # Calculate the new size while keeping the aspect ratio square
                if event.w == SQUARE_DIMENSION:
                    SQUARE_DIMENSION = event.h
                elif event.h == SQUARE_DIMENSION:
                    SQUARE_DIMENSION = event.w
                else:
                    SQUARE_DIMENSION = max(event.w, event.h)
                screen = pygame.display.set_mode((SQUARE_DIMENSION, SQUARE_DIMENSION), pygame.RESIZABLE)
                SCALE = round(SQUARE_DIMENSION / 11, 3)
                font = pygame.font.SysFont('Comic Sans MS', int(SCALE))
                text_surface_easy = font.render("Easy", True, BLACK)
                text_rect_easy = text_surface_easy.get_rect(
                    center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 2 - 4 * SCALE))
                text_surface_medium = font.render("Medium", True, BLACK)
                text_rect_medium = text_surface_medium.get_rect(
                    center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 2 - 2 * SCALE))
                text_surface_hard = font.render("Hard", True, BLACK)
                text_rect_hard = text_surface_hard.get_rect(center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 2))
                text_surface_solver = font.render("Solver", True, BLACK)
                text_rect_solver = text_surface_solver.get_rect(
                    center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 2 + 2 * SCALE))
                text_surface_manual = font.render("Manual", True, BLACK)
                text_rect_manual = text_surface_manual.get_rect(
                    center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 2 + 4 * SCALE))
                draw_user_screen_options()

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if text_rect_easy.collidepoint(mouse_pos):
                    sudoku_game_nxn.difficulty = "Easy"
                    sudoku_game_nxn.timer_on = True
                    sudoku_game_nxn.grid = Sudoku_Generator.__main__(size, "easy")[0]
                    option_screen(False)
                    SQUARE_DIMENSION = sudoku_game_nxn.SQUARE_DIMENSION
                elif text_rect_medium.collidepoint(mouse_pos):
                    sudoku_game_nxn.difficulty = "Medium"
                    sudoku_game_nxn.timer_on = True
                    sudoku_game_nxn.grid = Sudoku_Generator.__main__(size, "medium")[0]
                    option_screen(False)
                    SQUARE_DIMENSION = sudoku_game_nxn.SQUARE_DIMENSION
                elif text_rect_hard.collidepoint(mouse_pos):
                    sudoku_game_nxn.difficulty = "Hard"
                    sudoku_game_nxn.timer_on = True
                    sudoku_game_nxn.grid = Sudoku_Generator.__main__(size, "hard")[0]
                    option_screen(False)
                    SQUARE_DIMENSION = sudoku_game_nxn.SQUARE_DIMENSION
                elif text_rect_solver.collidepoint(mouse_pos):
                    sudoku_input.grid = [[0 for _ in range(size)] for _ in range(size)]
                    sudoku_input.solver = True
                    option_screen(True)
                    SQUARE_DIMENSION = sudoku_input.SQUARE_DIMENSION
                elif text_rect_manual.collidepoint(mouse_pos):
                    sudoku_input.grid = [[0 for _ in range(size)] for _ in range(size)]
                    sudoku_input.solver = False
                    option_screen(True)
                    SQUARE_DIMENSION = sudoku_input.SQUARE_DIMENSION
                screen = pygame.display.set_mode((SQUARE_DIMENSION, SQUARE_DIMENSION), pygame.RESIZABLE)
                SCALE = round(SQUARE_DIMENSION / 11, 3)
                font = pygame.font.SysFont('Comic Sans MS', int(SCALE))
                text_surface_easy = font.render("Easy", True, BLACK)
                text_rect_easy = text_surface_easy.get_rect(
                    center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 2 - 4 * SCALE))
                text_surface_medium = font.render("Medium", True, BLACK)
                text_rect_medium = text_surface_medium.get_rect(
                    center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 2 - 2 * SCALE))
                text_surface_hard = font.render("Hard", True, BLACK)
                text_rect_hard = text_surface_hard.get_rect(center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 2))
                text_surface_solver = font.render("Solver", True, BLACK)
                text_rect_solver = text_surface_solver.get_rect(
                    center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 2 + 2 * SCALE))
                text_surface_manual = font.render("Manual", True, BLACK)
                text_rect_manual = text_surface_manual.get_rect(
                    center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 2 + 4 * SCALE))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.display.set_caption("Sudoku Types")
                return

            if event.type == pygame.QUIT:
                sys.exit()

        draw_user_screen_options()

        pygame.display.flip()


# user_options_main()

