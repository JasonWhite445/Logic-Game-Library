import pygame

WIDTH = 600
background_color = (255, 255, 255)


def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku Solver")
    window.fill(background_color)

    # https://www.pygame.org/docs/ref/draw.html
    for i in range(0, 10):
        # drawing thicker lines for sub-grids
        if i % 3 == 0:
            pygame.draw.line(window, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(window, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        pygame.draw.line(window, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(window, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()


