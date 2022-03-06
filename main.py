import pygame
from config import *
from players import *
from obstacles import *
from game import *
from wall import walls
from ball import *

# Initialize pygame for game machanics
pygame.init()
# Initialize pygame for game sounds
pygame.mixer.init()

brick_sound = pygame.mixer.Sound('sounds/sounds_brick.wav')
paddle_sound = pygame.mixer.Sound('sounds/sounds_paddle.wav')
wall_sound = pygame.mixer.Sound('sounds/sounds_wall.wav')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONGOUT")

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(player1)
all_sprites_list.add(player2)
all_sprites_list.add(ball_1)
all_sprites_list.add(ball_2)


def main_game():

    step = 0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1.moveUP(paddle_1_speed)
        if keys[pygame.K_s]:
            player1.moveDOWN(paddle_1_speed)
            

        if keys[pygame.K_UP]:
            player2.moveUP(paddle_2_speed)
        if keys[pygame.K_DOWN]:
            player2.moveDOWN(paddle_2_speed)

        all_sprites_list.update()

        # Colisions ball 1
        if ball_1.rect.y > SCREEN_HEIGHT - WALL_WIDTH - 15:
            ball_1.vel[1] = -ball_1.vel[1]

        if ball_1.rect.y < WALL_WIDTH:
            ball_1.vel[1] = -ball_1.vel[1]

        if pygame.sprite.collide_mask(ball_1, player1):
            ball_1.bounce()
        if pygame.sprite.collide_mask(ball_1, player2):
            ball_1.bounce()

        # Colision with normal bricks

        brick_collision_list = pygame.sprite.spritecollide(ball_1, all_bricks, False)
        for brick in brick_collision_list:
            ball_1.bounce()
            brick.kill()
            brick_sound.play()
            
            
        # Colision with PU bricks

        brick_pu_collision_list = pygame.sprite.spritecollide(
            ball_1, all_bricks_pu, False)

        for brick in brick_pu_collision_list:
            ball_1.bounce()
            brick.kill()
            brick_sound.play()

        # ++++++++++++++++++++++++++++++++++++++++++++++++++

        # Colisions ball 2
        if ball_2.rect.y > SCREEN_HEIGHT - WALL_WIDTH - 15:
            ball_2.vel[1] = -ball_2.vel[1]

        if ball_2.rect.y < WALL_WIDTH:
            ball_2.vel[1] = -ball_2.vel[1]

        if pygame.sprite.collide_mask(ball_2, player1):
            ball_2.bounce()
        if pygame.sprite.collide_mask(ball_2, player2):
            ball_2.bounce()

        # Colision with normal bricks

        brick_collision_list = pygame.sprite.spritecollide(
            ball_2, all_bricks, False)

        for brick in brick_collision_list:
            brick.kill()
            ball_2.bounce()
            brick_sound.play()

        # Colision with PU bricks 2

        brick_pu_collision_list = pygame.sprite.spritecollide(
            ball_2, all_bricks_pu, False)

        for brick in brick_pu_collision_list:
            ball_2.bounce()
            brick.kill()
            brick_sound.play()

        

        screen.fill(colors["Black"])

        walls()

        all_bricks.draw(screen)
        all_bricks.update()
        all_bricks_pu.draw(screen)
        all_bricks_pu.update()

        all_sprites_list.draw(screen)

        pygame.display.update()

        power_up_1()
        power_up_2()
        power_up_3()

        timer()

        clock.tick(fps)


main_game()
