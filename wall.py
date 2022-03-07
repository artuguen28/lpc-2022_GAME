# Here goes all the walls in the scenario
import pygame
from config import *


def walls():
    from main import screen
    pygame.draw.rect(screen, colors["Blue_ball"], (0, 0, (SCREEN_WIDTH // 2), WALL_WIDTH))
    pygame.draw.rect(screen, colors["Red_ball"], ((SCREEN_WIDTH // 2), 0, (SCREEN_WIDTH // 2), WALL_WIDTH))
    
    pygame.draw.rect(screen, colors["Blue_ball"],
                     (0, (SCREEN_HEIGHT - WALL_WIDTH), (SCREEN_WIDTH // 2), WALL_WIDTH))
    pygame.draw.rect(screen, colors["Red_ball"],
                     ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT - WALL_WIDTH), (SCREEN_WIDTH // 2), WALL_WIDTH))
