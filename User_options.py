import sys
import sudoku_game9x9
import pygame


def user_options_main():

    # initialize colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (217, 247, 250)
    GRAY = (169, 169, 169)

    # initialize pygame
    pygame.init()

    # Initiaze user options
    WIDTH, HEIGHT = 550, 550
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Make Your Choice")

    # Create font objects
    font = pygame.font.SysFont('Comic Sans MS', 50)

    text_surface_easy = font.render("Easy", True, GRAY)
    text_rect_easy = text_surface_easy.get_rect(center=(WIDTH//2, HEIGHT//2 - 200))

    text_surface_medium = font.render("Medium", True, GRAY)
    text_rect_medium = text_surface_medium.get_rect(center=(WIDTH//2, HEIGHT//2-100))

    text_surface_hard = font.render("Hard", True, GRAY)
    text_rect_hard = text_surface_hard.get_rect(center=(WIDTH//2, HEIGHT//2))

    text_surface_manual = font.render("Manual", True, BLACK)
    text_rect_manual = text_surface_manual.get_rect(center=(WIDTH//2, HEIGHT//2+100))

    def draw_user_screen_options():
        screen.fill(BLUE)
        pygame.draw.rect(screen, BLACK, text_rect_easy, 1)
        screen.blit(text_surface_easy, text_rect_easy)
        pygame.draw.rect(screen, BLACK, text_rect_medium, 1)
        screen.blit(text_surface_medium, text_rect_medium)
        pygame.draw.rect(screen, BLACK, text_rect_hard, 1)
        screen.blit(text_surface_hard, text_rect_hard)
        pygame.draw.rect(screen, BLACK, text_rect_manual, 1)
        screen.blit(text_surface_manual, text_rect_manual)

    def option_screen():
        draw_user_screen_options()
        sudoku_game9x9.sudoku_9x9_main()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if text_rect_manual.collidepoint(mouse_pos):
                    option_screen()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

            if event.type == pygame.QUIT:
                return

        draw_user_screen_options()

        pygame.display.flip()


# user_options_main()
