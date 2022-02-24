# Here goes the ball class
import pygame
from config import BALL_VELOCITY, SCREEN_HEIGHT, SCREEN_WIDTH, colors

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.vel = [BALL_VELOCITY, BALL_VELOCITY]

    def update(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

    def bounce(self):
        self.vel[0] = - self.vel[0]
        self.vel[1] = + self.vel[1]

ball_1 = Ball(colors["Blue_ball"], 14, 14)
ball_1.rect.x = SCREEN_WIDTH // 4 - 7
ball_1.rect.y = SCREEN_HEIGHT // 2 - 7

ball_2 = Ball(colors["Red_ball"], 14, 14)
ball_2.rect.x = ((SCREEN_WIDTH * 3) // 4) - 7
ball_2.rect.y = SCREEN_HEIGHT // 2 - 7
