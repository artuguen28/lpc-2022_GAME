from email.mime import image
import pygame
from config import *
from pygame import surface

block_colors = [colors["Blue"], colors["Orange"], colors["Green"], colors["Yellow"], colors["Red"]]
obstacles = pygame.sprite.Group()
obstacles_pu = pygame.sprite.Group()

class Obstacle(pygame.sprite.Sprite):
    
    def __init__(self, obstacle_type, coord: tuple):
        super().__init__()
        self.image = pygame.Surface((15, 34))
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


class Obstacle_PU(pygame.sprite.Sprite):

    def __init__(self, coord: tuple):
        from time import sleep
        super().__init__()
        self.image = pygame.Surface((15, 34))
        self.image.fill(block_colors[4])
        self.rect = self.image.get_rect(topleft=coord)



def draw_obstacles():

    # Distance from one obstacle to another
    dist = 5
    
    # type of the obstacle
    obstacle_type = 0
    reverse = 0
    
    for i in range(7):
        # Obstacles coordinates
        x = 411
        y = WALL_WIDTH + 1
        
        for j in range(17):
            if i not in (1, 3, 5, 7):
                obstacles.add(Obstacle(obstacle_type, (x + dist, y)))
                y += 39
            else:
                if j % 2 == 1:
                    obstacles_pu.add(Obstacle_PU((x + dist, y)))
                    y += 39
                else:
                    obstacles.add(Obstacle(obstacle_type, (x + dist, y)))
                    y += 39
        y = WALL_WIDTH + 1
        dist += 17
        if obstacle_type == 3:
            reverse = 1
        if reverse == 0:
            obstacle_type += 1
        if reverse == 1:
            obstacle_type -= 1