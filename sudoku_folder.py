import pygame

import User_options
import sys


def sudoku_folder_main():

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (217, 247, 250)
    GRAY = (169, 169, 169)

    # Initialize Pygame
    pygame.init()

    # Set up the display
    WIDTH, HEIGHT = 550, 550
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku Types")

    # Create font objects
    font = pygame.font.SysFont('Cooper Black', 50)

    # Draw "Sudoku 9x9" text in a rectangle
    text_surface9x9 = font.render("Sudoku 9x9", True, BLACK)
    text_rect9x9 = text_surface9x9.get_rect(center=(WIDTH//2, HEIGHT//2))

    # Draw "Sudoku 12x12" text in a rectangle
    text_surface6x6 = font.render("Sudoku 6x6", True, BLACK)
    text_rect6x6 = text_surface6x6.get_rect(center=(WIDTH//2, HEIGHT//4))

    def draw_sudoku_folder_home_screen():
        screen.fill(BLUE)
        pygame.draw.rect(screen, BLACK, text_rect9x9, 1)
        screen.blit(text_surface9x9, text_rect9x9)
        pygame.draw.rect(screen, BLACK, text_rect6x6, 1)
        screen.blit(text_surface6x6, text_rect6x6)

    def launch_sudoku_folder_game():
        draw_sudoku_folder_home_screen()
        User_options.user_options_main()

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if text_rect9x9.collidepoint(mouse_pos):
                    User_options.size = 9
                    launch_sudoku_folder_game()             # different
                if text_rect6x6.collidepoint(mouse_pos):
                    User_options.size = 6
                    launch_sudoku_folder_game()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

            if event.type == pygame.QUIT:
                return

        # Draw the home screen
        draw_sudoku_folder_home_screen()

        # Update the full display Surface to the screen
        pygame.display.flip()


# sudoku_folder_main()

