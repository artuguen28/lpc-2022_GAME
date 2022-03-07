import pygame
from config import *

block_colors = [
    colors["Blue"],
    colors["Orange"],
    colors["Green"],
    colors["Yellow"],
    colors["Red"],
]

all_bricks = pygame.sprite.Group()
all_bricks_pu = pygame.sprite.Group()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obstacle_type, coord: tuple):
        super().__init__()
        self.image = pygame.Surface((15, 34))
        self.image.fill(block_colors[3])
        self.rect = self.image.get_rect(topleft=coord)
        if obstacle_type == 0:
            self.score = 7
        elif obstacle_type == 1:
            self.score = 5
        elif obstacle_type == 2:
            self.score = 3
        else:
            self.score = 1


def draw_obstacles():

    # Distance from one obstacle to another
    dist = 0
    # type of the obstacle
    obstacle_type = 0

    for i in range(2):

        if i == 0:
            # Obstacles coordinates
            x = (SCREEN_WIDTH / 2) - 18

        for j in range(2):

            if j == 0:
                y = WALL_WIDTH + 5
                dist = 0
            else:
                y = SCREEN_HEIGHT - WALL_WIDTH - 78

            for k in range(2):
                brick = Obstacle(obstacle_type, (x + dist, y))
                all_bricks.add(brick)
                y += 39

        x = x + 18
        dist += 17


brick_wall = draw_obstacles()
