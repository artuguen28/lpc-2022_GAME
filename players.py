import pygame
from config import *


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveUP(self, pixels):
        self.rect.x += pixels
        if self.rect.y < 10:
            self.rect.y = 10

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.y > SCREEN_HEIGHT - paddle_height - 10:
            self.rect.y = SCREEN_HEIGHT - paddle_height - 10


player1 = Paddle(colors["White"], paddle_width, paddle_height)
player1.rect.x = 25
player1.rect.y = (SCREEN_HEIGHT // 2) - (paddle_height // 2)

player2 = Paddle(colors["White"], paddle_width, paddle_height)
player2.rect.x = SCREEN_WIDTH - paddle_width - 25
player2.rect.y = (SCREEN_HEIGHT // 2) - (paddle_height // 2)
