import pygame
from config import *
from players import *
from obstacles import *
# from game import *
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

# Paddles

paddle_1_speed = 10
paddle_2_speed = 10

paddle_1_height = 75
paddle_2_height = 75

# Players

player1 = Paddle(colors["Blue_ball"], paddle_width, paddle_1_height)
player1.rect.x = 25
player1.rect.y = (SCREEN_HEIGHT // 2) - (paddle_1_height // 2)

player2 = Paddle(colors["Red_ball"], paddle_width, paddle_2_height)
player2.rect.x = SCREEN_WIDTH - paddle_width - 25
player2.rect.y = (SCREEN_HEIGHT // 2) - (paddle_2_height // 2)


# Balls

ball_1 = Ball_1(14, 14)
ball_1.rect.x = SCREEN_WIDTH // 4 - 7
ball_1.rect.y = SCREEN_HEIGHT // 2 - 7

ball_2 = Ball_2(14, 14)
ball_2.rect.x = ((SCREEN_WIDTH * 3) // 4) - 7
ball_2.rect.y = SCREEN_HEIGHT // 2 - 7

ball_pu = Ball_PU(14,14)
# ball_bonus.rect.x = Vai depender de onde o bloco foi quebrado
# ball_bonus.rect.y = Vai depender de onde o bloco foi quebrado

# Time control variables

loop = 0
seconds = 0

# Powerups time and state in order

# 1
p1_active_1 = False
p2_active_1 = False
p1_active_time_1 = 0
p2_active_time_1 = 0

#2
p1_active_2 = False
p2_active_2 = False
p1_active_time_2 = 0
p2_active_time_2 = 0

#3
p1_active_3 = False
p2_active_3 = False
p1_active_time_3 = 0
p2_active_time_3 = 0

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(player1)
all_sprites_list.add(player2)
all_sprites_list.add(ball_1)
all_sprites_list.add(ball_2)

# Controls time of power ups
def timer():
    global loop, seconds

    # Print can be enabled to check the seconds increasing up to 60
    # print(loop)
    if loop == 60:
        loop = 0
        seconds = seconds + 1

    # Seconds have relation with the powerup released by the bricks also the total power ups

    if seconds == 5:
        seconds = 0

    # Counting seconds every 60 game loop interactions
    loop = loop + 1


# Increase the size of the player paddle
def power_up_1():
    global loop, p1_active_1, p2_active_1, p1_active_time_1,\
        p2_active_time_1, paddle_1_height, paddle_2_height

    # Checking if powerup is at time limit

    if p1_active_1 is True or p2_active_1 is True:
        if p1_active_time_1 == 15:
            p1_active_time_1 = 0
            p1_active_1 = False

        if p2_active_time_1 == 15:
            p2_active_time_1 = 0
            p2_active_1 = False

    # Checking if Any powerup is active and counting the time it remains active
    if loop == 60 and (p1_active_1 or p2_active_1):
        if p1_active_1 is True:
            p1_active_time_1 = p1_active_time_1 + 1

        if p2_active_1 is True:
            p2_active_time_1 = p2_active_time_1 + 1

    if p1_active_1 is False:
        paddle_1_height = 75
    if p2_active_1 is False:
        paddle_2_height = 75

    if p1_active_1 is True:
        paddle_1_height = 130
    if p2_active_1 is True:
        paddle_2_height = 130


# Makes enemy ball invisible (black)
def power_up_2():
    global loop, ball_1, ball_2, p1_active_2, p2_active_2,\
        p1_active_time_2, p2_active_time_2

    if p1_active_2 is True or p2_active_2 is True:
        if p1_active_time_2 == 7:
            p1_active_time_2 = 0
            p1_active_2 = False

        if p2_active_time_2 == 7:
            p2_active_time_2 = 0
            p2_active_2 = False

    if loop == 60:
        if p1_active_2 is True:
            p1_active_time_2 = p1_active_time_2 + 1

        if p2_active_2 is True:
            p2_active_time_2 = p2_active_time_2 + 1

    if p1_active_2 is True:
        ball_2.bonus = True
        ball_2.change_colors()
    else:
        ball_2.bonus = False
        ball_2.change_colors()
    if p2_active_2 is True:
        ball_1.bonus = True
        ball_1.change_colors()
    else:
        ball_1.bonus = False
        ball_1.change_colors()


# Makes enemy paddle slower
def power_up_3():
    global loop, paddle_1_speed, paddle_2_speed, p1_active_3,\
        p2_active_3, p1_active_time_3, p2_active_time_3

    if p1_active_3 is True or p2_active_3 is True:
        if p1_active_time_3 == 10:
            p1_active_time_3 = 0
            p1_active_3 = False

        if p2_active_time_3 == 10:
            p2_active_time_3 = 0
            p2_active_3 = False

    if loop == 60:
        if p1_active_3 is True:
            p1_active_time_3 = p1_active_time_3 + 1

        if p2_active_3 is True:
            p2_active_time_3 = p2_active_time_3 + 1

    if p1_active_3 is True:
        paddle_2_speed = 5
    else:
        paddle_2_speed = 10
    if p2_active_3 is True:
        paddle_1_speed = 5
    else:
        paddle_1_speed = 10


def main_game():

    step = 0


    score1 = 10
    score2 = 10

    start_p = True
    pause = False
    

    font = pygame.font.Font('text_style/DSEG14Classic-Bold.ttf', 50)
    font2 = pygame.font.Font('text_style/DSEG14Classic-Bold.ttf', 30)

    # Start Screen
    while start_p:

        timer()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_p = False
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            start_p = False
            run = True

        screen.fill(colors["Black"])

        walls()


        if loop < 30:
            text = font.render("PONGOUT", 1, colors["Red"])
            screen.blit(text, ((SCREEN_HEIGHT// 2 ) - 10, (SCREEN_WIDTH// 2) - 300))
        else:
            text = font.render("PONGOUT", 1, colors["White"])
            screen.blit(text, ((SCREEN_HEIGHT// 2 ) - 10, (SCREEN_WIDTH// 2) - 300))

        text = font2.render("Press 'p' to start the game",1,  colors["White"])
        screen.blit(text, ((SCREEN_HEIGHT// 2 ) - 150, (SCREEN_WIDTH// 2) - 100))

        pygame.display.update()
        clock.tick(fps)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = True

        # Pause Screen

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = False

            screen.fill(colors["Black"])

            walls()
            text = font.render("Pause",1,  colors["White"])
            screen.blit(text, ((SCREEN_HEIGHT// 2 ) + 20, (SCREEN_WIDTH// 2) - 300))

            text = font2.render("Press 'esc' to remain",1,  colors["White"])
            screen.blit(text, ((SCREEN_HEIGHT// 2 ) - 110, (SCREEN_WIDTH// 2) - 150))


            pygame.display.update()
            clock.tick(fps)

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
        if ball_1.rect.x > SCREEN_WIDTH:
            score1 += 1
            score2 -= 2
            ball_1.rect.x = SCREEN_WIDTH // 4 - 7
            ball_1.rect.y = SCREEN_HEIGHT // 2 - 7

        if ball_1.rect.x < 0:
            score1 -= 1
            ball_1.rect.x = SCREEN_WIDTH // 4 - 7
            ball_1.rect.y = SCREEN_HEIGHT // 2 - 7

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

        # ++++++++++++++++++++++++++++++++++++++++++++++++++

        # Colisions ball 2
        if ball_2.rect.x < 0:
            score1 -= 2
            score2 += 1
            ball_2.rect.x = ((SCREEN_WIDTH * 3) // 4) - 7
            ball_2.rect.y = SCREEN_HEIGHT // 2 - 7

        if ball_2.rect.x > SCREEN_WIDTH:
            score2 -= 1
            ball_2.rect.x = ((SCREEN_WIDTH * 3) // 4) - 7
            ball_2.rect.y = SCREEN_HEIGHT // 2 - 7

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

        screen.fill(colors["Black"])

        walls()

        all_bricks.draw(screen)
        all_bricks.update()
        all_bricks_pu.draw(screen)
        all_bricks_pu.update()

        # HUD

        font = pygame.font.Font('text_style/DSEG14Classic-Bold.ttf', 50)

        if score1 < 15:
            text = font.render(str(f"{score1:03}"), 1, colors["White"])
            screen.blit(text, (150, 41))
        else:
            text = font.render(str(f"{score1:03}"), 1, colors["Red"])
            screen.blit(text, (150, 41))

        if score2 < 15:
            text = font.render(str(f"{score2:03}"), 1, colors["White"])
            screen.blit(text, (670, 41))
        else:
            text = font.render(str(f"{score2:03}"), 1, colors["Red"])
            screen.blit(text, (150, 41))

        all_sprites_list.draw(screen)

        pygame.display.update()


        # power_up_1()
        power_up_2()
        power_up_3()

        timer()

        clock.tick(fps)


main_game()
