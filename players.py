import pygame
from config import *


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.height = height

    def moveUP(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < WALL_WIDTH:
            self.rect.y = WALL_WIDTH

    def moveDOWN(self, pixels):
        self.rect.y += pixels
        if self.rect.y > SCREEN_HEIGHT - self.height - WALL_WIDTH:
            self.rect.y = SCREEN_HEIGHT - self.height - WALL_WIDTH
