import pygame
import sys
from game_parameters import *
import random

def draw_background(area):
    #load tiles
    road = pygame.image.load("../assets/sprites/roadTile6.png").convert()
    grass = pygame.image.load("../assets/sprites/terrainTile3.png").convert()

    # fill the screen
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            area.blit(grass, (x, y))

    #draw roads
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT-TILE_SIZE, TILE_SIZE):
            area.blit(road, (x, y))