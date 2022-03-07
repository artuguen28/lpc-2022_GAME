# Here goes all the constants, functions and global variables
import pygame


SCREEN_WIDTH = 950
SCREEN_HEIGHT = 700
BALL_VELOCITY = 3
WALL_WIDTH = 20

# Colors dictionary
colors = {
    "Blue_ball": (0, 0, 255),
    "Red_ball": (255, 0, 0), 
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
    "Grey": (212, 210, 212),
    "Orange": (183, 119, 0),
    "Green": (0, 127, 33),
    "Blue": (0, 97, 148),
    "Red": (162, 8, 0),
    "Yellow": (197, 199, 37),
}

# Screen loop variables
clock = pygame.time.Clock()
fps = 60

# Paddles` variables
paddle_width = 20
paddle_height = 75

# # Powerup 1 time and state in order
# p1_active_1 = False
# p2_active_1 = False
# p1_active_time_1 = 0
# p2_active_time_1 = 0

# # Paddles` variables
# paddle_width = 20

# paddle_1_height = 75
# paddle_2_height = 75