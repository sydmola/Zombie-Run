import pygame
from game_parameters import *
import random
from zombie import Zombie, zombies
pygame.display.init()
from fish import Fish, fishes
from powerup import Power, powers


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

def draw_start_menu(screen):
    screen.fill((100, 100, 150))
    menu_font =pygame.font.Font("../assets/fonts/Humongous of Eternity St.ttf", 30)
    title = menu_font.render('Zombie Run', True, (255, 255, 255))
    start_button = menu_font.render('Press Space to Start', True, (255, 255, 255))
    exit_button = menu_font.render('Press X to quit', True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2 - title.get_height()/2))
    screen.blit(start_button, (SCREEN_WIDTH/2 - start_button.get_width()/2, SCREEN_HEIGHT/2 + start_button.get_height()/2))
    screen.blit(exit_button, (SCREEN_WIDTH/2 - exit_button.get_width()/2, SCREEN_HEIGHT/2 + exit_button.get_height()*(3/2)))
    pygame.display.update()





#draw fish
def add_fishes(num_fishes):
    for _ in range(num_fishes):
        fishes.add(Fish(random.randint(0, SCREEN_WIDTH),
                            random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))


def add_zombies(num_zombies):
    for _ in range(num_zombies):
        zombies.add(Zombie(random.randint(SCREEN_WIDTH, (SCREEN_WIDTH * 1.5)),
                            random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))

def add_power(num_power):
    for _ in range(num_power):
        powers.add(Power(random.randint(0, SCREEN_WIDTH),
                            random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))
