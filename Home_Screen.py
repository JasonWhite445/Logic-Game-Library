import pygame
import sys
import sudoku_folder


def home_screen_main():
    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (217, 247, 250)

    # Initialize Pygame
    pygame.init()

    # Set up the display
    WIDTH, HEIGHT = 550, 550
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Home Screen")

    # Create font objects
    font = pygame.font.SysFont('Cooper Black', 50)

    # Draw "Sudoku" text in a rectangle
    text_surface_sudoku = font.render("Sudoku", True, BLACK)
    text_rect_sudoku = text_surface_sudoku.get_rect(center=(WIDTH//2, HEIGHT//2))

    # Draw "Sudoku 12x12" text in a rectangle
    text_surface_other_game = font.render("Other Game", True, BLACK)
    text_rect_other_game = text_surface_other_game.get_rect(center=(WIDTH//2, HEIGHT//4))

    def draw_home_screen():
        screen.fill(BLUE)
        pygame.draw.rect(screen, BLACK, text_rect_sudoku, 1)
        screen.blit(text_surface_sudoku, text_rect_sudoku)
        pygame.draw.rect(screen, BLACK, text_rect_other_game, 1)
        screen.blit(text_surface_other_game, text_rect_other_game)

    def launch_sudoku_game():
        # User_options.user_options_main()
        draw_home_screen()
        sudoku_folder.sudoku_folder_main()

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
                if text_rect_sudoku.collidepoint(mouse_pos):
                    launch_sudoku_game()

        # Draw the home screen
        draw_home_screen()

        # Update the full display Surface to the screen
        pygame.display.flip()


home_screen_main()

