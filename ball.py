# Here goes the ball class
import pygame
from config import BALL_VELOCITY, SCREEN_HEIGHT, SCREEN_WIDTH, colors

class Ball_1(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.vel = [BALL_VELOCITY, BALL_VELOCITY]

    def update(self):
        self.rect.x += self.vel[0]
        self.rect.y -= self.vel[1]

    def bounce(self):
        self.vel[0] = - self.vel[0]
        self.vel[1] = + self.vel[1]


class Ball_2(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.vel = [BALL_VELOCITY, BALL_VELOCITY]

    def update(self):
        self.rect.x -= self.vel[0]
        self.rect.y += self.vel[1]

    def bounce(self):
        self.vel[0] = - self.vel[0]
        self.vel[1] = + self.vel[1]


class Ball_PU(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.vel = BALL_VELOCITY

    def update(self):
        self.rect.x += self.vel[0]

ball_1 = Ball_1(colors["Blue_ball"], 14, 14)
ball_1.rect.x = SCREEN_WIDTH // 4 - 7
ball_1.rect.y = SCREEN_HEIGHT // 2 - 7

ball_2 = Ball_2(colors["Red_ball"], 14, 14)
ball_2.rect.x = ((SCREEN_WIDTH * 3) // 4) - 7
ball_2.rect.y = SCREEN_HEIGHT // 2 - 7

ball_bonus = Ball_PU(colors["White"], 14, 14)
# ball_bonus.rect.x = Vai depender de onde o bloco foi quebrado
# ball_bonus.rect.y = Vai depender de onde o bloco foi quebrado