import pygame
import sys
from game_parameters import *
import random
from zombie import Zombie, zombies
pygame.display.init()
from fish import Fish, fishes


def draw_background(screen):
    #load tiles
    road = pygame.image.load("../assets/sprites/roadTile6.png").convert()
    grass = pygame.image.load("../assets/sprites/terrainTile3.png").convert()
    fish = pygame.image.load("../assets/sprites/orange_fish_alt.png").convert()
    #png
    fish.set_colorkey((0,0,0))

    # fill the screen
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(grass, (x, y))

    #draw roads
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT-TILE_SIZE, TILE_SIZE*2):
            screen.blit(road, (x, y))


#draw fish
def add_fishes(num_fishes):
    for _ in range(num_fishes):
        fishes.add(Fish(random.randint(0, SCREEN_WIDTH),
                            random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))


def add_zombies(num_zombies):
    for _ in range(num_zombies):
        zombies.add(Zombie(random.randint(SCREEN_WIDTH, (SCREEN_WIDTH * 1.5)),
                            random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))
