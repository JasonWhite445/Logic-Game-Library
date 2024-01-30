import pygame
import sudoku_game
import sys

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 550, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Launcher")

# Create font objects
font = pygame.font.SysFont('Comic Sans MS', 50)

# Draw "Sudoku" text in a rectangle
text_surface = font.render("Sudoku", True, BLACK)
text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))


def draw_home_screen():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, text_rect, 1)
    screen.blit(text_surface, text_rect)


def launch_sudoku_game():
    sudoku_game.sudoku_main()


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
            if text_rect.collidepoint(mouse_pos):
                launch_sudoku_game()

    # Draw the home screen
    draw_home_screen()

    # Update the full display Surface to the screen
    pygame.display.flip()
    pygame.time.Clock().tick(30)
