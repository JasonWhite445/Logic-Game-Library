import pygame

import Math_Square
import User_options
import sys

# please commit :(
# Set up the display
SQUARE_DIMENSION = 500

def math_square_folder_main():
    global SQUARE_DIMENSION
    # Define colors
    BLACK = (0, 0, 0)
    BLUE = (217, 247, 250)
    SCALE = round(SQUARE_DIMENSION / 11, 3)

    # Initialize Pygame
    pygame.init()

    # WIDTH, HEIGHT = 550, 550
    screen = pygame.display.set_mode((SQUARE_DIMENSION, SQUARE_DIMENSION), pygame.RESIZABLE)
    pygame.display.set_caption("Math Square Types")

    # Create font objects
    font = pygame.font.SysFont('Cooper Black', int(SCALE))
    # buttons = [4, 6, 8, 9]
    text_surface3x3 = font.render("Math Square 3x3", True, BLACK)
    text_rect3x3 = text_surface3x3.get_rect(center=(SQUARE_DIMENSION//2, SQUARE_DIMENSION//8))

    # Draw "Math Square 4x4" text in a rectangle
    text_surface4x4 = font.render("Math Square 4x4", True, BLACK)
    text_rect4x4 = text_surface4x4.get_rect(center=(SQUARE_DIMENSION//2, 3*SQUARE_DIMENSION//8))

    text_surface5x5 = font.render("Math Square 5x5", True, BLACK)
    text_rect5x5 = text_surface5x5.get_rect(center=(SQUARE_DIMENSION//2, 5*SQUARE_DIMENSION//8))


    text_surface6x6 = font.render("Math Square 6x6", True, BLACK)
    text_rect6x6 = text_surface6x6.get_rect(center=(SQUARE_DIMENSION//2, 7*SQUARE_DIMENSION//8))

    def draw_math_square_folder_home_screen():
        screen.fill(BLUE)
        pygame.draw.rect(screen, BLACK, text_rect6x6, 1)
        screen.blit(text_surface6x6, text_rect6x6)
        pygame.draw.rect(screen, BLACK, text_rect4x4, 1)
        screen.blit(text_surface4x4, text_rect4x4)
        pygame.draw.rect(screen, BLACK, text_rect3x3, 1)
        screen.blit(text_surface3x3, text_rect3x3)
        pygame.draw.rect(screen, BLACK, text_rect5x5, 1)
        screen.blit(text_surface5x5, text_rect5x5)

    def launch_math_square_folder_game():
        draw_math_square_folder_home_screen()
        Math_Square.main()

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
                text_surface3x3 = font.render("Math Square 3x3", True, BLACK)
                text_rect3x3 = text_surface3x3.get_rect(center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 8))
                text_surface4x4 = font.render("Math Square 4x4", True, BLACK)
                text_rect4x4 = text_surface4x4.get_rect(center=(SQUARE_DIMENSION // 2, 3 * SQUARE_DIMENSION // 8))
                text_surface5x5 = font.render("Math Square 5x5", True, BLACK)
                text_rect5x5 = text_surface5x5.get_rect(center=(SQUARE_DIMENSION // 2, 5 * SQUARE_DIMENSION // 8))
                text_surface6x6 = font.render("Math Square 6x6", True, BLACK)
                text_rect6x6 = text_surface6x6.get_rect(center=(SQUARE_DIMENSION // 2, 7 * SQUARE_DIMENSION // 8))

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if text_rect6x6.collidepoint(mouse_pos):
                    Math_Square.size = 6
                    launch_math_square_folder_game()
                if text_rect4x4.collidepoint(mouse_pos):
                    Math_Square.size = 4
                    launch_math_square_folder_game()
                if text_rect3x3.collidepoint(mouse_pos):
                    Math_Square.size = 3
                    launch_math_square_folder_game()
                if text_rect5x5.collidepoint(mouse_pos):
                    Math_Square.size = 5
                    launch_math_square_folder_game()

                SQUARE_DIMENSION = screen.get_width()
                screen = pygame.display.set_mode((SQUARE_DIMENSION, SQUARE_DIMENSION), pygame.RESIZABLE)
                SCALE = round(SQUARE_DIMENSION / 11, 3)
                font = pygame.font.SysFont('Cooper Black', int(SCALE))
                text_surface3x3 = font.render("Math Square 3x3", True, BLACK)
                text_rect3x3 = text_surface3x3.get_rect(center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 8))
                text_surface4x4 = font.render("Math Square 4x4", True, BLACK)
                text_rect4x4 = text_surface4x4.get_rect(center=(SQUARE_DIMENSION // 2, 3 * SQUARE_DIMENSION // 8))
                text_surface5x5 = font.render("Math Square 5x5", True, BLACK)
                text_rect5x5 = text_surface5x5.get_rect(center=(SQUARE_DIMENSION // 2, 5 * SQUARE_DIMENSION // 8))
                text_surface6x6 = font.render("Math Square 6x6", True, BLACK)
                text_rect6x6 = text_surface6x6.get_rect(center=(SQUARE_DIMENSION // 2, 7 * SQUARE_DIMENSION // 8))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.display.set_caption("Home Screen")
                return

            if event.type == pygame.QUIT:
                sys.exit()

        # Draw the home screen
        draw_math_square_folder_home_screen()

        # Update the full display Surface to the screen
        pygame.display.flip()


# math_square_folder_main()