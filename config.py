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

# Paddles` variables
paddle_width = 20
paddle_height = 75

paddle_1_speed = 10
paddle_2_speed = 10

paddle_1_height = 75
paddle_2_height = 75