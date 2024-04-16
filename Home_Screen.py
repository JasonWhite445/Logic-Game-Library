import pygame
import sys
import sudoku_folder


def home_screen_main():
    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (217, 247, 250)
    GRAY = (169, 169, 169)

    # Initialize Pygame
    pygame.init()

    # Set up the display
    SQUARE_DIMENSION = min(pygame.display.Info().current_h, pygame.display.Info().current_w) - 100
    # SQUARE_DIMENSION = 400
    ORIGINAL_SCALE = round(SQUARE_DIMENSION / 11, 3)
    IMAGE_SIZE = (SQUARE_DIMENSION / 2.5, SQUARE_DIMENSION / 2.5)
    # WIDTH, HEIGHT = 550, 550
    screen = pygame.display.set_mode((SQUARE_DIMENSION, SQUARE_DIMENSION), pygame.RESIZABLE)
    pygame.display.set_caption("Home Screen")

    # Create font objects
    font = pygame.font.SysFont('Cooper Black', int(ORIGINAL_SCALE))

    # Defines and positions Sudoku logo to draw
    pic_surface_sudoku = pygame.image.load('./250_Sudoku.png')
    pic_surface_sudoku = pygame.transform.scale(pic_surface_sudoku, IMAGE_SIZE)
    pic_rect_sudoku = pic_surface_sudoku.get_rect(center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 1.35))

    # Defines and positions math squares logo to draw
    pic_surface_math_squares = pygame.image.load('./250_MathSquares.png')
    pic_surface_math_squares = pygame.transform.scale(pic_surface_math_squares, IMAGE_SIZE)
    pic_rect_math_squares = pic_surface_math_squares.get_rect(center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 3.75))

    def draw_home_screen():
        screen.fill(BLUE)
        screen.blit(pic_surface_sudoku, pic_rect_sudoku)
        screen.blit(pic_surface_math_squares, pic_rect_math_squares)
        # screen.blit(picture surface, picture location)

    def launch_sudoku_game():
        # User_options.user_options_main()
        # draw_home_screen()
        sudoku_folder.sudoku_folder_main()

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
                pic_surface_sudoku = pygame.transform.scale(pic_surface_sudoku,
                                                            (SQUARE_DIMENSION / 2.5, SQUARE_DIMENSION / 2.5))
                pic_surface_math_squares = pygame.transform.scale(pic_surface_math_squares,
                                                                  (SQUARE_DIMENSION / 2.5, SQUARE_DIMENSION / 2.5))
                pic_rect_sudoku = pic_surface_sudoku.get_rect(
                    center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 1.35))
                pic_rect_math_squares = pic_surface_math_squares.get_rect(
                    center=(SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 3.75))
                draw_home_screen()

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if pic_rect_sudoku.collidepoint(mouse_pos):
                    launch_sudoku_game()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

            if event.type == pygame.QUIT:
                return

        # Draw the home screen
        draw_home_screen()

        # Update the full display Surface to the screen
        pygame.display.flip()


home_screen_main()

