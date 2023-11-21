import pygame
from game_parameters import *

#create a pygame player sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #flip player if going the other way
        self.forward_image = pygame.image.load("../assets/sprites/female_stand.png")
        self.reverse_image = pygame.image.load("../assets/sprites/female_back.png")
        self.image = self.forward_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.y_speed = -1 * PLAYER_SPEED
        self.image = self. reverse_image

    def move_down(self):
        self.y_speed = PLAYER_SPEED
        self.image = self. forward_image

    def move_left(self):
        self.x_speed = -1 * PLAYER_SPEED

    def move_right(self):
        self.x_speed = PLAYER_SPEED
        self.image = self.forward_image

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        #make player stay on screen
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.rect.x >= SCREEN_WIDTH - TILE_SIZE:
            self.rect.x = SCREEN_WIDTH - TILE_SIZE
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.y >= SCREEN_HEIGHT - TILE_SIZE*2:
            self.rect.y = SCREEN_HEIGHT - TILE_SIZE*2
        if self.rect.y <= 0:
            self.rect.y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)