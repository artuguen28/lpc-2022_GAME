import pygame
from config import *

block_colors = [colors["Blue"], colors["Orange"], colors["Green"], colors["Yellow"]]
obstacles = pygame.sprite.Group()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obstacle_type, coord: tuple):
        super().__init__()
        self.image = pygame.Surface((15, 35))
        self.image.fill(block_colors[obstacle_type])
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
    # Obstacles coordinates
    x = 418
    y = 46

    # Distance from one obstacle to another
    dist = 0
    # type of the obstacle
    obstacle_type = 0
    reverse = 0
    for i in range(7):
        for j in range(1):
            for k in range(16):
                obstacles.add(Obstacle(obstacle_type, (x + dist, y)))
                y += 38
            y = 46
            dist += 17
            if obstacle_type == 3:
                reverse = 1
            if reverse == 0:
                obstacle_type += 1
            if reverse == 1:
                obstacle_type -= 1

