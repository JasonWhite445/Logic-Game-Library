import pygame
import sys
import User_options

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

# Draw "Sudoku 9x9" text in a rectangle
text_surface9x9 = font.render("Sudoku 9x9", True, BLACK)
text_rect9x9 = text_surface9x9.get_rect(center=(WIDTH//2, HEIGHT//2))

# Draw "Sudoku 12x12" text in a rectangle
text_surface12x12 = font.render("Sudoku 12x12", True, BLACK)
text_rect12x12 = text_surface12x12.get_rect(center=(WIDTH//2, HEIGHT//4))


def draw_home_screen():
    screen.fill(BLUE)
    pygame.draw.rect(screen, BLACK, text_rect9x9, 1)
    screen.blit(text_surface9x9, text_rect9x9)
    pygame.draw.rect(screen, BLACK, text_rect12x12, 1)
    screen.blit(text_surface12x12, text_rect12x12)


def launch_sudoku_game():
    User_options.main()
    draw_home_screen()


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
                launch_sudoku_game()

    # Draw the home screen
    draw_home_screen()

    # Update the full display Surface to the screen
    pygame.display.flip()
