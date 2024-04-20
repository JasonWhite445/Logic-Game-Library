import pygame

import User_options
import sys


# Set up the display
SQUARE_DIMENSION = 500

def sudoku_folder_main():
    global SQUARE_DIMENSION
    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (217, 247, 250)
    GRAY = (169, 169, 169)
    SCALE = round(SQUARE_DIMENSION / 11, 3)

    # Initialize Pygame
    pygame.init()

    # WIDTH, HEIGHT = 550, 550
    screen = pygame.display.set_mode((SQUARE_DIMENSION, SQUARE_DIMENSION), pygame.RESIZABLE)
    pygame.display.set_caption("Sudoku Types")

    # Create font objects
    font = pygame.font.SysFont('Cooper Black', int(SCALE))
    # buttons = [4, 6, 8, 9]
    text_surface4x4 = font.render("Sudoku 4x4", True, BLACK)
    text_rect4x4 = text_surface4x4.get_rect(center=(SQUARE_DIMENSION//2, SQUARE_DIMENSION//8))

    # Draw "Sudoku 6x6" text in a rectangle
    text_surface6x6 = font.render("Sudoku 6x6", True, BLACK)
    text_rect6x6 = text_surface6x6.get_rect(center=(SQUARE_DIMENSION//2, 3*SQUARE_DIMENSION//8))

    text_surface8x8 = font.render("Sudoku 8x8", True, BLACK)
    text_rect8x8 = text_surface8x8.get_rect(center=(SQUARE_DIMENSION//2, 5*SQUARE_DIMENSION//8))

    # Draw "Sudoku 9x9" text in a rectangle
    text_surface9x9 = font.render("Sudoku 9x9", True, BLACK)
    text_rect9x9 = text_surface9x9.get_rect(center=(SQUARE_DIMENSION//2, 7*SQUARE_DIMENSION//8))

    def draw_sudoku_folder_home_screen():
        screen.fill(BLUE)
        pygame.draw.rect(screen, BLACK, text_rect9x9, 1)
        screen.blit(text_surface9x9, text_rect9x9)
        pygame.draw.rect(screen, BLACK, text_rect6x6, 1)
        screen.blit(text_surface6x6, text_rect6x6)
        pygame.draw.rect(screen, BLACK, text_rect4x4, 1)
        screen.blit(text_surface4x4, text_rect4x4)
        pygame.draw.rect(screen, BLACK, text_rect8x8, 1)
        screen.blit(text_surface8x8, text_rect8x8)

    def launch_sudoku_folder_game():
        draw_sudoku_folder_home_screen()
        User_options.user_options_main()

    # Main loop
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
                font = pygame.font.SysFont('Cooper Black', int(SCALE))
                text_surface4x4 = font.render("Sudoku 4x4", True, BLACK)
                text_rect4x4 = text_surface4x4.get_rect(center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 8))
                text_surface6x6 = font.render("Sudoku 6x6", True, BLACK)
                text_rect6x6 = text_surface6x6.get_rect(center=(SQUARE_DIMENSION // 2, 3 * SQUARE_DIMENSION // 8))
                text_surface8x8 = font.render("Sudoku 8x8", True, BLACK)
                text_rect8x8 = text_surface8x8.get_rect(center=(SQUARE_DIMENSION // 2, 5 * SQUARE_DIMENSION // 8))
                text_surface9x9 = font.render("Sudoku 9x9", True, BLACK)
                text_rect9x9 = text_surface9x9.get_rect(center=(SQUARE_DIMENSION // 2, 7 * SQUARE_DIMENSION // 8))

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if text_rect9x9.collidepoint(mouse_pos):
                    User_options.size = 9
                    launch_sudoku_folder_game()
                if text_rect6x6.collidepoint(mouse_pos):
                    User_options.size = 6
                    launch_sudoku_folder_game()
                if text_rect4x4.collidepoint(mouse_pos):
                    User_options.size = 4
                    launch_sudoku_folder_game()
                if text_rect8x8.collidepoint(mouse_pos):
                    User_options.size = 8
                    launch_sudoku_folder_game()
                SQUARE_DIMENSION = screen.get_width()
                screen = pygame.display.set_mode((SQUARE_DIMENSION, SQUARE_DIMENSION), pygame.RESIZABLE)
                SCALE = round(SQUARE_DIMENSION / 11, 3)
                font = pygame.font.SysFont('Cooper Black', int(SCALE))
                text_surface4x4 = font.render("Sudoku 4x4", True, BLACK)
                text_rect4x4 = text_surface4x4.get_rect(center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 8))
                text_surface6x6 = font.render("Sudoku 6x6", True, BLACK)
                text_rect6x6 = text_surface6x6.get_rect(center=(SQUARE_DIMENSION // 2, 3 * SQUARE_DIMENSION // 8))
                text_surface8x8 = font.render("Sudoku 8x8", True, BLACK)
                text_rect8x8 = text_surface8x8.get_rect(center=(SQUARE_DIMENSION // 2, 5 * SQUARE_DIMENSION // 8))
                text_surface9x9 = font.render("Sudoku 9x9", True, BLACK)
                text_rect9x9 = text_surface9x9.get_rect(center=(SQUARE_DIMENSION // 2, 7 * SQUARE_DIMENSION // 8))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.display.set_caption("Home Screen")
                return

            if event.type == pygame.QUIT:
                sys.exit()

        # Draw the home screen
        draw_sudoku_folder_home_screen()

        # Update the full display Surface to the screen
        pygame.display.flip()


# sudoku_folder_main()

