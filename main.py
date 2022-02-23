import pygame

from config import *

# Initialize pygame for game machanics
pygame.init()
# Initialize pygame for game sounds
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONGOUT")


def main_game():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(colors["Black"])

        pygame.display.update()

        clock.tick(fps)


main_game()
