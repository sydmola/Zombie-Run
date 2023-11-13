import pygame
import sys
from game_parameters import *
from background import draw_background

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#load background
background = screen.copy()
draw_background(background)



