import pygame
import random
from game_parameters import *

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/zombie_stand.png").convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x, y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self,screen):
        screen.blit(self.image, self.rect)

zombies = pygame.sprite.Group()