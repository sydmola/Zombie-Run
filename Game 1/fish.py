#create fish class
import pygame

class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/orange_fish_alt.png")
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self,screen):
        screen.blit(self.image, self.rect)

fishes = pygame.sprite.Group()