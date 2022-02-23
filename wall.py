# Here goes all the walls in the scenario
import pygame
from config import *

def walls():
    from main import screen
    pygame.draw.rect(screen, colors["Grey"], (0, 0, SCREEN_WIDTH, WALL_WIDTH))
    pygame.draw.rect(screen, colors["Grey"],  (0, (SCREEN_HEIGHT - WALL_WIDTH), SCREEN_WIDTH, WALL_WIDTH))
