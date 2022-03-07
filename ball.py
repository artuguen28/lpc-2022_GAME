# Here goes the ball class
import pygame
from config import BALL_VELOCITY, SCREEN_HEIGHT, SCREEN_WIDTH, colors


class Ball_1(pygame.sprite.Sprite):
    
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.width = width
        self.height = height
        self.bonus = False
        self.color = colors["Blue_ball"]
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect()
        self.vel = [BALL_VELOCITY, BALL_VELOCITY]

    def update(self):
        self.rect.x += self.vel[0]
        self.rect.y -= self.vel[1]

    def bounce(self):
        self.vel[0] = - self.vel[0]
        self.vel[1] = + self.vel[1]

    def change_colors(self):
        if self.bonus is True:
            self.color = colors["Black"]
            pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        else:
            self.color = colors["Blue_ball"]
            pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])


class Ball_2(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.width = width
        self.height = height
        self.bonus = False
        self.color = colors["Red_ball"]
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect()
        self.vel = [BALL_VELOCITY, BALL_VELOCITY]

    def update(self):
        self.rect.x -= self.vel[0]
        self.rect.y += self.vel[1]

    def bounce(self):
        self.vel[0] = - self.vel[0]
        self.vel[1] = + self.vel[1]

    def change_colors(self):
        if self.bonus is True:
            self.color = colors["Black"]
            pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        else:
            self.color = colors["Red_ball"]
            pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])


class Ball_PU(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.color = colors["White"]
        self.direction = ["Left", "Right"]
        pygame.draw.rect(self.image, self.color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.vel = BALL_VELOCITY
        self.direction = 0

    def update(self):
        if self.direction == 0:
            self.rect.x += self.vel
        if self.direction == 1:
            self.rect.x -= self.vel

