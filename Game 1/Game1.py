import pygame
import sys
from game_parameters import *
from background import draw_background, add_zombies
from player import Player
import random
from zombie import zombies


#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('load background')

#clock object
clock = pygame.time.Clock()

#load background
running = True
background = screen.copy()
draw_background(background)

#create a player character
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

#draw zombies on the screen
add_zombies(3)

#draw lives
life_icon = pygame.image.load("../assets/sprites/heart.png").convert()
life_icon.set_colorkey((0,0,0))

#set lives
lives = NUM_LIVES


while NUM_LIVES>0 and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # control fish with keyboard
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("you pressed the up key")
                player.move_up()
            if event.key == pygame.K_DOWN:
                print("you pressed the down key")
                player.move_down()
            if event.key == pygame.K_LEFT:
                print("you pressed the left key")
                player.move_left()
            if event.key == pygame.K_RIGHT:
                print("you pressed the right key")
                player.move_right()

    #draw background
    screen.blit(background, (0,0))

    #draw player
    player.update()

    #update our zombie location
    zombies.update()

    #check for player/zombie collisions
    result = pygame.sprite.spritecollide(player, zombies, True)
    #print(result)
    if result:
        #lose lives if hurt
        lives -= len(result)
        #draw more zombies
        add_zombies(len(result))


    #check if zombie is off the screen
    for zombie in zombies:
        if zombie.rect.x < -zombie.rect.width:
            zombies.remove(zombie) #removing the zombie from the sprite group
            add_zombies(1)

    #draw game objects
    player.draw(screen)
    zombies.draw(screen)

    #draw lives in lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i*TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE))

    # update display
    pygame.display.flip()

    # limit frame rate
    clock.tick(50)

# quit pygame
pygame.quit()



