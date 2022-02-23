import pygame
from config import *
from players import *

# Initialize pygame for game machanics
pygame.init()
# Initialize pygame for game sounds
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONGOUT")

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(player1)
all_sprites_list.add(player2)

def main_game():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        all_sprites_list.update()

        screen.fill(colors["Black"])

        all_sprites_list.draw(screen)

        pygame.display.update()

        clock.tick(fps)


main_game()