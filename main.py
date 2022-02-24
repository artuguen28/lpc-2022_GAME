import pygame
from config import *
from players import *
from obstacles import *
from wall import walls

# Initialize pygame for game machanics
pygame.init()
# Initialize pygame for game sounds
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONGOUT")

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(player1)
all_sprites_list.add(player2)

draw_obstacles()


def main_game():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1.moveUP(10)
        if keys[pygame.K_s]:
            player1.moveDOWN(10)

        if keys[pygame.K_UP]:
            player2.moveUP(10)
        if keys[pygame.K_DOWN]:
            player2.moveDOWN(10)

        all_sprites_list.update()

        screen.fill(colors["Black"])

        walls()

        obstacles.draw(screen)
        obstacles.update()
        
        all_sprites_list.draw(screen)

        pygame.display.update()

        clock.tick(fps)


main_game()
