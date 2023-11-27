import pygame
import sys
from game_parameters import *
from background import draw_background, add_zombies, add_fishes, add_power
from player import Player
import random
from zombie import zombies
from fish import fishes
from powerup import powers

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

#initialize score
score = 0
score_font =pygame.font.Font("../assets/fonts/Humongous of Eternity St.ttf", 30)
text = score_font.render(f"{score}", True, (255,0,0))

#draw zombies on the screen
add_zombies(3)

#draw fish on screen
add_fishes(3)

#draw powerups
add_power(1)

#draw lives
life_icon = pygame.image.load("../assets/sprites/platformPack_item017.png").convert_alpha()
life_icon.set_colorkey((0,0,0))

#set lives
lives = NUM_LIVES


while lives > 0 and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # control player with keyboard
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

    #check for player/fish collisions
    result = pygame.sprite.spritecollide(player, fishes, True)
    #print(result)
    if result:
        score += len(result)
        #draw more fish
        add_fishes(len(result))

    #check for player/zombie collisions
    result = pygame.sprite.spritecollide(player, zombies, True)
    #print(result)
    if result:
        #lose lives if hurt
        lives -= len(result)
        #draw more zombies
        add_zombies(len(result))

    #check for player/powerup collisions
    result = pygame.sprite.spritecollide(player, powers, True)
    #print(result)
    if result:
        #gain lives if they collide
        lives += len(result)
        #draw more powerups
        add_power(len(result))
        #add zombies to make game harder
        if lives > 3:
            add_zombies(1)



    #check if zombie is off the screen
    for zombie in zombies:
        if zombie.rect.x < -zombie.rect.width:
            zombies.remove(zombie) #removing the zombie from the sprite group
            add_zombies(1)

    #draw game objects
    player.draw(screen)
    zombies.draw(screen)
    fishes.draw(screen)
    powers.draw(screen)

    #draw score
    screen.blit(text,(SCREEN_WIDTH-TILE_SIZE, 0))
    text = score_font.render(f"{score}", True, (255, 0, 0))

    #draw lives in lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i*TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE))

    # update display
    pygame.display.flip()


    # limit frame rate
    clock.tick(50)

#once all lives are gone:
#create new background when game over
screen.blit(background, (0, 0))

#show game over message and final score
message = score_font.render("You died.", True, (0,0,0))
screen.blit(message, (SCREEN_WIDTH/2 - message.get_width()/2, SCREEN_HEIGHT/2 - 2*message.get_height()))
score_text = score_font.render(f"Score: {score}", True, (0,0,0))
screen.blit(score_text, (SCREEN_WIDTH/2 - score_text.get_width()/2, SCREEN_HEIGHT/2 - score_text.get_height()/2))

#update display
pygame.display.flip()


#wait for user to exit game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




